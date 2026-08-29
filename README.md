# DG-202611 Literature Evidence Repository

> **MASTER REVIEW START HERE**

本仓库是 DG-202611“基于具身智能的无人平台多源导航定位技术”的 **Literature Evidence Repository / Research Audit Mirror**，保存 ZCode 已产出的文献研究资产，供 MASTER 人工复核、交叉比较与独立审计。

**本仓库不是 DG-202611 开发代码仓库。** 它不包含 ROS2、Gazebo、算法实现或项目实验结果，也不修改已冻结的第 2 章或其他方案书文件。

## MASTER 推荐审阅顺序

1. [17_RESEARCH_SYNTHESIS_FOR_DG202611.md](17_RESEARCH_SYNTHESIS_FOR_DG202611.md) — 综合研究总结
2. [06_COMPETITION_METRIC_LITERATURE_AUDIT.md](06_COMPETITION_METRIC_LITERATURE_AUDIT.md) — 比赛指标文献审计
3. [05_CLAIM_EVIDENCE_MATRIX.md](05_CLAIM_EVIDENCE_MATRIX.md) — Claim–Evidence Matrix
4. [03_PERFORMANCE_BENCHMARK_MATRIX.csv](03_PERFORMANCE_BENCHMARK_MATRIX.csv) — 性能数字与条件矩阵
5. [16_CONFLICTING_EVIDENCE.md](16_CONFLICTING_EVIDENCE.md) — 冲突证据与口径冲突
6. [10_REJECTED_OR_UNVERIFIED.md](10_REJECTED_OR_UNVERIFIED.md) — 淘汰与未核验记录
7. [staging/VERIFY_report_V2.json](staging/VERIFY_report_V2.json) 与 [staging/VERIFY_report_V1.json](staging/VERIFY_report_V1.json) — 第二轮核验记录
8. [references.bib](references.bib) — 引用库
9. [staging/](staging/) — 原始检索、合并、冲突与 QA 过程

完整资产导航见 [INDEX.md](INDEX.md)，逐文件哈希与上传状态见 [REPOSITORY_MANIFEST.md](REPOSITORY_MANIFEST.md)，源目录一致性见 [SOURCE_INTEGRITY.md](SOURCE_INTEGRITY.md)，本地排除项见 [LOCAL_EXCLUDED_SENSITIVE_FILES.md](LOCAL_EXCLUDED_SENSITIVE_FILES.md)。

## 证据边界

仓库中的 `VERIFIED`、`PARTIAL`、`PARTIALLY_VERIFIED`、`REJECTED`、性能数字与文献结论，均表示研究证据状态，不会自动转换为 DG-202611 项目已实现性能。

```text
LITERATURE_REPORTED != PROJECT_RESULT
COMPETITION_REQUIREMENT != PROJECT_ACHIEVED
SIMULATION_RESULT != REAL_ROBOT_RESULT
ABSTRACT_VERIFIED != FULLTEXT_VERIFIED
SECONDARY_CHECK != PRIMARY_SOURCE
```

正式方案书引用前，仍需由 MASTER 决定相关材料是否进入正式证据体系。第三方论文全文未包含在本镜像中；仓库保留元数据、DOI、官方 URL、引用记录、证据摘要、性能矩阵与核验记录。

## 镜像范围

- 正式研究资产：17 份
- 引用库：`references.bib`
- 审计过程：`staging/`（排除一份临时网页缓存，详见排除记录）
- 导航与审计文件：本 README、INDEX、manifest、source integrity 和本地排除记录
- License：未自动添加，避免对第三方元数据和研究记录擅自声明许可
