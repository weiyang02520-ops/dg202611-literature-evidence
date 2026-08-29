# 08 公开数据集清单（DG-202611 多源导航定位）

> 调研日期：2026-08-29。所有条目均在本会话内经实际抓取核验（官网/论文 API/GitHub API），核验方式见逐条 evidence 与 staging/DATASETS_raw.json。
> 状态标注：VERIFIED = 官方页面/官方仓库/API 元数据直接核验通过；PARTIAL = 存在性核验通过但官网当前不可达或字段不全。

## 一、总表

| Dataset | Sensors | Environment | Ground Truth | Size | License | Official Link | Useful For DG | Limitations |
|---|---|---|---|---|---|---|---|---|
| KITTI | 灰度/彩色双目 0.5MP@10Hz；Velodyne HDL-64E；OXTS GPS/IMU@10Hz；全套标定 | 德国卡尔斯鲁厄城市/乡村/高速（车载） | 官方 odometry 真值（Velodyne+GPS/IMU 生成） | 页面未标总量（分序列） | CC BY-NC-SA 语义（页面原文：署名+非商业+相同方式共享） | [cvlibs.net/datasets/kitti](https://www.cvlibs.net/datasets/kitti/) | 轮式车载多源基线；OXTS 可人工抠 GNSS 构造退化 | 城市峡谷多路径样本有限；无 UWB/雷达/事件相机；非商用 |
| EuRoC MAV | 双目 WVGA 灰度 2x20FPS；MEMS IMU 200Hz | 工业/室内环境（MAV 飞行） | Vicon 动捕 6D + Leica MS50 激光跟踪仪 | 页面未标总量 | 页面未标注（查 ETH Research Collection DOI 页） | [projects.asl.ethz.ch/datasets/euroc-mav](https://projects.asl.ethz.ch/datasets/euroc-mav/) | VIO 基准（ZED 2i+IMU 算法对照）；高精度 GT 评误差传播 | 无人机非轮式；无 GNSS/LiDAR/UWB |
| TUM-VI | 双目全局快门单色 1024x1024@20Hz；IMU 200Hz；硬件同步 | 室内房间/走廊/大厅 + 室外 + 劣光管道 | 动捕 120Hz（room 全轨迹，其余起止段） | 页面未标总量（rosbag/EuRoC/DSO 格式） | 数据 CC BY 4.0；代码 BSD-2-Clause | [cvg.cit.tum.de](https://cvg.cit.tum.de/data/datasets/visual-inertial-dataset) | VIO 基准 + 相机-IMU 标定/时间同步参照（Kalibr 流程） | 无 GNSS/LiDAR/轮速；手持平台 |
| MulRan | 雷达 + LiDAR（多模态测距）；IMU+GPS（2020-11 追加） | 韩国多城市；月级跨度、逆行/车道级重访 | 全序列 6D 基线轨迹 | 页面未标总量 | 2023-09 更新，许可文本在站点 Citation 标签页（未抓取，需查） | [sites.google.com/view/mulran-pr](https://sites.google.com/view/mulran-pr/home) | 雷达+LiDAR 定位/位置识别；长时退化测试；配 ROS 播放器 | 首页无传感器型号与 GT 生成细节 |
| Oxford Radar RobotCar | Navtech CTS350-X 毫米波 FMCW 雷达；双 HDL-32E；原 RobotCar 全套（含立体相机、GPS/INS） | 英国牛津城区，280 km | 优化后雷达里程计真值 | 280 km | CC BY-NC-SA 4.0（非商业学术） | [oxford-robotics-institute.github.io](https://oxford-robotics-institute.github.io/radar-robotcar-dataset/) | 毫米波雷达（拟采购）定位/里程计公开基准 | GT 非绝对定位级；非商用 |
| DSEC | 双 VGA 事件相机；双全局快门彩色相机；LiDAR；RTK GPS；IMU | 驾驶场景 53 序列（顺光/逆光/夜间） | 事件双目视差真值；光流/语义/检测标注 | 页面未标总量 | CC BY-SA 4.0（允许商用） | [dsec.ifi.uzh.ch](https://dsec.ifi.uzh.ch/) | 事件相机（拟采购）+LiDAR+RTK GPS 驾驶数据；明暗突变退化 | 无轮速/UWB/毫米波；定位级 GT 主页未明示 |
| MVSEC | 双目 DAVIS 事件相机（多载具）等（官网不可达，仅论文级核验） | 室内/室外/驾驶 | 未核对 | 未核对 | 未核对 | [mvsec.io](https://mvsec.io/)（当前不可达） | 事件+LiDAR+动捕驾驶数据（官网恢复后可用） | 官网 TLS 失败；**PARTIAL**，仅论文 DOI:10.1109/lra.2018.2800793 已核 |
| M3ED | Prophesee EVK4 HD 事件双目 1280x720；帧相机双目 1280x800；64 线 LiDAR | 轮式车（越野/密林 110min）+ Spot + 无人机 | evo 格式 GT 位姿（FasterLIO）+ GT 深度 + 语义 | 页面未标总量（processed/raw/code 开放） | CC BY-SA 4.0 | [m3ed.io](https://m3ed.io/) | 与本项目重叠度最高的事件类数据；密林=天然 LiDAR/视觉退化 | GT 为相对局部地图；无 GNSS/UWB/毫米波 |
| UrbanNav | 多频 GNSS 接收机（原始 RINEX）；HDL-32E LiDAR；相机；IMU | 亚洲深城市峡谷（香港 Honda Fit 车载 + 东京） | NovAtel SPAN-CPT GNSS/INS | 未标注（香港/东京两套） | 仓库未标注 license（需联系维护方） | [github.com/IPNL-POLYU/UrbanNavDataset](https://github.com/IPNL-POLYU/UrbanNavDataset) | **GNSS 退化首选**：RINEX 原始观测可剔除卫星/加噪构造 NLOS/多路径/outage；论文 DOI:10.33012/navi.602 | 许可未标注；需核对采集平台一致性 |
| KAIST Complex Urban | LiDAR + 立体相机 + 各类位置传感器（扩展版含 LAS 3D 图与 ROS 工具） | 韩国复杂城区（大都市/复杂建筑/居民区），40+ 序列 | 扩展论文含 3D SLAM 图（页面未展开） | 40+ 序列（更新日志推断） | CC BY-NC-SA 4.0（KAIST+Naver Labs 版权） | [sites.google.com/view/complex-urban-dataset](https://sites.google.com/view/complex-urban-dataset/) | 城市峡谷 GNSS 退化样本 + 地图匹配素材；论文 DOI:10.1177/0278364919843996 | 原官网不可达（以 Google Sites 为准）；非商用 |
| NCLT | HDL-32E；Ladybug3 全向相机；GX3 IMU；KVH 光纤陀螺；**轮式里程计**；标准 GPS + RTK GPS | 密歇根北校区 Segway 轮式平台，27 次采集跨 15 个月 | SLAM 图+里程计插值 ~100Hz GT（含协方差） | 34.9 h / 147.4 km | ODbL（Open Database License） | [robots.engin.umich.edu/nclt](https://robots.engin.umich.edu/nclt/) | **轮式契合度最高**：轮速+IMU+双 GPS 可自构 GNSS 降级对比；长时段退化 | 2012-13 数据较旧；无 UWB/事件/毫米波 |
| Newer College | D435i 双目+IMU；OS-1-64（原版）；Alphasense 四目 + OS-0-128（扩展） | 牛津校园手持步行 6.7 km；快运动/无纹理/光照突变 | 厘米级 6-DoF 每扫描位姿（BLK360 2.9 亿点） | 页面未标总量 | 页面未标注（查下载页） | [ori-drs.github.io/newer-college-dataset](https://ori-drs.github.io/newer-college-dataset/) | LiDAR/视觉 SLAM 高精度评测；剧烈运动=视觉退化样本 | 手持非轮式；无 GNSS 记录；许可未标注 |
| M2DGR / plus | 6 鱼眼+1 朝天+透视相机；事件相机；红外相机；VI 传感器；双 IMU；VLP-32C；消费 GNSS + RTK GNSS-IMU | 轮式地面机器人，室内外 36 序列 ~1TB | 动捕 + 激光 3D 跟踪仪 + RTK | 36 序列 ~1TB | MIT | [github.com/SJTU-ViSYS/M2DGR](https://github.com/SJTU-ViSYS/M2DGR) | 轮式+GNSS+事件相机一体化（RA-L 2021）；事件段可支撑事件退化研究 | 消费级 GNSS；室外 GT 覆盖有限 |
| SJTU_GVI | u-blox ZED-F9P（GNSS 原始观测）+ 视觉 + IMU | 真实车辆，面向 GNSS-SLAM | README 未列出（待核） | 未核对 | 未标注 | [github.com/sjtuyinjie/SJTU_GVI](https://github.com/sjtuyinjie/SJTU_GVI) | ZED-F9P 原始观测车载数据，与 UrbanNav 互补构造 RTK 失锁/浮点退化 | 许可与 GT 未核 |
| eWINE UWB-LOS-NLOS | UWB 测距/CIR（1016 采样点/测量） | 7 个室内场景 LOS/NLOS | LOS/NLOS 标注（轨迹级真值未核） | 7 场景 | CC BY 4.0 | [github.com/ewine-project/UWB-LOS-NLOS-Data-Set](https://github.com/ewine-project/UWB-LOS-NLOS-Data-Set) | UWB（有硬件）NLOS 识别/误差建模标准基准；为 UWB dropout 仿真提供真实误差分布 | 2017 年设备代差；无轨迹级数据 |
| Indoor UWB Positioning & Tracking（Sci Data 2023） | UWB 测距+CIR | 4 个室内环境 | 论文级描述（未开正文核） | 未核对 | CC BY 4.0 | [nature.com/articles/s41597-023-02639-5](https://www.nature.com/articles/s41597-023-02639-5) | 较新 UWB 定位/跟踪数据（DOI:10.1038/s41597-023-02639-5），支撑 UWB 误差建模 | 正文有 cookie 墙，数据仓储链接待开 |
| Deep UWB（Zenodo） | Decawave EVB1000 测距数据 | 室内 | 测距误差标注（ranging error mitigation） | 2 文件 | CC BY 4.0 | [zenodo.org/records/4399187](https://zenodo.org/records/4399187) | UWB bias/NLOS 误差模型参数化（配套 arXiv:2011.14684） | EVB1000 老款；规模有限 |
| UTIL UWB（UTIAS） | DWM1000 UWB（TDoA2/TDoA3）+ IMU + 光流 + ToF + 气压计（Crazyflie 四旋翼） | 7.0x8.0x3.5m 室内飞行场；LOS/NLOS 障碍；~150min 飞行 | 10x Vicon 毫米级动捕（锚点全站仪测量，RMSE~1.12mm） | 未标注（.7z + ROS1/ROS2 脚本 + 示例 EKF） | 页面/仓库未标注 | [learnsyslab.github.io/util-uwb-dataset](https://learnsyslab.github.io/util-uwb-dataset/) | UWB TDoA+IMU 融合与 UWB dropout 评测高真值数据（IJRR 2024） | 室内小尺度；旋翼非轮式 |

## 二、按本项目退化场景的选用建议

| 退化场景 | 首选数据集 | 用法 |
|---|---|---|
| GNSS outage / degraded（多路径、NLOS、失锁） | UrbanNav（RINEX 原始观测可编辑）+ KAIST Complex Urban + NCLT（标准 GPS vs RTK GPS） | 剔除卫星/注入偏差/直接删段构造 outage；以 RTK 真值段当基准 |
| LiDAR 退化（几何退化/天气） | M3ED（密林）+ NCLT（长时段）+ Newer College（无纹理） | 真实退化段做评测；天气型退化用仿真（见 05/组 J 报告），但**仿真结果不得当实车结论** |
| UWB dropout / NLOS | eWINE + Deep UWB + UTIL | 误差分布参数化 → 注入实车 UWB 数据；UTIL 用于融合算法对照 |
| VIO / 视觉退化（暗光、运动模糊） | EuRoC、TUM-VI、M3ED、M2DGR（事件相机段） | 注入时延/丢帧/噪声后测 VIO 漂移 |
| 毫米波雷达（拟采购） | Oxford Radar RobotCar + MulRan | 雷达里程计/位置识别基线；采购前可行性论证素材 |

## 三、使用注意（重要）

1. **数据集性能 ≠ 实车性能。** 任何"在 KITTI/UrbanNav 上表现好"的结论只说明算法在该数据分布内有效；数据集的传感器型号、安装位、时间同步质量、地面真值精度都与本项目实车（轮式平台 + 轮速计 + IMU + 北斗/GNSS/RTK + LiDAR + ZED 2i + UWB，外加拟采购毫米波雷达与事件相机）不同。数据集只能用于：算法选型、参数初值、失效模式分析、论文对照。
2. 数据集 GT 有层级差异：Vicon/全站仪（mm 级）> RTK/SPAN-CPT（cm 级）> 雷达里程计/SLAM 图（漂移随时间累积）。评估时必须注明 GT 类型，跨数据集比较精度数字没有意义。
3. 退化段（GNSS 多路径、隧道、密林）在数据集中占比小且标注少；用其统计误差分布时注意样本量与选择性偏差。
4. 许可约束：KITTI/Oxford Radar/Complex Urban 为 **非商业许可（NC 系）**，作品演示、论文、开源代码可用；若比赛成果涉及商业转化需重新评估或替换数据。UrbanNav/SJTU_GVI/util-uwb-dataset 等许可未标注，使用前联系维护方书面确认。
5. 本清单所有链接均于 2026-08-29 实际抓取核验；MVSEC 官网（mvsec.io）与 KAIST 原官网（irap.kaist.ac.kr）当日不可达，分别以论文 DOI 与官方 Google Sites 页替代核验，标注为 PARTIAL。
6. 未入池候选（查无实据或未核验，不得直接引用）：GOOSE、HeRCULES、4Seasons、TUM-VIE、RTK-SLAM（arXiv:2604.07151）、Nature Sci Data s41597-026-06716-3。详见 staging/DATASETS_raw.json rejected/conflicts。
