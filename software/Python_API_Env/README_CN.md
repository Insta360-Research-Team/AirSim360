# AirSim360 Pro — Python API 与用户指南

本文档是 AirSim360 Pro 仿真器的使用指南：如何安装本地 Python 客户端、运行仿真器、用 Python 接入、查询飞行器状态、使用全景 RGB / 深度 / 语义图，以及下发控制指令。基于本环境构建任何上层工作时，可将本文作为基础参考。

📌 关于 AirSim360 版本与使用的说明：

- **设计目标与性能**：AirSim360 Pro 与 Air 版面向不同的设计目标，UI 也因此存在差异。Pro 版的许多设计选择都优先保证了开发者所需的高帧率。
- **传感器激活**：Pro 版中所有传感器（包括主相机和全景相机）都需通过代码显式激活；默认仅启用第三人称观察视图。
- **控制与定制**：Pro 版支持通过自定义 API 直接向无人机下发外部控制指令（如速度、位置）；全景图分辨率完全可定制，但请注意更大的分辨率会拖慢性能。
- **发布计划**：受软件体积影响，Pro 版首批及对应场景、其它静态数据集将于 2026-04-17 前陆续推出。

目录

- 依赖安装（Dependencies）
- API 兼容性（API compatibility）
- 启动仿真器（Run the simulator）
- 从 Python 连接（Connect from Python）
- 全景 RGB 与深度（Panoramic RGB and depth）
- 飞行器状态（Vehicle state）
- 无人机控制（Drone control）
- 算法与集成（Algorithms and integration）

## 依赖安装

**平台说明**：无论使用 Windows 版本还是 Ubuntu 版本，均可按本文相同步骤安装 Python 客户端环境。上述流程已在 Windows 11 与 Ubuntu 24.04 上验证通过。

### 目录结构

本 README 所在目录的结构如下（本指南中所有路径均相对于该目录）：

```
Python_API_Slim/
├── README_EN.md                       # 英文版指南
├── README_CN.md                       # 本文档（中文版指南，从此入手）
├── environment.yml                    # Conda 环境定义
└── PythonClient/                      # 可安装的 airsim Python 包
    ├── LICENSE
    ├── setup.py
    ├── requirements.txt
    └── airsim/
        ├── __init__.py
        ├── client.py
        ├── pfm.py
        ├── types.py
        └── utils.py
```

### Conda（推荐）

在本目录下：

```bash
conda env create -f environment.yml
conda activate airsim360
```

这一份环境文件锁定 Python 3.10，并通过对本地 `airsim` 客户端做 editable 安装，自动拉入本指南所有脚本所需的运行时依赖（`numpy`、`msgpack-rpc-python`、`opencv-python`、`matplotlib`）。

更新已存在的 `airsim360` 环境（项目变更后）：

```bash
conda env update -f environment.yml --prune
```

### Plain pip 兜底（不使用 Conda）

如果无法使用 Conda，在任意 Python 3.10 venv 中执行：

```bash
pip install -e ./PythonClient
```

### 验证

```bash
python -c "import airsim; print(airsim.__version__)"
```

## API 兼容性

AirSim360 在客户端接口层面基本沿用了 AirSim 的定义（如 `MultirotorClient`、各类移动 API、状态查询等）。如果你已经熟悉 AirSim，迁移成本极低：连接、reset、轮询状态、下发指令——同一套心智模型直接适用。下文会专门标注 AirSim360 在全景方向上扩展的部分。

## 启动仿真器

启动编译好的仿真器可执行文件并保持运行；Python 进程会通过 RPC 通道连入。

## 从 Python 连接

```python
client = airsim.MultirotorClient()  # 可选: airsim.MultirotorClient(ip="", port=41451)
client.confirmConnection()
client.reset()
```

遵循标准 AirSim 流程：创建客户端、确认 RPC 连接、复位场景。

## 全景 RGB 与深度

下面三段示例覆盖了 AirSim360 特有的全景数据采集流程：设置分辨率、触发拍摄、用 `simGetImages` 配合全景相机名取图。

**全景 RGB**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_original", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_original", "")

responses_pano = client.simGetImages([
    airsim.ImageRequest("panorama_original", airsim.ImageType.Scene, False, False)
])
```

**全景深度**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_depth", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_depth", "")

responses_pd = client.simGetImages([
    airsim.ImageRequest("panorama_depth", airsim.ImageType.Scene, pixels_as_float=True, compress=False)
])
```

**全景语义**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_seg", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_seg", "")

responses_seg = client.simGetImages([
    airsim.ImageRequest("panorama_seg", airsim.ImageType.Scene, False, False)
])
```

**传感器说明**

- 全景 RGB 是标准的 3 通道图像。
- 该路径下的全景深度通过 `simGetImages` 的 `pixels_as_float=True` 返回单通道 float 缓冲；具体数值的物理含义以仿真器返回的场景单位为准。
- 全景语义遵循同样的"触发-取图"流程，返回 3 通道 scene 缓冲。
- **性能注意事项**：分辨率应只在启动时调用一次 `simSetPanoramaResolution`；不要在控制循环里反复设置。

## 飞行器状态

状态查询沿用标准的 AirSim 风格：

```python
client = airsim.MultirotorClient()
client.confirmConnection()

state = client.getMultirotorState()
p = state.kinematics_estimated.position
q = state.kinematics_estimated.orientation
v = state.kinematics_estimated.linear_velocity
```

仿真器使用 NED 坐标系（North-East-Down）。如需切换到自有坐标系请自行重映射。

## 无人机控制

控制 API 与经典 AirSim 一致（油门、世界系/机体系速度、位置、路径、角速率、电机 PWM）。

油门式 —— roll、pitch、yaw、throttle、duration：

```python
client.moveByRollPitchYawThrottleAsync(r, p, y, t, dt)
```

世界系速度（NED）—— `vx`、`vy`、`vz` 单位 m/s；`duration` 为指令持续时长。

```python
client.moveByVelocityAsync(vx, vy, vz, duration)
```

机体系速度 —— 前 / 右 / 下。

```python
client.moveByVelocityBodyFrameAsync(vx, vy, vz, duration)
```

位置 —— 目标点为 NED 坐标；`velocity` 为巡航速度。

```python
client.moveToPositionAsync(x, y, z, velocity)
```

路径：

```python
client.moveOnPathAsync(path, velocity)
```

速度 + 高度保持：

```python
client.moveByVelocityZAsync(vx, vy, z, duration)
```

机体角速率 + 油门：

```python
client.moveByAngleRatesThrottleAsync(roll_rate, pitch_rate, yaw_rate, throttle, duration)
```

电机 PWM：

```python
client.moveByMotorPWMsAsync(front_right_pwm, rear_left_pwm, front_left_pwm, rear_right_pwm, duration)
```

## 算法与集成

以上内容均聚焦于"如何使用本仿真器及其 API"。当你需要进入更重的集成阶段——完整的感知或规划栈、闭环实验，或类似障碍规避这种与本仿真器深度耦合的样例——请参阅配套仓库：https://github.com/Insta360-Research-Team/Fly360
