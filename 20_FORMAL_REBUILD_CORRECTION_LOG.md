# 20 FORMAL REBUILD CORRECTION LOG — P0 修复轮纠错与变更日志

记录日期：2026-08-30（ZCode P0 增量修复轮，TASK: DG202611_LITERATURE_P0_DELTA_REPAIR_AND_FREEZE）
规则：本文件永久保留。任何对已发布聚合资产的数值修正，必须在此登记"旧值 → 新值 → 证据 → 波及文件"，且不允许只改一个文件。

---

## CORRECTION-001（FIX-001）：GOReloc 成功率序列归属错误

- **发现途径**：MASTER 冻结前人工审计确认 `06_COMPETITION_METRIC_LITERATURE_AUDIT.md` 存在 `TUM fr2_person @ <2m = 17.43%` 错误。
- **旧值（错误关联）**："GOReloc 在 TUM fr2_person 上：TE<5 m 成功率 96.11%、TE<2 m 17.43%"——把两个不同序列的数值并列成同序列阈值对比；04 号文件更以"同方法同序列，TE<5 m 96.11% vs TE<2 m 17.43%"作为成功率口径警示的论据。
- **新值（正确口径）**（依据：arXiv:2408.07917 HTML 全文 Table II/III，2026-08-30 重读，含列定义确认）：
  - Table II（Object-level 对比；成功判据=纯平移阈值，四列依次为 成功率@2m、成功率@5m、TE best-10%、TE best-20%，无旋转列）：
    - ICL-Data Diamond 'Head'：GOReloc **17.43% @2m / 38.23% @5m**；
    - TUM RGB-D fr2_person：GOReloc **64.87% @2m / 96.11% @5m**。
  - Table III（fr2_person，与特征法 ORB-SLAM2 同序列对比，紧阈值 @0.5/1/2/3 m）：GOReloc 3.52%/22.79%/53.26%/70.17%；ORB-SLAM2 1.97%/6.42%/9.12%/9.17%。
  - 单帧耗时：19.025 ms（52.6 Hz, TUM RGB-D）；17.540 ms（57.0 Hz, ICL-Data）。
- **波及文件（全部已修复，未只改一个文件）**：
  1. `06_COMPETITION_METRIC_LITERATURE_AUDIT.md`（审计 4 文献基准整段重写，标注 FIX-001）；
  2. `04_SAFE_CLAIM_BOUNDARIES.md`（LITERATURE_BEST_REPORTED 序列拆分、SAFE_CURRENT_WORDING "96%→17%" 改为分序列 "96%→65%（fr2_person）/38%→17%（Diamond 'Head'）"、汇总表 96.11% 行补 fr2_person 归属）；
  3. `02_FILTERED_CORE_PAPERS.md`（RLC-17 关键证据行按序列拆分）；
  4. `16_CONFLICTING_EVIDENCE.md`（CF-19 注记补充 Diamond 'Head' 防混写警示）。
- **未波及（核验后确认本来正确）**：`01_RAW_LITERATURE_POOL.csv`（RLC-17 行）、`03_PERFORMANCE_BENCHMARK_MATRIX.csv`（PM-174/175 及 RLC-17 全部行，Diamond 'Head' 归属正确）、`staging/RELOCSYNC_raw.json`、`staging/verify_task.json`、`staging/VERIFY_report_V1.json`、`staging/perf_flags.json`。
- **grep 复验**：全库（排除 staging 缓存与本日志注记）`17.43` 现均正确绑定 ICL-Data Diamond 'Head'；`fr2_person` 相关联数值均为 64.87/96.11 或 Table III 紧阈值组。
- **残留风险**：无。staging 原始抓取缓存保留旧摘要字符串属历史快照，不作引用来源。

---

## CORRECTION-002（FIX-002）：低成本 RTK 高程数值横向/垂向、静态/动态串位

- **发现途径**：MASTER 冻结前人工审计确认聚合表述"低成本RTK高程0.25–0.30 m"存在串位。
- **旧值（错误口径）**："手机级 BDS/GPS RTK 高程 0.25–0.30 m（GNSS-10）"——0.25 m 是**静态垂向**，0.30 m 是**动态横向**，两者拼接成虚假的"高程区间"；动态垂向真实值缺失（摘要截断处）。
- **新值（四口径齐备）**（依据：MDPI 原文全文 web_reader 重读，含 Table 2/4 逐测段数值，2026-08-30）：
  - GNSS-10（Wang et al., Sensors 2016, 10.3390/s16122201；NovAtel OEM615 模块 + Samsung Galaxy A7，北京城区，cutoff 15°）：
    - **static horizontal = 0.15 m**（whole solutions RMS；固定解 H≤0.03 m）
    - **static vertical = 0.25 m**（whole solutions RMS；固定解 V≤0.04 m）
    - **dynamic horizontal = 0.30 m**（whole solutions RMS；固定解 H 约 0.10 m）
    - **dynamic vertical = 0.45 m**（whole solutions RMS；固定解 V 约 0.13 m）
    - whole solutions 逐测段：静态 S1 0.14/0.25、S2 0.15/0.21、S3 0.07/0.09；动态 K1 0.24/0.40、K2 0.28/0.47、K3 0.32/0.45（H/V，m）。
- **波及文件（全部已修复）**：
  1. `06_COMPETITION_METRIC_LITERATURE_AUDIT.md`（审计 2 文献基准整段重写，标注 FIX-002）；
  2. `04_SAFE_CLAIM_BOUNDARIES.md`（高程 <20 cm 条目的 LITERATURE_BEST_REPORTED 四口径重写）；
  3. `03_PERFORMANCE_BENCHMARK_MATRIX.csv`（PM-126/127 升级 ABSTRACT→FULLTEXT 并补动态垂向 0.45；**新增 PM-190/191 固定解两行**——低成本 RTK FIX 高程厘米级的直接证据，支撑 ALTITUDE_20CM 口径拆分）；
  4. `01_RAW_LITERATURE_POOL.csv`（GNSS-10 行验证证据补全文核验记录，截断注记关闭）；
  5. `07_TERMINOLOGY_AND_METRIC_DEFINITIONS.md`（新增词条 whole-solutions vs fixed-solutions RMS）。
- **grep 复验**：`0.25–0.30`/`0.25-0.30` 模糊高程区间表述已全库清除（仅本日志与修正注记中作为历史记录保留原文引用）。
- **连带口径修正**：`04_SAFE_CLAIM_BOUNDARIES.md` 高程 <20 cm 的安全表述从此拆分为"RTK FIX（固定解）高程厘米级≈可达 <20 cm；whole solutions/退化期动态垂向 0.45 m 量级"两档，禁止再合并表述。
- **残留风险**：无。PM-125（固定率 90%）仍为 ABSTRACT 级未独立复核，但该值与摘要原文一致且非本轮错误对象。

---

## 本轮其他资产变更（非纠错，均为 P0 增量）

| 文件 | 变更 |
|---|---|
| `01_RAW_LITERATURE_POOL.csv` | 新增 9 行：GNSS-27、GNSS-28、LDG-18、VIS-01、FRM-01、RLC-19、RLC-20（NEW-01~07）+ RLC-21、RLC-22（GAP-4 补查）；池总量 239→248 |
| `02_FILTERED_CORE_PAPERS.md` | 新增 "P0 增量修复轮新增核心"表（7 篇）；总量口径 60/30→67/37 |
| `03_PERFORMANCE_BENCHMARK_MATRIX.csv` | 新增 PM-192~PM-199（8 行，全部标注证据等级与引用边界） |
| `05_CLAIM_EVIDENCE_MATRIX.md` | CLAIM-04/07/11 证据行扩充（LDG-18/GNSS-27/RLC-20/RLC-21）；CLAIM-11 强度 MODERATE→STRONG（附口径警示） |
| `07_TERMINOLOGY_AND_METRIC_DEFINITIONS.md` | 新增 repeatability denominator family、success threshold 实例对照、whole vs fixed solutions RMS、PLD 四组词条 |
| `16_CONFLICTING_EVIDENCE.md` | 新增 CF-28（RLC-19 级联 vs 穷举、仿真 vs 异构真实自相张力） |
| `11_SEARCH_LOG.md` | 追加 342–354 共 13 条本轮检索与核验记录（含失败通道记录） |
| `references.bib` | 新增 9 条（239→248） |
| `staging/P0_DELTA_raw.json`、`staging/VERIFY_report_V3.json`、`staging/append_p0_rows.py`、`staging/append_p0_matrix.py`、`staging/fix_matrix_commas.py` | 本轮原始抓取与核验记录、执行脚本（过程留痕） |
| `18_FORMAL_REBUILD_P0_NEW_LITERATURE.md` | 新建：7 篇新增文献逐篇档案与证据边界 |
| `19_FORMAL_REBUILD_CLAIM_REFERENCE_MAP.md` | 新建：五大 claim 的文献映射（ALTITUDE_20CM / FEATURE_REPEATABILITY_95 / RELOCALIZATION_95 / ACTIVE_RELOCALIZATION / UWB_QUALITY_GATE） |

---

## CORRECTION-003（BDS-ASA-PATCH 2026-08-30）：短报文"发送频次无官方公开数值"结论被官方文件证伪

- **发现途径**：MASTER 新一轮官方核验指出《北斗卫星导航系统应用服务体系（1.0版）》（CSNO，2019-12）已公开 RSMC 服务频度。
- **旧结论（错误）**："短报文**发送频次限制无官方公开数值**（GNSS 组核验记录），方案书与原型设计不得引用任何频次数字"（06 审计审计6；05 CLAIM-10 CONDITIONS/UNSAFE；17 综合 §12）。
- **新结论（正确口径）**：官方应用服务体系 BDS-ASA-1.0 表 5"区域短报文通信服务（RSMC）"公开服务频度**一般 1 次/30 秒、最高 1 次/1 秒**（另含成功率 ≥95%、响应时延 ≤1 s、终端发射功率 ≤3 W 量级、容量约 1000 万次/小时、报文 14000 比特）；表 6"GSMC"公开成功率 ≥95%、响应时延 ≤1 分钟、报文 560 比特。此为**官方系统服务指标**：项目终端实际可用频度受服务权限、终端能力、场景与运营条件影响，必须以实际终端与服务配置验证，不得写成 DG 实测结果。
- **证据**：北斗官网解读页（原文级：文件名/发布机构/日期封面照 + "容量提升10倍、用户功率降至3W"）；gov.cn 白皮书《新时代的中国北斗》（14000 比特/1000 汉字、560 比特/40 汉字）；openstd.samr.gov.cn 三条现行国标（GB/T 44087-2024、GB/T 44086.1-2024、GB/T 44086.2-2024，2024-05-28 发布/实施，归口中央军委装备发展部）。
- **波及文件**：`04`（新增 §10 + 汇总行）、`05`（CLAIM-10 重写）、`06`（审计6 重写 + 汇总行）、`07`（新增 RSMC/GSMC 及三参数辨析词条）、`11`（355–359）、`17`（§12 修正）、`19`（新增 CLAIM MAP-6）、`01`（BDS-11/BDS-12/BDS-STD-01..03，池 248→253）、`03`（PM-200/201/202，矩阵 199→202）、`references.bib`（+5，248→253）、`21`（补丁报告新建）。
- **grep 复验**：正式资产中"发送频次限制无官方公开数值/频次无官方数字/无官方数值"表述仅存于本日志与修正注记的历史引用中，作为现行结论已全部替换。
- **残留风险**：表值细项（成功率/时延/容量）为"官方文件转载交叉级"（官方原 PDF 未在官网提供下载），直接引用细项前建议以官方原件复核；已在 21 号文件登记为遗留事项。

---

## 未决事项（移交 MASTER）

1. **付费墙待补**（四篇 Elsevier，详见 18 号文件逐篇边界）：GNSS-27 的 East/North/Up 绝对值；LDG-18 的 41.29% 对比基线、LiDAR 型号、ground-plane 细节；VIS-01 的 X/Y/Z 误差、数据集、传感器配置。取得全文后必须回写矩阵并复核 18/19 号文件边界。
2. **开放空缺**：动态目标移除后的 LiDAR 特征重复率直接量化文献（2025–2026 定向检索未命中）——以 LDY 池 + FRM-01 方法论邻接支撑，需自测补位。
3. **PREPRINT 隔离**：RLC-22（UQ-Loc）在正式发表前不入 CORE、不入方案书引用主体。
