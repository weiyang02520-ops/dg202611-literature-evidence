# 11 SEARCH LOG — 检索日志

生成日期：2026-08-29
本文件汇总 8 个研究组全部检索查询（含失败与限流记录），供复查检索覆盖面与复现。

总查询记录：341 条（覆盖 10 个组；个别组另执行了批量 DOI 解析等未逐条计数的操作，详见各组日志原文 staging/*_searchlog.json）。


## UWB 组（22 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 1 | UWB NLOS identification | OpenAlex API (python urllib, https://api.openalex.org/works?search=...) | 8 | 1 | 6 | 命中 Maranò 2010 JSAC（收录）；同时命中 Güvenç WCNC 2007（后改由查询9核验收录）；rejected: Khodjaev 2009 综述(旧)、Li 2013 ICCT、Zeng 2019 ICCE、Wu 2024 IoT-J TinyML、Deng 2023 GAF |
| 2 | UWB NLOS mitigation | OpenAlex API | 8 | 3 | 2 | 命中并收录 Kim 2022 IoT-J、Yu 2018 TVT、Wang 2023 Electronics 综述、Barral 2019 Sensors（同页复现）；rejected: Yang 2018 SPGP（纯仿真）、Khodjaev 2009 |
| 3 | UWB positioning accuracy LOS NLOS | OpenAlex API | 8 | 1 | 3 | 命中并收录 Jiang 2020 Comm. Letters；Jourdan 2008 TAES 亦在此页出现（经单篇 DOI 抓取核验后收录）；rejected: Yang 2021 JSEN(IMU虚拟点补偿)、Cui 2020 MWT-CNN（纯仿真）、Yang 2023 JSEN SVM |
| 4 | tightly coupled UWB IMU | OpenAlex API | 7 | 1 | 4 | 命中并收录 Hol 2009 ICUWB；rejected/未收录: Miraglia 2017、Wen 2020 TVT（行人）、Xu 2016 i2MTC、Nguyen 2021 VIRAL SLAM arXiv:2105.03296（池上限） |
| 5 | UWB inertial odometry | OpenAlex API | 7 | 1 | 5 | 命中并收录 Hyun & Myung 2021 NR-UIO；未收录: Lin 2022 Measurement、Gao 2022 IET、Shin 2021 MIR-VIO、Delama 2023 UVIO、Xu 2022 Omni-Swarm T-RO |
| 6 | UWB GNSS integration fusion | OpenAlex API | 7 | 2 | 1 | 命中并收录 Guo 2022 JSEN(GNSS/UWB时间标定+自适应加权)、Di Pietra 2020（后按池上限让位给 Wang 2021，记 rejected）；Alarifi 2016 与 Barbieri 2021 亦复现；rejected: Hsu 2017（GNSS 多径 ML，非 |
| 7 | UWB ranging error model | OpenAlex API | 7 | 3 | 3 | 命中并收录 Bellusci 2008（误差模型）、Dardari 2009 Proc. IEEE、Wymeersch 2012 TComm；rejected: Dizdarevic 2007、Şahinoğlu 2006、Perakis 2018 IPIN（池上限/重叠） |
| 8 | UWB anchor placement geometry dilution of precision | OpenAlex API | 6 | 3 | 3 | 命中并收录 Cao 2023 TIM(WPDOP)、Guo 2022 Remote Sensing(窄空间DOP)、Jiang 2022 JAT(停车场布站)；未收录: Albaidhani 2019、Wang 2020 IEEE Access(DOP适用性)、Fontaine 2020 autoe |
| 9 | robust adaptive Kalman filter UWB localization | OpenAlex API | 6 | 4 | 1 | 命中并收录 Dong 2023 IRACKF、Juston 2025 JSEN(轮式差分机器人)、Li 2020 JSEN(井下ESKF)、Zou 2023 Sensors(自适应R)；rejected: Chen 2015 WiFi/PDR（非UWB） |
| 10 | UWB RSSI first path power NLOS features | OpenAlex API | 6 | 1 | 3 | 命中并收录 Che 2022 JSEN(GGD)；Barral 2019 复现；未收录: Barral 2020 PDP加速（同团队重叠）、Ridolfi 2021 ACM CSUR、Leitch 2023 多技术综述 |
| 11 | UWB indoor positioning survey review | OpenAlex API | 6 | 1 | 5 | 命中并收录 Alarifi 2016 Sensors 综述；rejected: Al-Fuqaha 2015 IoT、Yassin 2016、Brena 2017、Mautz 2012、Mazhar 2017（通用/重叠） |
| 12 | UWB dataset LOS NLOS public | OpenAlex API | 6 | 3 | 2 | 命中并收录 Sang 2020 Applied Sciences、Zhao 2024 IJRR UTIL 数据集、Fontaine 2023 IoT-J 迁移学习；rejected: Leitch 2023、Wang 2025 JESTCH（与 Fontaine 2023 重叠） |
| 13 | GNSS UWB tightly coupled urban canyon | OpenAlex API | 6 | 2 | 2 | 命中并收录 Wang 2021 Remote Sensing(无缝GNSS/UWB/INS/地图)、Chen 2022 Remote Sensing(UWB/LiDAR NLOS识别)；rejected: Wang 2016 V2I GPS/INS/UWB（池上限）、Gakne 2018（GNSS/ |
| 14 | UWB number of anchors accuracy experimental | OpenAlex API | 6 | 0 | 3 | 主要为已收录文献复现（Li 2020、Barbieri 2021、Wymeersch 2012）；rejected/未收录: Poulose 2020 LSTM、Ridolfi 2018 运动姿态实测、Djosic 2020 指纹 |
| 15 | UWB LiDAR fusion robot localization | OpenAlex API | 6 | 1 | 3 | 命中并收录 Zhen & Scherer 2019 ICRA(隧道可定位性)；Chen 2022 RS 复现；rejected: Song 2019 ICRA 合作SLAM、Alatise 2020 综述、Xu 2022 3D LiDAR SLAM 综述 |
| 16 | "ultra-wideband time-difference-of-arrival indoor localization dataset"（UTIL 数据集 arXiv 版本确认） | arXiv API (export.arxiv.org/api/query, curl+python) | 5 | 1 | 0 | 确认 UTIL = arXiv:2203.14471（v6，2022-03-28 首发，2024 刊于 IJRR DOI 10.1177/02783649241230640） |
| 17 | MDPI 全文直连 https://www.mdpi.com/1424-8220/19/16/3464/htm 与 /2076-3417/10/11/3980/htm | curl (python urllib) | 2 | 0 | 0 | HTTP 403 Forbidden（反爬），放弃直连，改用 mcp web_reader 抓取同站正文页成功 |
| 18 | Barral 2019 Sensors 全文抓取 | mcp web_reader (https://www.mdpi.com/1424-8220/19/16/3464) | 1 | 1 | 0 | 获取全文：NLOS Soft/Hard 误差、GP 校正后 MAE、二分类 F1、CIR 读取 300 ms、'非 LOS 直接忽略'结论 |
| 19 | Sang 2020 Applied Sciences 全文抓取 | mcp web_reader (https://www.mdpi.com/2076-3417/10/11/3980) | 1 | 1 | 0 | 获取全文：阈值法 4.12±1.13 / 10.75±5.51 dBm、三分类同/跨环境精度、DW1000 标称 10 cm、MP 误差至 60 cm（转引 Schmid 2019） |
| 20 | Wang 2023 Electronics 综述全文抓取 | mcp web_reader (https://www.mdpi.com/2079-9292/12/7/1678) | 1 | 0 | 0 | 仅返回页面导航框架未获正文；该篇按 OpenAlex 摘要级核验收录，未引用正文数字 |
| 21 | UTIL arXiv 全文抓取与逐字校验（两次，含 Table 4/SNR 定义/卡方句） | mcp web_reader + python urllib (https://arxiv.org/html/2203.14471v6) | 1 | 1 | 0 | 逐字命中：'approximate positioning error of 10 cm in obstacle-free environments'、'deteriorates greatly'、'static obstacles consistently influence...'、'compl |
| 22 | 30 个入选 DOI 逐一 HEAD 解析验证 | python urllib HEAD https://doi.org/<doi> | 30 | 30 | 0 | IEEE/其他 18 个返回 202/200 解析成功；MDPI/SAGE/Hindawi 12 个对脚本 HEAD 返回 403（反爬，非 DOI 失效）——这些 DOI 均已由 OpenAlex 逐条记录核验，MDPI 数篇另经 web_reader 全文抓取证实 |

## RADAR 组（34 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 23 | radar odometry | Semantic Scholar API (graph/v1/paper/search) | 0 | 0 | 0 | 两次调用均返回 429 Too Many Requests；改用 arXiv/OpenAlex 完成该主题检索。 |
| 24 | radar inertial odometry | Semantic Scholar API | 20 | 9 | 11 | 命中 Doer&Trommer MFI2020、Michalczyk IROS2022、4D iRIOM RA-L2023、Go-RIO ICRA2025、Nissov ICRA2024、Temporal Delay IROS2025、RINO TASE2025 入池；VGC-RIO/FD-RIO/ |
| 25 | all:"radar odometry" (sortBy=relevance) | arXiv API | 20 | 6 | 14 | 入池 CFEAR/ORORA/Burnett/Kung/DRO 相关候选等；Masking-by-Moving、Fast-MbyM、SE(3)、What-Goes-Around、BFAR、LodeStar、RaDiVe、Equi-RO、DNOI-4DRO、off-road 2026、subarcti |
| 26 | radar odometry (cited_by_count:desc) | OpenAlex API | 15 | 0 | 15 | 按引用排序造成关键词碰撞，返回通用机器人综述（Thrun 2001、Colomina 2014 等），全部拒绝，已记录于 rejected。 |
| 27 | all:"radar place recognition" | arXiv API | 15 | 1 | 14 | 入池 Open-RadVLAD；RaPlace/SHeRLoc/AutoPlace/Off-the-Radar/ReFeree/OORD/XPRESS 等筛除。 |
| 28 | all:"4D radar" AND all:"SLAM" | arXiv API | 15 | 2 | 13 | 入池 NTU4DRadLM（另经 Crossref 升级 venue）；Doppler-SLAM/SNAIL/HeRCULES/DIDLM/Introspective-Loop-Closure/AgriLiRa4D 等筛除（SNAIL/HeRCULES 作为对比出现于 Low-Speed 论文全文） |
| 29 | all:"radar" AND all:"fog" AND cat:cs.RO | arXiv API | 15 | 3 | 12 | 入池 Oxford Radar RobotCar、RADIATE、RadarSLAM、New Wave 综述（同批命中）；RMap/RadarHD(2206.09273)/Get-It-For-Free/RaNDT 等筛除。 |
| 30 | all:"Oxford Radar" OR all:"MulRan" OR all:"Boreas dataset" | arXiv API | 15 | 3 | 12 | 入池 Oxford、Boreas、Are-We-Ready、Under-the-Radar(后因容量调整未入池，其后续 Burnett RSS2021 在池)。 |
| 31 | all:"Doppler-Aware Direct Radar Odometry" OR all:"Doppler radar odometry" | arXiv API | 1 | 1 | 0 | 入池 DRO (2504.20339)。 |
| 32 | all:"MulRan" OR all:"K-Radar" OR all:"View of Delft" | arXiv API | 15 | 1 | 14 | 入池 K-Radar；VoD 未命中；LoGG3D-Net/CenterRadarNet/SpikingRTNH 等检测类筛除。 |
| 33 | all:"MulRan" | arXiv API | 10 | 0 | 0 | 确认 MulRan 数据集论文不在 arXiv；改走 Crossref + Semantic Scholar DOI 核验。 |
| 34 | all:"radar-lidar" AND cat:cs.RO | arXiv API | 15 | 2 | 13 | 入池 GaRLIO（经 Crossref 升级 ICRA2025）与 AF-RLIO（经 Crossref 升级 ICRA2025）；Pointing-the-Way/IMU-Preintegrated-ASF/iKalibr/CaRLi-V 等筛除。 |
| 35 | all:"radar" AND all:"smoke" AND cat:cs.RO | arXiv API | 12 | 2 | 10 | 入池 Noh 浓烟融合 (2403.17441)；SubT IMU-drift 2026/RadarHD/Teach-Repeat/Kramer-Suburban 等筛除。 |
| 36 | all:"60 GHz" AND all:"radar" AND cat:cs.RO | arXiv API | 2 | 0 | 2 | 未找到 60GHz 机器人里程计专门论文（记入 rejected 数组第 5 条）；60GHz 证据改由 TI IWR6843 官方页支撑。 |
| 37 | all:"cross-modal" AND all:"radar" AND cat:cs.RO | arXiv API | 12 | 1 | 11 | 入池 LiDAR Teach, Radar Repeat (2605.02809)；Hidden-Gems/Towards-Dense-Accurate/UWB-SLAM 等筛除。 |
| 38 | all:"automotive radar" AND all:"survey" | arXiv API | 2 | 0 | 2 | 仅命中 radar-communication 共存类，与定位无关；汽车雷达能力差异证据改由 TI AWR2944 官方页 + New Wave 综述支撑。 |
| 39 | all:"4DRadarSLAM" OR all:"4D imaging radar" | arXiv API | 15 | 0 | 15 | 4DRadarSLAM 论文本体未在 arXiv 命中，改走 Crossref DOI 10.1109/icra48891.2023.10160670 核验（PARTIALLY_VERIFIED）；检测类条目筛除。 |
| 40 | query.bibliographic=MulRan Multimodal Range Dataset Urban Place Recognition | Crossref API | 2 | 1 | 1 | 命中 MulRan ICRA2020 DOI 10.1109/icra40945.2020.9197298（无摘要）；第二条为无关 VPR 论文。 |
| 41 | paper/DOI:10.1109/MFI49285.2020.9235254 | Semantic Scholar API | 1 | 1 | 0 | Doer & Trommer MFI2020 摘要全文（含 <0.6% 位置误差、200m+ 轨迹、动捕 GT）。 |
| 42 | paper/DOI:10.1109/icra40945.2020.9197298 | Semantic Scholar API | 1 | 1 | 0 | MulRan 摘要全文（数据形态、radar PR 优于 LiDAR PR）。 |
| 43 | paper/DOI:10.1109/IROS47612.2022.9981396 | Semantic Scholar API | 1 | 1 | 0 | Michalczyk IROS2022 摘要全文。 |
| 44 | id_list=2105.01457,2303.01876,2105.14152,2001.10789,2103.07908,2504.20339,2509.07683,2503.02509,2303.13962,2411.07699,2502.08093,2502.07703,2507.18317 | arXiv API (bulk id_list) | 27 | 26 | 1 | 一次抓取 27 篇摘要全文；2206.09273 (RadarHD) 后因容量让位未入池，其余 26 篇全部入池成为核心证据。 |
| 45 | https://www.ti.com/product/IWR6843 | WebFetch | 1 | 1 | 0 | 官方页规格引用：60-64GHz、3TX/4RX、4GHz 带宽、FMCW、点云访问（EVM）、CAN-FD/SPI/UART 等。 |
| 46 | https://www.ti.com/product/AWR2944 | WebFetch | 1 | 1 | 0 | 官方页规格引用：76-81GHz、>4GHz 带宽、4TX/4RX、方位面位置+速度跟踪、CAN-FD/Ethernet/LVDS/CSI2。 |
| 47 | Continental ARS548 High-Resolution-Radar 页面 | WebFetch + curl(UA) | 1 | 0 | 1 | continental-automotive.com -> 301 aumovio.com -> 404 / WebFetch 403；记入 rejected，ARS548 参数仅采信池内论文 (2509.07683) 全文自述。 |
| 48 | navtechradar.com/products/cir304-h/ | WebFetch + curl(UA) | 1 | 0 | 1 | 404；WebSearch 未获官方 datasheet 数值；CIR304-H 仅以 Boreas 论文描述入池。 |
| 49 | Navtech CIR304-H specifications | WebSearch | 8 | 0 | 8 | 返回 Boreas 论文 PDF、pyboreas、Scribd 转载 HDR100 等二手源，无官方 datasheet；仅采纳'Boreas 含 360° Navtech CIR304-H 扫描雷达'这一与 arXiv 摘要一致的信息。 |
| 50 | arxiv.org/html/2502.08093v2 / 2502.07703v2 / 2403.17441v2 | curl + HTML 文本抽取 | 3 | 3 | 0 | 全文抽取：Go-RIO 高程误差 18m/2.5km(0.72%)；GaRLIO 垂直均值误差 1.21m/2.045km、sweep reconstruction 同步；Noh 烟雾 NTU4DRadLM APE/RPE 表。 |
| 51 | arxiv.org/html/2203.10174v3 / 2509.07683v3 / 2303.13962v2 | curl + HTML 文本抽取 | 3 | 3 | 0 | 全文抽取：Are-We-Ready 0.1m 跨模态定位与雪暴序列条件；Low-Speed ARS548 级传感器、2cm GT、10cm@63%、RPE 0.06m vs Doppler-SLAM 0.14m；iRIOM ColoRadar 表 IV、~400 points/scan、Bynav  |
| 52 | arxiv.org/html/2105.01457v3 / 2504.20339v1 | curl + HTML 文本抽取 | 2 | 2 | 0 | 全文抽取：CFEAR 1.76%/0.5°/100m、CTS350-X 4.38cm、矿区 15m/1235m；DRO Boreas 榜 0.26%/0.05°、MulRan 1.45%/0.38°、消融 6.00%/1.57°、隧道 3/4<2.5%。 |
| 53 | query.bibliographic=4DRadarSLAM ... / Kellner Doppler ego-motion ... | Crossref API | 8 | 2 | 6 | 4DRadarSLAM ICRA2023 DOI 核验（入池，PARTIALLY_VERIFIED）；Kellner 2013/2014/2015 Doppler 自车运动系列确认存在（经典，未入池因容量）；其余条目为无关命中。 |
| 54 | 14 项标题逐一 query.bibliographic（CFEAR/Kung/RadarSLAM/DRO/Low-Speed/Oxford/Boreas/RADIATE/NTU4DRadLM/Open-RadVLAD/Burnett/AGV-survey/AF-RLIO/GaRLIO） | Crossref API (python 批处理) | 14 | 14 | 0 | 为入池条目升级 venue/DOI：IROS2021、ICRA2021、IROS2020、RSS2025、RA-L2026(检出)、ICRA2020、IJRR2023、ICRA2021、ITSC2023、RadarConf24、RSS2021、T-IV2024、ICRA2025×2。 |
| 55 | ORORA / Noh-Smoke venue 复核 | Crossref API | 4 | 1 | 3 | ORORA 命中 ICRA2023 DOI 10.1109/icra48891.2023.10160997；Noh 浓烟论文未检索到正式版，保持 arXiv preprint 标注。 |
| 56 | The Oxford Radar RobotCar Dataset（复核会议/期刊版本） | Crossref API | 5 | 1 | 4 | 同题 ICRA2020 DOI 10.1109/icra40945.2020.9196884 为本次实际核验到的记录；池内注明本会话未核验 IJRR 版记录。 |

## EVENT 组（33 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 57 | all:"event-based visual odometry" | arXiv API (export.arxiv.org) | 0 | 0 | 0 | 返回 'Rate exceeded'，未重试，立即改道 DBLP。 |
| 58 | all:"event camera" AND all:"visual inertial odometry" | arXiv API | 0 | 0 | 0 | 同上限流，改道 DBLP。 |
| 59 | q=event camera visual odometry | DBLP search/publ/api | 18 | 12 | 6 | 命中 Mueggler IJRR2017 数据集、ESVO2 TRO2025、Stereo-DEVO RA-L2025、LEVI-SAM、TIM2023 B-Spline、IROS2023 legged ATS、Sensors2022 ray warping、DEVO ICRA2022、EVIMO2 |
| 60 | search=event-based visual odometry event camera | OpenAlex API | 0 | 0 | 0 | 返回 'Rate limit exceeded / Insufficient budget'（当日预算耗尽，resets midnight UTC）；本会话放弃 OpenAlex。 |
| 61 | q=event camera synchronization | DBLP | 6 | 3 | 3 | 命中 Event Density Alignment (ICIRA2023/arXiv2507.04314)、Event-CMOS CNN-DGCNN (Sensors2024)、Wide-baseline sync (arXiv2309.16990)；2015/2005 音视频与普通相机网络同步两 |
| 62 | q=event frame fusion odometry | DBLP | 0 | 0 | 0 | 0 命中，改用 frame-event fusion 关键词。 |
| 63 | q=event camera fusion | DBLP | 25 | 7 | 18 | 命中 InfFusion2026 帧事件融合综述、TUMTraf Event TIV2024、AdaFuse-Det、TIE2026 event-triggered async fusion (cam+UWB)、Radar+Event arXiv2506.18443、Dense Depth even |
| 64 | q=event-based SLAM survey | DBLP | 0 | 0 | 0 | 0 命中；改 q=event-based vision survey。 |
| 65 | q=event camera high dynamic range | DBLP | 0 | 0 | 0 | 首次返回非 JSON（瞬时错误），未死磕；主题经 E2VID 专查补齐。 |
| 66 | q=event-based vision survey | DBLP | 7 | 2 | 5 | 命中 Gallego TPAMI2022 综述（arXiv1904.08405）与 arXiv1902? 无——另命中 Deep Learning for Event-based Vision 2302.08890、FPGA survey 等；正式池只收 Gallego。 |
| 67 | q=ultimate SLAM event | DBLP | 1 | 1 | 0 | 命中 RA-L2018 DOI 10.1109/LRA.2018.2793357。 |
| 68 | q=event camera low light | DBLP | 8 | 4 | 4 | 命中 EvLight++ TPAMI2026/arXiv2408.16254、AdaFuse-Det、ERetinex ICRA2025、ASTEF FCCM2025；DarkShake-DVS、冷却SNR(TBioCAS2018) 等未入池。 |
| 69 | q=stereo event camera depth | DBLP | 2 | 1 | 1 | 命中 CVPR2022 'Stereo Depth from Events Cameras: Concentrate and Focus on the Future'；IECON2023 adaptive stacks 未入池（篇幅）。 |
| 70 | q=event camera simulator | DBLP | 9 | 1 | 8 | 命中 ESIM CoRL2018（PMLR 页核验）；v2e 由专查命中；其余 NeRF 模拟器、slip detection、attention 模拟器不相关。 |
| 71 | q=DSEC stereo event + q=hierarchy event-based time-surfaces | DBLP | 4 | 2 | 2 | 命中 DSEC RA-L2021 与 HOTS TPAMI2017；FPGA gesture (Sensors2020) 不入池。 |
| 72 | q=multi vehicle stereo event camera dataset | DBLP | 1 | 1 | 0 | 命中 MVSEC arXiv1801.10202；期刊版经 Crossref 确认为 RA-L2018 10.1109/LRA.2018.2800793。 |
| 73 | q=high speed high dynamic range video event | DBLP | 3 | 2 | 1 | 命中 E2VID TPAMI（DOI 10.1109/TPAMI.2019.2963386, arXiv1906.07165）与 Zou CVPR2021 Learning To Reconstruct；后者因篇幅未入正式池。 |
| 74 | q=asynchronous fusion localization | DBLP | 6 | 2 | 4 | 命中 TIE2026 event-triggered async fusion (cam+UWB) 与 ICRA2018 Geneva Asynchronous Multi-Sensor Fusion；其余（多机器人协同、粒子滤波、2003 CIRA）不入池。 |
| 75 | q=temporal calibration event | DBLP | 6 | 3 | 3 | 命中 TIM2025 CMax 标定、ROBIO2025 EvMultiCalib (arXiv2508.12564)、RA-L2024 Spatio-Temporal Calibration (arXiv2307.06810)；fMRI 2007 与重复记录剔除。 |
| 76 | q=TUM stereo visual inertial event + q=multi-vehicle multi-sensor event dataset | DBLP | 2 | 1 | 1 | 命中 TUM-VIE IROS2021 (arXiv2108.07329)；M3ED 该查询 0 命中，改 q=M3ED event 后命中 CVPRW2023（未入正式池，venue 误记已记入 rejected）。 |
| 77 | q=v2e video to events + q=voxel grid event camera | DBLP | 3 | 1 | 2 | 命中 v2e CVPRW2021 (arXiv2006.07722)；voxel grid 查询仅命中 2026 稀疏检测 arXiv2603.21638（不入池）；Zenodo 数据集记录剔除。 |
| 78 | q=1 megapixel event camera dataset + q=frame event camera odometry | DBLP | 0 | 0 | 2 | 两查询均 0 命中；1Mpx 记忆候选判为未证实（记入 rejected）。 |
| 79 | q=Ev-FlowNet + q=M3ED event | DBLP | 3 | 2 | 1 | 命中 EV-FlowNet RSS2018 (DOI 10.15607/RSS.2018.XIV.062) 与 M3ED CVPRW2023。 |
| 80 | q=frame-event fusion + q=contrast maximization event | DBLP | 94 | 6 | 88 | frame-event fusion 71 条中命中 Frame-Event Alignment CVPR2023 (arXiv2305.15688)、InfFusion 综述等；contrast maximization 23 条中命中 CMax-SLAM TRO2024 (arXiv2403.0 |
| 81 | q=low-latency automotive vision + Crossref query.bibliographic=The Multi Vehicle Stereo Event Camera Dataset | DBLP + Crossref API | 7 | 2 | 5 | 命中 Nature2024 Low-latency automotive vision (10.1038/s41586-024-07409-w) 与 MVSEC RA-L2018 (10.1109/lra.2018.2800793)；其余 Crossref 噪声剔除。 |
| 82 | Crossref DOI 直查 x6：10.1109/LRA.2018.2793357 / 10.1038/s41586-024-07409-w / 10.1109/TIE.2026.3657005 / 10.1109/TIM.2025.3568945 / 10.1109/TRO.2024.3378 | Crossref API (api.crossref.org/works/DOI) | 6 | 6 | 0 | 全部确认题名/作者/venue/年份；仅 Nature 返回截断摘要（后续由 Semantic Scholar 补全）。 |
| 83 | https://arxiv.org/abs/1904.08405 | WebFetch | 1 | 1 | 0 | 成功：拿到 11 位作者、journal-ref TPAMI 2020、DOI，及摘要定量句 '140 dB vs. 60 dB'、'microseconds'、'kHz'。 |
| 84 | https://arxiv.org/abs/1906.07165 ; /abs/2410.09374 ; /abs/2202.02556 | WebFetch（并行4路） | 3 | 0 | 3 | 分别遇 captcha verify failed / user concurrency limit exceeded / 超时；未死磕，改用 Semantic Scholar API + curl 全文 HTML。 |
| 85 | Semantic Scholar bulk 39 titles (fields=title,authors,year,venue,externalIds,abstract) | api.semanticscholar.org (python urllib, 1.3s 间隔) | 39 | 4 | 35 | 成功返回完整摘要 4 篇：E2VID、MVSEC、Nature2024、EV-FlowNet；其余 35 次 HTTP 429（未认证限额），各仅重试一次即放弃。 |
| 86 | arXiv API ti:"<标题>" x32（Ultimate SLAM、DSEC、TUM-VIE、ESVO2、DEVO、两篇 sync、ST-calib、EvLight++、AdaFuse-Det、FE240hz、CMax-SLAM、v2e、legged ATS、ERetinex、Stereo- | arXiv API (python urllib, 3s 间隔) | 32 | 24 | 8 | 24 篇命中并取回完整摘要/作者/journal-ref；8 篇不在 arXiv（ESIM、Geneva ICRA2018、Zou CVPR2021、Nam CVPR2022、INTSYS2019、BMVC2017、LEVI-SAM、TIM2023 B-Spline、InfFusion 综述、M3E |
| 87 | https://ar5iv.labs.arxiv.org/html/2103.06011 (DSEC 全文) | curl + python 本地解析 | 1 | 1 | 0 | 取到硬件同步链细节（GPS PPS→MC→20Hz trigger→special events→GPS clock）、>120 dB、sub-ms latency、静态场景无事件等原文。 |
| 88 | https://arxiv.org/html/2410.09374 (ESVO2 全文) | WebFetch（超时弃用）→ curl + python 本地解析 | 1 | 1 | 0 | 取到 Table VI（ARE°/ATE cm，DSEC/MVSEC/rpg 行）、mapping 20 Hz VGA CPU、back-end 5 ms、ESIO 37.34 ms、RTK GT 车载数据集等原文。 |
| 89 | https://proceedings.mlr.press/v87/rebecq18a.html (ESIM) | WebFetch | 1 | 1 | 0 | PMLR 官方页：标题/作者/CoRL2018 v87 pp.969-982/摘要确认；页面无量化指标。 |

## FUSION 组（39 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 90 | Sage-Husa adaptive Kalman filter | OpenAlex | 10 | 1 | 9 | 入池: Liu2021(modified SH SINS/DVL)。其余为 FOG 去噪/EV 等离题或同质重复；Narasimhappa2019(MSHARKF) 核验后因池容量放弃。 |
| 91 | innovation-based adaptive estimation Kalman filter | OpenAlex | 10 | 1 | 9 | 入池: Mohamed & Schwarz 1999。大量数据同化(EnKF)/电力系统结果被剔除。 |
| 92 | Mahalanobis gating tracking | OpenAlex | 10 | 1 | 9 | 入池: Bailey et al. 2006 验证门理论。DeepSORT/MOT 类为视觉跟踪应用被剔除。 |
| 93 | chi-square test fault detection Kalman filter navigation | OpenAlex | 10 | 3 | 7 | 入池: Brumback & Srinath 1987、Joerger & Pervan 2013、Yu et al. 2021。Geng2017 FTKF、Jiao2024 T-Rel、El-Mowafy2019、Gao2020 CSTRKF 等核验后因池容量/重复未入池。 |
| 94 | measurement rejection Kalman filter outlier | OpenAlex | 10 | 2 | 8 | 入池: Li et al. 2020 (TSP variational)、Davari & Gholami 2019（后被 Särkkä2009 替换）。Olson2006/Vaganay1996/Bloesch2013 经典但领域(水下/足式)偏移。 |
| 95 | robust Kalman filter outliers navigation | OpenAlex | 10 | 1 | 9 | 入池: Gao et al. 2022 (TVT, 卡方+SPRT 约束 R 的 MLE, 有数值)。Student-t/双核/重力匹配等因池容量未入池。 |
| 96 | GNSS UWB adaptive fusion Kalman | OpenAlex | 10 | 2 | 8 | 入池: Zhu et al. 2020 (TVT 联邦 KF 自适应信息分配)、Barbieri et al. 2021 (TIM UWB 可见性跟踪)。WiFi 室内定位/综述类剔除。 |
| 97 | switchable constraints robust SLAM factor graph | OpenAlex | 10 | 1 | 9 | 入池: Sünderhauf & Protzel 2012。ORB-SLAM3/Kimera-Multi/Lynen2013 核验后未入池（池容量）；Sünderhauf2013 比较文在 conflicts 中提及。 |
| 98 | max-mixture robust mapping networks of mixtures | OpenAlex | 8 | 0 | 8 | 全不相关（SCENIC/GAN 等），改用 DBLP 命中。 |
| 99 | outlier-robust Kalman filter Agamennoni unsupervised | OpenAlex | 8 | 0 | 8 | OpenAlex 全文搜索未命中，改用 DBLP 成功。 |
| 100 | recursive noise adaptive Kalman filtering variational Bayes | OpenAlex | 8 | 1 | 7 | 经后续精确检索命中 Särkkä & Nummenmaa 2009 (TAC, DOI 10.1109/tac.2008.2008348) 并取回摘要，替换 Davari2019 入池。 |
| 101 | LiDAR inertial odometry degeneracy degradation detection | OpenAlex | 10 | 1 | 9 | 入池: GenZ-ICP 2024。LVI-SAM/Wildcat/Wisth2021/Cho2018 等未入池（Wisth 因池容量让位雷达/视觉不确定度方向）。 |
| 102 | UWB NLOS identification mitigation localization | OpenAlex | 10 | 1 | 9 | 入池: Güvenç et al. 2007 (EURASIP JASP WLS)。Maranò2010 JSAC/Yu2018 TVT/Barral2019 等核验后未入池。 |
| 103 | GNSS stochastic model signal-to-noise ratio elevation weighting | OpenAlex | 8 | 1 | 7 | 入池: Zhang et al. 2018 (RS 自适应加权)。Paziewski2021 (C/N0 vs elevation 证据, 有数值) 核验后因池容量未入池，其观点记录在 conflicts；Luo2008 SNR 加权未入池。 |
| 104 | 4D millimeter wave radar odometry localization robust | OpenAlex | 8 | 2 | 6 | 入池: Cheng et al. 2023 (JFR 视觉退化重定位)、DGRO 2024 (Sensors RCS 加权)。GV-iRIOM2025 记入 rejected。 |
| 105 | wheel odometer fault detection integrated navigation | OpenAlex | 8 | 2 | 6 | 入池: Huang & Su 2015 (GOS FDI)、Al Hage et al. 2020 (T-ITS 完整性+FDE)。轮速/里程计专文按评审五类范围裁剪（见 rejected 第4条）。 |
| 106 | Approaches to adaptive filtering Mehra | Crossref | 5 | 1 | 4 | 入池: Mehra 1972 (TAC)。同作者 1970 会议版一并核验。 |
| 107 | Adaptive filtering with unknown prior statistics Sage Husa | Crossref | 6 | 1 | 5 | 入池: Sage & Husa 1969 (IEEE Symposium on Adaptive Processes)。JACC 常引版本未命中 → rejected 第1条。 |
| 108 | networks of mixtures robust mapping | DBLP | 3 | 1 | 2 | 入池: Olson & Agarwal 2013 (IJRR; 另核验 RSS2012 版本)。 |
| 109 | outlier-robust Kalman filter Agamennoni | DBLP | 1 | 1 | 0 | 入池: Agamennoni et al. 2011 (ICRA)。 |
| 110 | degeneracy optimization-based state estimation | DBLP | 1 | 1 | 0 | 入池: Zhang, Kaess, Singh 2016 (ICRA)。作者名单纠正：Ji Zhang（非常被误记的 Jingdong Zhang）。 |
| 111 | visual odometry uncertainty aware failure detection texture | OpenAlex | 8 | 1 | 7 | 入池: D3VO 2020 (arXiv, 学习型光度不确定度加权)。 |
| 112 | wheel slip detection odometry vehicle localization | OpenAlex | 8 | 0 | 8 | Reina2006/Maimone2007 核验后按范围裁剪（见 rejected 第4条）。 |
| 113 | LiDAR rain fog degraded point cloud localization weather | OpenAlex | 8 | 1 | 7 | 入池: Kim et al. 2023 (Sensors 雨雾退化定量实测)。感知类雪天仿真等剔除。 |
| 114 | sensor reliability weighting fusion localization health | OpenAlex | 8 | 0 | 8 | 结果偏向结构健康监测/活动识别，全不相关。 |
| 115 | adaptive fading factor Kalman filter GNSS INS | OpenAlex | 8 | 2 | 6 | 入池: Gao et al. 2018 (Sensors, Mahalanobis 距离自适应渐消+最优融合)、Jiang et al. 2021 (GPS Solutions 评估, PARTIAL)。Gao2021CJA/Lou2019/Ning2018 未入池。 |
| 116 | UWB GNSS integration urban NLOS vehicle localization | OpenAlex | 8 | 1 | 7 | 入池: Hsu 2017 (ITSC GNSS 多径 ML 分类, 75% 数值)。DiPietra2020/Che2022 未入池。 |
| 117 | all:"GenZ-ICP" | arXiv API | 1 | 1 | 0 | 确认 arXiv id 2411.06766，随后 WebFetch HTML 全文提取表格数值。 |
| 118 | all:"robust variational" AND all:"Kalman" AND all:"outlier" | arXiv API | 0 | 0 | 0 | 无结果；Li et al. 2020 TSP 摘要改由 OpenAlex 获取。 |
| 119 | id_list=2003.01060 (D3VO) | arXiv API | 1 | 1 | 0 | 取回 D3VO 摘要全文与作者。 |
| 120 | filter=doi:<12-14 DOIs 批量元数据+摘要> x4 轮 | OpenAlex | 52 | 30 | 22 | 对候选池按 DOI 批量抓取完整摘要与作者；摘要为空的(Mohamed&Schwarz/Jiang2021/Davari2019/GV-iRIOM 等)另行补抓或放弃。'rejected' 计数指未最终入池的已核验候选。 |
| 121 | DOI:10.1007/s001900050236 (Mohamed & Schwarz) | Semantic Scholar | 1 | 0 | 1 | 仅元数据，无摘要；摘要最终经 WebFetch Springer 落地页获取。 |
| 122 | works/10.1007/s10291-021-01165-4 与 works/10.1016/j.oceaneng.2019.01.012 | Crossref | 2 | 1 | 1 | 两者均无 abstract 字段；Jiang2021 入池(PARTIAL)，Davari2019 被 Särkkä2009 替换。 |
| 123 | https://arxiv.org/html/2411.06766 (GenZ-ICP 全文) | WebFetch | 1 | 1 | 0 | 提取权重公式(local surface variation λ3/Σλ, α=N_pl/(N_pl+N_po))与 KITTI/MulRan/Newer College/SubT-MRS/Ground-Challenge 表格数值 → FULLTEXT 级性能数据 4 条。 |
| 124 | https://www.mdpi.com/2072-4292/10/7/1157 (Zhang2018RS 全文) | WebFetch | 1 | 0 | 1 | HTTP 403，全文数值未获取；该文以 ABSTRACT 级入池。 |
| 125 | https://onlinelibrary.wiley.com/doi/10.1155/2021/1745383 (Yu2021 全文) | WebFetch | 1 | 0 | 1 | cookie 拦截错误页，全文数值未获取；该文以 ABSTRACT 级入池。 |
| 126 | http://www.roboticsproceedings.org/rss08/p40.html (Olson RSS2012) | WebFetch | 1 | 1 | 0 | 仅摘要页；确认 RSS2012 版本存在与定性结论，无数值。 |
| 127 | https://link.springer.com/article/10.1007/s001900050236 (Mohamed & Schwarz, 经 idp.springer 两次重定向) | WebFetch | 1 | 1 | 0 | 确认卷期页(JoG 73:193-203, 1999)并读摘要：IAE/MMAE、权因子极大似然选择、两次动态实测；状态从 PARTIAL 升为 VERIFIED。 |
| 128 | container-title 批量确认 6 个会议/期刊 DOI | Crossref | 6 | 6 | 0 | 确认 icif.2006(FUSION 9th)、iros.2012、icra.2016、itsc.2017、icra.2011、EURASIP JASP(2007 在线/2008 卷) 的正式 venue 名称。 |

## GNSS 组（22 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 129 | search=GNSS denied navigation (per-page=14) | OpenAlex API (api.openalex.org/works) | 14 | 3 | 11 | 命中 Schmidt 2014 (CJA 综述)、Tang 2015 (LiDAR+INS, UGV)、Dai 2019 (RNN, Defence Technology)。其余多为 UAV 专用（UWB、协同、RSSI、雷达/视觉里程计等），按轮式平台相关性筛除；Mostafa 2018、Jarr |
| 130 | search=GNSS urban canyon positioning (per-page=10) | OpenAlex API | 10 | 3 | 4 | 收录 Groves 2011 shadow matching、Xie & Petovello 2014 (IEEE TIM 多路径分布实测)、Bai/Wen/Hsu 2020 (鱼眼+LiDAR 辅助 SPP)。Bourdeau 2012、Kumar & Petovello 2014、Suzuki  |
| 131 | search=GNSS NLOS detection multipath urban (per-page=10) | OpenAlex API | 10 | 4 | 2 | 收录 Groves & Jiang 2013（C/N0 加权/高度辅助/一致性检验）、Hsu 2015（RAIM+3D 建筑模型）、Hsu 2017（SVM 三分类 ~75%）、Suzuki & Amano 2021（NN 97.7%）、Sun 2021（IMU 辅助多故障 FDE，仅元数据）。Po |
| 132 | search=GNSS outage inertial navigation drift (per-page=10) | OpenAlex API | 10 | 4 | 5 | 收录 Falco 2017（松/紧组合真实城市实测）、GVINS 2022 (T-RO)、Chang 2020（IMU/ODO/LiDAR-SLAM，2 分钟模拟中断漂移降幅）、Li Xingxing 2021（PPP+S-VINS 半紧耦合）。Li Tuan 2019（单目+MEMS+RTK）与  |
| 133 | search=GNSS satellite selection weighted HDOP (per-page=10) | OpenAlex API | 10 | 4 | 4 | 收录 Jang 2022（HDOP/VDOP 双星座分析）、Kubo 2020（C/N0 时间序列 NLOS 检测）、Zhang Guohao 2020（3DMA 协同 FGO，30 m→<10 m）、Fredeluces 2024（修正 RTK fix 可靠性）。Gerbeth 2016（航空 A |
| 134 | search=BeiDou RTK positioning urban (per-page=10) | OpenAlex API | 10 | 5 | 3 | 收录 Teunissen 2013（BDS+GPS 高截止角瞬时 RTK）、Odolinski 2015（GPS+BDS 短/中/长基线）、Wang Liang 2016（智能手机 BDS/GPS RTK 城市 97%/90% 固定率）、Huang 2022（农机 RTK-BDS/INS 三路况）、 |
| 135 | search=GNSS robust adaptive Kalman filter innovation weighting (per-page=10) | OpenAlex API | 10 | 1 | 4 | 收录 Zhang Qieqie 2018（PPP 抗差自适应 KF，观测粗差+动态模型误差定权）。高超声速飞行器 UKF 系列（Hu Gaoge 等）、自适应渐消 UKF 多传感器融合等与轮式平台主题不符筛除。 |
| 136 | search=BeiDou short message communication (per-page=10) | OpenAlex API | 10 | 5 | 3 | 收录 Li Gang 2021（BDS-3 全球短报文架构+在轨测试）、Bofeng Li 2019（海洋高精度定位+短报文）、Nie 2020（海上实时 PPP+短报文）、Hu 2023（海事安全信息压缩，直面消息长度限制）、Qiao 2023（UAV 短报文路径重规划）。An 2020 船舶监管 |
| 137 | search=BeiDou RDSS satellite (per-page=10) | OpenAlex API | 10 | 4 | 4 | 收录 Yang Yuanxi 2021（BDS-3 特色服务性能：RSMCS 99.9%/GSMCS 95.6%/RDSS <12 m 等）、Lu Jun 2020（BDS 全球能力）、Wang Fei 2020（CRDSS 抗欺骗，RDSS 双向应答机制）、Li Xiaojie 2022（RDSS |
| 138 | search=polarized skylight navigation (per-page=8) | OpenAlex API | 8 | 4 | 2 | 收录 Kong 2023（CJA 综述，非成像式 ±0.1°）、Karman 2012（Sensors 综述）、Hamaoui 2016（Applied Optics 状态估计路线）、Dou 2021（SINS+偏振+里程计 GPS-denied 车载）。Sakura 2007、Wehner 200 |
| 139 | search=polarization odometry bio-inspired (per-page=8) | OpenAlex API | 8 | 2 | 5 | 收录 Du 2020（移动机器人偏振 SLAM，定位误差 -30% 仿真）、Xie 2021（IROS 偏振相机多传感器系统）。普通里程计/定位综述、蝗虫视觉模型、差分机器人编队、光学流自动驾驶等筛除。 |
| 140 | search=celestial optical navigation spacecraft (per-page=8) | OpenAlex API | 8 | 1 | 6 | 收录 Christian 2019 StarNAV（恒星相对论性光行差导航）。Gaia、ICRF/VLBI、FITS 坐标、航天器着陆光学制导（Miso 1999，着陆制导主题偏深空任务）、IAU 分辨率等筛除并记入 rejected 代表条目。 |
| 141 | works?filter=doi:... 批量摘要抓取 #1（12 个 A 块 DOI：s150717329/itsc.2017.8317700/s21072503/s20144059/s0373463313000350/s10291-021-01181-4/s17020255/rs10020205 | OpenAlex API (filter=doi:.../...) | 12 | 12 | 0 | 全部命中并取得完整摘要；Sun 2021 (GPS Solutions) 摘要为空，转 S2 补查仍无，标记 PARTIALLY_VERIFIED。关键性能数字来源：Groves & Jiang 2013（35%/4x/8%/-60%）、Hsu 2015（8.4%/36.2%）、Suzuki 202 |
| 142 | works?filter=doi:... 批量摘要抓取 #2（12 个 DOI：tro.2021.3133730/s0373463311000087/s43020-020-00033-9/rs11060610/s150716710/s20174702/s24092712/tits.2020.2988 | OpenAlex API (filter=doi:.../...) | 12 | 12 | 0 | 全部命中。关键数字来源：Chang 2020（62.8/72.3/52.1/62.1%，2 分钟模拟中断）、Zhang Guohao 2020（>30 m→<10 m）、Wang Liang 2016（97%/90%、0.15/0.25/0.30 m）、Xia 2020（87.0/45.9/69.6 |
| 143 | works?filter=doi:... 批量摘要抓取 #3（14 个 DOI：s00190-013-0686-4/tvt.2015.2481509/tim.2014.2342452/1361-6501-ab52cb/agriculture12081169/s43020-025-00162-z/ac | OpenAlex API (filter=doi:.../...) | 14 | 10 | 0 | 14 个 DOI 全部命中；Ko & Kong 2015、Zidan 2020、Ouyang 2020、Jarraya 2025 复核后移入 rejected，最终 10 条进入论文库。Teunissen 2013、多数命中；Kong 2023（±0.1°）、Du 2020（30%/25%）、Wan |
| 144 | graph/v1/paper/DOI:{s00190-013-0686-4, s10291-021-01181-4, ao.56.000b37, 1748-3190-ab7ab7, iros51168.2021.9635932, s22165985, s10291-017-0670-1}（间隔 4  | Semantic Scholar API | 7 | 3 | 0 | Liang 2020（Rayleigh 模型局限）、Xie 2021（IROS）、Cao 2022（SINS/GPS/偏振/地磁，最终受 F 块 8 篇上限未收录）取得摘要；Teunissen 2013、Sun 2021、Hamaoui 2016、Kubo 2017 无摘要，仅元数据交叉确认。 |
| 145 | graph/v1/paper/DOI:{asr.2020.12.011, scib.2021.06.013, s00190-018-1145-z, s00190-020-01411-6}（间隔 4 秒） | Semantic Scholar API | 4 | 2 | 0 | Li Gang 2021（GSMC 架构/GMDSS）、Yang 2021（BDS-3 特色服务性能全量数字）取得完整摘要；Bofeng Li 2019 与 Nie 2020 摘要被出版社隐藏（abstract elided by publisher），标 PARTIALLY_VERIFIED。此前 |
| 146 | curl http://www.beidou.gov.cn/xt/gfxz/（官方规范/ICD 下载页，HTTP 200） | curl (beidou.gov.cn 官网) | 0 | 0 | 0 | 确认官网在列 ICD：国际搜救、BDSBAS-B1C、PPP-B2b、地基增强等；未见独立的区域短报文 ICD 条目。页面同时列出《公开服务性能规范（3.0版）》中英文 PDF（本次未下载解析）。 |
| 147 | curl http://m.beidou.gov.cn/lbt/202008/t20200803_20935.html（北斗三号建成开通新闻发布会，HTTP 200） | curl (beidou.gov.cn 官网) | 1 | 1 | 0 | 官方原文核实：『区域通信能力达到每次14000比特（1000汉字）……并支持每次560比特（40个汉字）的全球通信能力』；另载国际搜救检测概率优于 99%、全球实测定位精度均值 2.34 米。作为 K 块官方规格条目收录（candidate_core=true）。 |
| 148 | WebSearch『北斗三号 区域短报文 1000汉字 全球短报文 40汉字 官方 规格』 | WebSearch | 8 | 0 | 2 | 作用是定位到官网发布会 URL；搜索摘要中出现的『系统容量 1000 万次/小时、响应时间<1 秒、1200 万用户』来自百度百科/知乎等非官方来源，无法在官网核实，记入 rejected；华力创通终端营销页亦不作为规格依据。 |
| 149 | curl http://www.beidou.gov.cn/zt/gfhd/202211/t20221123_25461.html（2022 短报文服务成果发布会页，HTTP 200） | curl (beidou.gov.cn 官网) | 1 | 0 | 0 | 页面确认 2022-07-30 北斗三号短报文通信服务成果发布会（大众智能手机短报文功能、星地融合方案），但正文无消息长度/频次数值，未产生新规格条目。 |
| 150 | WebFetch opg.optica.org/ao/abstract.cfm?uri=ao-56-2-b37（Hamaoui 摘要页）与 https://www.mdpi.com/1424-8220/20/14/4059（Kubo 2020 全文） | WebFetch | 2 | 0 | 0 | Optica 页 404、MDPI 页 403（反爬），均未取到正文；相应条目仅以 OpenAlex 摘要（ABSTRACT 级）为准，未抄录全文表格数值。另 WebFetch https://arxiv.org/abs/2103.07899 成功确认 GVINS 标题/作者/摘要（arxiv_id |

## LIDAR 组（36 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 151 | LiDAR degeneracy detection | Semantic Scholar API (api.semanticscholar.org/graph/v1/paper/search) | 0 | 0 | 0 | HTTP 429 限流，切换数据源；后续一次重试返回空响应，S2 全程未产出记录。 |
| 152 | LiDAR degeneracy SLAM | OpenAlex API /works?search= | 15 | 10 | 5 | 命中 DALI-SLAM、P2d-DO、Real-Time Degeneracy Sensing(T-ITS)、Switch-SLAM、Intensity-Augmented(T-IM)、Intermittent VIO(T-IM)、GenZ-ICP、Anti-Degeneracy PF(RA-L) |
| 153 | all:"LiDAR degeneracy" | arXiv API | 5 | 0 | 2 | 返回雷达融合类传感器退化论文（2403.17441、2403.05332 等），与几何退化主题不符。 |
| 154 | all:"degeneracy-aware" AND all:"LiDAR" | arXiv API | 14 | 6 | 8 | 命中 LODESTAR(2511.09142)、LF-GICP(2608.19522)、Probabilistic Degeneracy Detection(2410.10784)、Informed Constrained Aligned(2408.11809)、DCReg(2509.06285)、 |
| 155 | dynamic object removal LiDAR SLAM | OpenAlex API /works?search= | 15 | 8 | 7 | 命中 DOR-LINS、SPLIN(T-IM 2025)、Nonparametric Background Model(T-ITS 2022)、RF-LIO(IROS 2021)、Coarse-to-Fine(ION GNSS+ 2021)、Review of Dynamic Object Filt |
| 156 | semantic LiDAR odometry dynamic objects localization | OpenAlex API /works?search= | 15 | 1 | 14 | 命中 SD-SLAM(Big Data Research 2024) 等语义路线备份，最终因已含足量几何/占据类动态方法未入池。 |
| 157 | localizability LiDAR odometry degeneracy | OpenAlex API /works?search= | 12 | 4 | 8 | 命中 LIVER(RA-L 2024)、Rail Vehicle Tunnels(IEEE Sensors 2023)、Train Localization(Sensors 2025)、RELEAD(ICRA 2024)。 |
| 158 | tunnel LiDAR SLAM featureless self-similar | OpenAlex API /works?search= | 12 | 3 | 9 | 命中 GEODE 数据集(IJRR 2025)、MULLS(arXiv 2021) 等。 |
| 159 | scan matching inlier ratio uncertainty LiDAR localization | OpenAlex API /works?search= | 12 | 0 | 12 | 结果噪声大（视觉里程计/移动测图综述），未产出匹配条目；scan-matching 置信度主题改由 X-ICP/P2d-DO/GenZ-ICP 覆盖。 |
| 160 | title.search:erasor | OpenAlex API | 8 | 0 | 8 | OpenAlex title.search 对该词不生效（返回 Random Erasing 等无关结果），改用 DBLP。 |
| 161 | title.search:removert | OpenAlex API | 0 | 0 | 0 | 0 命中，改用 DBLP。 |
| 162 | ERASOR | DBLP publ/api | 5 | 3 | 2 | 命中 ERASOR(RA-L 2021, DOI 10.1109/LRA.2021.3061363)、ERASOR++(ICRA 2024)、ERASOR2(RSS 2023)。 |
| 163 | Removert | DBLP publ/api | 0 | 0 | 0 | 0 命中（DBLP 未以 Removert 名收录），改以原题检索。 |
| 164 | remove then revert point cloud | DBLP publ/api | 1 | 1 | 0 | 命中 Removert IROS 2020 DOI 10.1109/IROS45743.2020.9340856（Giseop Kim, Ayoung Kim）。 |
| 165 | X-ICP localizability | DBLP publ/api | 3 | 2 | 1 | 命中 X-ICP(T-RO 2024, arXiv 2211.16335) 与 LP-ICP(arXiv 2501.02580)。 |
| 166 | degeneracy optimization-based state estimation | OpenAlex API /works?filter=title.search: | 1 | 1 | 0 | 精确命中 Zhang, Kaess, Singh ICRA 2016 DOI 10.1109/icra.2016.7487211。 |
| 167 | all:"ERASOR" AND cat:cs.RO | arXiv API | 3 | 3 | 0 | 命中 ERASOR(2103.04316)、ERASOR++(2403.05019)、DynaHull(2401.07541)。 |
| 168 | all:"GenZ-ICP" | arXiv API | 1 | 1 | 0 | 命中 arXiv 2411.06766。 |
| 169 | all:"Remove, then Revert" | arXiv API | 0 | 0 | 0 | 0 命中（Removert 原文无 arXiv 预印本），转 DBLP 命中。 |
| 170 | all:"On degeneracy of optimization-based state estimation" | arXiv API | 0 | 0 | 0 | 0 命中，Zhang 2016 无 arXiv 预印本，以 OpenAlex+Crossref 题录核验。 |
| 171 | all:"degeneracy" AND all:"condition number" AND all:"LiDAR" | arXiv API | 1 | 1 | 0 | 命中 LODESTAR（条件数+localizability 贡献筛选量测）。 |
| 172 | ti:"degenerate" AND abs:"benchmark" AND abs:"LiDAR" | arXiv API | 2 | 2 | 0 | 命中 GEODE(2409.04961) 与 Adaptive Denoising-Enhanced LIO(2309.14641，备份未入池)。 |
| 173 | all:"FAST-LIO2" | arXiv API | 8 | 1 | 7 | 命中 FAST-LIO2(2107.06829) 作为基线收录；其余为引用它的论文。 |
| 174 | id_list=2211.16335,2411.06766,2409.04961,2410.10784,2102.03771,2501.02580 | arXiv API (摘要批取) | 6 | 6 | 0 | 拉取6篇摘要原文作 ABSTRACT 级证据。 |
| 175 | id_list=2608.19522,2511.09142,2309.14641,2408.11809,2103.04316,2403.05019,2401.07541 | arXiv API (摘要批取) | 7 | 7 | 0 | 拉取7篇摘要原文；LF-GICP 摘要含 KITTI 0.865% 数值。 |
| 176 | id_list=2608.19522,2511.09142,2408.11809,2410.10784,2401.07541,2309.14641,2102.03771,2411.06766,2211.16335,2409.04961,2103.04316,2403.05019 | arXiv API (作者批取) | 12 | 12 | 0 | 核验12篇 arXiv 论文完整作者名单。 |
| 177 | DOI 批量: 12个 RA-L/T-ITS/T-IM/Sensors/IROS/GNSS+ DOI | OpenAlex API /works?filter=doi:.../...&select=abstract_inverted_index | 12 | 12 | 0 | 重建12篇付费墙论文摘要（P2d-DO、RF-LIO、Switch-SLAM、LIVER、DOR-LINS、Nonparametric、SPLIN、RailTunnel、RealTimeDeg、AntiDegPF、IntensityAug、DALI-SLAM空）与第二批16条作者/venue元数据。 |
| 178 | Crossref works/ 7个 DOI (DALI-SLAM, Zhang2016, ERASOR2, RELEAD, JFR, GNSS+ 2021, Sensors review) | Crossref API | 7 | 3 | 4 | JFR(10.1002/rob.70026)与Sensors综述返回摘要；DALI-SLAM/Zhang2016/ERASOR2/RELEAD/GNSS+ 无摘要（仅题录核验）。 |
| 179 | ar5iv 2103.04316 (ERASOR 全文表格) | curl + python 解析表格行 | 15 | 6 | 0 | 抓到 TABLE II 全部 PR/RR/F1 行（00/01/02/05/07 各方法）与 TABLE III runtime 行。 |
| 180 | arxiv.org/html/2411.06766v1 (GenZ-ICP 全文) | curl + python 解析 table/figcaption | 21 | 8 | 0 | 抓到 TABLE I-VI 数值与 caption（Newer College/MulRan/KITTI/HILTI-Oxford/Ground-Challenge/SubT-MRS）。 |
| 181 | arxiv.org/html/2409.04961v2 (GEODE 全文) | curl + python 解析 table/figcaption | 9 | 4 | 0 | 抓到 Table 6 ATE(M) 全部序列行（Inland Waterways/Metro Tunnels 等）与传感器规格表。 |
| 182 | arxiv.org/html/2403.05019v1 (ERASOR++ 全文) | curl + python 解析 table | 10 | 2 | 0 | 抓到 TABLE I（KITTI seq. 00/01/02/05/07 PR/RR/F1/时间）与 TABLE II。 |
| 183 | arxiv.org/html/2401.07541v2 (DynaHull 全文) | curl + python 解析 table/figcaption | 4 | 3 | 0 | 抓到 Table 2/3 数值与 Fig.8 定位失败 caption。 |
| 184 | arxiv.org/html/2211.16335v4 (X-ICP 全文) | curl + python 解析 table/figcaption | 29 | 5 | 0 | 抓到 Seemühle 矿井 APE/RPE 表与 Rümlang 耗时表。 |
| 185 | RF-LIO 作者核验 | Crossref API + DBLP + WebSearch + arXiv API | 1 | 1 | 0 | Crossref/DBLP/OpenAlex 均无作者；WebSearch 指向 arXiv 2206.09463；arXiv API 核验作者 Chenglong Qian, Zhaohong Xiang, Zhuoran Wu, Hongbin Sun。 |
| 186 | RF-LIO Removal-First Tightly-coupled Lidar Inertial Odometry IROS 2021 authors | WebSearch (内置搜索) | 4 | 1 | 3 | 搜索摘要指向 arXiv 2206.09463；最终以 arXiv API 原文为证据源。 |

## RELOCSYNC 组（43 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 187 | search=active relocalization robot | OpenAlex | 15 | 3 | 12 | 命中 TIE 2022 变电站主动位姿重定位、TPAMI 2018/2019 主动相机重定位、RAS 1998。本次会话 OpenAlex 共约11次查询后预算耗尽（API 返回 'Insufficient budget... dailyRemainingUsd 0.0003'），后续全部改用 Cr |
| 188 | search=active localization mobile robot uncertainty | OpenAlex | 15 | 1 | 14 | 命中 Robust Monte Carlo localization (AIJ 2001)。 |
| 189 | search=kidnapped robot problem recovery | OpenAlex | 15 | 3 | 12 | 命中 IROS 2004 expansion resetting、TIM 2026 稀疏假设采样（后经 Crossref 核验）、ROSE 2013 resume navigation（收入候选池后未进最终35篇）。 |
| 190 | all:"active relocalization" | arXiv API (curl export.arxiv.org) | 0 | 0 | 0 | 持续限流（'Rate exceeded'/HTTP 429），本次会话多次重试（间隔3-6s）均失败；改用 WebFetch 抓 arXiv 搜索页。 |
| 191 | filter=title.search:active localization (sorted by citations) | OpenAlex | 25 | 4 | 21 | 命中 Active Markov localization (RAS 1998)、Jensfelt active global localization (TRA 2001)、Active SLAM survey (TRO 2023)。标题检索噪声大（医学生物类），人工筛选。 |
| 192 | search="relocalization success rate" | OpenAlex | 16 | 2 | 14 | 命中 GOReloc (RA-L 2024)、Tackling the Kidnapped Robot Problem (TIM 2026)。 |
| 193 | search=active Markov localization robot | OpenAlex | 10 | 0 | 0 | 复核性查询，与 title.search 结果交叉确认 Active Markov localization。 |
| 194 | search=coastal navigation mobile robot uncertainty | OpenAlex | 10 | 1 | 9 | 命中 Coastal navigation (ICRA 1999)；OpenAlex 年份字段标 2003（疑错误），Crossref 无年份，按 DOI/会议记 1999 并在 raw 中标注冲突。 |
| 195 | search=optimizing motions global localization planning | OpenAlex | 10 | 0 | 10 | 记忆候选 'Planning for the Unexpected' 经 DBLP 证实为腿式跑步论文（主题无关），记入 rejected。 |
| 196 | search=viewpoint selection robot localization uncertainty | OpenAlex | 10 | 0 | 10 | 噪声为主；视点选择方向的可用文献经 JIRS 2009 active visual perception 覆盖。 |
| 197 | search=active LiDAR relocalization exploration | OpenAlex | 15 | 3 | 12 | 命中 Global LiDAR Localization survey (arXiv 2302.07433, 后经 arXiv abs 页核验为 IJCV 出版)、Relocalization with Submaps (RA-L 2020)、Active SLAM review last deca |
| 198 | q=global localization planning unexpected | DBLP | 0 | 0 | 0 | 0 命中；用于排除记忆候选。 |
| 199 | search=active Monte Carlo localization action selection | OpenAlex | 12 | 1 | 11 | 命中 Active Visual Perception for Mobile Robot Localization (JIRS 2009)。 |
| 200 | search=POMDP active localization robot | OpenAlex | 12 | 0 | 12 | POMDP 规划文献为主，无主动重定位直接命中。 |
| 201 | search=entropy action selection global localization particle filter | OpenAlex | 12 | 1 | 11 | 命中 Information Gain-based Exploration Using RBPF (RSS 2005)，收入候选池未进最终35篇（偏 SLAM 建图探索）。 |
| 202 | query=targetless LiDAR camera extrinsic calibration | Crossref | 15 | 6 | 9 | 命中 Pandey AAAI MI 标定、AI Review 2023 survey、Galibr/EdgeCalib/TIV-OU/TLAC（后三者收入候选池，因35篇上限未收录）。 |
| 203 | query=temporal spatial calibration camera IMU multi-sensor | Crossref | 15 | 6 | 9 | 命中 Furgale IROS（年份据 Crossref 定为2013）、Li&Mourikis ICRA 2013、Liu&Hu ICPR 2018（未收录）、3DV 2024 global pose sensor、GLIC-Calib IROS 2025。 |
| 204 | q=targetless calibration lidar camera | DBLP | 51 | 0 | 0 | 复核性查询：与 Crossref 交叉确认 targetless 方向文献（AI Review survey、Galibr、EdgeCalib、TIV 等）。 |
| 205 | query=end-to-end active camera relocalization | Crossref | 10 | 1 | 9 | 命中 ICASSP 2018 active camera relocalization (Miao/Tian/Feng)。 |
| 206 | query=online temporal calibration monocular visual-inertial | Crossref | 10 | 3 | 7 | 命中 Qin&Shen IROS 2018、Feng Sensors 2019、EKF-Based Radar-Inertial Odometry With Online Temporal Calibration (RA-L 2025)。 |
| 207 | q=radar camera extrinsic calibration | DBLP | 0 | 0 | 0 | DBLP 间歇性失败（连接重置/空响应），重试一次仍空；雷达方向改用 Crossref 完成。 |
| 208 | query=event camera temporal calibration synchronization | Crossref | 12 | 2 | 10 | 命中 EF-Calib (RA-L 2024)、EventAlign (ITSC 2024，未收录)。附带发现 Ekalibr-Stereo (RA-L 2025，未收录)。 |
| 209 | query=hardware time synchronization multi-sensor PPS PTP robot | Crossref | 12 | 1 | 11 | 命中 Hardware-Based Time Synchronization for a Multi-Sensor System (IROS 2024)；PTP/ISPCS 类工业文献与机器人场景贴合度低未收录。 |
| 210 | query=spatiotemporal calibration LiDAR IMU continuous-time | Crossref | 12 | 5 | 7 | 命中 Lv IROS 2020、TMech 2024 (Xingxing Li)、Sensors 2017 时延标定 (Wanli Liu)、Sensors 2025 方法综述 (Lyu)、TII 2024 multi-LiDAR（未收录）。 |
| 211 | query=radar camera targetless extrinsic calibration automotive | Crossref | 12 | 1 | 11 | 命中 Targetless Radar-Camera Calibration via Trajectory Alignment (Sensors 2025)；NAECON/ICUFN/CaRaCTO 等未收录。 |
| 212 | query=timestamp offset time delay impact sensor fusion localization accuracy | Crossref | 12 | 0 | 12 | 噪声为主（声源定位/TDOA）；‘时偏→融合精度’的量化证据改由 Sensors 2017/2019 两篇 OA 全文覆盖。 |
| 213 | query=active relocalization reinforcement learning robot navigation recovery | Crossref | 12 | 0 | 12 | RL 导航通用文献为主，无主动重定位直接命中。 |
| 214 | query=active global localization mobile robot exploration | Crossref | 12 | 3 | 9 | 命中 Jensfelt TRA 2001（含作者）、Burgard entropy minimization 1997（含作者）、Heuristic Search Assisted Active Localization (ROBOT 2012)。 |
| 215 | query=next best view planning robot localization uncertainty | Crossref | 12 | 0 | 12 | NBV 文献以三维重建为主，与重定位弱相关。 |
| 216 | query=time synchronization error effect visual inertial odometry calibration | Crossref | 12 | 1 | 11 | 命中 Robotica 2024 double-stage EKF 在线时标（收入候选池未进最终35篇）。 |
| 217 | query.bibliographic 批量解析 arXiv ID（GOReloc/GLIC-Calib/EKF-RIO/Cross-modality/EdgeCalib/VINS-Mono/Pandey 等13题） | Crossref | 39 | 5 | 0 | 确认 GLIC-Calib/GRIL-Calib(附带发现)/EdgeCalib/EKF-RIO/VINS-Mono 的 DOI 与年份；大多数 RA-L/IROS 论文无 arXiv 预印本 DOI 记录。 |
| 218 | q=active relocalization | DBLP | 8 | 3 | 0 | 关键命中：SII 2024 position-lost recovery、arXiv 2204.06580 + Neurocomputing 2022 (illumination-invariant ACR)、ICVS 2017 active loop closure；并交叉确认 TIE/TPAMI |
| 219 | 单条记录批量核验（H块10个DOI） | Crossref | 10 | 10 | 0 | 逐条确认标题/作者/venue；IEEE 记录均无摘要字段。 |
| 220 | 单条记录批量核验（I块 20个DOI，含完整作者名单补全） | Crossref | 24 | 24 | 0 | 确认 Furgale=IROS 2013（pages 1280-1286）、EF-Calib/GRIL-Calib/EKF-RIO/Lv/GLIC/3DV/硬件同步/TIM2026/GOReloc 等；补全全部作者名单。 |
| 221 | ti 批量标题检索（EF-Calib/GOReloc/Submaps/Lv/EKF-RIO/ActiveSLAM survey/TPAMI ACR/ACR 2022，8题） | arXiv API (curl) | 0 | 0 | 0 | 全部 'Rate exceeded'（持续限流），0 获取。 |
| 222 | title search 7题（EF-Calib/GOReloc/Submaps/Lv/EKF-RIO/ActiveSLAM survey/VINS-Mono） | Semantic Scholar Graph API | 0 | 0 | 0 | 返回空 data（限流），0 获取。 |
| 223 | query 批量查 arXiv 预印本 DOI（6题, 10.48550 前缀） | Crossref | 48 | 0 | 0 | EF-Calib/GOReloc/Submaps/Lv/EKF-RIO/GRIL-Calib 均无 arXiv DOI 记录；GRIL-Calib 的 arXiv ID 改由 arXiv 搜索页获得。 |
| 224 | WebFetch https://arxiv.org/search/?query=GRIL-Calib | WebFetch | 1 | 1 | 0 | 获得 arXiv:2312.14035（v1 2023-12-21, v2 2024-05-24）。 |
| 225 | WebFetch https://arxiv.org/search/?query=%22active+relocalization%22 | WebFetch | 1 | 0 | 1 | 仅命中生物物理论文；证实 arXiv 无以 active relocalization 为题的机器人论文，记忆候选记入 rejected。 |
| 226 | WebFetch https://arxiv.org/search/?query=GOReloc | WebFetch | 1 | 1 | 0 | 获得 arXiv:2408.07917。 |
| 227 | WebFetch abs 页深读：2204.06580 / 1708.03852 / 2302.07433 / 2312.14035 / 2408.07917(abs+html) / 2209.06404 | WebFetch | 7 | 6 | 1 | 2204.06580(ACR 1.6x加速)、1708.03852(VINS-Mono 摘要无数值→rejected)、2302.07433(Global LiDAR survey, IJCV 出版确认)、2312.14035(标定精度表)、2408.07917(成功率定义+表格+耗时)、2209. |
| 228 | webReader 开放获取全文：MDPI 17/3/539 (Liu 2017)、19/10/2273 (Feng 2019)、25/24/7574 (Durmaz 2025)；IEEE ieeexplore.ieee.org/document/9341405 | webReader (mcp web_reader) | 4 | 3 | 1 | MDPI 三篇全文成功抽取性能数值（时延9.58→0.50ms；时偏扫描 RMSE；雷达相机标定精度）；IEEE Xplore 返回 'Request Rejected'（反爬），IEEE 付费墙论文一律不填数值。MDPI 对 WebFetch 返回 403，webReader 可用。 |
| 229 | OpenAlex search=unified temporal and spatial calibration multi-sensor systems / targetless LiDAR camera extrinsic calibration | OpenAlex | 0 | 0 | 0 | 发起时 OpenAlex 已超每日预算（'Rate limit exceeded / Insufficient budget'，retryAfter≈67381s），0 获取；同批 Crossref/DBLP 完成同等查询。 |

## SIM 组（35 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 230 | search_query=all:"event camera simulator" | arXiv API (http) |  |  |  |  |
| 231 | search_query=all:gazebo AND all:GNSS | arXiv API (http) |  |  |  |  |
| 232 | search=gazebo GNSS simulation | OpenAlex API |  |  |  |  |
| 233 | search_query=all:"event camera simulator" | arXiv API (https) |  |  |  |  |
| 234 | query=event camera simulator ESIM&rows=8 | Crossref |  |  |  |  |
| 235 | query=v2e event camera simulator Hu&rows=8 | Crossref |  |  |  |  |
| 236 | query=CARLA open urban driving simulator Dosovitskiy | Crossref |  |  |  |  |
| 237 | query=AirSim high fidelity visual physical simulation autonomous vehicles | Crossref |  |  |  |  |
| 238 | q=event camera simulator | DBLP |  |  |  |  |
| 239 | q=CARLA | DBLP |  |  |  |  |
| 240 | query=sensor fault injection robot localization simulation | Crossref |  |  |  |  |
| 241 | query=UWB localization simulation Gazebo ROS | Crossref |  |  |  |  |
| 242 | query=automotive radar sensor simulation open source | Crossref |  |  |  |  |
| 243 | query=UrbanNav GNSS urban canyon dataset | Crossref |  |  |  |  |
| 244 | query.bibliographic=UrbanNav&rows=8 | Crossref |  |  |  |  |
| 245 | query=v2e flexible visual simulator event cameras | Crossref |  |  |  |  |
| 246 | ti:"CARLA" AND ti:"simulator" | arXiv API |  |  |  |  |
| 247 | works/10.1371/journal.pone.0244664（记忆 DOI 验证） | Crossref |  |  |  |  |
| 248 | query.bibliographic=GNSS outage simulation MEMS IMU navigation degraded | Crossref |  |  |  |  |
| 249 | query.title=v2e&rows=10 | Crossref |  |  |  |  |
| 250 | query.bibliographic=UUV simulator Gazebo underwater vehicle ROS | Crossref |  |  |  |  |
| 251 | query.bibliographic=ROS2 communication latency packet loss evaluation | Crossref |  |  |  |  |
| 252 | all:"sim-to-real" AND all:"LiDAR" AND all:"SLAM" | arXiv API |  |  |  |  |
| 253 | query.title=flexible visual simulator event cameras | Crossref |  |  |  |  |
| 254 | all:"sensor degradation" AND all:"SLAM" | arXiv API |  |  |  |  |
| 255 | query.bibliographic=UWB NLOS identification deep learning dataset | Crossref |  |  |  |  |
| 256 | all:"event camera" AND all:"simulator" AND cat:cs.RO | arXiv API |  |  |  |  |
| 257 | abs:"Gazebo" AND abs:"SLAM" AND abs:"noise" | arXiv API |  |  |  |  |
| 258 | all:"ns-3" AND all:"ROS" | arXiv API |  |  |  |  |
| 259 | all:"GNSS outage" AND all:"simulation" | arXiv API |  |  |  |  |
| 260 | all:"UWB" AND all:"simulator" | arXiv API |  |  |  |  |
| 261 | query.bibliographic=GNSS-SDR open source software receiver | Crossref |  |  |  |  |
| 262 | all:"LiDAR" AND all:"adverse weather" AND all:"simulation" | arXiv API |  |  |  |  |
| 263 | id_list=1711.03938,2107.07004,2312.12772,2606.23708,2608.08522,2607.08098,2109.00892,2411.12250,2503.04838 | arXiv API |  |  |  |  |
| 264 | ti:"ESIM: an Open Event Camera Simulator" | arXiv API |  |  |  |  |

## DATASETS 组（37 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 265 | https://www.cvlibs.net/datasets/kitti/ | WebFetch |  |  |  |  |
| 266 | https://www.cvlibs.net/datasets/kitti/raw_data.php | curl |  |  |  |  |
| 267 | https://www.cvlibs.net/datasets/kitti/（主站） | curl |  |  |  |  |
| 268 | https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets | WebFetch |  |  |  |  |
| 269 | https://ethz-asl.github.io/datasets/ | WebFetch |  |  |  |  |
| 270 | https://projects.asl.ethz.ch/datasets/ | WebFetch |  |  |  |  |
| 271 | https://projects.asl.ethz.ch/datasets/euroc-mav/ | WebFetch |  |  |  |  |
| 272 | https://cvg.cit.tum.de/data/datasets/visual-inertial-dataset | WebFetch |  |  |  |  |
| 273 | https://sites.google.com/view/mulran-pr/home | WebFetch |  |  |  |  |
| 274 | https://oxford-robotics-institute.github.io/radar-robotcar-dataset/ | WebFetch |  |  |  |  |
| 275 | https://dsec.ifi.uzh.ch/ | WebFetch |  |  |  |  |
| 276 | https://mvsec.io/ | curl |  |  |  |  |
| 277 | https://m3ed.io/ | WebFetch |  |  |  |  |
| 278 | repos/IPNL-POLYU/UrbanNav | GitHub API |  |  |  |  |
| 279 | search/repositories?q=UrbanNav | GitHub API |  |  |  |  |
| 280 | repos/IPNL-POLYU/UrbanNavDataset | GitHub API |  |  |  |  |
| 281 | raw.githubusercontent.com/IPNL-POLYU/UrbanNavDataset/master/README.md | curl |  |  |  |  |
| 282 | query.bibliographic=Complex Urban Dataset multi-level sensors | Crossref |  |  |  |  |
| 283 | https://irap.kaist.ac.kr/datasets/ | curl |  |  |  |  |
| 284 | "Complex Urban" dataset KAIST 3D map GPS RTK download | WebSearch |  |  |  |  |
| 285 | https://sites.google.com/view/complex-urban-dataset/ | WebFetch |  |  |  |  |
| 286 | NCLT dataset University of Michigan download | WebSearch |  |  |  |  |
| 287 | https://robots.engin.umich.edu/NCLT/（旧） | curl |  |  |  |  |
| 288 | https://robots.engin.umich.edu/nclt/ | curl |  |  |  |  |
| 289 | repos/ori-drs/newer_college_dataset 与 ori-dss/... | GitHub API |  |  |  |  |
| 290 | search q=newer college dataset | GitHub API |  |  |  |  |
| 291 | UWB dataset indoor localization public download NLOS ranging CIR benchmark | WebSearch |  |  |  |  |
| 292 | works/10.1038/s41597-023-02639-5 | Crossref |  |  |  |  |
| 293 | https://zenodo.org/api/records/4399187 | curl |  |  |  |  |
| 294 | repos/ewine-project/UWB-LOS-NLOS-Data-Set | GitHub API |  |  |  |  |
| 295 | https://learnsyslab.github.io/util-uwb-dataset/ | WebFetch |  |  |  |  |
| 296 | GNSS outage degraded dataset benchmark vehicle navigation open download urban canyon multipath | WebSearch |  |  |  |  |
| 297 | https://navi.ion.org/content/70/4/navi.602 | WebFetch |  |  |  |  |
| 298 | repos/SJTU-ViSYS/M2DGR 与 M2DGR-plus | GitHub API |  |  |  |  |
| 299 | raw.githubusercontent.com/SJTU-ViSYS/M2DGR/master/README.md | curl |  |  |  |  |
| 300 | query.bibliographic=EuRoC micro aerial vehicle datasets Burri | Crossref |  |  |  |  |
| 301 | repos/sjtuyinjie/SJTU_GVI | GitHub API |  |  |  |  |

## OPENSOURCE 组（40 条）

| # | Query | Tool | Screened | Accepted | Rejected | Notes |
|---|---|---|---|---|---|---|
| 302 | repos/hku-mars/FAST_LIO | GitHub API |  |  |  |  |
| 303 | repos/TixiaoShan/LIO-SAM | GitHub API |  |  |  |  |
| 304 | repos/HKUST-Aerial-Robotics/VINS-Fusion | GitHub API |  |  |  |  |
| 305 | repos/ucla-vision/openvins | GitHub API |  |  |  |  |
| 306 | repos/borglab/gtsam | GitHub API |  |  |  |  |
| 307 | repos/HKUST-Aerial-Robotics/GVINS | GitHub API |  |  |  |  |
| 308 | repos/rtklibexplorer/RTKLIB | GitHub API |  |  |  |  |
| 309 | repos/ethz-asl/kalibr | GitHub API |  |  |  |  |
| 310 | repos/cra-ros-pkg/robot_localization | GitHub API |  |  |  |  |
| 311 | repos/locusrobotics/fuse | GitHub API |  |  |  |  |
| 312 | search q=openvins | GitHub API |  |  |  |  |
| 313 | repos/rpng/open_vins | GitHub API |  |  |  |  |
| 314 | repos/uzh-rpg/rpg_dvs_ros | GitHub API |  |  |  |  |
| 315 | repos/uzh-rpg/esim_ros | GitHub API |  |  |  |  |
| 316 | repos/SensorManipulation/v2e | GitHub API |  |  |  |  |
| 317 | repos/tu-darmstadt-ros-pkg/hector_gazebo | GitHub API |  |  |  |  |
| 318 | repos/ros-simulation/gazebo_ros_pkgs | GitHub API |  |  |  |  |
| 319 | repos/PX4/PX4-SITL_gazebo | GitHub API |  |  |  |  |
| 320 | repos/xinhe-yifan/gnss-ins-sim | GitHub API |  |  |  |  |
| 321 | repos/utiasDSL/util-uwb-dataset | GitHub API |  |  |  |  |
| 322 | search q=esim+event+camera+simulator | GitHub API |  |  |  |  |
| 323 | search q=v2e+event | GitHub API |  |  |  |  |
| 324 | search q=PX4-SITL_gazebo | GitHub API |  |  |  |  |
| 325 | search q=gnss-ins-sim | GitHub API |  |  |  |  |
| 326 | search q=util-uwb-dataset | GitHub API |  |  |  |  |
| 327 | repos/gazebosim/gz-sim | GitHub API |  |  |  |  |
| 328 | search q=radar+odometry sort=stars | GitHub API |  |  |  |  |
| 329 | search q=uwb+localization+ros sort=stars | GitHub API |  |  |  |  |
| 330 | hku-mars/FAST_LIO README.md | raw README |  |  |  |  |
| 331 | TixiaoShan/LIO-SAM README.md | raw README |  |  |  |  |
| 332 | HKUST-Aerial-Robotics/VINS-Fusion README.md | raw README |  |  |  |  |
| 333 | rpng/open_vins ReadMe.md（注意大小写） | raw README |  |  |  |  |
| 334 | HKUST-Aerial-Robotics/GVINS README.md | raw README |  |  |  |  |
| 335 | cra-ros-pkg/robot_localization README.md | raw README |  |  |  |  |
| 336 | locusrobotics/fuse README.md | raw README |  |  |  |  |
| 337 | url-kaist/outlier-robust-radar-odometry README.md | raw README |  |  |  |  |
| 338 | ethz-asl/rio README.md | raw README |  |  |  |  |
| 339 | christopherdoer/rio README.md | raw README |  |  |  |  |
| 340 | uzh-rpg/rpg_esim、SensorsINI/v2e、hector_gazebo、Aceinna/gnss-ins-sim、ntnu-arl/lidar_degeneracy_datasets README | raw README |  |  |  |  |
| 341 | repos/rpng/open_vins/contents/ | GitHub API |  |  |  |  |
| 342 | FIX-001 复核：WebFetch arxiv.org/html/2408.07917（Table II/III 逐行重读+列定义确认） | WebFetch | 2 | 2 | 0 | 确认 17.43=ICL-Data Diamond 'Head' @2m；fr2_person @2m/5m=64.87/96.11；Table III 为 fr2_person 与 ORB-SLAM2 紧阈值对比（0.5/1/2/3m）；Table II 四列=成功率@2m/5m+TE best10%/20%（无旋转列）。 |
| 343 | FIX-002 复核：web_reader 抓取 MDPI 原文全文（s16122201）含 Table 2/4 | web_reader | 1 | 1 | 0 | 静态 H0.15/V0.25、动态 H0.30/V0.45（whole solutions RMS）；固定解：静态 H≤3cm/V≤4cm、动态 H约10cm/V约13cm；逐测段 S1-S3/K1-K3 数值齐备；NovAtel OEM615+Samsung Galaxy A7、cutoff 15°、北京城区。 |
| 344 | NEW-01~04 元数据批量核验（4 DOI） | Crossref | 4 | 4 | 0 | 全部命中：ASR 76(11):6847-6862 (2025)、ASR 77(4):4731-4745 (2026)、Measurement 279:121711 (2026)、Measurement 254:117623 (2025)；PII 与官方 URL 一并取得。 |
| 345 | NEW-05~07 元数据核验（DOI 10.32604/cmc.2022.031602、10.3390/s24196288）+ ActLoc 出处检索 | Crossref + WebSearch | 3 | 3 | 0 | CMC 73(3):6495-6511（El rube'）、Sensors 24(19):6288（Chai/Liu/Xiong）；ActLoc=arXiv:2508.20981=CoRL 2025 PMLR v305 li25b（ETH Zürich；项目页+代码库确认）。 |
| 346 | NEW-05 全文核验（TechScience HTML 全文+官方 PDF 公式区提取） | web_reader + curl + pypdf | 2 | 2 | 0 | R1=min 分母、R2=average 分母（Eq.7）、R4=调和平均分母（Eq.9，Awrangjeb 系）、two-fold=(RA,RB)（Eq.10）、symmetric mean=双向算术平均（Eq.11）；图像域影响数值。CC-BY 开放获取。 |
| 347 | NEW-06 全文核验（MDPI 全文，成功判据/仿真/NCD 数值） | web_reader | 1 | 1 | 0 | 成功=3D位置误差<1.0m（无旋转阈值）；仿真 99.85%→摘要约99%、~11Hz；NCD 43770 模板@0.2m、600 测试帧、级联 94.67%（0.135s/帧）、穷举 97.83%（191s/帧）；Leica BLK360→Ouster OS-0 异构；Python 单线程。 |
| 348 | NEW-07 全文核验（arXiv HTML 全文） | web_reader | 1 | 1 | 0 | LocMap=注意力模型预测航点 yaw/pitch 精度分布；混合代价图 C+λ·马氏距离 接入 OMPL（航点 20cm）；阈值族 0.1m/1°、0.25m/2°、0.5m/5°、5m/10°；110ms/航点 vs LWL 8230ms；@1m 远点+35%/近点+11%/全部+5.8%。表格逐格数值未在 HTML 文本层渲染。 |
| 349 | NEW-01 内容核验（ScienceDirect 摘要页 web_reader + WebSearch 摘要要点；浏览器直连被 Cloudflare Turnstile 拦截，合规全文路径无 OA 副本） | web_reader + WebSearch + Unpaywall | 4 | 2 | 2 | 已核验：四场景（open-sky/urban canyon/glass curtain wall/tree）、综合模型较三类单指标模型 50.0%/17.6%/8.5%、open-sky fix>99%。未取得：East/North/Up 绝对值、PLD 精确定义（付费墙）。Unpaywall 确认 4 篇 Elsevier 均 is_oa=False。 |
| 350 | NEW-02 内容核验（WHU Scholars 门户完整摘要 + SD Highlights） | WebFetch + web_reader | 3 | 3 | 0 | 完整摘要：多频多系统 PPP-RTK 平台→概率周跳检测→PDOP+高程残差抗差→城市实测验证；定性结论 significantly improve ambiguity fix rate & positioning accuracy；摘要无数值。Published 15 Feb 2026。 |
| 351 | NEW-03 内容核验（SD 预览 Highlights + WebSearch 摘要片段 + 百度学术/X-MOL 镜像） | web_reader + WebSearch | 5 | 3 | 2 | 已核验：multi-metric 约束保证地图点精度、未知高度/弱可观地图点垂直观测优化、41.29%=urban canyon 位置+姿态精度改善。未取得：41.29% 对比基线、LiDAR 型号、ground-plane 约束细节（付费墙）。 |
| 352 | NEW-04 内容核验（SD 预览 + WebSearch 摘要要点） | web_reader + WebSearch | 4 | 2 | 2 | 已核验：SVIO 实时位置+深度、立体匹配深度约束、体渲染解码。未取得：X/Y/Z 误差、数据集、传感器配置（付费墙）。 |
| 353 | 五空缺限定补查（4 次定向检索：LiDAR 动态移除后重复率/不确定感知候选过滤/主动定位/垂向 2025-26） | WebSearch + arXiv API | 6 | 4 | 2 | 空缺1（垂向）由 FIX-002+NEW-01/02 覆盖；空缺2（动态移除后特征重复率直接量化）未找到 2025-26 直接文献，记为开放空缺（LDY 池+FRM-01 方法论邻接覆盖）；空缺3（紧阈值重定位）由 NEW-06 覆盖；空缺4 新增 RLC-21（Mason, IROS 2023, arXiv:2210.01361，arXiv API 元数据核验）+ RLC-22（UQ-Loc, arXiv:2608.06307 预印本，PREPRINT 状态）；空缺5（主动定位）由 NEW-07 覆盖。 |
| 354 | S2/OUCI/ADS/RG/MDPI-curl 备用通道连通性测试（本轮访问路径记录） | curl/WebFetch | 6 | 0 | 6 | Semantic Scholar 429 限流；OUCI 502；ADS 405；ResearchGate Access Denied；SD 直连 curl=JS 壳页（Cloudflare）；MDPI curl=403。全库核验按 web_reader→WebSearch→门户镜像 预案完成。 |
