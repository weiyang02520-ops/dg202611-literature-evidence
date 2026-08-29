# 09 开源实现图谱（DG-202611 多源导航定位）

> 调研日期：2026-08-29。所有仓库均经 GitHub API（api.github.com）核验 license/语言/更新时间；ROS1/ROS2 支持仅采信 README/仓库文件中的明示证据（raw README 抓取），未检出证据者标"未核验"。
> 风险声明：**本图谱未执行任何仓库代码，仅做调研与链接核验**。reproducibility 为基于维护活跃度/文档/使用广度的调研判断，不等于已复现。

## 一、总表

| Paper / Tool | Repository | Official or Third-party | License | Language | ROS1-ROS2 | Last Update | Reproducibility | Relevant Module | Risk |
|---|---|---|---|---|---|---|---|---|---|
| FAST-LIO（LIO，迭代 EKF 路线） | [hku-mars/FAST_LIO](https://github.com/hku-mars/FAST_LIO) | 官方（HKU MARS） | GPL-2.0 | C++ | ROS1（README：ROS >= Melodic）；ROS2 社区分支未核验 | pushed 2025-01-15，5109★ | 高（未实机复现） | LiDAR 里程计/建图 | GPL 传染性；未执行代码 |
| LIO-SAM（因子图 LIO） | [TixiaoShan/LIO-SAM](https://github.com/TixiaoShan/LIO-SAM) | 官方（论文作者） | BSD-3-Clause | C++ | ROS1 主干 + 官方 ros2 分支（README 明示） | pushed 2025-02-14，4899★ | 高（未实机复现） | LiDAR SLAM；因子图融合同源参考 | 未执行代码 |
| VINS-Fusion（VIO+GPS 融合） | [HKUST-Aerial-Robotics/VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) | 官方 | GPL-3.0 | C++ | ROS1（Kinetic/Melodic 检出）；ROS2 未检出 | pushed 2024-05-23，4689★ | 高（未实机复现） | VIO+GNSS 融合（ZED 2i+IMU+GNSS） | 维护放缓；未执行代码 |
| OpenVINS（滤波 VIO 平台） | [rpng/open_vins](https://github.com/rpng/open_vins) | 官方（Delaware rpng） | GPL-3.0 | C++ | ROS1+ROS2（Dockerfile_ros1_*/Dockerfile_ros2_* 与 CI 徽章明示） | pushed 2025-11-30，3064★ | 高（未实机复现） | VIO 基线与算法研究 | 未执行代码 |
| GVINS（GNSS-视觉-惯性紧耦合） | [HKUST-Aerial-Robotics/GVINS](https://github.com/HKUST-Aerial-Robotics/GVINS) | 官方（ICRA 2022） | GPL-3.0 | C++ | ROS1（Kinetic/catkin 检出） | pushed 2021-09-11，1157★ | 中（年久未更，依赖旧环境） | GNSS 退化下紧耦合融合核心参考 | 维护停滞；未执行代码 |
| GTSAM（因子图 C++ 库） | [borglab/gtsam](https://github.com/borglab/gtsam) | 官方（Georgia Tech） | API 返回 NOASSERTION（以仓库 LICENSE 为准） | C++/Python | 非 ROS 库（双版本均可集成） | pushed 2026-08-28，3658★ | 高（未实机复现） | 多源融合因子图底座（轮速/IMU/GNSS/UWB/雷达统一） | license 字段未标准化，需人工核对条款 |
| RTKLIB 增强版（低成本 RTK） | [rtklibexplorer/RTKLIB](https://github.com/rtklibexplorer/RTKLIB) | 第三方维护分支（主线 rtklib.com） | API 返回 NOASSERTION | C | 非 ROS（独立解算器，桥接接入） | pushed 2026-08-28，966★ | 高（未实机复现） | 北斗/GNSS/RTK 前端解算与质量控制 | 增强分支与官方线差异需评估 |
| Kalibr（相机-IMU 标定） | [ethz-asl/kalibr](https://github.com/ethz-asl/kalibr) | 官方（ETH ASL） | API 返回 NOASSERTION | C++/Python | ROS1（README 明示）；ROS2 未核验 | pushed 2024-03-30，5684★ | 高（未实机复现） | ZED 2i-IMU 外参/时偏标定 | ROS2 需容器；未执行代码 |
| robot_localization（EKF 融合节点） | [cra-ros-pkg/robot_localization](https://github.com/cra-ros-pkg/robot_localization) | 官方（社区标准包） | API 返回 NOASSERTION | C++ | ROS1+ROS2（默认分支 rolling-devel） | pushed 2026-07-16，1949★ | 高（未实机复现） | 轮速+IMU+GNSS/UWB EKF 兜底融合 | EKF 表达力有限；未执行代码 |
| fuse（因子图融合框架） | [locusrobotics/fuse](https://github.com/locusrobotics/fuse) | 官方（Locus Robotics） | API 返回 NOASSERTION | C++ | README 未明示 ROS2 状态（未核验） | pushed 2026-08-19，876★ | 中 | 自定义因子融合（UWB/雷达因子扩展） | ROS2 迁移状态不明；未执行代码 |
| ESIM 事件相机仿真器 | [uzh-rpg/rpg_esim](https://github.com/uzh-rpg/rpg_esim) | 官方（CoRL 2018） | MIT | C++ | README 未明示（ROS1 catkin 历史）；未核验 | pushed 2023-12-25，727★ | 中（依赖较老） | 事件相机仿真/退化注入 | 旧地址 esim_ros 已 404；未执行代码 |
| v2e 视频转事件仿真器 | [SensorsINI/v2e](https://github.com/SensorsINI/v2e) | 官方（CVPRW 2021 作者） | MIT | Python | 非 ROS | pushed 2026-04-13，481★ | 高（未运行验证） | 实拍视频→事件流（退化输入构造） | 未执行代码 |
| rpg_dvs_ros（事件驱动/评测） | [uzh-rpg/rpg_dvs_ros](https://github.com/uzh-rpg/rpg_dvs_ros) | 官方 | MIT | C++ | ROS1（历史驱动） | pushed 2025-03-11，332★ | 中 | 事件相机数据链路参考 | 绑定老硬件；未执行代码 |
| hector_gazebo（GPS/IMU 漂移噪声插件） | [tu-darmstadt-ros-pkg/hector_gazebo](https://github.com/tu-darmstadt-ros-pkg/hector_gazebo) | 官方（TU Darmstadt） | 未标注（API None） | C++ | ROS1 生态；未核验 | pushed 2023-10-10，200★ | 中 | Gazebo GNSS 漂移/IMU 噪声注入插件基础 | license 未标注；未执行代码 |
| gazebo_ros_pkgs（ROS-Gazebo 桥+传感器插件） | [ros-simulation/gazebo_ros_pkgs](https://github.com/ros-simulation/gazebo_ros_pkgs) | 官方（Open Robotics） | 未标注（API None） | C++ | ROS1 版已归档（ROS2 版走独立分支/新生态） | **archived: true**，pushed 2025-02-26，864★ | 中（仅作参考） | GPS/IMU/LiDAR 插件参考实现 | **仓库已归档**，勿作新开发基线 |
| gz-sim（新一代 Gazebo） | [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | 官方 | Apache-2.0 | C++ | 面向 ROS2（ros_gz 桥接） | pushed 2026-08-29，1472★ | 高（未实机复现） | 退化场景仿真底座（ROS2 路线） | 与 Gazebo Classic 插件不兼容，迁移有成本 |
| PX4-SITL_gazebo-classic（传感器模型/世界包） | [PX4/PX4-SITL_gazebo-classic](https://github.com/PX4/PX4-SITL_gazebo-classic) | 官方（PX4） | 未标注（API None） | C++ | 非 ROS 绑定（MAVROS/uxrce 接入） | pushed 2026-07-15，466★ | 中 | GPS 精度/IMU 噪声参数模型参考 | classic 版路线取舍需评估 |
| gnss-ins-sim（GNSS+INS 误差仿真器） | [Aceinna/gnss-ins-sim](https://github.com/Aceinna/gnss-ins-sim) | 官方（Aceinna） | MIT | Python | 非 ROS | pushed 2024-11-27，1485★ | 高（未运行验证） | IMU bias/随机游走 + GNSS 噪声/失锁序列生成 | 误差模型需与本项目器件标定参数适配 |
| util-uwb-dataset（UWB TDoA 数据+示例 EKF） | [learnsyslab/util-uwb-dataset](https://github.com/learnsyslab/util-uwb-dataset) | 官方（IJRR 2024 数据） | 未标注（API None） | 脚本（ROS1/ROS2 均提供） | ROS1+ROS2（官网明示） | pushed 2025-10-27，60★ | 高（未运行验证） | UWB TDoA 解析与 UWB-IMU 融合基准 | license 未标注 |
| ORORA（外点鲁棒雷达里程计，ICRA 2023） | [url-kaist/outlier-robust-radar-odometry](https://github.com/url-kaist/outlier-robust-radar-odometry) | 官方（KAIST URL） | GPL-3.0 | C++ | ROS1（catkin build 检出） | pushed 2025-03-27，214★ | 中 | 毫米波雷达里程计（拟采购雷达基线） | GPL 传染性；未执行代码 |
| RIO 图优化雷达-惯性里程计 | [ethz-asl/rio](https://github.com/ethz-asl/rio) | 官方（ETH ASL） | BSD-3-Clause | C++ | ROS1 Noetic（README 明示） | pushed 2025-08-04，156★ | 中 | 雷达-惯性组合（轮式平台参考） | 未执行代码 |
| RIO EKF 4D 雷达-惯性 | [christopherdoer/rio](https://github.com/christopherdoer/rio) | 官方（论文作者） | GPL-3.0 | C++/Python | ROS1（Kinetic/Melodic/Noetic 明示） | pushed 2022-08-11，303★ | 中 | 4D 毫米波雷达 EKF 融合 | 维护停滞；未执行代码 |
| lidar_degeneracy_datasets（LiDAR 退化数据） | [ntnu-arl/lidar_degeneracy_datasets](https://github.com/ntnu-arl/lidar_degeneracy_datasets) | 官方（NTNU ARL） | BSD-3-Clause | 数据集 | README 未明示 | pushed 2026-02-03，200★ | 高 | LiDAR 几何退化评测（隧道/走廊/空旷） | 数据即用但未下载验证 |
| TIERS uwb-drone-dataset | [TIERS/uwb-drone-dataset](https://github.com/TIERS/uwb-drone-dataset) | 官方（Tampere TIERS） | 未标注（API None） | 数据集 | 未核验 | pushed 2022-09-14，105★ | 中 | GNSS 拒止下 UWB 定位数据 | license 未标注 |
| uwb-tracking-ros（UWB 跟踪示例） | [cliansang/uwb-tracking-ros](https://github.com/cliansang/uwb-tracking-ros) | 第三方 | MIT | ROS 包 | 未核验 | pushed 2025-02-03，50★ | 中 | UWB 接入与跟踪管道示例 | 示例级实现，需自验正确性 |

## 二、按项目模块的选型建议

| 本项目模块 | 推荐组合 | 说明 |
|---|---|---|
| LiDAR 里程计/SLAM | LIO-SAM（因子图）或 FAST-LIO（滤波） | 两者都有大规模实车/机器人验证；LIO-SAM 官方 ROS2 分支便于与 ROS2 栈统一 |
| VIO | OpenVINS（首选，ROS2 就绪）对照 VINS-Fusion | OpenVINS 维护最活跃、模块化好 |
| 多源融合框架 | GTSAM 底座自建因子（轮速/GNSS/UWB/雷达）+ 参考 fuse/robot_localization 兜底 | 复杂退化场景建议因子图路线；robot_localization 适合快速工程原型 |
| GNSS/RTK | RTKLIB 增强版解算 + GVINS（紧耦合参考） + gnss-ins-sim（误差序列生成） | 北斗多频可用 RTKLIB 路线；UrbanNav RINEX 数据可先离线验证 |
| UWB | UTIL 数据/EKF 流程 + TDoA2/3 解析；示例参考 uwb-tracking-ros | dropout 场景在数据回放层注入 |
| 毫米波雷达（拟采购） | ORORA / ethz-asl/rio / christopherdoer-rio 三选一作基线 | ORORA 维护最活跃；采购前先用 Oxford Radar/MulRan 数据验证算法可行性 |
| 事件相机（拟采购） | ESIM（ROS 内仿真）+ v2e（实拍视频转事件） | 仿真事件流只作算法开发，不可当实机性能 |
| 标定 | Kalibr（相机-IMU） | ROS2 环境需容器化运行 |
| 仿真平台（退化场景构造） | gz-sim + ROS2（新项目）；hector_gazebo 插件思路（GNSS 漂移/噪声）；PX4-SITL 模型参数参考 | gazebo_ros_pkgs 已归档，勿作新基线 |

## 三、使用注意（重要）

1. **未执行代码声明**：以上全部条目仅做仓库存在性、license、语言、更新时间、ROS 支持声明的核验，未编译、未运行、未做安全审计。引入任何仓库前须自行审查代码与依赖供应链。
2. **License 分级**：MIT/BSD/Apache 宽松（v2e、rpg_esim、LIO-SAM、gz-sim、ethz-asl/rio、lidar_degeneracy_datasets 等）；GPL 系（FAST-LIO、VINS-Fusion、OpenVINS、GVINS、ORORA、christopherdoer/rio）注意与闭源模块的边界；API 返回 NOASSERTION/None 者（GTSAM、RTKLIB、Kalibr、robot_localization、fuse、hector_gazebo、gazebo_ros_pkgs、PX4-SITL、util-uwb-dataset、TIERS）必须打开仓库 LICENSE 文件人工确认后才可集成。
3. **ROS 版本证据口径**：ROS1/ROS2 支持只采信 README/仓库文件的明示证据。凡标"未核验"者不得在方案书中直接声称支持。
4. **仓库迁移警示**（原地址已 404）：ucla-vision/openvins→rpng/open_vins；uzh-rpg/esim_ros→uzh-rpg/rpg_esim；SensorManipulation/v2e→SensorsINI/v2e；PX4/PX4-SITL_gazebo→PX4/PX4-SITL_gazebo-classic；xinhe-yifan/gnss-ins-sim→Aceinna/gnss-ins-sim；utiasDSL/util-uwb-dataset→learnsyslab/util-uwb-dataset。
5. **仿真性能 ≠ 实车性能**：本图谱中所有仿真器（ESIM、v2e、gnss-ins-sim、gz-sim 等）用于构造退化场景与算法开发，其上得到的精度/鲁棒性数字不得写入实车性能结论；实车性能只以实车实测为准。
6. 备选池（已核验存在、本次未入主表）：utiasASRL/steam_icp、HKUST-Aerial-Robotics/RIO、ailab-hanyang/Radar4Motion、keenan-burnett/yeti_radar_odometry、TIERS/uwb-vio-lidar-fusion、TIERS/uwb-cooperative-mrs-localization、advoard/advoard_localization 等，详见 staging/OPENSOURCE_raw.json rejected。
