# 16 CONFLICTING EVIDENCE — 冲突文献与口径冲突记录

生成日期：2026-08-29
原则：不同论文结论冲突时不强行合并答案，逐条记录差异条件与最可能解释，给出"我们能安全说什么"。

---

## 一、实质性结论冲突

### CF-01｜UWB NLOS 误差恶化量级
- **Paper A**：Fontaine 2023（IoT-J，10.1109/jiot.2023.3299319）：NLOS 误差 typically >30 cm。
- **Paper B**：Barral 2019（Sensors，10.3390/s19163464）：NLOS Hard 原始 MAE ≈1.9 m；Soft 约 +30 cm。
- **差异条件**：遮挡严重程度分级（轻/硬）、材质与几何。
- **最可能解释**：NLOS 不是单一状态。30 cm 是轻度遮挡典型下限，完全遮挡可达 1–2 m 或失锁（UTIL）。
- **我们能安全说**：UWB NLOS 误差为"0.3 m（轻度）至 1–2 m（硬遮挡）并可能完全失锁"的区间，禁止单值表述。

### CF-02｜UWB LOS 典型精度
- **Paper A**：Fontaine 2023：TWR 工业场景 1–10 cm。**Paper B**：UTIL 2024：低成本 DWM1000 TDOA+ESKF ≈10 cm RMSE。
- **解释**：测距模式（TWR/TDOA）与硬件代次差异。
- **安全表述**：注明测距模式与硬件后再给数值。

### CF-03｜RSSI 类特征对 UWB NLOS 识别是否足够
- **Paper A**：Barral 2019：单场景二分类 F1>0.9（够用）。**Paper B**：Sang 2020（10.3390/app10113980）：跨环境三分类 91.9%→72.9–75.4%（不足）。
- **解释**：单环境二分类 vs 跨环境三分类（含多径类）。
- **安全表述**：RSS 类特征单场景够用；跨环境需 CIR/首径功率差/残差组合特征并重校准（Fontaine 迁移学习：50 样本恢复 93%）。

### CF-04｜恶劣天气下雷达能否替代 LiDAR
- **Paper A**：Are We Ready（arXiv 2203.10174）：雪暴中 LiDAR-only 仍最准，雷达"有竞争力+地图小"。**Paper B**：K-Radar/NTU4DRadLM/RadarSLAM 等：雾/烟/雨雪中雷达可用证据。
- **解释**：天气类型细分——中等降水对 LiDAR 影响被高估；浓烟/浓雾/低光照才是雷达优势区。
- **安全表述**：雷达=遮蔽/退化场景的补充与冗余备份，非全天候替代（RADAR-18）。

### CF-05｜CFEAR 雷达里程计误差数字（1.76% vs 0.61%）
- **解释**：数据集与评测协议不同（Oxford 自报 vs Boreas 榜单引用）。
- **安全表述**：跨数据集百分比不可直接比较；本项目评测必须绑定数据集+指标定义。

### CF-06｜事件相机动态范围数值（120 vs 140 dB）
- **Paper A**：TPAMI 2022 综述：140 dB vs 60 dB。**Paper B**：DSEC（>120 dB）、ESVO2 引 Lichtsteiner 2008（120 dB）。
- **解释**：传感器型号与口径（规格上限 vs 概括）。
- **安全表述**："依型号 120–140 dB"，绑定具体传感器。

### CF-07｜多相机时间同步是否必须硬件触发
- **Paper A**：DSEC：GPS PPS+MC+20 Hz 触发硬件链。**Paper B**：ICIRA 2023（hardware-free 事件密度对齐）：软件对齐 <10 ms；部分型号（CeleX5）不支持硬件同步。
- **解释**：互补方案而非矛盾：硬件精度最高，软件免布线但 ms 级。
- **安全表述**：硬件触发打底线+软件在线时偏估计兜底；软件同步误差比事件原生 µs 差 3–4 个数量级，高速场景会成为主导误差。

### CF-08｜暗光下事件相机是否"天然免疫"
- **Paper A**：Ultimate SLAM：低光/HDR 是优势场景。**Paper B**：EvLight++（TPAMI 2026）、Stereo-DEVO（RA-L 2025）：暗光 SNR 时空变化恶化，需 SNR 感知处理。
- **解释**："输出事件"≠"高质量观测"：依赖亮度变化，但光子噪声仍在。
- **安全表述**：暗光可用但需去噪/SNR 感知处理，非"免疫"。

### CF-09｜GNSS 随机模型权重基础：高度角 vs C/N0
- **Paper A**：Zhang 2018（Remote Sensing）：高度角基础+C/N0 偏差修正。**Paper B**：Paziewski 2021（未入池，仅核验存在）：智能手机 C/N0 加权可能更优。
- **解释**：接收机类型不同（测地型 vs 消费级）。
- **安全表述**：权重函数依赖硬件，必须用本平台数据自标定。

### CF-10｜因子图鲁棒核两条路线
- **Paper A**：Switchable constraints（Sünderhauf & Protzel 2012, IROS）。**Paper B**：Max-mixtures（Olson & Agarwal 2013, IJRR）。
- **解释**：软拒绝（开关变量）vs 混合误差模型联合推断，各有保守性/鲁棒性权衡。
- **安全表述**：两条路线都成熟；选型需结合本项目滤波/优化架构，不引用二者间的比较结论。

### CF-11｜同一恶劣天气下 LiDAR 退化而雷达稳健
- **Paper A**：Kim 2023（Sensors）：雨雾使 LiDAR 点数/强度显著下降。**Paper B**：DGRO 2024：4D 雷达"以恶劣天气鲁棒性著称"。
- **解释**：非矛盾，是同环境两类传感器退化模式互补；但雷达点云自身噪声更大。
- **安全表述**：互补性是多源融合的依据；两类观测需分别标定噪声模型。

### CF-12｜GNSS"剔除不一致观测"是否可靠提升精度
- **Paper A**：Groves & Jiang 2013：常规顺序剔除使水平精度劣化 60%（伦敦）。**Paper B**：Hsu 2015：3D 模型+RAIM 使错侧解 -8.4%/-36.2%。
- **解释**：盲目剔除（不知哪颗是 NLOS）会破坏几何；带环境先验的剔除有效。
- **安全表述**：先降权后剔除；剔除需环境先验或持续性判据。

### CF-13｜C/N0 的正确用法：连续加权 vs 门槛剔除
- **Paper A**：Groves & Jiang 2013：C/N0 加权 +8%。**Paper B**：Kubo 2020（Sensors）：单时刻 C/N0 阈值不足以剔除 NLOS，需连续时间序列。
- **安全表述**：C/N0 连续加权（软）+ 持续低值才降权/拒绝（硬）的组合策略。

### CF-16｜X-ICP 在退化环境是否稳健
- **Paper A**：X-ICP（T-RO 2024）：自报 LiDAR-challenging 环境性能与可靠性提升。**Paper B**：GenZ-ICP 第三方复现：SubT-MRS 长走廊 X-ICP 全部指标发散（Div.）；Ground-Challenge Corridor2 X-ICP APE 5.85 m vs GenZ-ICP 0.18 m。
- **解释**：实验设置/传感器/参数不同。
- **安全表述**：localizability 约束型方法在超长直走廊仍可能失效；引用 X-ICP 须绑定其原实验条件。

### CF-17｜ERASOR 动态去除性能
- **Paper A**：ERASOR 自报：SemanticKITTI Seq00 PR 93.98%。**Paper B**：DynaHull 室内基准：ERASOR FP 82.14%、Precision 0.18。
- **解释**：室外道路 vs 室内人员密集场景（地面接触假设失效）。
- **安全表述**：动态去除方法强依赖场景先验，跨场景数字不可外推——对我们室内外混合场景是重要警示。

### CF-18｜FAST-LIO2 是否"足够鲁棒"
- **Paper A**：FAST-LIO2：主流高精度 LIO 基线。**Paper B**：GEODE（IJRR 2025）：FAST-LIO2 内陆水道 ATE 70.26 m、盾构隧道失败。
- **安全表述**：强基线≠退化免疫——正是本项目"几何质量感知"论点的依据。

### CF-19｜重定位成功率数值口径
- **Paper A/B**（同文不同表，GOReloc RA-L 2024，均为 fr2_person）：Table II 宽阈值 @5m 96.11% vs Table III 紧阈值 @0.5–3m 3.52–70.17%；ORB-SLAM2 @1m 仅 6.42%。（另注：Table II 中 ICL Diamond 'Head' @2m 17.43%，勿与 fr2_person 混写【FIX-001 修正 2026-08-30】。）
- **安全表述**：成功率是口径函数；比赛指标必须先固定定义。

### CF-20｜统一时间基准：硬件同步 vs 软件在线时偏估计
- **Paper A**：IROS 2024 硬件同步多传感器系统。**Paper B**：Feng 2019：纯软件在线时偏估计达亚毫秒级；未补偿 100 ms 时 RMSE 1.141 m。
- **安全表述**：两条路线数值口径不同（同步残留 vs 融合精度增益），不可互换；建议"硬件打底线+在线估计兜底"。

### CF-28｜同文内成功率自相张力：级联 vs 穷举、仿真 vs 异构真实（RLC-19，P0 新增）
- **Paper 内部**（RLC-19, Sensors 2024）：同一 1.0 m 纯位置阈值下，仿真（同传感器模板）99.85% vs Newer College 真实异构（Leica 建图→Ouster 在线）级联 94.67% vs 同设置穷举 97.83%；穷举耗时至 ~191 s/帧，级联 0.135 s/帧。
- **安全表述**："99%"级数字属于仿真同传感器口径；真实异构地图下即使用穷举也只有 ~98%（且不可实时）。方案书引用重定位成功率时必须绑定"仿真/真实 × 模板同源/异构 × 级联/穷举"三重条件；实时性要求会直接压低可报告的成功率上限。

## 二、元数据级冲突（引用时注意）

### CF-14/CF-15｜年份口径
- Teunissen et al.（BeiDou+GPS RTK）：OpenAlex 2013（在线优先）vs Semantic Scholar 2014（卷期）→ 按 2014 卷期引用。
- Bofeng Li et al.（北斗短报文海洋定位）：2018（在线）vs 2019（卷期）→ 按 2019 记录。Hamaoui（偏振光导航）2016/2017 同类差异。

### CF-21–CF-27｜同名多义与链接变迁（SIM/DATASETS 组）
- v2e 记忆中的 PLoS DOI 经 Crossref 证伪（实为无关医学论文），正确为 CVPRW 2021（10.1109/cvprw53098.2021.00144）——**一次真实的"AI 记忆 DOI"拦截记录**。
- UrbanNav 存在三个同名工作（数据集论文/AAAI 2026 语言导航/UAM 仿真框架），本库采用 IPNL-PolyU 数据集（DOI:10.33012/navi.602）；其 GitHub 仓库由 UrbanNav 迁移至 UrbanNavDataset。
- CARLA/ESIM 亦有多篇同名无关工作；EuRoC 站点 301 迁移；NCLT 旧链接 404（现行 robots.engin.umich.edu/nclt/）；KAIST Complex Urban 原官网不可达（改用官方 Google Sites）。
- mvsec.io 当前不可达（TLS/ECONNRESET 双通道确认），MVSEC 数据集条目按 PARTIAL 处理。

### CF-28–CF-32｜开源图谱口径
- License 为 NOASSERTION/None 的仓库（GTSAM、RTKLIB、Kalibr、robot_localization、fuse 等）集成前必须人工打开 LICENSE 核对。
- ROS2 支持仅采信仓库内明示证据（LIO-SAM ros2 分支、OpenVINS Dockerfile_ros2 等）。
- **gazebo_ros_pkgs 已归档**（GitHub API archived: true，pushed 2025-02-26）——新仿真建议 gz-sim（Apache-2.0）+ROS2 桥接。

## 三、第二层性能核验发现的"证据内部问题"（2026-08-29 独立核验）

1. **PM-002（UWB-03）NO**："NLOS Soft +30 cm / Hard +1 m（both devices 相对 LOS）"未见于 Barral 2019 全文（该文仅用 Pozyx 单一设备），疑为他文串入。**处理：该行禁止引用**；UWB Soft/Hard 分级数值改以 UWB-03 全文实际数字（Hard MAE≈1.9 m、combined≈1 m）与 UWB-08（NLOS>30 cm）分层表述。
2. **PM-187/188/189（SYN-17）三行 NO**：矩阵声称的 K-Radar/NuScenes/闭环 EC 数字在论文全文均不存在（实际为室内 OptiTrack+无人机实验，0.70°/0.275 m），**疑似提取幻觉，整组作废**。
3. **PM-103（FUSION-24）PARTIAL**：0.18 m 主值正确，但条件栏中"DLO 0.41 m、Zhang 0.20 m"实为 Ours 行的 Max/RMSE 列（原文 DLO=0.72、Zhang=0.21）——**对比基线数字已更正**。
4. **PM-011/012（UWB-04）**：跨环境 MLP F1 原文 0.72（矩阵误写 0.73，已标 PARTIAL）；"DW1000 6.5 GHz 10 cm 精度"句不在原文（NO，禁引）。
5. **PM-128（GNSS-14）**：论文自身不一致——摘要/结论 97.7% vs 正文 4.3 节 97.8%；本库采用与摘要一致的 97.7% 并注记。

## 四、平台/工具类记录（非学术冲突）

- Semantic Scholar/OpenAlex/arXiv API 全程多次 429 限流；各组按预案轮换 OpenAlex→Crossref→DBLP→arXiv(https)→web_reader 完成，未影响覆盖（CF-23）。
- beidou.gov.cn www/https 通道 TLS 被重置，BDS-01 经官网同页移动版 http 通道完成核验（V1 报告）。
