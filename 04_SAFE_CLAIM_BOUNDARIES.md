# 04 SAFE CLAIM BOUNDARIES — 我们最多安全写多少

生成日期：2026-08-29
数据来源：`03_PERFORMANCE_BENCHMARK_MATRIX.csv`（仅使用 EXTRACTION_VERIFIED=VERIFIED/PARTIAL 的行）与 12–15 号专题评审。
**本文件回答一个问题：针对比赛关键指标，文献证据允许我们把方案书写到什么程度。**
核心纪律：LITERATURE_REPORTED（文献报道）/ COMPETITION_REQUIREMENT（比赛要求）/ PROJECT_DESIGN_TARGET（项目设计目标）/ SIMULATION_MEASURED（仿真实测）/ REAL_ROBOT_MEASURED（实车实测）五类口径严禁混淆。当前项目无任何 REAL_ROBOT_MEASURED 数据；UWB/毫米波雷达/事件相机均未实机集成。

---

## 1. 平面定位误差 < 20 cm

- **COMPETITION_REQUIREMENT**：平面定位误差 < 20 cm。
- **LITERATURE_BEST_REPORTED**：UWB LOS 工业场景 TWR 1–10 cm（UWB-08，Fontaine 2023，IoT-J）；室内 TDOA+ESKF ≈10 cm RMSE（UWB-29，UTIL，IJRR 2024，8 基站 DWM1000+Vicon GT）；开阔天空 RTK FIX 亚厘米~厘米级（GNSS 池 GNSS-12/GNSS-11，条件为短基线+良好天空视野）。
- **LITERATURE_TYPICAL_RANGE**：多源融合良好条件下 5–15 cm（UWB LOS / RTK FIX / LiDAR 近场匹配的组合）；一般室内外混合环境 10–30 cm；GNSS 单独在城市峡谷为 1 m 至数十米（GNSS-16：深峡谷 >30 m；GNSS 池 Bai 2020：密集城区最高 100 m）。
- **TEST_CONDITIONS**：所有 <20 cm 数值均有严格条件——UWB 需 LOS+标定过的基站几何；RTK 需 FIX 且开阔；LiDAR 需几何非退化（见第 8 条）。
- **DIRECTLY_COMPARABLE**：NO（部分）。文献的 <20 cm 都是"单一技术+良好条件"，我们是"多源融合+混合环境"，环境定义不同。
- **WHY**：文献证明各传感器在各自最优条件下都能达到 <20 cm，但没有任何论文保证"全场景 <20 cm"。融合的意义正是扩大 <20 cm 的适用范围，而不是证明更优的单点精度。
- **OUR_CURRENT_EVIDENCE**：NONE（未实测）。
- **SAFE_CURRENT_WORDING**（现在就能写）："文献表明 UWB（LOS，TWR，1–10 cm）、RTK（FIX，厘米级）与 LiDAR 匹配（近场）在各自适用条件下均可达到 20 cm 以内精度【UWB-08, UWB-29, GNSS-12】。本项目通过多源自适应融合，设计目标为在各自退化互补下维持 20 cm 以内的平面定位能力（PROJECT_DESIGN_TARGET）。"
- **SAFE_TARGET_WORDING**（作为目标）："设计目标：混合环境下平面定位误差 < 20 cm（COMPETITION_REQUIREMENT + PROJECT_DESIGN_TARGET）；预期由 RTK（开阔）+ UWB（室内/遮挡）+ LiDAR（局部退化时）接力保障。"
- **UNSAFE_WORDING**："本系统定位精度达 10 cm/6.8 cm/厘米级"（无实测、且把文献最优值写成项目能力）；"全场景 20 cm 以内"（无场景定义）。
- **NEEDED_EXPERIMENT**：开阔+遮挡+室内三类场景各 ≥10 条轨迹；RTK-RTK/全站仪或动作捕捉 GT；报告 2D RMSE + 95 分位，分场景统计。

## 2. 高程定位误差 < 20 cm

- **COMPETITION_REQUIREMENT**：高程定位误差 < 20 cm。
- **LITERATURE_BEST_REPORTED**：RTK FIX 开阔天空高程厘米级（GNSS-12/GNSS-11）；低成本 RTK（GNSS-10，NovAtel OEM615+手机端，城市，whole-solutions RMS）静态垂向 0.25 m、动态垂向 0.45 m（静态横向 0.15 m、动态横向 0.30 m）【FIX-002 修正 2026-08-30：原稿"高程 0.25–0.30 m"误将动态横向并入垂向】——低成本接收机高程是弱轴且动态下进一步恶化；LiDAR SLAM 高程依赖几何（Go-RIO RADAR-12：2.5 km 高程漂移 18 m = 0.72%——这是雷达里程计，反证非 RTK 源高程难达 20 cm 量级）。
- **LITERATURE_TYPICAL_RANGE**：RTK FIX 时 <10 cm；RTK FLOAT/遮挡时高程 0.3–1 m 量级；无 RTK 时（LiDAR/视觉里程计）漂移随里程增长，米级。
- **DIRECTLY_COMPARABLE**：NO。高程是文献公认的弱轴，<20 cm 高程实际上等价于"RTK FIX 可用率"指标。
- **WHY**：除 RTK 外，其余传感器（LiDAR/视觉/雷达/UWB）对高程的约束都明显弱于平面；UWB 三维定位的高程分量对基站几何极度敏感（UWB 池）。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："高程精度主要由 RTK FIX 保障；文献表明 RTK FIX 条件下高程可达厘米级，FLOAT/遮挡条件下显著恶化【GNSS-10, GNSS-12】。项目设计目标为 RTK 可用时段高程 <20 cm，并以气压计/IMU 约束 RTK 中断期的高程漂移（PROJECT_DESIGN_TARGET）。"
- **SAFE_TARGET_WORDING**："RTK FIX 时高程 <20 cm；RTK 退化期间以'高程漂移有界'替代'高程精度 <20 cm'表述。"
- **UNSAFE_WORDING**："高程精度 <20 cm"（不写条件——这实际上默认了 RTK 全程 FIX）；"多源融合保证高程 20 cm"。
- **NEEDED_EXPERIMENT**：RTK FIX/FLOAT 分状态统计高程误差；记录 fix type 时间占比作为配套指标。

## 3. 相邻帧有效特征重复率 ≥95%

- **COMPETITION_REQUIREMENT**：相邻帧有效特征重复率 ≥95%。
- **LITERATURE_BEST_REPORTED**：**NO_DIRECT_STANDARD_EQUIVALENT_FOUND**（详见 `06_COMPETITION_METRIC_LITERATURE_AUDIT.md` 专项审计）。
- **LITERATURE_TYPICAL_RANGE**：最接近的三个学术指标——①经典 repeatability rate（Schmid/Mohr/Bauckhage，IJCV 2000，跨视角检测器评价，ε 邻域定义，非相邻帧）；②percentage of tracked features over time（UZH RPG rpg_feature_tracking_analysis 事实参考实现）；③expected feature age / average track length（CVPR 2023）。均未以"相邻帧 ≥95%"形式报告，无法给出文献区间。
- **DIRECTLY_COMPARABLE**：NO——定义不同，禁止把上述任一指标当成同一指标引用。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："比赛指标'相邻帧有效特征重复率'在学术文献中无完全相同的标准定义；最接近的是特征检测 repeatability rate 与 VIO 特征跟踪保持率类指标。本项目将给出该指标的明确操作性定义（'有效'的判据、重复判定半径、统计窗口）并自建测试测量（COMPETITION_REQUIREMENT 口径）。"
- **UNSAFE_WORDING**："特征重复率 95% 符合学术界公认标准"（不存在该标准）；引用 repeatability rate 文献数值冒充本指标。
- **NEEDED_EXPERIMENT**：先在方案书定义公式，再在标准序列上报告该指标并与我们实现的其他指标（跟踪保持率）并列。

## 4. 重定位成功率 >95%

- **COMPETITION_REQUIREMENT**：重定位成功率 >95%。
- **LITERATURE_BEST_REPORTED**：GOReloc（RLC-17，RA-L 2024）：成功率随阈值与序列剧烈变化（Table II，纯平移阈值）——fr2_person：TE<5 m 96.11% → TE<2 m 64.87%；ICL-Data Diamond 'Head'：TE<5 m 38.23% → TE<2 m 17.43%【FIX-001 修正 2026-08-30：原稿将两序列数值并列误作"同序列"】。TE<1 m 下 ORB-SLAM2 仅 6.42%（Table III，fr2_person）；单帧重定位 19.025 ms。
- **LITERATURE_TYPICAL_RANGE**：文献"成功率"普遍在 50–96% 区间，但阈值（平移/旋转）、初始不确定度、评测序列定义各不相同。
- **DIRECTLY_COMPARABLE**：NO。成功率是一个"口径函数"，不定义口径的数值无意义（CF-19）。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："文献表明重定位成功率强烈依赖成功判据（GOReloc：同一方法因阈值从 5 m 收紧到 2 m，成功率在 fr2_person 从 96% 降至 65%，在 ICL-Data Diamond 'Head' 从 38% 降至 17%）【RLC-17】。本项目将按'位置+姿态双阈值+初始不确定度'定义成功率并在统一口径下报告。"
- **SAFE_TARGET_WORDING**："设计目标：在给定初始不确定度界与阈值（建议 0.25 m/5° 量级，最终以方案书定义为准）下重定位成功率 >95%（PROJECT_DESIGN_TARGET）。"
- **UNSAFE_WORDING**："重定位成功率 96%（文献已证明）"——那是别人在 5 m 阈值下的数字；不写阈值直接写 ">95%"。
- **NEEDED_EXPERIMENT**：绑架实验（多点、多初始不确定度档），报告成功率-阈值曲线与重定位时间分布。

## 5. 重定位时间

- **COMPETITION_REQUIREMENT**：重定位时间（比赛细则口径待查，需定义起点/终点）。
- **LITERATURE_BEST_REPORTED**：GOReloc 单帧重定位总耗时 19.025 ms（52.6 Hz）；ACR 2022 较基线快 1.6×（RLC/RELOC 池）。
- **LITERATURE_TYPICAL_RANGE**：算法级单帧处理 20–200 ms；"从丢位到恢复控制权"的系统级时间文献报告差异极大（含主动搜索行为时，秒级）。
- **DIRECTLY_COMPARABLE**：NO（算法时间 vs 系统恢复时间是两个量）。
- **SAFE_CURRENT_WORDING**：区分"候选生成/验证计算时间"（文献百毫秒内）与"主动重定位恢复全程时间"（含运动，秒级），分别声明。
- **UNSAFE_WORDING**："重定位时间 <100 ms"（混合了算法与系统口径）。
- **NEEDED_EXPERIMENT**：以"健康评估触发→位姿恢复→控制权交回"全链路计时，报告分布而非单值。

## 6. GNSS 拒止情况下定位误差

- **COMPETITION_REQUIREMENT**：GNSS 拒止情况下定位误差（比赛要求口径待细化：拒止时长/场景）。
- **LITERATURE_BEST_REPORTED**：轮式相关——GNSS/IMU/ODO/LiDAR-SLAM（GNSS-20，Sensors 2020）：2 分钟 GNSS 中断期间相对 GNSS/INS/ODO 的最大位置漂移 RMS 降低 62.8/72.3/52.1%（N/E/H）（ABSTRACT）；退化基准上界——GEODE（LDG-05，IJRR 2025）：FAST-LIO2 内陆水道长序列 ATE 70.26 m、盾构隧道全系统失败（>100 m）；城市峡谷 GNSS 自身误差 1 m 至 100 m（GNSS-16、GNSS 池 Bai 2020）。
- **LITERATURE_TYPICAL_RANGE**：拒止期误差由"拒止时长 × 退化场景 × 备援传感器"三元决定：室内/结构化环境 + LiDAR+UWB：分米级；退化几何（长走廊/隧道/开阔水面）：米级至数十米。
- **DIRECTLY_COMPARABLE**：NO（必须先固定拒止时长与场景类型）。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："文献表明 GNSS 拒止误差高度依赖时长与场景：结构化环境配合 LiDAR+UWB 可达分米级【UWB-29】，而退化几何场景下即使 SOTA LiDAR 惯性系统也可漂移数十米【LDG-05】。本项目设计目标：短时拒止（≤2 min）结构化场景误差有界（PROJECT_DESIGN_TARGET），并显式报告退化场景的降级行为。"
- **UNSAFE_WORDING**："GNSS 拒止下精度 <20 cm"（无时长/场景限定）；引用 62.8% 的"相对降幅"冒充绝对精度。
- **NEEDED_EXPERIMENT**：按 30s/1min/2min/5min 拒止时长 × 开阔/遮挡/室内三场景实测；报告绝对漂移而非相对改善。

## 7. UWB 辅助定位精度

- **LITERATURE_BEST_REPORTED**：LOS/TWR 工业场景 1–10 cm（UWB-08）；TDOA+ESKF 8 基站 ≈10 cm RMSE（UWB-29，Vicon GT，FULLTEXT）。
- **LITERATURE_TYPICAL_RANGE**：LOS 5–15 cm；轻度 NLOS（Soft）+30 cm 量级；硬遮挡 MAE ≈1.9 m、遮挡序列 RMSE 0.16–0.92 m、可完全失锁（UWB-03、UWB-29）。
- **DIRECTLY_COMPARABLE**：YES（对室内段），但必须绑定测距模式（TWR/TDOA）、基站数、几何与环境。
- **OUR_CURRENT_EVIDENCE**：NONE（老师已确认有现成 UWB 硬件，未验证）。
- **SAFE_CURRENT_WORDING**："UWB 在 LOS 条件下典型精度 1–10 cm（TWR）/约 10 cm（低成本 TDOA+ESKF 基准）；NLOS 下误差从 +30 cm（轻度）到米级（硬遮挡）甚至完全失锁【UWB-03, UWB-08, UWB-29】——这正是'信号稳定时使用、覆盖边缘或遮挡时降权/弃用'策略的文献依据。"
- **UNSAFE_WORDING**："UWB 精度 10 cm"（不写 LOS 条件与测距模式）；"UWB 全程可用"。
- **NEEDED_EXPERIMENT**：实测本项目硬件的 LOS/NLOS/边缘三档精度 + 质量指标（SNR/功率差/残差）与误差的相关性曲线。

## 8. 雷达退化环境辅助效果

- **LITERATURE_BEST_REPORTED**：浓烟场景 LiDAR 失败、LiDAR+Radar APE 1.133 m（RADAR-16，FULLTEXT，注意其为仿真去扫描实现）；雷达里程计 Boreas 0.26%（RADAR-05 DRO）；雪暴中 LiDAR-only 仍最准、雷达为"有竞争力补充"（RADAR-18）。
- **LITERATURE_TYPICAL_RANGE**：雷达里程计相对误差 0.26–2%；对雾/烟/尘/黑夜场景提供可用观测；对 LiDAR 是补充与冗余备份，不是全天候替代。
- **DIRECTLY_COMPARABLE**：NO（我们未集成雷达）。
- **OUR_CURRENT_EVIDENCE**：NONE（拟采购）。
- **SAFE_CURRENT_WORDING**："文献表明毫米波雷达在浓烟/浓雾/黑夜等 LiDAR/视觉退化场景可提供几何与 Doppler 观测（浓烟中 LiDAR+雷达融合 APE 1.133 m，LiDAR 单独失败）【RADAR-16, RADAR-07, RADAR-22】；雪暴等场景中 LiDAR 仍最准，雷达定位为补充/冗余而非替代【RADAR-18】。雷达型号采购与集成后另行实测。"
- **UNSAFE_WORDING**："毫米波雷达保证全天候定位"；把雷达里程计榜单百分比直接写成我们系统精度。
- **NEEDED_EXPERIMENT**：集成后按雾/尘/暗光/正常四档做消融（有/无雷达）。

## 9. 事件相机抗强光/暗光效果

- **LITERATURE_BEST_REPORTED**：HDR/高速下事件+帧+IMU 较帧+IMU 精度 +85%、较纯事件 +130%（EVENT-02 Ultimate SLAM，RA-L 2018）；20 fps RGB+事件相机等效 5000 fps 延迟（EVENT-09，Nature 2024）；双目事件 VIO DSEC 56.17 cm ATE（EVENT-04 ESVO2）。
- **LITERATURE_TYPICAL_RANGE**：事件相机动态范围 120–140 dB（传感器型号口径不同，CF-06）；**但暗光≠免疫**：暗光下光子噪声使 SNR 恶化，需去噪/SNR 感知处理（CF-08，EvLight++/Stereo-DEVO 共识）。
- **DIRECTLY_COMPARABLE**：NO（未采购未集成）。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："文献表明事件相机在 HDR/强反光/高速场景与帧相机互补，融合可显著提升退化场景精度【EVENT-02, EVENT-09】；暗光下事件输出仍受光子噪声限制，需 SNR 感知处理，并非'天然免疫'【CF-08】。"
- **UNSAFE_WORDING**："事件相机解决暗光问题"；"事件相机 140 dB 动态范围"（不注传感器型号与口径）。
- **NEEDED_EXPERIMENT**：采购后按强光逆光/暗光/高速转动三场景与 ZED 2i 做并列消融。

## 10. 北斗短报文通信能力【BDS-ASA-PATCH 2026-08-30 新增】

- **COMPETITION_REQUIREMENT**：北斗短报文应急链路集成（消息长度/发送频度硬约束）。
- **LITERATURE_BEST_REPORTED（官方规格）**：BDS-01（官网发布会口径）区域短报文单次 14000 比特/1000 汉字、全球短报文 560 比特/40 汉字；BDS-ASA-1.0（CSNO《应用服务体系（1.0版）》2019-12）表 5 RSMC：服务频度**一般 1 次/30 秒、最高 1 次/1 秒**、成功率 ≥95%、响应时延 ≤1 s、发射功率 ≤3 W 量级、容量约 1000 万次/小时；表 6 GSMC：成功率 ≥95%、时延 ≤1 分钟、560 比特。现行国标 GB/T 44087-2024 / GB/T 44086.1-2024 / GB/T 44086.2-2024（2024-05-28 发布实施，现行）规定终端技术要求与接口。
- **DIRECTLY_COMPARABLE**：NO。以上均为**官方系统服务指标**，不是任何项目终端的实测值。
- **OUR_CURRENT_EVIDENCE**：NONE。
- **SAFE_CURRENT_WORDING**："官方口径下 BDS-3 区域短报文单次 14000 比特（约 1000 汉字）、官方服务体系公开服务频度一般 1 次/30 秒、最高 1 次/1 秒【BDS-ASA-1.0 表5，系统服务指标】；项目终端实际可用频度受服务权限、终端能力、场景与运营条件影响，以实测为准。原型按'状态摘要+关键遥测'紧凑编码设计。"
- **SAFE_TARGET_WORDING**："设计目标：应急状态下以官方报文长度与频度约束为前提，每 N 秒上报一条 ≥ 关键状态遥测（N 由实测可用频度确定）。"
- **UNSAFE_WORDING**："发送频次无官方数值"（已被 BDS-ASA-1.0 证伪——2026-08-30 前的旧结论）；把官方频度写成 DG 实测；混用 RSMC/GSMC 参数（GSMC 仅 560 比特、时延 ≤1 分钟）；用北斗定位精度数字冒充短报文性能。
- **NEEDED_EXPERIMENT**：实际终端+服务权限下实测可达频度与时延；紧凑报文编码的遥测完整性验证。

---

## 汇总表

| 指标 | 文献最好值（条件） | 我们现在能写的 | 目标表述上限 |
|---|---|---|---|
| 平面 <20 cm | UWB LOS 1–10 cm；RTK FIX 厘米级 | 设计目标+文献条件化引用 | 混合环境设计目标 <20 cm |
| 高程 <20 cm | RTK FIX 厘米级 | 设计目标（绑定 RTK FIX 状态） | RTK FIX 时 <20 cm |
| 特征重复率 ≥95% | 无标准对应 | 自定义口径声明 | 定义后自测 |
| 重定位 >95% | 96.11% @5m 阈值（GOReloc，fr2_person 序列） | 阈值依赖性警示 | 双阈值定义后自测 |
| 重定位时间 | 单帧 19 ms；系统级秒级 | 分口径声明 | 全链路分布报告 |
| GNSS 拒止 | 分米级（结构化+LiDAR+UWB）至数十米（退化几何） | 条件化区间 | 短时拒止有界+降级行为声明 |
| UWB 精度 | LOS 1–10 cm | 条件化引用 | 集成后实测 |
| 雷达辅助 | 浓烟融合 1.133 m APE | 角色定位（补充/冗余） | 集成后消融 |
| 事件相机 | +85%（HDR/高速融合） | 互补性+SNR 限制 | 采购后消融 |
| 短报文 | 官方 14000/560 比特 + RSMC 频度 1次/30秒（一般）、1次/1秒（最高） | 官方系统指标引用+自测计划 | 终端实测后声明 |
