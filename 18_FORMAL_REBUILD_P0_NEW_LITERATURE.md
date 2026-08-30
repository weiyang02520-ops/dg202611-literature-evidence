# 18 FORMAL REBUILD P0 NEW LITERATURE — 正式方案重建新增核心文献档案

记录日期：2026-08-30（P0 增量修复轮）
任务来源：MASTER 冻结的正式方案书结构要求 7 个强制新增来源（NEW-01~07）+ 围绕五个空缺的限定补查。
核验分级：**FULLTEXT**（全文逐数值核验）> **ABSTRACT 完整**（完整摘要文本，无数值可核）> **ABSTRACT/PREVIEW**（摘要+预览要点，部分数值）> **PREPRINT**（未经同行评审）。
配套文件：`19_FORMAL_REBUILD_CLAIM_REFERENCE_MAP.md`（claim 映射）、`20_FORMAL_REBUILD_CORRECTION_LOG.md`（纠错日志）、`03_PERFORMANCE_BENCHMARK_MATRIX.csv`（PM-192~199）、`staging/VERIFY_report_V3.json`。

---

## NEW-01 → GNSS-27｜综合随机模型 RTK（2025, Adv. Space Res.）

- **题名/出处**：A robust stochastic model for GNSS real-time kinematic positioning in challenging environments via combining elevation-angle, C/N0, and PLD. Dai Wujiao, Qi Qiang, Yu Wenkun, Cai Changsheng, Zheng Bin, Pan Jiabao. ASR 76(11):6847-6862. DOI: 10.1016/j.asr.2025.09.039。
- **核验状态**：ABSTRACT/PREVIEW（Crossref 元数据 + SD 预览页 + WebSearch 摘要要点；Unpaywall is_oa=False，Cloudflare 拦截浏览器直连）。
- **已核验要点**：
  - 四类场景验证：open-sky / urban canyon / glass curtain wall / tree；
  - 综合随机模型较**三个单指标随机模型**精度提升 **50.0% / 17.6% / 8.5%**（三组两两对比，配对顺序未在摘要标明）；
  - open-sky 条件下 fix 率 >99%（预览结论片段）。
- **未核验（付费墙）**：East/North/Up 分量绝对值；PLD 量的精确定义与归一化；接收机型号与 RTK 处理参数细节。
- **引用边界（硬约束）**：
  1. 50.0/17.6/8.5 是"综合 vs 单指标"相对提升，**禁止**当作 E/N/U 分量或绝对精度引用；
  2. 本文是 **RTK 可用条件下**的观测随机建模，机制成果**不得迁移**到 BDS outage/长时间拒止场景（outage 期无观测可加权）；
  3. 引用前必须取得全文补 E/N/U 核验。

## NEW-02 → GNSS-28｜PPP-RTK/INS 城市紧组合（2026, Adv. Space Res.）

- **题名/出处**：Improving positioning performance of PPP-RTK by tightly coupled integration with INS in urban environment. Zhang Laihong, Zhang Weixing, Zhao Sidi, Lou Yidong. ASR 77(4):4731-4745（Published 15 Feb 2026）. DOI: 10.1016/j.asr.2025.12.042。
- **核验状态**：ABSTRACT 完整（Crossref + WHU Scholars 门户全文摘要 + SD Highlights）。
- **已核验要点**（完整摘要，**纯定性、无数值**）：
  - 多频多系统 PPP-RTK 实时软件平台 → **tightly coupled** PPP-RTK/INS；
  - 概率化周跳检测方法；
  - 基于 **PDOP 与高程残差**的抗差估计抵抗 outlier；
  - 结论口径："significantly improve the ambiguity fix rate and positioning accuracy"（urban 实测）。
- **未核验**：精度改善具体数值；结果是否分 East/North/U 报告（摘要未说明）。
- **引用边界**：只能作为"城市 GNSS 退化期紧组合维持模糊度固定率与精度"的方法论与定性结论引用；**不得**给方案书引用任何具体百分比。

## NEW-03 → LDG-18｜MMC-LIG 多度量约束 LIG（2026, Measurement）

- **题名/出处**：MMC-LIG: a LiDAR-INS-GNSS integration navigation system with multi-metric constraints in urban environments. Zhang Zhen, Xu Tianhe, Cong Yangzi, Nie Wenfeng, Wu Paipai, Zhang Wei, Yao Linghan. Measurement 279:121711. DOI: 10.1016/j.measurement.2026.121711。
- **核验状态**：ABSTRACT/HIGHLIGHTS（Crossref + SD 预览 Highlights + WebSearch 摘要片段 + 百度学术/X-MOL 镜像）。
- **已核验要点**：
  - 动机：城市 GNSS 退化/中断导致 LiDAR 里程计漂移与 INS 发散；
  - 测量方程**多度量约束**保证地图点精度（Highlights 原文）；
  - 对**未知高度、弱可观**地图点用垂直观测信息优化（对应 "vertical observation insufficiency" 主题，Highlights 原文）；
  - **41.29%** = urban canyon 下"位置与姿态精度改善"幅度（摘要片段口径；对比基线未在摘要出现）。
- **未核验（付费墙）**：41.29% 的对比基线与指标定义分层；LiDAR 型号/扫描线数；ground-plane 约束的具体形式。
- **引用边界**：
  1. 41.29% 只能写"urban canyon 下位置+姿态精度改善 41.29%（对比方法待全文核验）"；
  2. 本文为 **3D LiDAR**（+INS+GNSS）系统——其垂直观测增强机制**不得**写成 DG 当前 **2D RPLidar** 已具备的能力，只能作为"垂直观测不足需专门约束"的机制论据与方案书展望。

## NEW-04 → VIS-01｜SVIO + 神经体渲染室内定位建图（2025, Measurement）

- **题名/出处**：Indoor positioning and mapping method combining stereo visual-inertial odometry and neural volume rendering. Liu Mingyue, Zhu Huizhong, Zhang Shoujian, Xu Xinchao, Ma Youqing, Liu Ziao, Fu Xiaotian. Measurement 254:117623. DOI: 10.1016/j.measurement.2025.117623。
- **核验状态**：ABSTRACT（Crossref + SD 预览 + WebSearch 摘要要点）。
- **已核验要点**：SVIO 实时获取载体位置与深度 → 与神经体渲染（NVR）融合实现室内高精度定位与稠密建图；立体匹配提供可靠深度约束；体渲染解码（Highlights/摘要要点）。
- **未核验（付费墙）**：X/Y/Z 误差数字、评测数据集、传感器配置（相机/IMU 型号）、与哪些基线对比。
- **引用边界**：
  1. **禁止**把本文结果写成 DG 的 ZED 2i 实测——本文传感器配置未核验，且本文是论文实验非 DG 实验；
  2. X/Y/Z 误差数字在取得全文前禁止引用；
  3. 当前用途限定为"视觉定位+神经渲染建图"室内增强路线的方法学参照（方案书展望/路线图用）。

## NEW-05 → FRM-01｜Two-Fold/Symmetric Repeatability（2022, CMC）【FULLTEXT】

- **题名/出处**：Two-Fold and Symmetric Repeatability Rates for Comparing Keypoint Detectors. Ibrahim El rube'. CMC 73(3):6495-6511. DOI: 10.32604/cmc.2022.031602（CC-BY 4.0 开放获取）。
- **核验状态**：**FULLTEXT**（TechScience 官方 HTML 全文 + 官方 PDF 公式区提取，Eq.5–11 逐条核对）。
- **核心定义（已逐条核验）**：
  - 重复点数 N_rp(d) 由 ε-邻域判定；重复率 = N_rp / 分母，**分母选择即口径**：
    - **R1 = N_rp / min(N_a, N_b)**——min 分母（Schmid 系），数值最高；
    - **R2 = N_rp / average(N_a, N_b′)**——存活特征算术平均分母（Ehsan 系）；
    - **R4 = N_rp / 调和平均(N_a, N_b)**（Eq.9，Awrangjeb & Lu 系）；
  - **directional（方向性）**：沿 A→B 与 B→A 计算不对称（RA ≠ RB），且**图像域**（邻域尺寸）选择影响数值——比较检测器必须报告双向 two-fold（Eq.10：R(d)=⟨RA(d), RB(d)⟩）；
  - **symmetric mean**（Eq.11）：R_i^M(d) = (R_i^A(d) + R_i^B(d))/2，i∈{1,2,3,4}——**双向 directional 率的算术平均**；
  - 实证排序 R2M ≤ R4M ≤ R3M ≤ R1M。
- **对 DG 的约束**：DG 伴随指标 **R_avg = 2M/(N₁+N₂)**（M 为重复点数）在代数上等价于 N_rp / 算术平均(N₁,N₂)，属 R2 家族的双向合并计算；它**不是** FRM-01 的 symmetric mean 公式本身。方案书必须写"采用平均分母形式的双向重复率（项目伴随指标）"，**禁止**写"采用文献 symmetric formula"或把 R_avg 说成论文唯一对称公式。

## NEW-06 → RLC-19｜3D LiDAR 实时全局重定位（2024, Sensors）【FULLTEXT】

- **题名/出处**：A Real-Time Global Re-Localization Framework for a 3D LiDAR-Based Navigation System. Chai Ziqi, Liu Chao, Xiong Zhenhua（SJTU）. Sensors 24(19):6288. DOI: 10.3390/s24196288（开放获取）。
- **核验状态**：**FULLTEXT**（MDPI 全文，全部数值逐条核对）。
- **方法结构**：离线模板库（在先验地图内以 Gazebo 虚拟 LiDAR 重采样生成模板扫描，PCASC 描述子）+ 在线级联粗精匹配（LSH+KD-tree）；支持异构地图（建图传感器 ≠ 在线传感器）。
- **成功判据**：3D **位置误差** < 阈值（主口径 **1.0 m**，**纯位置、无旋转阈值**）。
- **数值与各自设置（防止混引）**：
  - 仿真：10 万模板、2000 测试样本、K=10、cluster 0.1 → **99.85%**（正文 Fig 口径）/**约 99%**（摘要口径）@1.0 m；匹配 ~30 ms + 描述子 ~60 ms → 约 11 Hz（Python 单线程）；
  - Newer College（真实、异构：Leica BLK360 建图 → Ouster OS-0-64 在线；43,770 模板@0.2 m 步长；600 测试帧）：**级联 LSH-KDT（K=40）94.67%** @1.0 m，匹配 0.135 s/帧；**穷举匹配 97.83%** @1.0 m，~191 s/帧。
- **口径结论（衔接 CF-28 与 19 号文件 RELOCALIZATION_95）**：
  1. "99%"级数字属于**仿真+同传感器模板+1 m 纯位置阈值**口径；
  2. 真实异构地图口径即穷举也只有 ~98% 且不可实时（191 s vs 0.135 s）；
  3. 若 DG 采用紧阈值（如 0.25 m）+ 姿态阈值，本文与 GOReloc Table III 均不支持 >95%。

## NEW-07 → RLC-20｜ActLoc 主动视角选择（2025, CoRL / PMLR 305）【FULLTEXT-HTML】

- **题名/出处**：ActLoc: Learning to Localize on the Move via Active Viewpoint Selection. Li Jiajie, Sun Boyang, Di Giammarino Luca, Blum Hermann, Pollefeys Marc（ETH Zürich 等）. CoRL 2025, PMLR v305（li25b）；arXiv:2508.20981；代码 github.com/cvg/ActLoc。
- **核验状态**：**FULLTEXT-HTML**（arXiv HTML 全文；表格逐格数值未在 HTML 文本层渲染，如需表格精确值需读 PDF——方法结构、阈值族、效率与摘要级提升数字均已核验）。
- **方法结构**：注意力模型从 SfM 度量地图（3D landmark + 建图相机位姿）预测**任意 3D 航点在 yaw/pitch 上的定位精度分布（LocMap，单次前向）**；规划器以混合代价图 M_x = C_x + λ·D_x（D 为对上一视角的马氏距离，保证视角连续）接入 OMPL 路径规划（航点间隔 20 cm），逐航点选视角。
- **数值（已核验）**：
  - 定位成功判据阈值族：0.1 m/1°、0.25 m/2°、0.5 m/5°、5 m/10°（规划口径 <5 m/10°）；
  - @1 m 阈值：远点平均定位准确率 **+35%**、近点 **+11%**、整体可定位点 **+5.8%**（相对非主动基线）；
  - 效率：**110 ms/航点**（vs LWL 批处理 8230 ms，约 75×）；训练 HM3D 100 场景，泛化 ScanNet。
- **引用边界**：
  1. ActLoc 是**视觉定位（SfM 地图+相机）**的主动视角方法——只能作为"主动视角选择提升定位成功率/可用率"的**机制参照**与 DG 方案书"主动恢复"模块设计依据；
  2. **禁止**写成"DG 已使用 ActLoc"或把 +35%/+5.8% 搬进 DG 传感器口径的成功率承诺。

---

## 限定补查结果（五个空缺，2026-08-30）

| 空缺 | 结论 | 处置 |
|---|---|---|
| 1. 2025–2026 高程/垂向定位 | 由 FIX-002（GNSS-10 四口径补全 + PM-190/191 固定解新行）+ NEW-01（综合随机模型）+ NEW-02（PPP-RTK/INS 紧组合）覆盖 | 无需额外检索；口径拆分见 19 号文件 ALTITUDE_20CM |
| 2. LiDAR 动态目标移除后的稳定 feature repeatability | **未找到 2025–2026 直接量化文献**（定向检索命中均为动态移除方法本身，库内 LDY-01~11 已覆盖该侧） | 记为**开放空缺**：机制侧由 LDY 池 + FRM-01 度量方法论邻接支撑；数值必须自测补位（19 号文件 FEATURE_REPEATABILITY_95） |
| 3. tight threshold relocalization | NEW-06（1.0 m 纯位置阈值口径 + 级联/穷举权衡）+ FIX-001 后的 GOReloc Table III（0.5–3 m 紧阈值）覆盖 | 已入矩阵 PM-194~197；口径警示见 CF-28 |
| 4. uncertainty-aware relocalization candidate filtering | 新增 2 篇：**RLC-21**（Mason et al., IROS 2023, arXiv:2210.01361，每预测地点附不确定度、支持过滤不确定候选；元数据+摘要级）+ **RLC-22**（UQ-Loc, arXiv:2608.06307，LiDAR SCR 各向异性协方差；**PREPRINT**） | RLC-21 入池作机制参照；RLC-22 PREPRINT 隔离（不入 CORE） |
| 5. active localization / active perception | NEW-07（ActLoc）+ 库内 RLC-01/02/04/07/08/11/13/15/16 既有主动定位族覆盖 | CLAIM-11 强度升为 STRONG（视觉口径警示） |

扩散禁令执行情况：本轮未引入大模型 Agent、mmWave、event camera、无关机器人文献；五空缺之外零新增。

---

## 平台与通道记录（本轮）

- 成功通道：Crossref（元数据）、MDPI/TechScience/arXiv/WHU Scholars（全文或完整摘要）、web_reader（穿透 SD 摘要预览）、WebSearch（摘要要点补掘）、arXiv API、Unpaywall。
- 失败通道（已记录，避免复试）：SD 直连 curl（JS 壳页）、浏览器直连（Cloudflare Turnstile 人工验证不可自动通过）、ResearchGate（Access Denied）、OUCI（502）、ADS（405）、Semantic Scholar（429 限流）、MDPI curl（403）。
- 结论：四篇 Elsevier 均确认 is_oa=False 且无合法 OA 副本，ABSTRACT 级核验为本轮合规上限；全文核验待后续（如机构访问）并已在 20 号文件登记为未决事项。
