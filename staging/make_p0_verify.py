# -*- coding: utf-8 -*-
"""P0 delta: write staging raw-capture + verification records (2026-08-30)."""
import json
import io
import os

os.chdir(r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research')

p0_raw = {
    "round": "P0_DELTA_REPAIR_AND_FREEZE",
    "date": "2026-08-30",
    "fixes": {
        "FIX-001": {
            "paper": "RLC-17 GOReloc (arXiv:2408.07917)",
            "refetch": [
                {"url": "https://arxiv.org/html/2408.07917", "via": "WebFetch", "what": "Table II/III rows + column definitions"},
                {"what": "Table II columns = Success Rate @2m/@5m + TE(best 10%/20%); no rotation columns"},
                {"what": "Diamond 'Head' GOReloc 17.43@2m/38.23@5m; Fr2_person GOReloc 64.87@2m/96.11@5m"},
                {"what": "Table III fr2_person tight 0.5/1/2/3m: ORB-SLAM2 1.97/6.42/9.12/9.17; GOReloc 3.52/22.79/53.26/70.17"}
            ]
        },
        "FIX-002": {
            "paper": "GNSS-10 (doi:10.3390/s16122201)",
            "refetch": [
                {"url": "https://www.mdpi.com/1424-8220/16/12/2201", "via": "web_reader", "what": "full text + Table 2/4"},
                {"what": "abstract RMS: static H0.15/V0.25; kinematic H0.30/V0.45 (whole solutions)"},
                {"what": "fixed-solution RMS: static H0.02-0.03/V0.03-0.04; kinematic H0.08-0.11/V0.12-0.14"},
                {"what": "per-station whole: S1 0.14/0.25, S2 0.15/0.21, S3 0.07/0.09; K1 0.24/0.40, K2 0.28/0.47, K3 0.32/0.45"},
                {"what": "equipment NovAtel OEM615 + Samsung Galaxy A7; cutoff 15 deg; Beijing urban; fix rates 97%/90%"}
            ]
        }
    },
    "new_papers": {
        "GNSS-27": {
            "doi": "10.1016/j.asr.2025.09.039", "pii": "S0273117725010324",
            "sources": ["https://api.crossref.org/works/10.1016/j.asr.2025.09.039",
                        "https://www.sciencedirect.com/science/article/abs/pii/S0273117725010324 (web_reader preview)",
                        "WebSearch abstract snippets", "Unpaywall is_oa=False"],
            "captured": ["scenarios: open-sky/urban canyon/glass curtain wall/tree",
                         "comprehensive vs three single-indicator stochastic models: +50.0%/+17.6%/+8.5%",
                         "open-sky fix rate >99%"],
            "not_captured": ["East/North/Up absolute values", "PLD precise definition"]
        },
        "GNSS-28": {
            "doi": "10.1016/j.asr.2025.12.042", "pii": "S0273117725014693",
            "sources": ["https://api.crossref.org/works/10.1016/j.asr.2025.12.042",
                        "https://scholars.whu.edu.cn/en/publications/improving-positioning-performance-of-ppp-rtk-by-tightly-coupled-i/",
                        "SD Highlights"],
            "captured": ["full abstract: multi-freq multi-GNSS PPP-RTK platform; probability-based cycle slip detection; robust estimation w/ PDOP + height residuals; urban field validation; published 15 Feb 2026",
                         "qualitative result: significantly improve ambiguity fix rate and positioning accuracy"],
            "not_captured": ["numeric accuracy values (none in abstract)"]
        },
        "LDG-18": {
            "doi": "10.1016/j.measurement.2026.121711", "pii": "S026322412601420X",
            "sources": ["Crossref", "SD Highlights (web_reader)", "WebSearch abstract snippet", "xueshu.baidu.com", "x-mol.com/paper/1947550878354075648"],
            "captured": ["multi-metric constraints in measurement equation ensure map point accuracy",
                         "map points with unknown height and poor observability optimized via vertical observation",
                         "41.29% = urban canyon position+attitude accuracy improvement"],
            "not_captured": ["41.29% baseline identity", "LiDAR model", "ground-plane constraint details"]
        },
        "VIS-01": {
            "doi": "10.1016/j.measurement.2025.117623", "pii": "S0263224125009820",
            "sources": ["Crossref", "SD preview (web_reader)", "WebSearch abstract snippets"],
            "captured": ["SVIO real-time position+depth; stereo matching depth constraints; neural volume rendering fusion; volume rendering decoding"],
            "not_captured": ["X/Y/Z errors", "dataset", "sensor configuration"]
        },
        "FRM-01": {
            "doi": "10.32604/cmc.2022.031602",
            "sources": ["Crossref", "https://www.techscience.com/cmc/v73n3/49101.html (HTML full text)",
                        "https://cdn.techscience.press/ueditor/files/cmc/TSP_CMC-73-3/TSP_CMC_31602/TSP_CMC_31602.pdf (PDF eq extraction, pypdf)"],
            "captured": ["R1=min denominator; R2=average denominator (Eq.7); R4=harmonic-mean denominator (Eq.9, Awrangjeb); two-fold (Eq.10); symmetric mean RiM=(RiA+RiB)/2 (Eq.11); ordering R2M<=R4M<=R3M<=R1M; image-domain effect"]
        },
        "RLC-19": {
            "doi": "10.3390/s24196288",
            "sources": ["Crossref", "https://www.mdpi.com/1424-8220/24/19/6288 (full text)"],
            "captured": ["success = 3D position error < threshold (1.0 m, no rotation)",
                         "simulation 99.85% (K=10, cluster 0.1) -> ~99% abstract; ~30 ms matching + ~60 ms descriptor ~11 Hz",
                         "NCD: 43770 templates@0.2m, 600 test scans, cascade LSH-KDT K=40 94.67% @1m (0.135 s/frame); exhaustive 97.83% @1m (~191 s/frame)",
                         "heterogeneous map Leica BLK360 -> Ouster OS-0-64; Python single-thread"]
        },
        "RLC-20": {
            "arxiv": "2508.20981",
            "sources": ["https://arxiv.org/abs/2508.20981", "https://arxiv.org/html/2508.20981v1",
                        "WebSearch: PMLR v305 li25b (CoRL 2025); github.com/cvg/ActLoc"],
            "captured": ["LocMap attention model predicts per-waypoint yaw/pitch accuracy distribution from SfM map",
                         "mixed cost map Mx=Cx+lambda*Dx (Mahalanobis) into OMPL; waypoints 20 cm",
                         "thresholds 0.1m/1deg, 0.25m/2deg, 0.5m/5deg, 5m/10deg",
                         "@1m: far +35%, near +11%, all localized +5.8%; 110 ms/waypoint vs LWL 8230 ms"],
            "not_captured": ["per-table success-rate cells (not rendered in ar5iv text layer)"]
        },
        "RLC-21": {
            "arxiv": "2210.01361",
            "sources": ["arXiv API id_list=2210.01361", "WebSearch code repo csiro-robotics/Uncertainty-LPR"],
            "captured": ["authors Mason/Knights/Ramezani/Moghadam/Miller; accepted IROS 2023; uncertainty-aware LiDAR place recognition w/ per-prediction uncertainty, filtering uncertain candidates"]
        },
        "RLC-22": {
            "arxiv": "2608.06307",
            "sources": ["WebSearch arXiv record"],
            "captured": ["UQ-Loc: anisotropic per-voxel covariance for LiDAR SCR; consistent 6-DoF accuracy improvement, well-calibrated covariances; PREPRINT only"]
        }
    },
    "failed_channels": ["SD curl = JS shell (Cloudflare)", "IAB browser direct = Turnstile captcha",
                        "ResearchGate = Access Denied", "OUCI = 502", "ADS = 405",
                        "Semantic Scholar = 429", "MDPI curl = 403"]
}

with io.open('staging/P0_DELTA_raw.json', 'w', encoding='utf-8') as f:
    json.dump(p0_raw, f, ensure_ascii=False, indent=2)

v3 = {
    "report": "VERIFY_report_V3 (P0 delta round)",
    "date": "2026-08-30",
    "fix_verification": [
        {"Matrix_ID": "PM-174", "Paper_ID": "RLC-17", "verdict": "YES",
         "checked_url": "https://arxiv.org/html/2408.07917",
         "note": "FIX-001 复核：17.43 确属 ICL-Data Diamond 'Head' @2m；fr2_person 为 64.87@2m/96.11@5m；Table II 无旋转列；Table III fr2_person 紧阈值对比确认。聚合层 02/04/06/16 已修复。"},
        {"Matrix_ID": "PM-126", "Paper_ID": "GNSS-10", "verdict": "YES",
         "checked_url": "https://www.mdpi.com/1424-8220/16/12/2201",
         "note": "FIX-002 复核：静态 whole H0.15/V0.25 属实；升级 FULLTEXT；新增固定解行 PM-190。"},
        {"Matrix_ID": "PM-127", "Paper_ID": "GNSS-10", "verdict": "YES",
         "checked_url": "https://www.mdpi.com/1424-8220/16/12/2201",
         "note": "FIX-002 复核：动态 whole H0.30/V0.45 补全（原摘要截断 0.45 缺失）；新增固定解行 PM-191。"}
    ],
    "new_matrix_rows": [
        {"Matrix_ID": "PM-192", "Paper_ID": "GNSS-27", "verdict": "ABSTRACT_ONLY",
         "note": "50.0/17.6/8.5 = 综合 vs 三单指标模型相对提升；E/N/U 未核验，禁止当 E/N/U 引用。"},
        {"Matrix_ID": "PM-193", "Paper_ID": "LDG-18", "verdict": "ABSTRACT_ONLY",
         "note": "41.29% = urban canyon 位置+姿态精度改善；基线未核验。"},
        {"Matrix_ID": "PM-194", "Paper_ID": "RLC-19", "verdict": "YES", "note": "MDPI 全文核验：仿真 99.85/约99 @1m。"},
        {"Matrix_ID": "PM-195", "Paper_ID": "RLC-19", "verdict": "YES", "note": "MDPI 全文核验：NCD 级联 94.67 @1m。"},
        {"Matrix_ID": "PM-196", "Paper_ID": "RLC-19", "verdict": "YES", "note": "MDPI 全文核验：NCD 穷举 97.83 @1m（191s）。"},
        {"Matrix_ID": "PM-197", "Paper_ID": "RLC-19", "verdict": "YES", "note": "MDPI 全文核验：0.135s 级联匹配 / ~11Hz 仿真整体。"},
        {"Matrix_ID": "PM-198", "Paper_ID": "RLC-20", "verdict": "YES", "note": "arXiv HTML：+35/+11/+5.8 @1m（视觉口径相对提升）。"},
        {"Matrix_ID": "PM-199", "Paper_ID": "RLC-20", "verdict": "YES", "note": "arXiv HTML：110ms vs 8230ms 每航点。"}
    ],
    "paper_level": [
        {"ID": "GNSS-27", "level": "ABSTRACT/PREVIEW"},
        {"ID": "GNSS-28", "level": "ABSTRACT-FULLTEXT-TEXT (no numbers)"},
        {"ID": "LDG-18", "level": "ABSTRACT/HIGHLIGHTS"},
        {"ID": "VIS-01", "level": "ABSTRACT"},
        {"ID": "FRM-01", "level": "FULLTEXT"},
        {"ID": "RLC-19", "level": "FULLTEXT"},
        {"ID": "RLC-20", "level": "FULLTEXT-HTML"},
        {"ID": "RLC-21", "level": "ABSTRACT (metadata verified)"},
        {"ID": "RLC-22", "level": "PREPRINT/ABSTRACT"}
    ],
    "counts": {"fulltext_verified": 3, "abstract_only": 4, "preprint": 1,
               "matrix_rows_added": 8, "raw_pool_added": 9, "bib_added": 9}
}

with io.open('staging/VERIFY_report_V3.json', 'w', encoding='utf-8') as f:
    json.dump(v3, f, ensure_ascii=False, indent=2)

print('staging files written')
