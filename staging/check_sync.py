# -*- coding: utf-8 -*-
import os
import hashlib

SOURCE = r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research'
MIRROR = r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research_github_mirror'
SEP = chr(92)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


src = []
for root, dirs, files in os.walk(SOURCE):
    dirs[:] = [d for d in dirs if d != '.git']
    for fn in files:
        rel = os.path.relpath(os.path.join(root, fn), SOURCE).replace(SEP, '/')
        if rel != 'xicp_tmp2.html':
            src.append(rel)
issues = 0
for rel in sorted(src):
    mp = os.path.join(MIRROR, rel)
    sp = os.path.join(SOURCE, rel)
    if not os.path.exists(mp):
        print('MISSING in mirror:', rel)
        issues += 1
    elif sha(sp) != sha(mp):
        print('DIFFERS:', rel)
        issues += 1
print('issues:', issues, 'of', len(src))
