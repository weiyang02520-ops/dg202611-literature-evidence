# 02 FILTERED CORE PAPERS — DG-202611 高价值论文与核心证据论文

生成日期：2026-08-29（2026-08-30 P0 增量修复轮更新：新增 9 篇入池、7 篇入 CORE，另 2 篇不确定性过滤机制文献入池未入核）
数据来源：`01_RAW_LITERATURE_POOL.csv`（248 篇去重后论文，222 VERIFIED / 26 PARTIALLY_VERIFIED）
筛选原则：①与项目方法直接相关；②有真实实验；③实验条件清楚；④Ground Truth 清楚；⑤指标定义清楚；⑥有具体数值；⑦近 5 年优先；⑧经典可保留；⑨高质量 venue 优先；⑩可复现性优先。不按引用数排名。

筛选结果：
- **FILTERED（高价值层）：67 篇**（下表 A+B）
- **CORE EVIDENCE（核心证据层）：37 篇**（A 表，用于性能声明与实验设计的直接依据）
- 其余 181 篇保留在 raw pool 中作为背景/检索线索，不进入方案书引用主体。

---

## A. DG-202611 CORE EVIDENCE PAPERS（30 篇）

> 每一条"关键证据"均为从论文摘要或开放获取全文中实际抓取的数值，且绑定实验条件；详细条件见 `03_PERFORMANCE_BENCHMARK_MATRIX.csv` 对应行。

### UWB 方向（3 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| UWB-03 | NLOS Identification and Mitigation Using Low-Cost UWB Devices | 2019, Sensors | 老师"UWB 不稳定即弃用"策略最直接的文献依据：非 LOS 判决→量测直接忽略 | TWR/DW1000 实测：NLOS Hard 原始 MAE ≈1.9 m；NLOS combined ≈1 m；LOS/NLOS 二分类 F1>0.9（FULLTEXT） |
| UWB-08 | Transfer Learning for UWB Error Correction and (N)LOS Classification in Multiple Environments | 2023, IEEE IoT-J | 给出 LOS/NLOS 精度量级权威区间，并证明质量判别器需按环境校准 | 工业场景：LOS 1–10 cm；NLOS 通常 >30 cm；新环境 50 条样本迁移后 ±10 cm、检测率 93%（ABSTRACT+全文） |
| UWB-29 | UTIL: An ultra-wideband time-difference-of-arrival indoor localization dataset | 2024, IJRR | 公开 TDOA 数据集+基准，定义 DW1000 质量指标（SNR、功率差 Pd）并内置卡方剔除基准 | 无遮挡 RMSE ≈10 cm（8 基站 ESKF）；遮挡序列 0.16–0.92 m；静态 NLOS 偏差可重复、动态 NLOS 不可预测（FULLTEXT） |

### 毫米波雷达方向（5 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| RADAR-05 | DRO: Doppler-Aware Direct Radar Odometry | 2025, RSS | 当前公开榜单最强雷达里程计之一，利用 Doppler 且隧道无特征场景可行 | Boreas 榜单 0.26% 平移误差；Doppler 使能 0.18%；MulRan 1.45%（FULLTEXT） |
| RADAR-07 | An EKF Based Approach to Radar Inertial Odometry | 2020, IEEE MFI | radar-inertial odometry 奠基工程路线，明确面向 GNSS 拒止与黑暗/雾/烟 | 位置误差 <0.6% 行驶距离（ABSTRACT） |
| RADAR-16 | Adaptive LiDAR-Radar Fusion for Outdoor Odometry Across Dense Smoke Conditions | 2024, arXiv | 烟尘中 LiDAR 退化、雷达可用、融合最优——雷达角色定位的核心证据链 | 浓烟序列：LiDAR+Radar APE 1.133 m，radar-only 2.142 m，LiDAR 失败（FULLTEXT） |
| RADAR-18 | Are We Ready for Radar to Replace Lidar in All-Weather Mapping and Localization? | 2022, arXiv v3 | 对"雷达能否替代 LiDAR"给出克制结论：补充/冗余而非替代 | 雪暴中 LiDAR-only 最准；radar-only 有竞争力且地图小；跨模态定位 ~0.1 m（FULLTEXT） |
| RADAR-22 | A New Wave in Robotics: Survey on Recent mmWave Radar Applications in Robotics | 2024, T-RO | 雷达能力分级与路线图的权威综述入口 | 76–81 GHz FMCW 可穿透雾/尘/烟的能力表述（ABSTRACT） |

### 事件相机方向（4 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| EVENT-02 | Ultimate SLAM? Combining Events, Images, and IMU for Robust Visual SLAM in HDR and High-Speed Scenarios | 2018, RA-L | 事件+帧+IMU 互补融合的开山之作，直接支撑项目"事件补帧相机退化"假设 | 较纯事件 pipeline 精度 +130%，较帧+IMU +85%（HDR/高速场景，ABSTRACT） |
| EVENT-04 | ESVO2: Direct Visual-Inertial Odometry with Stereo Event Cameras | 2025, T-RO | 双目事件 VIO 当前代表 SOTA，CPU 实时 | DSEC city04_a ATE 56.17 cm（vs ESVO 370.32 cm）；MVSEC indoor 7.63 cm；rpg box 4.31 cm（FULLTEXT） |
| EVENT-09 | Low-latency automotive vision with event cameras | 2024, Nature | Nature 级证据：帧相机不必提帧率，事件流补高频观测 | 20 fps RGB+事件相机 = 5000 fps 相机的等效延迟、45 fps 的等效带宽（ABSTRACT） |
| EVENT-19 | Spatio-Temporal Calibration for Omni-Directional Vehicle-Mounted Event Cameras | 2024, RA-L | 与平台最贴合：用事件线速度与轮式里程计速度的运动学相关性联合估计时偏+外参 | 方法论文（标定精度见原文；本轮无表格级数值抽取）（ABSTRACT） |

### 自适应融合方向（5 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| FUSION-03 | A Chi-square test for fault-detection in Kalman filters | 1987, IEEE T-AC | 卡方故障检测奠基文献，"innovation 卡方检验→降权/拒绝"的理论出处 | 方法论文（ABSTRACT） |
| FUSION-16 | Localization Integrity for Intelligent Vehicles Through Fault Detection and Position Error Characterization | 2020, T-ITS | "质量评估→测量拒绝→误差界定/保护级"整车完整链路，与项目链路同构 | 方法框架+实车实验（ABSTRACT；数值待全文） |
| FUSION-18 | Site-Specific Unmodeled Error Mitigation for GNSS Positioning in Urban Environments Using a Real-Time Adaptive Weighting Model | 2018, Remote Sensing | GNSS 观测"按质量降权而不必剔除"的直接范式 | 城市车辆，C/N0 相对标称模板的自适应随机模型（ABSTRACT） |
| FUSION-23 | On degeneracy of optimization-based state estimation problems | 2016, ICRA | 退化感知"部分接受观测"奠基方法：按几何结构分离退化方向、仅在良态方向求解 | 方法论文+相机/LiDAR 实验（ABSTRACT） |
| FUSION-24 | GenZ-ICP: Generalizable and Degeneracy-Robust LiDAR Odometry Using an Adaptive Weighting | 2024, RA-L | 按局部几何特征值自适应加权 ICP 的最新代表，多数据集+退化场景定量验证 | 走廊退化 APE 1.69 m（Ground-Challenge Corridor2 0.18 m）；相对平移误差 0.46–0.94%（FULLTEXT） |

### GNSS/北斗方向（4 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| GNSS-03 | Height Aiding, C/N0 Weighting and Consistency Checking for GNSS NLOS and Multipath Mitigation in Urban Areas | 2013, J. Navigation | 无额外硬件下三种退化对策的实测对比，并警示盲目剔除可能适得其反（-60%） | 伦敦市中心：高度辅助 +35% 平面；C/N0 加权 +8%；常规顺序一致性检验最差 -60%（ABSTRACT） |
| GNSS-14 | NLOS Multipath Classification of GNSS Signal Correlation Output Using Machine Learning | 2021, Sensors | 相关器波形+ML 的 NLOS 判别高性能参考 | 城市实测 NN 判别正确率 97.7%（ABSTRACT） |
| GNSS-18 | GVINS: Tightly Coupled GNSS–Visual–Inertial Fusion for Smooth and Consistent State Estimation | 2022, T-RO | GNSS 间歇可用/退化场景多源紧组合代表（开源） | 最少 1 颗卫星即可参与状态估计（vs 常规 4 颗）（ABSTRACT） |
| GNSS-20 | GNSS/IMU/ODO/LiDAR-SLAM Integrated Navigation System Using IMU/ODO Pre-Integration | 2020, Sensors | 轮式平台强相关：2 分钟 GNSS 中断期间的定量漂移降幅 | 中断期最大位置漂移 RMS 较 GNSS/INS/ODO 降低 62.8/72.3/52.1%（N/E/H）（ABSTRACT） |

### 北斗短报文（1 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| BDS-01 | 北斗三号建成开通新闻发布会（短报文服务规格官方表述） | 2020, beidou.gov.cn | 短报文消息长度的唯一官方权威口径 | 区域短报文 14000 比特/次（1000 汉字）；全球短报文 560 比特/次（40 汉字）；全球实测定位精度周均值 2.34 m（官方页） |

### LiDAR 退化/动态方向（4 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| LDG-02 | X-ICP: Localizability-Aware LiDAR Registration for Robust Localization in Extreme Environments | 2024, T-RO | 逐自由度 localizability 检测+弱方向约束更新——"按几何质量逐方向调权"的工程范式 | 极端环境 APE 平移均值 2.05 m（前 15 m 对齐）；RPE 0.17 m/10 m；注册 12.65 ms（FULLTEXT） |
| LDG-05 | Heterogeneous LiDAR Dataset for Benchmarking Robust Localization in Diverse Degenerate Scenarios (GEODE) | 2025, IJRR | 退化场景专用公开基准，量化 SOTA 系统在退化场景的失败 | FAST-LIO2 内陆水道 ATE 70.26 m；盾构隧道全系统失败 >100 m；64 条轨迹/64 km（FULLTEXT） |
| LDY-01 | ERASOR: Egocentric Ratio of Pseudo Occupancy-based Dynamic Object Removal | 2021, RA-L | 动态物体去除代表作，条件化指标完整 | SemanticKITTI Seq00：PR 93.98%/RR 97.08%；0.0732 s/迭代（FULLTEXT） |
| LDY-05 | DynaHull: Density-centric Dynamic Point Filtering in Point Clouds | 2024, arXiv | 含"动态地图导致机器人无法自定位"的直接实验记录 | 室内建图 MAE 0.102 m；Figure 8 记录动态地图使机器人在第三转弯后无法自定位（FULLTEXT） |

### 重定位方向（2 篇）

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| RLC-15 | A Survey on Active Simultaneous Localization and Mapping | 2023, T-RO | 主动定位/主动 SLAM 权威综述，"健康评估→主动重定位"模块的选型地图 | 综述（ABSTRACT） |
| RLC-17 | GOReloc: Graph-Based Object-Level Relocalization for Visual SLAM | 2024, RA-L | 明确的"成功率-阈值"定义与逐帧耗时，供比赛指标口径设计参照 | 成功率强烈依赖阈值与序列（Table II）：fr2_person TE<2 m 64.87% / TE<5 m 96.11%；ICL Diamond 'Head' TE<2 m 17.43% / TE<5 m 38.23%；单帧 19.025 ms（FULLTEXT）【FIX-001 修正 2026-08-30】 |

### 时间同步/标定方向（2 篇）
| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件） |
|---|---|---|---|---|
| SYN-01 | Unified temporal and spatial calibration for multi-sensor systems | 2013, IROS | Kalibr 奠基论文，标定链路的理论与工具起点 | 方法论文（ABSTRACT） |
| SYN-04 | Online Spatial and Temporal Calibration for Monocular Direct Visual-Inertial Odometry | 2019, Sensors | "未补偿 100 ms 时偏→轨迹 RMSE 1.141 m，补偿后 0.205 m"的量化证据链 | EuRoC MH5：100 ms 时偏未补偿 RMSE 1.141 m vs 补偿后 0.205 m；初始化时偏误差 <3 ms（FULLTEXT） |

---

### P0 增量修复轮新增核心（7 篇，2026-08-30）

> 依据 `20_FORMAL_REBUILD_CORRECTION_LOG.md` 与 `18_FORMAL_REBUILD_P0_NEW_LITERATURE.md`：两处聚合错误修复后，为正式方案书重建强制新增 7 个核心来源。证据等级逐条标注；ABSTRACT 级条目引用前必须完成全文核验。

| ID | 论文 | 年份/Venue | 入选理由 | 关键证据（含条件与边界） |
|---|---|---|---|---|
| GNSS-27 | A robust stochastic model for GNSS RTK... combining elevation-angle, C/N0, and PLD | 2025, Adv. Space Res. | 观测质量综合随机模型（仰角+C/N0+PLD），支撑"质量驱动降权"方法族 | 四场景验证（open-sky/urban canyon/glass curtain wall/tree）；综合模型较三类单指标模型精度提升 50.0%/17.6%/8.5%；open-sky fix 率 >99%（ABSTRACT/PREVIEW）。**E/N/U 绝对值未核验（付费墙）；不得迁移到 BDS outage** |
| GNSS-28 | Improving positioning performance of PPP-RTK by tightly coupled integration with INS in urban environment | 2026, Adv. Space Res. | 城市 PPP-RTK/INS 紧组合完整方法链（概率周跳检测+PDOP/高程残差抗差） | 完整摘要核验（WHU 门户）：significantly improve ambiguity fix rate & positioning accuracy（**纯定性，摘要无数值**；是否分 E/N/U 未说明）（ABSTRACT 完整） |
| LDG-18 | MMC-LIG: a LiDAR-INS-GNSS integration navigation system with multi-metric constraints | 2026, Measurement | 城市多度量约束 LIG；垂直观测不足地图点优化 | urban canyon 位置+姿态精度改善 41.29%（对比基线未在摘要出现）；测量方程多度量约束保证地图点精度（ABSTRACT/HIGHLIGHTS）。**3D LiDAR 系统，不得映射为 DG 2D RPLidar 能力** |
| VIS-01 | Indoor positioning and mapping method combining stereo VIO and neural volume rendering | 2025, Measurement | 视觉定位+神经渲染稠密建图方法学参照 | SVIO 实时位置+深度、立体匹配深度约束、体渲染（ABSTRACT）。**X/Y/Z 误差、数据集、传感器配置未核验；禁止写成 ZED 2i 实测** |
| FRM-01 | Two-Fold and Symmetric Repeatability Rates for Comparing Keypoint Detectors | 2022, CMC | 重复率度量定义权威：min/average/调和分母、双向不对称、对称均值 | R1=min 分母、R2=平均分母、R4=调和平均分母（Eq.9）、symmetric mean=双向算术平均 RiM=(RA+RB)/2（Eq.11）；图像域影响数值（FULLTEXT）。**DG 的 R_avg=2M/(N1+N2) 是平均分母家族的项目伴随指标，不是本文唯一 symmetric formula** |
| RLC-19 | A Real-Time Global Re-Localization Framework for a 3D LiDAR-Based Navigation System | 2024, Sensors | 成功率-阈值口径参照（1.0 m 纯位置阈值）+级联 vs 穷举权衡 | 仿真 99.85%→摘要约99% @1m（同传感器模板，~11 Hz）；Newer College 级联 94.67% @1m（异构地图，0.135 s/帧）；穷举 97.83% @1m（191 s/帧）（FULLTEXT） |
| RLC-20 | ActLoc: Learning to Localize on the Move via Active Viewpoint Selection | 2025, CoRL/PMLR 305 | 主动视角选择提升定位：ACTIVE_RELOCALIZATION 核心机制参照 | LocMap yaw/pitch 精度分布单次前向；混合代价图接入 OMPL；@1m：远点 +35%/近点 +11%/全部 +5.8%；110 ms/航点 vs LWL 8230 ms（FULLTEXT-HTML）。**视觉 SfM 地图口径；禁止写成 DG 已使用 ActLoc** |

---

## B. FILTERED HIGH-VALUE（仅高价值层，30 篇）

| ID | 论文 | 年份/Venue | 选择理由 |
|---|---|---|---|
| UWB-04 | Identification of NLOS and Multi-Path Conditions in UWB Localization Using Machine Learning Algorithms | 2020, Sensors | ML 判别 NLOS/多路径的代表作，含 6 条条件化数据 |
| UWB-19 | Robust Error State Sage-Husa Adaptive Kalman Filter for UWB Localization | 2025, 期刊（见池内记录） | Sage-Husa 自适应+抗差在 UWB 上的最新组合 |
| UWB-25 | Enhanced EKF-Based Time Calibration for GNSS/UWB Tight Integration | 2022, Sensors | GNSS/UWB 紧组合+在线时间标定，对应本项目标定链路 |
| UWB-27 | Improved-UWB/LiDAR-SLAM Tightly Coupled Positioning System with NLOS Identification | 2022, 期刊（见池内记录） | UWB 与 LiDAR-SLAM 紧耦合+NLOS 识别的融合路线 |
| UWB-16 | An Improved UWB/IMU Tightly Coupled Positioning Algorithm Study | 2023, Sensors | "按 NLOS 判决实时调整量测噪声 R"的自适应协方差直接范例（+46.15%） |
| RADAR-01 | CFEAR Radarodometry | 2021, IROS | 免学习雷达里程计基线，跨传感器/环境泛化 |
| RADAR-06 | Radar-Based Odometry for Low-Speed Driving | 2025, 期刊（见池内记录） | 低速场景雷达里程计——轮式平台低速工况直接相关 |
| RADAR-09 | Impact of Temporal Delay on Radar-Inertial Odometry | 2025, 期刊（见池内记录） | 雷达-IMU 时延影响的量化，支撑同步需求 |
| RADAR-17 | LiDAR Teach, Radar Repeat | 2026, 期刊（见池内记录） | 跨模态 LiDAR 建图/雷达重定位，退化与季节变化场景 |
| RADAR-24 | The Oxford Radar RobotCar Dataset | 2020, ICRA | 雷达定位首选公开基准数据集 |
| EVENT-22 | DSEC: A Stereo Event Camera Dataset for Driving Scenarios | 2021, RA-L | "GPS PPS→MC→20 Hz 触发→special event"硬件同步链的设计模板 |
| EVENT-24 | TUM-VIE: The TUM Stereo Visual-Inertial Event Dataset | 2021, IROS | 事件 µs + 20 Hz 帧 + 200 Hz IMU 硬件同步并存的多速率标杆 |
| EVENT-30 | Frame-Event Alignment and Fusion Network for High Frame Rate Tracking | 2023, CVPR | 显式处理帧/事件不同测量速率的对齐融合，240 Hz 跟踪 |
| EVENT-15 | Event-Triggered Asynchronous Fusion Localization for an Autonomous Mobile Robot | 2026, 期刊（见池内记录） | 事件触发的异步融合定位——与项目"异步多速率融合"直接对口 |
| FUSION-04 | Adaptive Kalman Filtering for INS/GPS | 1999, J. Geodesy | IAE/MMAE 自适应滤波经典综述路线 |
| FUSION-13 | Kalman Filter-Based Integrity Monitoring Against Sensor Faults | 2013, IEEE（见池内记录） | 多传感器故障完整性监测基础方法 |
| FUSION-20 | NLOS Identification and Weighted Least-Squares Localization for UWB Systems | 2007, 期刊（见池内记录） | UWB NLOS 识别+加权最小二乘的早期经典 |
| FUSION-22 | An Integrated GNSS/UWB/DR/VMM Positioning Strategy for Intelligent Vehicles | 2020, 期刊（见池内记录） | GNSS+UWB+航位推算多源组合的车辆实例 |
| GNSS-01 | Navigation sensors and systems in GNSS degraded and denied environments | 2014, 期刊（见池内记录） | GNSS 退化/拒止的权威综述框架（Groves） |
| GNSS-05 | LiDAR Scan Matching Aided Inertial Navigation System in GNSS-Denied Environments | 2015, Sensors | GNSS 拒止期 LiDAR 匹配辅助 INS 的路线依据 |
| GNSS-06 | NLOS Correction/Exclusion for GNSS Measurement Using RAIM and City Building Models | 2015, Sensors | 3D 建筑模型+RAIM 剔除 NLOS：中峡谷 -8.4%、深峡谷 -36.2% 大误差解 |
| BDS-03 | Featured services and performance of BDS-3 | 2021, 期刊（见池内记录） | BDS-3 特色服务与性能的权威论文（含 6 条条件化数据） |
| BDS-08 | UAV Path Replanning Based on BeiDou Short Message Communication Function | 2023, 期刊（见池内记录） | 短报文在无人平台的应用案例 |
| LDG-04 | LF-GICP: Parameter-Free Degeneracy-Aware LiDAR Odometry | 2026, arXiv | 提供两种可直接借鉴的退化度量（f0/λ0），KITTI 0.865% |
| LDG-17 | FAST-LIO2: Fast Direct LiDAR-inertial Odometry | 2022, T-RO | 项目 LiDAR 主线的默认基线系统（开源） |
| LDY-06 | RF-LIO: Removal-First Tightly-coupled Lidar Inertial Odometry in High Dynamic Environments | 2021, IROS | 高动态环境先删后配，ATE 较 LOAM/LIO-SAM 提升 90%/70% |
| RLC-13 | Active Pose Relocalization for Intelligent Substation Inspection Robot | 2022, T-IE | 轮式/轨道巡检机器人主动重定位的工业级对照实现 |
| RLC-16 | Active Search and Relocalization Framework for Position-Lost Recovery | 2024, SII | 丢位检测→主动搜索→重定位成功的恢复状态机参照 |
| SYN-11 | LiDAR-IMU Time Delay Calibration Based on ICP and Iterated Sigma Point Kalman Filter | 2017, Sensors | 时延 9.58→0.50 ms、对准误差 0.09–0.17 m→0.02 m 级的量化证据 |
| SYN-13 | Camera, LiDAR, and IMU Spatiotemporal Calibration: Methodological Review and Resource | 2025, 期刊（见池内记录） | 时空标定方法学最新综述+资源汇总 |

---

## C. 遴选与淘汰记录

- 60 篇高价值 = 30 CORE + 30 FILTERED-ONLY，均出自 `01_RAW_LITERATURE_POOL.csv`，验证状态见池内记录（B 表中 RLC-13 为 PARTIALLY_VERIFIED，引用前需补齐元数据）。
- 未入选但保留在 raw pool 的 179 篇主要为：背景综述、单点技术（如纯检测/纯去噪）、数据集论文、经典老文献（被更新综述覆盖）、以及 FUTURE_OUTLOOK 展望类（偏振光/天基光学 8 篇，仅用于方案书展望章节，不作为性能依据）。
- 北斗短报文块共 10 条，其中官方规格（BDS-01）入 CORE；其余学术论文大多为海洋/海事应用，与轮式机器人原型关联较弱，保留在池中备查。
- 所有"关键证据"数值只覆盖论文实际报告的实验条件；任何把论文数值直接写成本项目能力的做法都被 `04_SAFE_CLAIM_BOUNDARIES.md` 明确禁止。
