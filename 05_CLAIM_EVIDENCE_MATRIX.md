# 05 CLAIM–EVIDENCE MATRIX — 方案书技术结论与文献绑定

生成日期：2026-08-29
用途：方案书中每一条技术性结论，先在此表登记证据，再落笔。STRENGTH 判据：STRONG = ≥2 篇独立 VERIFIED 文献+条件化数值；MODERATE = 有 VERIFIED 文献但数值/条件不全或仅单一来源；WEAK = 仅方法论文/综述支撑，无数值。
所有证据行仅取自 `03_PERFORMANCE_BENCHMARK_MATRIX.csv` 中 EXTRACTION_VERIFIED ≠ NO 的条目。

---

## CLAIM-01：UWB 在 NLOS 环境下定位误差显著增加，因此必须进行质量判断与异常观测拒绝

- **EVIDENCE**：UWB-03（Barral 2019, Sensors：NLOS Hard 原始 MAE ≈1.9 m；F1>0.9 判别；全文结论"未判为 LOS 的量测一律忽略"）、UWB-08（Fontaine 2023, IoT-J：LOS 1–10 cm vs NLOS >30 cm）、UWB-29（UTIL, IJRR 2024：遮挡序列 RMSE 0.16–0.92 m；静态 NLOS 偏差可重复、动态 NLOS 不可预测；ESKF 卡方剔除基准）
- **STRENGTH**：STRONG
- **CONDITIONS**：低成本 UWB（DW1000 系）、室内、TWR/TDOA、基站 4–8；误差量级随遮挡程度分层。
- **SAFE_WORDING**："实测研究表明 UWB 测距误差从 LOS 的厘米级恶化到 NLOS 的分米至米级，且动态遮挡误差不可预测；主流处理方式是质量判别后降权或直接拒绝。"
- **UNSAFE_EXAGGERATION**："NLOS 使 UWB 误差增大一个数量级"（必须分层表述）；"我们的 UWB 在 NLOS 下仍保持厘米级"。

## CLAIM-02：事件相机在高动态范围和高速运动条件下具有传统帧相机不具备的异步视觉优势

- **EVIDENCE**：EVENT-02（Ultimate SLAM, RA-L 2018：HDR/高速场景融合较帧+IMU +85%）、EVENT-09（Nature 2024：20 fps RGB+事件 = 5000 fps 等效延迟）、EVENT-01（TPAMI 2022 综述：140 dB vs 60 dB、µs 级时间分辨率）、EVENT-04（ESVO2, T-RO 2025：双目事件 VIO 现状水平）
- **STRENGTH**：STRONG
- **CONDITIONS**：HDR/强反光/高速；动态范围数值依传感器型号 120–140 dB 口径不一（CF-06）；暗光下受光子噪声限制（CF-08）。
- **SAFE_WORDING**："事件相机以异步、µs 级时间分辨率与高动态范围（依型号 120–140 dB）见长，在 HDR/高速场景与帧相机互补，融合可显著提升精度。"
- **UNSAFE_EXAGGERATION**："事件相机不受光照限制"；"事件相机可替代帧相机"。

## CLAIM-03：毫米波雷达可在低照度及部分视觉退化环境下提供几何和 Doppler 信息

- **EVIDENCE**：RADAR-07（EKF RIO, MFI 2020：面向 GNSS 拒止/黑暗/雾/烟，误差 <0.6% 行驶距离）、RADAR-22（T-RO 2024 综述：76–81 GHz FMCW 穿透雾/尘/烟能力）、RADAR-05（DRO, RSS 2025：Doppler 使能 0.18% 且隧道可行）、RADAR-16（浓烟融合 APE 1.133 m）
- **STRENGTH**：STRONG
- **CONDITIONS**：需点云级 FMCW（逐点 range+azimuth+Doppler 开放）硬件；浓烟实验为仿真去扫描实现（PM-054 核验注记）；雪暴中 LiDAR 仍最准（RADAR-18）。
- **SAFE_WORDING**："毫米波雷达可在低照度、雾/烟/尘等遮蔽场景提供距离-方位-Doppler 观测，是 LiDAR/视觉退化时的补充与冗余观测源；其定位角色是补充而非全天候替代。"
- **UNSAFE_EXAGGERATION**："雷达保证全天候定位"；把榜单百分比写成系统精度。

## CLAIM-04：LiDAR 在退化几何（走廊/隧道/开阔/重复结构）下会失效，需几何质量感知的降权/降级机制

- **EVIDENCE**：LDG-05（GEODE, IJRR 2025：FAST-LIO2 内陆水道 ATE 70.26 m、盾构隧道失败）、FUSION-23（Zhang/Kaess/Singh 2016：退化方向在线分离奠基方法）、LDG-02（X-ICP, T-RO 2024：逐方向 localizability 约束更新）、FUSION-24（GenZ-ICP, RA-L 2024：自适应加权，走廊 APE 0.18–1.69 m）
- **STRENGTH**：STRONG
- **CONDITIONS**：退化基准（GEODE 64 轨迹/7 场景）；X-ICP 在超长直走廊亦有第三方复现发散记录（CF-16）——退化处理本身不是银弹。
- **SAFE_WORDING**："公开退化基准显示主流 LiDAR 惯性系统在长走廊/隧道等几何退化场景可漂移数十米；文献已形成'检测退化方向→约束/降权更新'的方法族。"
- **UNSAFE_EXAGGERATION**："我们的退化检测保证不失效"。

## CLAIM-05：动态物体（行人/车辆）会污染 LiDAR 地图与配准，需动态点处理

- **EVIDENCE**：LDY-01（ERASOR, RA-L 2021：SemanticKITTI PR 93.98%/RR 97.08%）、LDY-05（DynaHull, arXiv 2024：含动态点的地图使机器人第三转弯后无法自定位——直接失败证据）、LDY-06（RF-LIO, IROS 2021：高动态环境较 LOAM/LIO-SAM ATE 提升 90%/70%）
- **STRENGTH**：STRONG
- **CONDITIONS**：方法强依赖场景先验：城市道路基准与室内场景表现差异巨大（CF-17，ERASOR 室内 FP 82.14%）。
- **SAFE_WORDING**："动态物体残留会阻碍定位与导航（有直接失败记录）；动态点去除方法在道路基准上 PR/RR 可达 94–97%，但跨场景迁移需重新验证。"
- **UNSAFE_EXAGGERATION**："动态物体已被完全解决"；把道路基准数字用于我们室内外混合场景。

## CLAIM-06：innovation/残差卡方检验与 Mahalanobis 门控是观测异常检测的正式理论基础

- **EVIDENCE**：FUSION-03（Brumback & Srinath 1987, T-AC：卡方故障检测奠基）、FUSION-16（Al Hage 2020, T-ITS：FDE+保护级完整性框架）、FUSION-12（假设检验约束鲁棒 KF, 2022）、UWB-29（ESKF 卡方剔除公开基准实现）
- **STRENGTH**：STRONG
- **CONDITIONS**：阈值依赖量测噪声建模质量；纯新息阈值剔除在 GNSS 深峡谷会误剔正确观测（CF-12）。
- **SAFE_WORDING**："以新息卡方检验/Mahalanobis 门控为核心的故障检测与排除（FDE）在导航文献中有成熟理论基础与整车级完整性框架。"
- **UNSAFE_EXAGGERATION**："卡方检验可以检测所有异常"（对共模故障/软偏差检出能力有限，需残差累计类方法补充）。

## CLAIM-07：GNSS 城市退化观测应"先降权、慎剔除"，权重可由 C/N0 等质量指标驱动

- **EVIDENCE**：GNSS-03（Groves & Jiang 2013, J. Navigation：C/N0 加权 +8%，常规顺序剔除 -60%）、GNSS-06（Hsu 2015：3D 模型+RAIM 中/深峡谷错侧解 -8.4%/-36.2%）、FUSION-18（Zhang 2018：C/N0 相对标称模板自适应加权）、GNSS-14（相关器波形 ML NLOS 判别 97.7%）
- **STRENGTH**：STRONG
- **CONDITIONS**：权重函数形式依赖接收机类型（测地型 vs 消费级，CF-09）；单时刻 C/N0 硬阈值不可靠、需连续时间序列判据（CF-13）。
- **SAFE_WORDING**："城市环境 GNSS 退化观测的主流处理是质量加权（C/N0/高度角/机器学习判别）配合环境先验辅助剔除；盲目顺序剔除可能适得其反（伦敦实测水平精度劣化 60%）。"
- **UNSAFE_EXAGGERATION**："C/N0 阈值剔除即可解决城市多径"。

## CLAIM-08：多源异步传感器融合不要求相同帧率；事件流与帧相机按各自速率对齐融合

- **EVIDENCE**：EVENT-09（Nature 2024：20 fps+事件流补高频观测）、EVENT-30（CVPR 2023：显式 cross-frame-rate 对齐融合，240 Hz）、EVENT-24（TUM-VIE：事件 µs+20 Hz 帧+200 Hz IMU 硬件同步并存）、EVENT-15（2026：事件触发异步融合定位）
- **STRENGTH**：STRONG
- **CONDITIONS**：对齐方式（nearest/accumulation/插值/time surface）决定误差量级：软件对齐 ms 级 vs 事件原生 µs 级（CF-07）。
- **SAFE_WORDING**："文献与数据集实践均采用多速率异步融合：帧相机无需与事件流同频，按时间对齐策略融合即可。"
- **UNSAFE_EXAGGERATION**："必须把 ZED 提到与事件相机等效帧率"。

## CLAIM-09：时间偏移/延迟若不标定，融合精度会显著恶化

- **EVIDENCE**：SYN-04（Feng 2019, Sensors：未补偿 100 ms 时偏 EuRoC MH5 RMSE 1.141 m vs 补偿后 0.205 m）、SYN-11（LiDAR-IMU 时延 9.58→0.50 ms，对准误差 0.09–0.17 m→0.02 m 级）、RADAR-09（时延对 radar-inertial odometry 的影响）
- **STRENGTH**：STRONG
- **CONDITIONS**：数值绑定各自主实验（VIO/LiDAR-IMU）；通用结论为"未标定时延主导融合误差"。
- **SAFE_WORDING**："实测研究表明，100 ms 量级的未补偿时偏可使 VIO 轨迹误差增大数倍；LiDAR-IMU 时延校准可将点云对准误差降低约一个数量级。"
- **UNSAFE_EXAGGERATION**："软件时间戳足够，无需硬件同步"（应表述为"硬件打底线+在线时偏估计兜底"，CF-20）。

## CLAIM-10：北斗短报文可为无人平台提供超视距应急通信链路，消息长度有硬约束

- **EVIDENCE**：BDS-01（北斗官网官方口径：区域短报文 14000 比特/1000 汉字、全球短报文 560 比特/40 汉字）、BDS-03（BDS-3 特色服务性能论文，6 条条件化数据）、BDS-02（GSMC 系统架构论文）、BDS-08（UAV 应用案例）
- **STRENGTH**：STRONG（规格）；MODERATE（机器人应用案例少）
- **CONDITIONS**：发送频次限制无官方数值（GNSS 组核验记录：不可引用任何频次数字）；区域/全球服务能力差异大。
- **SAFE_WORDING**："按官方口径，BDS-3 区域短报文单次 14000 比特（约 1000 汉字）、全球短报文单次 560 比特（约 40 汉字）；原型设计以状态摘要+关键遥测的紧凑编码为前提。"
- **UNSAFE_EXAGGERATION**："短报文可传输视频/图像流"；引用任何发送频次数字。

## CLAIM-11：主动重定位/恢复（做动作改善定位）有文献范式可循，但系统级成功率数字少

- **EVIDENCE**：RLC-15（Active SLAM 综述, T-RO 2023：目标函数与动作选择框架）、RLC-16（SII 2024：丢位→主动搜索→恢复状态机）、RLC-13（T-IE 2022：变电站巡检机器人主动重定位，PARTIALLY_VERIFIED）
- **STRENGTH**：MODERATE（框架强、条件化数值少）
- **CONDITIONS**：多为结构化/已知地图场景；"主动停止+旋转扫描+候选验证"的完整闭环在我们场景需自证。
- **SAFE_WORDING**："主动 SLAM/主动定位文献提供了基于不确定性下降与信息增益的恢复行为设计范式，可映射为本项目的'健康评估→主动重定位'状态机。"
- **UNSAFE_EXAGGERATION**："主动重定位成功率 >95%（文献支持）"——文献未给出该系统级数字。

## CLAIM-12：仿真用于构造退化场景与验证算法逻辑，不能作为性能证据

- **EVIDENCE**：SIM-12（NAVIGATION 2023：仿真城市构造 GNSS 退化评估 PPP/INS——方法论定位）、SIM-14（LISA：物理化 LiDAR 雨/雾/雪散射）、SIM-15（RadioRange：UWB 测距数字孪生）；ADV2E（SIM-06：现役事件仿真器忽略模拟电路效应的偏差警示）
- **STRENGTH**：MODERATE（方法可用性）；其"可信边界"结论为文献明确陈述
- **CONDITIONS**：各仿真器对传感器损伤建模程度不同（事件相机仿真器的已知偏差）。
- **SAFE_WORDING**："仿真仅用于退化场景构造、故障注入与算法回归测试；全部性能结论以实车实测为准。"
- **UNSAFE_EXAGGERATION**："仿真验证通过即证明达到 XX 精度"。

## CLAIM-13（反向声明，禁止写入方案书）：把文献最优值写成项目能力

- 任何"Paper X 达到 6.8 cm，因此本系统达到 6.8 cm"式推理都被本证据库禁止。文献值仅能支撑"技术路线合理性"与"目标可达性论证"，能力声明只能来自 PROJECT_DESIGN_TARGET 或 REAL_ROBOT_MEASURED。

---

## 使用说明

1. 方案书写作时逐条对照：结论 → CLAIM 编号 → 证据 → STRENGTH → SAFE_WORDING。
2. 证据行如被后续核验降级（EXTRACTION_VERIFIED=NO），本矩阵对应 CLAIM 自动降级，需回改方案书。
3. 新增结论必须先补文献核验再写入，不得先写后补。
