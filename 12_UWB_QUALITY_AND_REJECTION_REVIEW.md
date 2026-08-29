# 12 · UWB 信号质量判断与弃用策略 —— 文献评审（研究组 B：UWB 定位）

> 项目：DG-202611"基于具身智能的无人平台多源导航定位技术"（轮式平台）
> 本文目的：为"**UWB 信号稳定时使用、不稳定或覆盖边缘时弃用**"的策略提供真实文献依据。
> 证据库：`staging/UWB_raw.json`（30 篇，26 VERIFIED + 4 PARTIALLY_VERIFIED，29 条带条件的性能数据）；检索日志 `staging/UWB_searchlog.json`。
> 核验方式：所有条目均经 OpenAlex API 逐条抓取（标题/作者/年份/venue/完整摘要）；4 篇开放获取论文另经 MDPI/arXiv 全文 HTML 逐句提取数字（source_level=FULLTEXT）；30 个 DOI 逐一做了解析检查。所有性能数字均绑定实验条件，未抓到正文的一律不填数字。
>
> **重要声明：此为文献框架，非本项目实测结论，所有阈值需后续实验确定。**

---

## 一、UWB 误差来源（文献归纳）

1. **传播效应**：UWB TOA 测距依赖首径（first path）到达时间估计，但"直射径可能不存在或不是最强径"是 TOA 误差的首要来源；误差源还包括时钟漂移与干扰 [12 Dardari 2009, Proc. IEEE]。
2. **NLOS 正偏**：墙体等障碍使距离估计产生系统性正偏（positively biased）[1 Maranò 2010]；NLOS 测距误差统计上呈"高斯 + 指数（正偏尾部）"分布，LOS 为高斯 [11 Bellusci 2008]。
3. **距离与带宽依赖**：测距误差的均值与标准差随收发距离和信号带宽显著变化 [11 Bellusci 2008]；量测质量随距离退化，且基站几何配置共同决定定位精度上限 [20 Jourdan 2008]。
4. **多径/遮挡分层**：轻遮挡（NLOS Soft）与硬遮挡（NLOS Hard）误差量级差异巨大（见第三节）；静态障碍造成**一致可重复**的偏差，动态遮挡（如移动金属障碍）误差**不可预测**，严重 NLOS 下量测可**完全中断** [29 Zhao 2024 UTIL]。
5. **工程侧问题**：商用 COTS UWB 与其他传感器时钟独立，量测时序错位需在线标定 [25 Guo 2022 JSEN]；低成本模块读取 CIR 原始数据有毫秒级开销（Pozyx 读 CIR 约 300 ms/次）[3 Barral 2019]。

## 二、LOS 典型精度（均带条件）

| 数值 | 条件 | 来源 |
|---|---|---|
| **1–10 cm** | 工业 4.0 用例、UWB 室内定位、LOS 环境（摘要级通用陈述） | [8 Fontaine 2023, IEEE IoT-J]（ABSTRACT） |
| **厘米级** | 3.1–10.6 GHz 满带宽 TOA 实测，LOS | [11 Bellusci 2008]（ABSTRACT） |
| **≈10 cm RMSE** | 8×DWM1000 基站 TDOA 模式、7×8×3.5 m 场馆、四旋翼 0.45 m/s、Vicon 毫米级 GT、ESKF（含卡方离群剔除）、无遮挡 constellation #1–2：0.094–0.123 m（Const.3 略差：0.19–0.34 m） | [29 Zhao 2024, IJRR]（FULLTEXT, Table 4） |
| **10 cm** | DW1000 器件标称精度（厂商口径，LOS） | [4 Sang 2020]（FULLTEXT，转述 datasheet） |
| F1>0.9 的 LOS/NLOS 二分类前提 | Pozyx/DW1000、走廊、静态 | [3 Barral 2019]（FULLTEXT） |

**结论（答问题 1）**：LOS 下 UWB 通常为厘米级；写方案书时应表述为"**TWR 模式 1–10 cm（工业场景文献区间）**；低成本 TDOA 模式全场 RMSE 约 10 cm"，并注明硬件与场地条件，不可笼统写"厘米级"。

## 三、NLOS 恶化程度（均带条件）

| 数值 | 条件 | 来源 |
|---|---|---|
| NLOS 下误差 **typically >30 cm** | 工业 4.0 UWB 定位通用区间 | [8 Fontaine 2023]（ABSTRACT） |
| NLOS Soft **约 +30 cm**、NLOS Hard **约 +1 m**（相对 LOS） | Pozyx 等两台商用设备、室内走廊、静态 | [3 Barral 2019]（FULLTEXT） |
| NLOS Hard 原始 MAE **≈1.9 m**；Soft+Hard 混合 **≈1 m** | 同上 | [3 Barral 2019]（FULLTEXT） |
| 硬遮挡 GP 校正后可回到 **<0.2 m**（需同场景训练数据） | 同上 | [3 Barral 2019]（FULLTEXT） |
| 遮挡环境定位 RMSE **0.16–0.92 m**（最差序列 ESKF 0.919 m），而无遮挡仅 ≈0.10 m | 8 基站 TDOA、金属/木质静态障碍+移动金属柜动态遮挡、四旋翼飞行 | [29 Zhao 2024]（FULLTEXT, Table 4） |
| MP（多径）条件误差 **数 cm 至 60 cm**；人遮挡 NLOS 最严重 | 转引 Schmid et al. IPIN 2019；约 6 m 距离静态 | [4 Sang 2020]（FULLTEXT，二手转引） |
| NLOS 误差模型：高斯+指数（正偏），均值/标准差随距离、带宽变化 | 3.1–10.6 GHz 实测 | [11 Bellusci 2008]（ABSTRACT） |

**结论（答问题 2）**：NLOS 恶化是**分层的**——轻度遮挡典型下限 ~30 cm；完全遮挡（墙/金属/人体）可达 **1–2 m 且可能完全失锁**。方案书必须写区间并注明遮挡严重程度，禁止单一数字。

## 四、覆盖边缘（coverage edge）表现

文献没有统一术语"coverage edge"，但有四类直接对应的证据：

1. **几何退化 → 精度上限恶化（理论）**：量测质量随标签-基站距离退化，基站几何配置决定精度上限；提出 **localization outage probability**（定位中断概率）刻画整个区域内定位质量的空间分布 [20 Jourdan 2008]。任何关于 NLOS 基站的先验知识都能显著提升精度（密集杂波环境尤甚）[20]。
2. **窄空间实测（DOP）**：无论基站如何配置，**窄空间内 DOP 值显著高于开阔空间，并直接导致更大定位误差**；"测距误差低 ≠ 定位误差低"；把 DOP 自适应引入 KF 可抑制该误差 [22 Guo 2022, Remote Sensing]。考虑各基站不同误差方差的 **WPDOP** 优化布站（V 形最优）可将平均 WPDOP 改善 ≥37.6% [21 Cao 2023, TIM]。
3. **遮挡/边缘实证**：8 基站中受遮挡影响的 constellation #4 使 RMSE 从 ≈0.10 m 恶化到 0.16–0.92 m；静态障碍偏差一致、动态遮挡不可预测、严重 NLOS 完全失锁 [29 Zhao 2024]。地下停车场布站研究按**坡道/表面起伏/狭窄区**做差异化精度分区，用更少基站满足 AVP 精度 [23 Jiang 2022, J. Adv. Transp.]。
4. **可定位性评估**：隧道等几何退化环境提出 degeneration characterization model，在先验地图上估计给定位置的 **localizability**（含 UWB 与 LiDAR），并做概率融合 [24 Zhen 2019, ICRA]。

**结论（答问题 6）**：覆盖边缘的表现 = DOP/几何退化 + NLOS 概率上升 + 偏差可重复但与位置强相关；**可检测**：可用 DOP/WPDOP 计算 [21,22]、可定位性/退化模型 [24]、以及滤波器在线跟踪"可见性状态"（见 5.6）。

## 五、可靠性指标逐个分析

### 5.1 RSSI / 接收功率——是否足够？
- **单场景、二分类时基本够用**：仅用测距值+RSS 的均值/方差特征，Pozyx 走廊静态数据二分类（LOS/非LOS）**F1>0.9** [3 Barral 2019, FULLTEXT]。
- **跨环境、三分类时不够**：同样的 ML 思路加入 CIR 等特征做 LOS/NLOS/MP 三分类，同环境 91.9%，**跨环境掉到 72.9–75.4%**，MP 类最难分 [4 Sang 2020]。
- **不平衡数据需专门处理**：NLoS 样本少、LoS 样本多的真实部署中，常规 ML 分类器退化（SVM 92.6%…），需 GGD 类专门检测器（96.7–98.0%）[6 Che 2022]。
- **RSSI 也有工程优点**：Pozyx 读 CIR 慢（300 ms），作者实际用 RSS+测距统计特征替代 [3 Barral 2019]。
- **判定：RSSI 可作第一道筛子，但单独不足以支撑"稳定才用"的判决；跨环境必须重校准或组合其他指标**（答问题 4）。

### 5.2 First-path power / 功率差 / SNR（来自 CIR 寄存器）
- DW1000 提供四个原始质量量：first path amplitude（Amf）、CIR 估计噪声标准差（σn）、总接收功率（Pr）、首径功率（Pf）；定义 **SNR=Amf/σn、Pd=Pr−Pf**，"SNR 越高或 Pd 越低 → 信号质量越好"（Decawave 用户手册口径）[29 Zhao 2024, FULLTEXT]。
- **阈值法（power difference）有实测门限**：Decawave 约定 LOS<6 dBm、NLOS>10 dBm；Sang 等实测 LOS 4.12±1.13 dBm、NLOS 10.75±5.51 dBm（DWM1000、7 种室内环境）[4 Sang 2020, FULLTEXT]。这是本项目起步阈值的直接文献参考（仍需实测重标定）。
- 机器学习可直接吃 CIR：CIR 输入 CNN-LSTM [5 Jiang 2020]、LSTM 学习"CIR→测距误差"映射后送 EKF [7 Kim 2022]、CIR 基迁移学习 50 个新环境样本即可恢复 ±10 cm 精度与 93% (N)LOS 检测率 [8 Fontaine 2023]。
- **判定：首径功率差/SNR 是比 RSSI 更接近物理本质的判别量，文献支持其作为主判据之一**（答问题 5 前半）。

### 5.3 CIR 波形特征
- 经典统计特征：峭度、平均超额时延扩展、RMS 时延扩展做联合似然比检验，仿真中对多数 802.15.4a 信道模型识别率 >90% [2 Güvenç 2007]。
- 实测 campaign 中从信道脉冲响应提取特征做 ML 分类+回归，可判 LOS/NLOS 并回归校正测距偏差 [1 Maranò 2010；10 Wymeersch 2012]。

### 5.4 Range residual / 新息（innovation）
- 综述将"**残差分析判断法**"列为 NLOS 识别四大方法族之一（与统计特征、机器学习、几何特征并列）[13 Wang 2023]。
- 工程实现：滑窗多项式拟合残差实时区分"观测离群 vs 运动模型误差"，再分别启用鲁棒/自适应分支 [18 Dong 2023]；ESKF 基准用**卡方检验**剔除大离群 [29 Zhao 2024, FULLTEXT]；KF 预处理抑制 UWB 测距跳变后再进紧组合 [16 Zou 2023]。

### 5.5 几何指标 GDOP/WPDOP
- DOP 与误差分布并不完全等价，且窄空间 DOP 显著升高并直接放大定位误差 [22 Guo 2022]；WPDOP 把各锚点不同误差方差（LOS/NLOS 状态不同）纳入几何评估 [21 Cao 2023]；隧道环境用退化模型估计可定位性 [24 Zhen 2019]。
- **判定：几何指标回答"这里能不能用"，信号质量指标回答"这条量测能不能用"，二者互补**（答问题 5、9 部分）。

### 5.6 可见性状态 / 时间一致性
- 把"天线视距可见性"建模为**随时间变化的状态**，用贝叶斯/粒子滤波与运动状态联合跟踪（工厂实测 Decawave/Sewio/Ubisense 三种商用系统）[28 Barbieri 2021]。这是"信号是否稳定"的显式状态化实现，可直接映射为本项目的 UWB 质量状态机。

## 六、已发表的自适应协方差 / 鲁棒加权 / 离群剔除 / NLOS 分类方法列举（全部为池内已核验文献）

| 类别 | 论文 | 方法要点 |
|---|---|---|
| **自适应协方差（R 膨胀）** | [16 Zou 2023] | NLOS 判决结果实时调整量测噪声协方差 R；实测紧组合精度提升 46.15% |
| | [25 Guo 2022 JSEN] | GNSS/UWB 紧组合 double-update EKF 内嵌 UWB 量测自适应加权；实测 RMSE 改善 57.58%/31.03% |
| | [28 Barbieri 2021] | 粒子滤波联合估计可见性状态，按状态调制 UWB 量测置信 |
| **自适应 Q/R（Sage-Husa 族）** | [19 Juston 2025] | Sage-Husa 模糊自适应 + ANFIS 训练 + P/R 正定约束；差分轮式机器人（IMU+轮编码器），两条实测路线提升约 25–30% |
| | [18 Dong 2023] | 鲁棒+自适应 CKF 分工（观测离群 vs 模型误差），滑窗多项式拟合先识别类型；位置误差降 25.3–45.1% |
| **鲁棒加权（WLS/robust LS）** | [2 Güvenç 2007] | 按 MPC 统计对可疑（可能正偏）量测给小权重的 WLS |
| | [9 Yu 2018] | NLOS 量测选择规则 + 等式约束 Taylor 鲁棒最小二乘（ECTSRLS）抑制残余 NLOS 误差 |
| | [26 Wang 2021 RS] | 改进自适应鲁棒 EKF（AREKF），INS+地图信息识别并消除 UWB NLOS 误差 |
| **离群剔除（rejection）** | [29 Zhao 2024] | ESKF 内**卡方检验**剔除大离群（公开基准+数据集） |
| | [16 Zou 2023] | KF 预处理抑制 range 突变值后再融合 |
| | [22 Guo 2022 RS] | DOP 值自适应引入 KF 更新（几何级加权） |
| **NLOS 分类（统计/ML）** | [2 Güvenç 2007] | 信道统计量 + 联合似然比检验（仿真 >90%） |
| | [1 Maranò 2010] | 实测 CIR 特征 + ML 分类与回归 |
| | [3 Barral 2019] | 测距+RSS 统计特征 ML（F1>0.9） |
| | [4 Sang 2020] | SVM/RF/MLP 三分类 LOS/NLOS/MP（91.9%→72.9% 跨环境） |
| | [5 Jiang 2020] | CIR 直接输入 CNN-LSTM（7 站点开源数据集） |
| | [6 Che 2022] | 不平衡数据 GGD 检测（96.7–98.0%） |
| | [7 Kim 2022] | LSTM 学习 CIR→测距误差映射，送 EKF 定位 |
| | [8 Fontaine 2023] | 跨环境迁移学习（CIR/特征两路，50 样本恢复 93% 检测率） |
| **几何/外源辅助 NLOS 判别** | [27 Chen 2022 RS] | LiDAR 点云实时障碍检测→UWB NLOS 识别 + REKF；RMSE 0.094 m |
| | [26 Wang 2021 RS] | INS+地图几何判别消除 UWB NLOS |
| | [17 Hyun 2021] | IMM 多模型并行假设 LOS/NLOS 并在线估计 NLOS 因子（NR-UIO） |

## 七、UWB 与 IMU/GNSS/LiDAR 融合的典型方法（答问题 10）

- **UWB/IMU 紧组合（EKF/ESKF）**：开创性 6DOF 紧耦合，NLOS/多径下保持连续 [14 Hol 2009]；井下巷道 ESKF 融合+锚点部署优化 [15 Li 2020]；KF 预处理+EKF+自适应 R [16 Zou 2023]；IMM 结构 [17 Hyun 2021]；轮式差分车 Sage-Husa 自适应 [19 Juston 2025]。
- **GNSS/UWB**：紧组合 EKF + 在线时间偏移标定 + UWB 自适应加权 [25 Guo 2022]；多 GNSS RTK/INS/UWB/地图无缝紧组合 + AREKF（车辆）[26 Wang 2021]。
- **UWB/LiDAR（/视觉）**：LiDAR 点云做 NLOS 识别的紧组合 [27 Chen 2022]；LiDAR/UWB 可定位性估计与概率融合 [24 Zhen 2019]。
- **质量进入滤波器的三种接口**：① 判类别→选/弃量测（Kim、Yu、Chen、Wang）；② 判类别→调制 R（Zou、Guo、Juston、Dong、Barbieri）；③ 不显式判别→多模型/因子估计（Hyun IMM）。

## 八、必答问题逐条回答（速查）

1. **LOS 典型精度？** TWR 型 1–10 cm（工业场景）[8]；满带宽实测厘米级 [11]；低成本 TDOA+ESKF 全场 ≈10 cm RMSE [29]；DW1000 标称 10 cm [4]。须注明模式/硬件/场地。
2. **NLOS 恶化程度？** 轻遮挡 +30 cm 量级、硬遮挡 +1 m（原始 MAE ≈1.9 m）[3]；通用区间 >30 cm [8]；遮挡场景 RMSE 0.16–0.92 m [29]；严重时完全失锁 [29]。
3. **常见质量判断指标？** RSSI/接收功率、首径功率与功率差 Pd、SNR=Amf/σn、CIR 统计特征（峭度/平均超额时延/RMS 时延）、range residual/新息+卡方检验、分类器置信度、DOP/WPDOP/可定位性、可见性状态。来源 [2,3,4,13,18,21,22,24,28,29]。
4. **RSSI 是否足够？** 单场景二分类够（F1>0.9）[3]；跨环境/三分类不足（91.9%→72.9%）[4]；不平衡数据需专门检测器 [6]。结论：可作粗筛，不可单独定生死。
5. **CIR/first-path power/receive power/residual 的作用？** Pd=Pr−Pf 与 SNR 是 DW1000 官方质量量 [29]；功率差阈值 6/10 dBm 有实测分布支撑 [4]；CIR 特征支撑最强判别器 [1,2,5,7,8]；residual/卡方是滤波端最后防线 [13,18,29]。
6. **覆盖边缘如何表现/检测？** 表现：DOP 升高→定位误差放大 [22]、RMSE 恶化 3–9 倍 [29]、偏差位置相关且可重复 [29]；检测：DOP/WPDOP 计算 [21,22]、退化/可定位性模型 [24]、可见性状态跟踪 [28]。
7. **何时该降权？** 识别为 MP 或轻度 NLOS（偏差小但非零）、分类器置信度不足、DOP 偏高、时序指标边缘、动态遮挡后恢复期——对应自适应 R/加权文献 [16,18,19,22,25,28]；鲁棒与自适应适用条件不同，须先分型再处理 [18]。
8. **何时该拒绝？** 硬 NLOS/完全失锁 [3,29]、卡方检验未过的大离群 [29]、range 突变 [16]、地图/点云判明遮挡 [26,27]、"未能判为 LOS 的一律忽略"（Barral 2019 全文结论）[3]。
9. **基站数量与几何布局的影响？** 几何决定精度上限 [20]；窄空间 DOP 恶化不可避免但可加权抑制 [22]；WPDOP 优化布站改善 ≥37.6%（V 形最优）[21]；按区域差异化布站可在减少基站下保精度 [23]；巷道锚点部署策略影响精度维持 [15]。
10. **融合典型方法与自适应/鲁棒/剔除文献？** 见第六、七节：紧/松组合 EKF/ESKF、IMM、粒子滤波可见性跟踪、鲁棒 WLS、Sage-Husa/ANFIS 自适应、卡方剔除、ML NLOS 分类，条目齐全。

## 九、文献支持的决策框架（正常使用 / 降权 / 拒绝）

> **再次声明：此为文献框架，非本项目实测结论，所有阈值需后续实验确定。**

| 档位 | 触发条件（判据思路） | 处理 | 主要依据 |
|---|---|---|---|
| **A 正常使用** | ① 信号级：Pd=Pr−Pf 低于标定门限（文献起步参考：LOS<6 dBm [4]）、SNR 高 [29]；② 分类器判 LOS 且置信度高 [1,3,7,8]；③ 残差/新息通过卡方一致性检验 [29]；④ DOP/WPDOP 低于场地标定门限 [21,22]；⑤ 可见性状态=LOS [28] | 正常权重进入紧组合滤波 | [3,4,8,16,21,22,28,29] |
| **B 降权** | ① 判为 MP 或轻度 NLOS（Soft，偏差 +30 cm 量级）[3,4]；② 分类置信度处于中间带 [7,8]；③ DOP 偏高/窄空间/边缘区 [22,23]；④ 残差持续小-中幅偏大（未达剔除限）[18]；⑤ 动态遮挡后恢复期 [29] | 膨胀量测噪声 R / 自适应加权 / 鲁棒权函数；IMM 类可让 NLOS 因子连续吸收偏差 [16,17,18,19,22,25,28] | [3,4,16,17,18,19,22,25,28,29] |
| **C 拒绝（弃用）** | ① 判为硬 NLOS / 量测完全中断（UWB 数据缺失或物理层指标越过硬限）[3,29]；② 卡方检验拒绝的大离群 [29]；③ range 突变 [16]；④ LiDAR 点云/地图几何判明锚-标间存在遮挡 [26,27]；⑤ 连续多帧分类为 NLOS 且残差系统增大 | 该帧/该锚点量测直接剔除，由 IMU/轮速/LiDAR 短时顶替；若整片区域 DOP 恶化则 UWB 整体降级为不可用 | [3,16,26,27,29]（Barral 2019 原文："it seems more feasible to mitigate only the LOS measurements, whereas the rest (any measurement not classified as LOS) are simply ignored"） |

**框架落点提示**：本项目已有 LiDAR 与 ZED 2i，可同时启用信号级判据（Pd/SNR/残差）与外源几何判据（点云遮挡检测 [27]、地图判别 [26]）；UWB 质量状态机可仿照 [28] 用滤波器状态实现，档位切换对应 A/B/C。

## 十、引用论文清单（与 staging/UWB_raw.json 一致）

| # | 文献 | DOI | 核验 |
|---|---|---|---|
| 1 | Maranò et al., IEEE JSAC 2010 | 10.1109/jsac.2010.100907 | VERIFIED (摘要) |
| 2 | Güvenç et al., WCNC 2007 | 10.1109/wcnc.2007.296 | PARTIAL (venue 依 DOI 前缀推断) |
| 3 | Barral et al., Sensors 2019 | 10.3390/s19163464 | VERIFIED (摘要+全文) |
| 4 | Sang et al., Applied Sciences 2020 | 10.3390/app10113980 | VERIFIED (摘要+全文) |
| 5 | Jiang et al., IEEE Comm. Lett. 2020 | 10.1109/lcomm.2020.2999904 | VERIFIED (摘要) |
| 6 | Che et al., IEEE Sensors J. 2022 | 10.1109/jsen.2022.3198680 | VERIFIED (摘要) |
| 7 | Kim et al., IEEE IoT-J 2022 | 10.1109/jiot.2022.3209735 | VERIFIED (摘要) |
| 8 | Fontaine et al., IEEE IoT-J 2023 | 10.1109/jiot.2023.3299319 | VERIFIED (摘要) |
| 9 | Yu et al., IEEE TVT 2018 | 10.1109/tvt.2018.2883810 | VERIFIED (摘要) |
| 10 | Wymeersch et al., IEEE TComm 2012 | 10.1109/tcomm.2012.042712.110035 | VERIFIED (摘要) |
| 11 | Bellusci et al., ICUWB 2008 | 10.1109/icuwb.2008.4653448 | PARTIAL (venue 依 DOI 前缀推断) |
| 12 | Dardari et al., Proc. IEEE 2009 | 10.1109/jproc.2008.2008846 | VERIFIED (摘要) |
| 13 | Wang et al., Electronics 2023 | 10.3390/electronics12071678 | VERIFIED (摘要) |
| 14 | Hol et al., ICUWB 2009 | 10.1109/icuwb.2009.5288724 | PARTIAL (venue 依 DOI 前缀推断) |
| 15 | Li et al., IEEE Sensors J. 2020 | 10.1109/jsen.2020.2976097 | VERIFIED (摘要) |
| 16 | Zou et al., Sensors 2023 | 10.3390/s23135918 | VERIFIED (摘要) |
| 17 | Hyun & Myung, Sensors 2021 | 10.3390/s21237886 | VERIFIED (摘要) |
| 18 | Dong et al., Sensors 2023 | 10.3390/s23052669 | VERIFIED (摘要) |
| 19 | Juston et al., IEEE Sensors J. 2025 | 10.1109/jsen.2025.3549315 | VERIFIED (摘要) |
| 20 | Jourdan et al., IEEE TAES 2008 | 10.1109/taes.2008.4560210 | VERIFIED (摘要) |
| 21 | Cao et al., IEEE TIM 2023 | 10.1109/tim.2023.3250304 | VERIFIED (摘要) |
| 22 | Guo et al., Remote Sensing 2022 | 10.3390/rs14215409 | VERIFIED (摘要) |
| 23 | Jiang et al., J. Adv. Transportation 2022 | 10.1155/2022/3815306 | VERIFIED (摘要) |
| 24 | Zhen & Scherer, ICRA 2019 | 10.1109/icra.2019.8794167 | PARTIAL (venue 依 DOI 前缀推断) |
| 25 | Guo et al., IEEE Sensors J. 2022 | 10.1109/jsen.2022.3223974 | VERIFIED (摘要) |
| 26 | Wang et al., Remote Sensing 2021 | 10.3390/rs14010027 | VERIFIED (摘要) |
| 27 | Chen et al., Remote Sensing 2022 | 10.3390/rs14061380 | VERIFIED (摘要) |
| 28 | Barbieri et al., IEEE TIM 2021 | 10.1109/tim.2021.3074403 | VERIFIED (摘要) |
| 29 | Zhao et al., IJRR 2024 (arXiv:2203.14471) | 10.1177/02783649241230640 | VERIFIED (摘要+全文) |
| 30 | Alarifi et al., Sensors 2016 | 10.3390/s16050707 | VERIFIED (摘要) |

## 十一、未解决疑点

1. **4 篇 venue 标注为推断**（#2/#11/#14/#24）：OpenAlex venue 字段为 null，会议名依 DOI 前缀推断；记录本身（标题/作者/摘要）已完全核验。
2. **Sang 2020 中"MP 误差至 60 cm"为二手转引**（其引用 Schmid et al. IPIN 2019），引用时应注明"转引"。
3. **Kim 2022 / Zou 2023 / Dong 2023 等的部分百分比缺少更细条件**（如场地尺寸、GT 设备）——仅摘要可见，正文付费墙未抓取；方案书引用这些百分比时须注明"文献报告值，条件为其原文所述"。
4. **DW1000 功率差阈值（6/10 dBm）与 LOS 4.12/10.75 dBm 实测分布来自 Decawave 系模块**；本项目若选型不同（如 Qorvo DW3000 或其他厂商），阈值需在赛场实测重标定。
5. **"覆盖边缘"缺乏统一文献术语**：本文用 DOP/可定位性/可见性状态/遮挡实证四类证据拼合，属合理外推，未见单篇论文直接以"coverage edge"为题做系统研究（已在 rejected 记录中筛查过相关候选）。
