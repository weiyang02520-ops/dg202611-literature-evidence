# 06 COMPETITION METRIC LITERATURE AUDIT — 比赛指标文献审计

生成日期：2026-08-29
目的：逐项审查比赛关键指标在学术文献中的对应情况——是否存在相同定义、文献基准值是多少、哪些口径必须先定义才能比较。

---

## 审计 1：平面定位误差 < 20 cm

- **学术对应**：存在大量同型指标（2D RMSE / mean horizontal error / 2DRMS），定义基本一致（水平面位置误差），可比性最好。
- **文献基准**：
  - UWB：LOS/TWR 工业场景 1–10 cm（UWB-08）；室内 TDOA+ESKF ≈10 cm RMSE，Vicon GT（UWB-29，FULLTEXT）。
  - RTK：开阔天空 FIX 亚厘米~厘米级（GNSS-12）；低成本手机级 BDS/GPS RTK 静态平面 0.15 m（GNSS-10）【FIX-002 修正 2026-08-30：补注为"静态"横向值】。
  - LiDAR：X-ICP RPE 平移 0.17 m/10 m（LDG-02）；GenZ-ICP 相对平移误差 0.46–0.94%（FUSION-24）。
- **结论**：<20 cm 在各传感器各自最优条件下属于文献常规水平（非激进）；但"混合环境全程 <20 cm"没有文献先例保证，属设计目标。
- **审计判定**：指标合理；必须附场景分档报告。

## 审计 2：高程定位误差 < 20 cm

- **文献基准**：RTK FIX 高程厘米级（GNSS-12/GNSS-11）；低成本 RTK（GNSS-10，NovAtel OEM615+手机端，城市环境，whole-solutions RMS）：静态垂向 0.25 m、动态（50–80 km/h）垂向 0.45 m、静态横向 0.15 m、动态横向 0.30 m【FIX-002 修正 2026-08-30：原稿"高程 0.25–0.30 m"系把动态横向 0.30 与静态垂向 0.25 串成垂向区间，动态垂向实为 0.45 m，已按 MDPI 原文重核】；雷达/LiDAR 里程计高程漂移随里程线性增长（RADAR-12：2.5 km 高程 18 m）。
- **结论**：高程 <20 cm 实质上是"RTK FIX 保持能力"指标；无 RTK 时文献不支持该量级。
- **审计判定**：作为 RTK 可用时段的指标合理；作为全程指标偏激进，建议方案书绑定 fix type 表述。

## 审计 3：相邻帧有效特征重复率 ≥95%（专项审计）

- **完全相同定义检索结果**：**NO_DIRECT_STANDARD_EQUIVALENT_FOUND**。未检索到任何学术文献/标准使用"相邻帧有效特征重复率（≥95%）"这一定义。
- **最接近的学术指标**（按接近程度排序，**禁止与比赛指标混同**）：
  1. **Repeatability rate（特征重复率）**：Schmid, Mohr & Bauckhage, *Evaluation of Interest Point Detectors*（IJCV 2000）——定义"同一物理点在不同视角图像中被重复检测出的比例"，以 ε 邻域（约 1.5–2.5 px 投影半径）判定；用于检测器跨视角评价，**不是相邻帧、且数值由检测器与环境决定，不能直接迁移 95% 阈值**。（来源：[HAL-Inria 论文页](https://inria.hal.science/inria-00548302/document)；[Semantic Scholar 条目](https://www.semanticscholar.org/paper/Evaluation-of-Interest-Point-Detectors-Schmid-Mohr/2713e7a59105a832e20c01c3c202b9dcd2b5f889)）
  2. **Percentage of tracked features over time（随时间被成功跟踪的特征百分比）**：VIO 前端跟踪质量的事实标准绘图指标，UZH RPG 的 [rpg_feature_tracking_analysis](https://github.com/uzh-rpg/rpg_feature_tracking_analysis) 工具箱为其参考实现；**与"相邻帧有效特征重复率"语义最接近，但仍是"跟踪保持率"而非"重复率"**。
  3. **Expected feature age / average track length（特征期望寿命/平均跟踪长度）**：Messikommer et al., Data-driven Feature Tracking for Event Cameras（CVPR 2023）补充材料；衡量跟踪持续性。（来源：[CVPR 2023 supplementary](https://openaccess.thecvf.com/content/CVPR2023/supplemental/Messikommer_Data-Driven_Feature_Tracking_CVPR_2023_supplemental.pdf)）
  4. **Feature tracking rate**：部分 KLT 跟踪器论文使用（如 gyro-aided KLT 大运动场景），但无统一公式。
- **审计结论**：
  1. 比赛该指标需要我们**自行给出操作性定义**："有效"的判据（被跟踪/被匹配/通过外点剔除？）、重复判定几何（像素距离/描述子距离）、统计窗口（相邻帧 or 短序列）、分子分母。
  2. 文献不支持也不否定 95%——该数值只能作为比赛要求（COMPETITION_REQUIREMENT）引用，不能声称"符合学术标准"。
  3. 建议方案书同时报告"percentage of tracked features"作为可对照的文献口径，建立学术沟通桥梁。

## 审计 4：重定位成功率 >95%

- **学术对应**：存在（success rate / relocalization success），但**定义不统一**——成功阈值（平移/旋转）、初始不确定度、测试协议各论文不同。
- **文献基准**：GOReloc（RLC-17，RA-L 2024）。【FIX-001 修正 2026-08-30：原稿误将 ICL Diamond 'Head' 的 @2m 值 17.43% 记为 TUM fr2_person 的数值，已按原文 Table II/III 重核】正确口径（成功率均为纯平移阈值，Table II 无旋转列）：
  - TUM RGB-D fr2_person（Table II）：TE<5 m 成功率 96.11%、TE<2 m 64.87%；
  - ICL-Data Diamond 'Head'（Table II）：TE<5 m 38.23%、TE<2 m 17.43%；
  - fr2_person 上另一张与特征法 ORB-SLAM2 同序列对比表（Table III，紧阈值 @0.5/1/2/3 m）：GOReloc 3.52%/22.79%/53.26%/70.17%，ORB-SLAM2 1.97%/6.42%/9.12%/9.17%（即 TE<1 m 下 ORB-SLAM2 仅 6.42%）；
  - 单帧重定位 19.025 ms（TUM RGB-D）/ 17.540 ms（ICL-Data）。
- **审计结论**：>95% 只有在宽松阈值（米级平移）下文献可达；紧阈值（分米级+姿态）下 >95% 无文献支持。**比赛指标 >95% 的合理性完全取决于其成功率定义**——需向主办方确认阈值；方案书必须先固定口径。
- **审计判定**：条件性合理；强烈建议双阈值报告（成功率-阈值曲线）。

## 审计 5：重定位时间

- **文献基准**：算法级单帧：GOReloc 19.025 ms；系统级（含主动搜索/运动恢复）：秒级且少有论文报告分布。
- **审计结论**：必须区分"计算时间"与"恢复全程时间"两个口径分别报告；比赛若未定义，建议我们主动给出定义（触发→恢复→控制权交回）。

## 审计 6：北斗短报文集成验证

- **官方规格**：BDS-01（beidou.gov.cn，官方发布会口径，本库经官网页面原文核验）：区域短报文 14000 比特/次（1000 汉字）；全球短报文 560 比特/次（40 汉字）；全球实测定位精度周均值 2.34 m；国际搜救检测概率 >99%。
- **学术支撑**：BDS-02（GSMC 架构，Adv. Space Res. 2021）、BDS-03（BDS-3 特色服务性能）、BDS-08（UAV 路径重规划应用）。
- **已核验边界**：短报文**发送频次限制无官方公开数值**（GNSS 组核验记录），方案书与原型设计不得引用任何频次数字；区域/全球服务能力差异必须写明。
- **审计判定**：原型集成可行（消息长度约束明确）；性能声明只能绑定官方规格与后续自测。

## 汇总

| 比赛指标 | 文献相同定义 | 文献可达性 | 审计判定 |
|---|---|---|---|
| 平面 <20 cm | 有（2D RMSE 等） | 各自最优条件常规水平 | 合理，需分场景 |
| 高程 <20 cm | 有 | 仅 RTK FIX 条件 | 条件性合理 |
| 特征重复率 ≥95% | **无（NO_DIRECT_STANDARD_EQUIVALENT_FOUND）** | 无文献基准 | 需自定义口径+自测 |
| 重定位 >95% | 有但口径不一 | 宽松阈值可达 | 先定义口径 |
| 重定位时间 | 有但口径不一 | 算法级 20–200 ms | 分口径报告 |
| 北斗短报文 | 官方规格明确 | 规格硬约束 | 可集成，频次无官方数字 |
