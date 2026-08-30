# -*- coding: utf-8 -*-
"""Fix unquoted commas in PM-126/127/190/191/194 rows (2026-08-30)."""
import io
import csv

path = r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research\03_PERFORMANCE_BENCHMARK_MATRIX.csv'

with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

fixes = {
    'PM-126': 'PM-126,GNSS-10,GNSS,2016,城市静态 BDS/GPS RTK（whole solutions RMS，含未固定历元；固定解 RMS H≤0.03/V≤0.04 m）,REAL,,,,"positioning accuracy (RMS), static test",,better than 0.15 (horizontal) / 0.25 (vertical),m,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,"the average positioning accuracies (RMS) were better than 0.15 m (horizontal) and 0.25 m (vertical) for the static test（Table 2 whole solutions: S1 0.14/0.25; S2 0.15/0.21; S3 0.07/0.09；fixed solutions H≤3 cm / V≤4 cm）",,,【FIX-002 2026-08-30】MDPI 原文全文+Table 2 核验（web_reader），升级 ABSTRACT→FULLTEXT,YES',
    'PM-127': 'PM-127,GNSS-10,GNSS,2016,城市动态测试，车速 50-80 km/h（whole solutions RMS，含未固定历元；固定解 RMS H约0.10/V约0.13 m；K1 0.24/0.40; K2 0.28/0.47; K3 0.32/0.45）,REAL,,,,"positioning accuracy (RMS), kinematic test",,0.30 (horizontal) / 0.45 (vertical),m,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,"and 0.30 m (horizontal) and 0.45 m (vertical) for the kinematic test（Table 4 whole solutions）",,,【FIX-002 2026-08-30】MDPI 原文全文+Table 4 核验，补全原摘要截断的动态垂向 0.45 m；升级 ABSTRACT→FULLTEXT,YES',
    'PM-190': 'PM-190,GNSS-10,GNSS,2016,城市静态 BDS/GPS RTK，固定解（ambiguity-fixed epochs only；三测段 S1/S2/S3 范围）,REAL,,,,"positioning accuracy (RMS), static test, fixed solutions",,≤0.03 (horizontal) / ≤0.04 (vertical),m,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,"fixed solutions RMS static: H 0.02-0.03 m / V 0.03-0.04 m（S1 0.03/0.04; S2 0.02/0.04; S3 0.02/0.03；原文文字：better than 3 cm horizontal and 4 cm vertical）",,,【FIX-002 2026-08-30 新增】低成本接收机 RTK FIX 高程厘米级的直接证据（支撑 ALTITUDE_20CM 口径），MDPI 原文全文核验,YES',
    'PM-191': 'PM-191,GNSS-10,GNSS,2016,城市动态测试（50-80 km/h），固定解（K1/K2/K3 三测段范围）,REAL,,,,"positioning accuracy (RMS), kinematic test, fixed solutions",,约0.08-0.11 (horizontal) / 约0.12-0.14 (vertical),m,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,"fixed solutions RMS kinematic: H 0.08-0.11 m / V 0.12-0.14 m（K1 0.08/0.12; K2 0.09/0.13; K3 0.11/0.14；原文文字：about 10 cm horizontal and 13 cm vertical）",,,【FIX-002 2026-08-30 新增】低成本 RTK 固定解动态高程约 13 cm，仍满足 <20 cm 设计带；whole solutions 则 0.45 m——两条口径必须分开写,YES',
    'PM-194': 'PM-194,RLC-19,Relocalization,2024,"仿真：Gazebo 虚拟LiDAR模板库（10万模板）+2000测试样本+同传感器模板；成功判据=3D位置误差<1.0 m（纯位置，无旋转阈值）",PUBLIC_DATASET,,,,全局重定位成功率 @1.0 m,,约99（摘要口径）/ 99.85（K=10，cluster 0.1）,%,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,"仿真99.85%成功率（Fig.7口径）→摘要99%口径; matching约30ms+描述子约60ms",,【口径警示】同传感器模板+纯位置1m阈值口径；不可与DG紧阈值（0.25m+姿态）直接对比,YES,MDPI全文核验（open access）,YES',
}

out = []
for ln in lines:
    for k, v in fixes.items():
        if ln.startswith(k + ','):
            ln = v
            break
    out.append(ln)

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write('\n'.join(out))

with io.open(path, encoding='utf-8') as f:
    parsed = list(csv.reader(f))
bad = [(i, len(r), r[0] if r else '?') for i, r in enumerate(parsed) if len(r) != 24]
print('bad rows now:', bad)
print('total:', len(parsed))
