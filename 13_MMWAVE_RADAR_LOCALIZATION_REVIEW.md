# 13 毫米波雷达定位技术评审（研究组 C / RADAR）

项目：DG-202611“基于具身智能的无人平台多源导航定位技术”，轮式平台。
传感器主线：轮式里程计 + IMU + 北斗/GNSS/RTK + LiDAR + ZED 2i 双目 + UWB + **毫米波雷达（拟采购）** + 事件相机（拟采购）。

**本文档中毫米波雷达的角色定位**：在 GNSS 拒止、视觉退化、LiDAR 局部退化场景下提供**几何 + Doppler** 的补充观测，而非替代主传感器。

**证据来源声明**：本文件所有引用均来自同目录 `staging/RADAR_raw.json` 池（29 篇论文 + 2 条厂商官方页条目，30 条 VERIFIED、1 条 PARTIALLY_VERIFIED），每条含 verification_evidence；性能数字全部绑定实验条件，标注 ABSTRACT / FULLTEXT 来源层级。厂商 datasheet 未能直接核验的部分（Navtech、Continental 官网 404/403）已如实记录在池的 rejected 数组，相关硬件描述仅采信论文原文。

引用缩写：CFEAR = arXiv 2105.01457；Kung-NDT = arXiv 2103.07908；ORORA = arXiv 2303.01876；Burnett-RSS21 = arXiv 2105.14152；DRO = arXiv 2504.20339；LowSpeed = arXiv 2509.07683；Doer-MFI20 = DOI 10.1109/MFI49285.2020.9235254；Michalczyk-IROS22 = DOI 10.1109/IROS47612.2022.9981396；TempDelay = arXiv 2503.02509；iRIOM = arXiv 2303.13962；RINO = arXiv 2411.07699；Go-RIO = arXiv 2502.08093；GaRLIO = arXiv 2502.07703；AF-RLIO = arXiv 2507.18317；Nissov = arXiv 2403.05332；NohSmoke = arXiv 2403.17441；LTR2 = arXiv 2605.02809；AreWeReady = arXiv 2203.10174；RadarSLAM = arXiv 2005.02198；4DRadarSLAM = DOI 10.1109/icra48891.2023.10160670；Open-RadVLAD = arXiv 2401.15380；NewWave = arXiv 2305.01135 (IEEE T-RO 2024)；AGV-Survey = arXiv 2307.07861 (IEEE T-IV 2024)；Oxford = arXiv 1909.01300；MulRan = DOI 10.1109/icra40945.2020.9197298；Boreas = arXiv 2203.10168 (IJRR)；K-Radar = arXiv 2206.08171；RADIATE = arXiv 2010.09076；NTU4DRadLM = arXiv 2309.00962；TI-60G = ti.com/product/IWR6843；TI-77G = ti.com/product/AWR2944。

---

## 1. REQUIRED_CAPABILITIES（必需能力）

**Q1：毫米波雷达能提供 range / velocity / angle / point cloud / Doppler 中的哪些？取决于哪类硬件？**

毫米波雷达的能力完全由硬件形态决定，本池证据可分四类：

| 硬件类别 | 提供的观测量 | 池内证据 |
|---|---|---|
| 目标级车载雷达（内置检测/跟踪固件） | 目标列表（位置+速度），一般不开放原始点云 | AreWeReady（FULLTEXT）：“the target extraction algorithms built into automotive radar may not necessarily be optimal for mapping and localization” |
| 单芯片车载点云 FMCW（76-81GHz，如 TI AWR2944 类） | 逐目标 3D 位置 + 径向 Doppler 速度；MIMO 给方位角（俯仰视天线） | Doer-MFI20（ABSTRACT）：“A standard automotive FMCW radar which measures the 3D position and Doppler velocity of each detected target”；TI-77G 官方页：“76 to 81GHz coverage with over 4GHz continuous bandwidth”，参考设计“estimate and track the position (in the azimuthal plane) and velocity of objects” |
| 2D 扫描式 FMCW（Navtech CTS350-X / CIR304-H 类，76-77GHz） | 360° 极坐标强度图（range × azimuth），帧率约 4Hz；Doppler 可观测性取决于调频波形 | CFEAR（FULLTEXT）：“roof-mounted Navtech CTS350-X FMCW radar running at 4 Hz, configured with a range resolution of γ = 4.38 cm”；Boreas（ABSTRACT）：“a 360° Navtech CIR304-H scanning radar”；DRO（FULLTEXT）说明其 Doppler 约束要求“specific frequency modulation pattern that makes radial Doppler velocities observable” |
| 4D imaging radar（加 elevation 通道） | 距离 + 方位 + **高度** + 速度四类信息，输出稀疏点云（约 400 点/帧） | iRIOM（FULLTEXT）：“the 4D imaging millimeter wave radar greatly improves the resolution in the vertical direction, thus providing four types of information: distance, azimuth, height, and velocity”，以及“point clouds are still very sparse (~400 points/scan)”；K-Radar（ABSTRACT）定义 4DRT 为“power measurements along the Doppler, range, azimuth, and elevation dimensions” |

**Q2：哪类适合机器人定位？**

结论（按本项目优先级）：

1. **最低必需配置 = 逐点/逐目标的 range + azimuth + 径向 Doppler velocity，且 Doppler 必须可观测、数据必须开放**。这是全部主流路线的公共输入：
   - 纯雷达里程计：CFEAR 在 Oxford 基准平移误差 1.76%（FULLTEXT）；DRO 在 Boreas 榜单 0.26%（FULLTEXT），并在“feature-deprived environments”的隧道中依靠 Doppler 约束保持可行。
   - 雷达-惯性里程计（RIO）：Doer-MFI20 用“3D position + Doppler velocity”实现 <0.6% 路程的终端位置误差（ABSTRACT，>200m 轨迹、动捕 GT）；Go-RIO 用点级速度把垂直漂移压到 <1%（ABSTRACT）/ 0.72%（FULLTEXT）。
   - 低速场景：LowSpeed 紧耦合“feature positions and Doppler velocities”，10cm 精度覆盖 63% 测试用例（FULLTEXT）。
2. **若承担“LiDAR 局部退化时补充”的任务，优先 4D imaging radar（有 elevation）**：NohSmoke 在 NTU4DRadLM 浓烟序列中实测 LiDAR 退化（表中 LiDAR 列为“-”），4D 雷达提供可用观测，融合后 APE 1.133m 优于纯雷达 2.142m（FULLTEXT）；iRIOM（ColoRadar，APE RMSE 0.916m vs EKFRIO 5.048m，FULLTEXT）与 Go-RIO 的高程控制都依赖 4D 点云。K-Radar 进一步说明：没有 elevation 的 3DRT“it is challenging to estimate the 3D bounding box”，同理也限制 3D 配准与建图。
3. **2D 扫描式（Navtech 类）与 4D 车载雷达都是可行路线**：Kung-NDT（ABSTRACT）证明同一 NDT 算法在 Oxford（扫描式）与 nuScenes（车载式）上都达“centimeter-level accuracy as lidar odometry, and automotive and scanning RO have similar accuracy”。选哪类取决于本项目更看重 360° 大范围重定位（扫描式，MulRan 实证“radar-based place recognition outperforms LiDAR-based one exploiting its longer-range measurements”）还是与 LiDAR/IMU 紧耦合的 3D 里程计（4D 车载式）。

**Q3：60GHz 与 77/79GHz 常见区别（以池内官方页证据为限）**

- 60GHz：TI-60G（官方页）为“Single-chip 60-GHz to 64-GHz intelligent mmWave sensor”，3TX/4RX，“4GHz continuous bandwidth”，定位工业与自主机器人（people counting、autonomous robots、area scanning），典型室内/中短距。
- 77/79GHz：TI-77G（官方页）为“Automotive, second-generation 76-GHz to 81-GHz high-performance SoC for corner and long-range radar”，4TX/4RX，“over 4GHz continuous bandwidth”，短/中/长距可配置；NewWave（ABSTRACT）指出机器人研究主流为“FMCW mmWave radars operating in the 76--81GHz range”，K-Radar（ABSTRACT）同样以 77~81GHz 为对象并论述其在恶劣天气的波长优势。
- 本项目为室外轮式平台，**应选 76-81GHz 车载/机器人段**；60GHz 类更偏室内短距，且池内未检索到 60GHz 室外里程计论文（见 rejected 记录）。

**恶劣天气/退化场景优势证据（Q4，供 REQUIRED 支撑）**：

- 浓烟：NohSmoke（FULLTEXT，NTU4DRadLM）LiDAR 失败、雷达可用、融合最优；AF-RLIO（ABSTRACT）在“smoke, tunnels”中自适应切换；LTR2（ABSTRACT）在“nighttime smoke”下 40+ km、6 个月长期运行。
- 雾/尘/烟的物理机制：NewWave（ABSTRACT）：“its longer wavelengths have the ability to bypass visual clutter such as fog, dust, and smoke”。
- 雾/雪/雨数据与系统级验证：RadarSLAM（ABSTRACT）“dark night, dense fog and heavy snowfall”；RADIATE（ABSTRACT）雾/雪采集“unique”；K-Radar（ABSTRACT）“4D Radar is a more robust sensor for adverse weather conditions”。
- 诚实校准：AreWeReady（ABSTRACT/FULLTEXT）在 Boreas 雪暴中“lidar-only pipeline achieved the best localization accuracy even during a snowstorm”，雷达-only“competitive accuracy with a much smaller map”。**因此雷达应定位为退化场景的补充与冗余备份（“redundant backup system”，AreWeReady 原文），不是全天候全面替代**。

---

## 2. NICE_TO_HAVE（加分能力）

1. **Elevation/俯仰通道**（即 4D 化）：LiDAR 退化时的 3D 配准与建图、垂直漂移控制（iRIOM、Go-RIO 证据链）。
2. **可观测 Doppler 的调频波形 + 开放 Doppler 数据**：DRO 显示具备该波形的雷达可把平移误差从 0.26% 进一步降到 0.18%（ABSTRACT/FULLTEXT），并在隧道中决定成败。
3. **多雷达支持/多路输出**：LowSpeed 明确支持 multi-radar 并以此覆盖角盲区（FULLTEXT 摘要级能力声明“multi-radar support”）。
4. **丰富数据形态输出**（raw 强度阵列 / 极坐标图 / 点云+Doppler）：MulRan（ABSTRACT）同时提供“raw-level and image-format data”，便于算法迭代与跨模态研究。
5. **明确角精度/量程规格文档**：LowSpeed 自采平台用“angular accuracy of 0.5°、detection range up to 250 m”的 ARS548 级雷达完成厘米级验证（FULLTEXT），说明角精度指标对低速精配准有实际意义。
6. **与陀螺/IMU 的安装稳定性**：DRO 消融显示去掉陀螺偏向估计后误差恶化至 6.00%/1.57°（FULLTEXT），雷达安装角 0.172° 未修正即引入 1.46% 误差（FULLTEXT）——机械安装面与标定手段是隐性加分项。

---

## 3. UNNECESSARY_FEATURES（不必要/不应付费的能力）

1. **只有目标级存在检测/跟踪输出、不开放点云与 Doppler 的“黑盒”雷达**：池内全部定位算法（CFEAR、ORORA、DRO、Go-RIO、iRIOM、NohSmoke 等）都消费点云/强度图/Doppler；AreWeReady（FULLTEXT）明确指出车载雷达内置目标提取“may not necessarily be optimal for mapping and localization”。**这类硬件无法支撑本项目的定位研究**。
2. **无 elevation 的 3D 张量类输出（3DRT）**：K-Radar（ABSTRACT）说明其难以支撑 3D 任务；若采购 4D 雷达，务必确认输出含 elevation 的点云/张量而非降维 3DRT。
3. **面向 ADAS 检测/分类的专用固件能力**（如目标分类、跟踪框输出）：与里程计/建图主线无直接关系，属感知域功能，不应作为本项目选型权重（池内定位文献无一依赖目标类别）。
4. **超远量程堆料**：池内低速厘米级验证（LowSpeed）与主流数据集（Oxford 4Hz、约 4.38cm 分辨率，CFEAR FULLTEXT）都在中短距完成；“更远”没有对应的池内定位收益证据，不作为优先项（此为工程判断，非文献结论）。

---

## 4. COMMON_INTERFACES（常见接口）

以池内两条官方页条目与论文实测平台为据：

- **TI 单芯片类（60/77GHz）**：板载处理（Cortex + DSP + radar hardware accelerator，硬件 CFAR/FFT），EVM 可“enable access to point-cloud data”（TI-60G 官方页）；对外接口：CAN-FD、SPI、UART、QSPI、I2C、LVDS（TI-60G），AWR2944 增至“2× CAN-FD, Ethernet, 4-lane Aurora LVDS, CSI2”（TI-77G 官方页）。
- **Navtech 扫描式类**：论文消费形态为 360° polar intensity image / 1D 强度阵列（MulRan ABSTRACT 的数据形态描述；Oxford 4.7TB、240,000+ 扫描，ABSTRACT），帧率 4Hz（CFEAR FULLTEXT）；DRO 自采平台使用“Navtech RAS6 radar, a Silicon Sensing DMU41 imu, a Velodyne Alpha Prime lidar, and an accurate Applanix RTK-GNSS/INS solution”（DRO FULLTEXT）。**厂商以太网接口细节本次未能从官网核验（404），采购阶段需索取 datasheet 确认**（见 rejected 记录）。
- **数据形态清单**（采购技术协议应覆盖）：raw IQ / polar intensity image / 点云（含逐点 Doppler 径向速度）/（4D 雷达）含 elevation 的点云或张量。
- **时间戳载体**：与 IMU/LiDAR 共钟的打点机制（见下节）。

---

## 5. SYNC_REQUIREMENTS（时间戳/触发要求）

池内证据一致表明：**雷达-IMU 时间同步是 RIO 精度的一等公民**。

1. TempDelay（ABSTRACT）：在线时延标定“significantly reduces localization error compared to systems that disregard time synchronization”——系统必须支持在线时延估计或硬件级同步。
2. Go-RIO（FULLTEXT）指出既有方法“often ignore temporal discrepancies between radar and IMU by simplifying the complexities of asynchronous data streams”，并用连续时间 GP 预积分处理异步；GaRLIO（FULLTEXT）用“sweep reconstruction to synchronize the end timestamp of LiDAR and radar, using the radar's timestamp”——要求雷达输出**扫描级结束时间戳**。
3. DRO（FULLTEXT）在 MulRan 上实测“the difference between consecutive imu data timestamps presents a variation of ±35% around the nominal period of 10 ms and ... a constant offset with respect to the other sensors”，且需修正雷达安装航向 0.172°——**数据集级时间戳质量缺陷是常态，硬件上要预留标定手段**。
4. iRIOM（FULLTEXT）支持在线外参估计，并给出 GT 侧参考：RTK 良好时约 3cm，RTK 中断 10s 降至 25cm——本项目在 GNSS 拒止评测时同样需要 GT 降级策略。

**给采购/集成的要求（工程结论）**：雷达需提供稳定设备时间戳（与 IMU 同钟源，或 PPS/触发输入），扫描周期与时间戳抖动需在 datasheet 中给出；软件侧保留在线时延/外参标定接口。

---

## 6. RESEARCH_DATASETS（公开数据集）

| 数据集 | 规模与传感器 | 天气/场景 | 适配用途 |
|---|---|---|---|
| Oxford Radar RobotCar | 280km、32 遍、240,000+ Navtech CTS350-X 扫描（4Hz、4.38cm 分辨率）、双 Velodyne、GPS/INS，附优化雷达里程计 GT | 城市，天气/交通/光照多样 | 2D 扫描式里程计/重定位基线（CFEAR、ORORA、Open-RadVLAD 均在此评测） |
| MulRan | 城市 PR 数据集，radar+LiDAR，raw 阵列+极坐标图，6D GT | 韩国多城市，时/空多样性 | 重定位、跨模态；DRO MulRan 平均 1.45% |
| Boreas | >350km、一年四季重复路线，Navtech CIR304-H + Alpha Prime + 相机，厘米级 GT，公开榜单 | 雨、雪、夜 | 里程计/定位榜单对标（DRO 0.26%）、恶劣天气校准（AreWeReady 雪暴实验） |
| K-Radar | 35K 帧 4DRT（Doppler/range/azimuth/elevation）+ 3D 框 + LiDAR/双目/RTK-GPS | 雾、雨、雪 | 4D 雷达感知与恶劣天气论证 |
| RADIATE | 3h 雷达图像、>200K 标注（约 4.6 目标/幅）+ 双目 + 32 线 LiDAR + GPS | 日/夜/雨/雾/雪 | 恶劣天气感知与融合、定位建图 |
| NTU4DRadLM | 17.6km、85min、6 条轨迹（246m–6.95km），4D 雷达+热像+IMU+LiDAR+可见光+RTK GPS，精调 GT 与预设回环 | 雨/雪/烟/雾，结构化与非结构化；**含低速机器人平台** | **与本项目传感器组合最贴合**；NohSmoke、AF-RLIO 等以此为退化实验场 |

补充（作为池内论文的实验数据集出现，未单列入池）：ColoRadar（iRIOM 表 IV）、SNAIL Radar 与 HeRCULES（LowSpeed 低速序列 RPE 0.06m 的对比实验）。

---

## 7. KNOWN_ALGORITHMS（代表性方法与性能，全部带条件）

**A. 雷达里程计（2D 扫描式 / 跨类型）**
- CFEAR（IROS 2021）：oriented surface points + point-to-line。Oxford 基准平移 1.76% / 0.5°/100m（SCV），55Hz 单 CPU 线程；矿区/试验场大环 15m/1235m（1.2%）（FULLTEXT）。
- Kung-NDT（ICRA 2021）：NDT 配准，同一算法兼容扫描式与车载式；对 SOTA 平移误差降 51%（Oxford）/30%（nuScenes），“centimeter-level accuracy as lidar odometry”（ABSTRACT）。
- ORORA（ICRA 2023）：GNC 旋转 + 各向异性平移估计，专治雷达外点与互干扰（ABSTRACT，无数值）。
- Burnett-RSS21（RSS 2021）：无监督学习特征 + 滑窗概率估计，“outperforms most hand-crafted methods”，并在恶劣天气验证（ABSTRACT）。
- **DRO（RSS 2025，当前公开榜最强之一）**：直接法 + Doppler 畸变补偿 + 陀螺。Boreas 榜 0.26%/0.05°/100m（对比 CFEAR++ 0.51%、STEAM-RIO++ 0.62%）；Doppler 使能波形下 0.18%；MulRan 平均 1.45%/0.38°；隧道场景 Doppler 约束是成败关键（FULLTEXT）。

**B. 雷达-惯性里程计（RIO）**
- Doer-MFI20（MFI 2020，奠基）：车载 FMCW 逐目标 3D 位置+Doppler → RANSAC 自车速度 → EKF。>200m 室内外轨迹终端误差 <0.6% 路程，动捕 GT（ABSTRACT）。
- Michalczyk-IROS22（IROS 2022）：EKF 紧耦合雷达 3D 点 range+velocity 与 IMU，UAV 真机，面向 GNSS 拒止/烟雾/异常光照（ABSTRACT）。
- RINO（IEEE T-ASE 2025）：自适应松耦合 + 投票式位姿 + 不确定性入 MAP；相对 ORORA 平移再降 1.06%、旋转再降 0.09°/100m（ABSTRACT）。
- Go-RIO（ICRA 2025）：4D 雷达地面优化滤波 + GP 连续速度预积分；高程误差 0.72%（18m/2.5km）、垂直漂移 <1%（FULLTEXT/ABSTRACT）。
- iRIOM（RA-L 2023）：首个 4D 雷达惯性 SLAM（GNC 自车速度 + scan-to-submap + 回环）；ColoRadar Seq1 APE RMSE 0.916m（vs EKFRIO 5.048m）（FULLTEXT）。
- TempDelay（IROS 2025）：因子图内在线时延标定显著降低定位误差（ABSTRACT）。

**C. Radar + LiDAR + IMU 融合（本项目最相关的成熟路线）**
- GaRLIO（ICRA 2025）：雷达点级速度用于重力估计与动态剔除；垂直均值误差 1.21m/2.045km（FULLTEXT）。
- Nissov（ICRA 2024）：因子图按退化轴传递雷达信息，LiDAR 正常时保精度（真机飞行平台，ABSTRACT）。
- NohSmoke（2024）：浓烟中 LiDAR 失败、融合 APE 1.133m vs 纯雷达 2.142m（FULLTEXT，NTU4DRadLM）。
- AF-RLIO（ICRA 2025）：4D 雷达判定 LiDAR 退化并切源，烟/隧道实测（ABSTRACT）。
- LTR2（2026）：LiDAR teach + 4D radar repeat 跨模态范式，40+ km、6 个月、3 平台、夜间烟雾，厘米级（ABSTRACT）。

**D. 重定位 / Place Recognition**
- Open-RadVLAD（RadarConf 2024）：870 对轨迹穷举，median Recall@1 91.52%（vs RaPlace 69.55%）（ABSTRACT）。
- MulRan（ICRA 2020）：实证雷达 PR 优于 LiDAR PR（量程更长）（ABSTRACT）。

**E. 低速场景**
- LowSpeed（2025/RA-L 2026 版）：紧耦合雷达-Doppler EKF + 多雷达 + 特征裁剪；63% 用例 ≤10cm、末端 13cm；公开低速序列 RPE 0.06m vs Doppler-SLAM 0.14m（FULLTEXT）。

---

## 必答问题对照小结

1. **能提供哪些观测量、取决于什么硬件**：见第 1 节表格——目标级 / 单芯片点云 / 2D 扫描式 / 4D imaging 四类，能力从“目标列表”到“距离+方位+高度+速度”递进。
2. **哪类适合机器人定位**：逐点 range+azimuth+Doppler 是底线；LiDAR 退化补充任务优先 4D imaging（有 elevation）；2D 扫描式与 4D 车载均可行，取决于重定位覆盖 vs 3D 紧耦合的侧重。
3. **60GHz vs 77/79GHz**：60-64GHz 偏室内/工业中短距（TI IWR6843）；76-81GHz 为机器人/车载室外主流（NewWave、K-Radar、TI AWR2944），本项目应选 76-81GHz。
4. **恶劣环境优势证据**：浓烟（NohSmoke 定量表、AF-RLIO、LTR2）、雾/尘/烟物理机制（NewWave）、雾/雪/夜（RadarSLAM、RADIATE、K-Radar）；同时以 AreWeReady 校准“雪暴中 LiDAR 仍最准”的边界。
5. **Radar Odometry 通常性能**：城市基准平移误差 0.26%~3.7% 区间（DRO 0.26% Boreas / CFEAR 1.76% Oxford / DRO-MulRan 1.45% / Cen 3.72%），旋转 0.05~0.5°/100m；RIO 终端误差 <0.6% 路程（Doer，>200m）。
6. **Radar+IMU/LiDAR 融合成熟路线**：RIO（EKF/因子图/GP 预积分，Doer→Michalczyk→RINO→Go-RIO）与 Radar-LiDAR-IMU（GaRLIO/Nissov/AF-RLIO/NohSmoke）两条线均已开源可复现（GaRLIO、DRO、ORORA、Burnett 等代码公开，见各自 notes）。
7. **公开数据集**：Oxford Radar RobotCar、MulRan、Boreas、K-Radar、RADIATE、NTU4DRadLM（主表），另有 ColoRadar、SNAIL、HeRCULES 作为池内论文实验场。

## 未解决疑点（移交采购/下一阶段）

1. Navtech（CIR304-H/CTS350-X）与 Continental（ARS548）官方 datasheet 未能直接核验（官网 404/403），采购询价时必须索取正式 datasheet 核对：扫描帧率、距离分辨率、Doppler 可观测性与开放接口、时间戳/触发。
2. 4DRadarSLAM 为元数据级验证（PARTIALLY_VERIFIED），未读摘要，不入性能结论。
3. 60GHz 频段缺室外定位侧文献（检索无命中），如供应链仅能提供 60GHz 方案需另行补充调研。
4. NohSmoke 与 AreWeReady 的正式发表 venue 未在本次会话核验到，引用时保持 arXiv 编号。
5. 各数据集间百分比误差不可直接互比（评测协议不同，见池 conflicts 第 2 条）；本项目自建评测必须固定 KITTI 风格子序列定义与 GT 等级。
