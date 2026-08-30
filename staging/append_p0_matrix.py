# -*- coding: utf-8 -*-
"""P0 delta: append performance matrix rows PM-192..PM-199 (2026-08-30)."""
import io
import csv

path = r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research\03_PERFORMANCE_BENCHMARK_MATRIX.csv'

rows = [
"PM-192,GNSS-27,GNSS,2025,挑战环境静态RTK（open-sky/urban canyon/glass curtain wall/tree 四场景）；多频多系统接收机带PLD输出,REAL,,,,综合随机模型较三个单指标随机模型的定位精度提升（综合=仰角+C/N0+PLD）,,50.0 / 17.6 / 8.5,%,UNSPECIFIED,DEGRADED-RELATED,,,ABSTRACT-ONLY,The positioning accuracy of comprehensive stochastic models has improved by 50.0% 17.6% and 8.5% compared to the three single-indicator stochastic models（对应 vs 仰角模型/vs C/N0模型/vs PLD模型 三组对比——具体配对顺序未在摘要标明）,,【边界】非E/N/U分量数字，禁止当E/N/U引用；East/North/Up绝对值付费墙内未核验；本文是RTK可用条件随机建模，不迁移到BDS outage,NO,摘要级核验完成；E/N/U绝对值与配对顺序需全文,NO",
"PM-193,LDG-18,LiDAR Degeneracy,2026,urban canyon 城市峡谷场景；LiDAR-INS-GNSS多度量约束系统 vs 对比方法,REAL,,,,位置+姿态精度改善幅度（相对对比方法；具体基线未在摘要出现）,,41.29,%,UNSPECIFIED,DEGRADED-RELATED,,,ABSTRACT-ONLY,the position and attitude accuracy improvements ... reach 41.29% indicating that the proposed system achieves the best...,,【边界】对比基线/指标定义/指标分层未核验；3D LiDAR系统能力不得映射到DG 2D RPLidar,NO,摘要级核验完成；需全文确认基线与指标,NO",
"PM-194,RLC-19,Relocalization,2024,仿真：Gazebo虚拟LiDAR模板库（10万模板@采样）+2000测试样本+同传感器模板；成功判据=3D位置误差<1.0 m（纯位置,无旋转阈值）,PUBLIC_DATASET,,,,全局重定位成功率 @1.0 m,,约99（摘要口径）/ 99.85（K=10,cluster 0.1）,%,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,仿真99.85%成功率（Fig.7口径）→摘要99%口径; matching约30ms+描述子约60ms,,【口径警示】同传感器模板+纯位置1m阈值口径；不可与DG紧阈值（0.25m+姿态）直接对比,YES,MDPI全文核验（open access）,YES",
"PM-195,RLC-19,Relocalization,2024,Newer College Dataset真实数据：43770模板（0.2m步长）+600真实测试帧（Ouster OS-0）+Leica BLK360异构地图；级联LSH+KD-tree（K=40）;成功判据同上@1.0m,PUBLIC_DATASET,,,,全局重定位成功率 @1.0 m（级联匹配）,,94.67,%,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,Newer College 94.67% @1m (LSH-KDT cascade K=40); matching 0.135 s/frame（整体约7Hz含描述子）,,【口径警示】异构建图传感器+真实数据口径——比仿真99%保守；仍为纯位置阈值,YES,MDPI全文核验（open access）,YES",
"PM-196,RLC-19,Relocalization,2024,同上Newer College设置但穷举匹配（exhaustive matching）;成功判据同上@1.0m,PUBLIC_DATASET,,,,全局重定位成功率 @1.0 m（穷举匹配上界）,,97.83,%,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,Newer College 97.83% @1m (exhaustive) but ~191 s/frame,,【权衡】穷举仅比级联高约3pp但耗时三个数量级（191s vs 0.135s）——准确率上限与实时性不可兼得,YES,MDPI全文核验（open access）,YES",
"PM-197,RLC-19,Relocalization,2024,算法级匹配耗时（Python单线程实现）;仿真与NCD级联口径,PUBLIC_DATASET,,,,单帧匹配+描述子耗时,,约0.135 s（NCD级联匹配）;~11 Hz（仿真整体含描述子）,s; Hz,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,0.135 s per sample matching on NCD; ~30 ms matching + ~60 ms descriptor (simulation) ~11 Hz overall,,Python单线程实现——C++工程实现可显著加速;文献值为机制参照非性能承诺,YES,MDPI全文核验（open access）,YES",
"PM-198,RLC-20,Relocalization,2025,HM3D/ScanNet视觉定位主动视角选择（LocMap预测yaw/pitch精度分布）;@1m定位阈值,PUBLIC_DATASET,,,,可定位点比例提升（相对非主动基线）:远点+35%/近点+11%/全部+5.8,,+35（远点）/ +11（近点）/ +5.8（全部）,%,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,improves the average localization accuracy by up to 35% for distant points and 11% for nearby ones resulting in 5.8% more localized points when a 1 m threshold is applied,,【边界】视觉SfM地图+相机口径的相对提升，非成功率绝对值；禁止写成DG已使用ActLoc,YES,arXiv HTML全文核验,YES",
"PM-199,RLC-20,Relocalization,2025,单航点视角选择推理耗时;分辨率136×36;RTX 4090,PUBLIC_DATASET,,,,每航点视角选择耗时（vs LWL批处理）,,约110（ActLoc）/ 8230（LWL）,ms,UNSPECIFIED,UNSPECIFIED,,,FULLTEXT,110 ms per waypoint vs LWL 8230 ms（约75倍）;耗时与分辨率近似无关,,效率数字为机制参照;DG无视觉SfM地图不直接适用,YES,arXiv HTML全文核验,YES",
]

with io.open(path, 'r', encoding='utf-8-sig') as f:
    existing = f.read()
if not existing.endswith('\n'):
    existing += '\n'
existing += '\n'.join(rows) + '\n'
with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(existing)

with io.open(path, encoding='utf-8') as f:
    parsed = list(csv.reader(f))
print('total rows:', len(parsed))
bad = [(i, len(r)) for i, r in enumerate(parsed) if len(r) != 24]
print('bad col rows:', bad[:10])
print('last IDs:', [r[0] for r in parsed[-8:]])
