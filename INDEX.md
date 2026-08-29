# DG-202611 正式研究资产索引

本索引依据 17 份实际文件的标题、章节、字段和内容建立，不改变任何原始研究结论。优先级用于 MASTER 审阅导航，不代表证据等级。

| 编号 | 文件名 | 用途与主要内容 | 性能数字 | 引用 | 综合资产 | 审核优先级 |
|---:|---|---|:---:|:---:|:---:|:---:|
| 01 | [`01_RAW_LITERATURE_POOL.csv`](01_RAW_LITERATURE_POOL.csv) | 239 条原始文献池；记录元数据、研究方向、相关性、核验状态、核验依据与性能数据计数 | 是 | 是 | 否 | 中 |
| 02 | [`02_FILTERED_CORE_PAPERS.md`](02_FILTERED_CORE_PAPERS.md) | 60 篇高价值论文与其中 30 篇核心证据论文的筛选结果、入选理由和淘汰记录 | 是 | 是 | 否 | 高 |
| 03 | [`03_PERFORMANCE_BENCHMARK_MATRIX.csv`](03_PERFORMANCE_BENCHMARK_MATRIX.csv) | 189 条条件绑定性能记录；含场景、传感器、指标定义、数值、来源层级、限制与独立核验字段 | 是 | 是 | 否 | 最高 |
| 04 | [`04_SAFE_CLAIM_BOUNDARIES.md`](04_SAFE_CLAIM_BOUNDARIES.md) | 对平面/高程误差、特征重复率、重定位、GNSS 拒止、UWB、雷达与事件相机声明划定安全边界 | 是 | 是 | 是 | 最高 |
| 05 | [`05_CLAIM_EVIDENCE_MATRIX.md`](05_CLAIM_EVIDENCE_MATRIX.md) | 将 12 类技术主张绑定证据、强度、适用条件、安全措辞、禁用措辞与所需项目验证 | 是 | 是 | 是 | 最高 |
| 06 | [`06_COMPETITION_METRIC_LITERATURE_AUDIT.md`](06_COMPETITION_METRIC_LITERATURE_AUDIT.md) | 审计平面/高程定位、特征重复率、重定位、重定位时间和北斗短报文等比赛指标 | 是 | 是 | 是 | 最高 |
| 07 | [`07_TERMINOLOGY_AND_METRIC_DEFINITIONS.md`](07_TERMINOLOGY_AND_METRIC_DEFINITIONS.md) | 统一轨迹误差、重定位、特征匹配、卫星导航、滤波估计和传感器系统术语及使用规则 | 是 | 是 | 否 | 高 |
| 08 | [`08_DATASET_CATALOG.md`](08_DATASET_CATALOG.md) | 多源导航公开数据集总表、按退化场景的选用建议及使用注意事项 | 是 | 是 | 否 | 中 |
| 09 | [`09_OPEN_SOURCE_IMPLEMENTATION_MAP.md`](09_OPEN_SOURCE_IMPLEMENTATION_MAP.md) | 多源导航开源实现总表、按项目模块的选型建议及使用注意事项 | 否 | 是 | 否 | 中 |
| 10 | [`10_REJECTED_OR_UNVERIFIED.md`](10_REJECTED_OR_UNVERIFIED.md) | 分技术组保存 rejected、unverified、重复或不宜使用的证据，以及性能数字核验问题 | 是 | 是 | 否 | 最高 |
| 11 | [`11_SEARCH_LOG.md`](11_SEARCH_LOG.md) | 分 UWB、雷达、事件、融合、GNSS、LiDAR、重定位/同步、仿真、数据集和开源组保存检索日志 | 否 | 是 | 否 | 中 |
| 12 | [`12_UWB_QUALITY_AND_REJECTION_REVIEW.md`](12_UWB_QUALITY_AND_REJECTION_REVIEW.md) | UWB 误差、LOS/NLOS、覆盖边缘、质量指标、融合与正常使用/降权/拒绝决策框架 | 是 | 是 | 否 | 高 |
| 13 | [`13_MMWAVE_RADAR_LOCALIZATION_REVIEW.md`](13_MMWAVE_RADAR_LOCALIZATION_REVIEW.md) | 毫米波雷达能力、频段、接口、同步、数据集、算法性能、采购边界与遗留疑点 | 是 | 是 | 否 | 高 |
| 14 | [`14_EVENT_CAMERA_ZED_SYNC_REVIEW.md`](14_EVENT_CAMERA_ZED_SYNC_REVIEW.md) | 事件相机与 ZED 2i 的时间模型、软硬件同步选项、风险和推荐研究方向 | 是 | 是 | 否 | 高 |
| 15 | [`15_ADAPTIVE_FUSION_EVIDENCE_REVIEW.md`](15_ADAPTIVE_FUSION_EVIDENCE_REVIEW.md) | 质量感知融合的指标来源、不确定度、协方差自适应、门控、故障检测、阈值边界与局限 | 是 | 是 | 否 | 高 |
| 16 | [`16_CONFLICTING_EVIDENCE.md`](16_CONFLICTING_EVIDENCE.md) | 保存实质性结论冲突、元数据冲突、第二层性能核验问题和平台/工具记录 | 是 | 是 | 是 | 最高 |
| 17 | [`17_RESEARCH_SYNTHESIS_FOR_DG202611.md`](17_RESEARCH_SYNTHESIS_FOR_DG202611.md) | 综合回答成熟路线、项目路线合理性、各传感器角色、同步标定、融合、重定位和指标可声明边界 | 是 | 是 | 是 | 最高 |

## 补充入口

- 引用库：[`references.bib`](references.bib)
- 全过程审计：[`staging/`](staging/)
- 逐文件完整性：[`REPOSITORY_MANIFEST.md`](REPOSITORY_MANIFEST.md)
