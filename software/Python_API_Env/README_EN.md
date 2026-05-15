# AirSim360 Pro — Python API & User Guide

This document is the simulator usage guide for AirSim360 Pro: how to install the local Python client, run the application, attach a Python session, query vehicle state, use panoramic RGB / depth / segmentation, and issue control commands. Treat it as the baseline reference for any work built on this environment.

📌 Note on AirSim360 Versions and Usage:

- **Design & Performance:** AirSim360 Pro and Air versions serve different design purposes, which is reflected in their distinct UIs. Crucially, many design choices in the Pro version prioritize maintaining high framerates for developers.
- **Sensor Activation:** In the Pro version, all sensors (including the main and panoramic cameras) must be explicitly activated via code. By default, only the third-person observation view is enabled.
- **Control & Customization:** The Pro version supports sending external control commands (e.g., velocity or position) directly to the UAV via the custom API. Additionally, the panoramic image resolution is fully customizable; however, please note that larger sizes will negatively impact performance.
- **Release Schedule:** Due to the large file size of the software, the first batch of the Pro version and its corresponding scenes, along with other static datasets, will be rolled out by April 17, 2026.

Table of contents

- Dependencies
- API compatibility
- Run the simulator
- Connect from Python
- Panoramic RGB and depth
- Vehicle state
- Drone control
- Algorithms and integration

## Dependencies

**Platform note:** Whether you use the Windows or Ubuntu build of the simulator, install the Python client environment using the same steps in this guide. These instructions have been verified on Windows 11 and Ubuntu 24.04.

### Layout

The folder containing this README has the following structure (all paths in this guide are relative to it):

```
Python_API_Slim/
├── README_EN.md                       # this guide (English, start here)
├── README_CN.md                       # Chinese version of this guide
├── environment.yml                    # Conda environment definition
└── PythonClient/                      # installable airsim package
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

### Conda (recommended)

From this directory:

```bash
conda env create -f environment.yml
conda activate airsim360
```

That single environment file pins Python 3.10 and pulls in every runtime package needed by this guide (`numpy`, `msgpack-rpc-python`, `opencv-python`, `matplotlib`) by editable-installing the local `airsim` client.

To refresh an existing `airsim360` environment after a project update:

```bash
conda env update -f environment.yml --prune
```

### Plain pip fallback (no Conda)

If Conda is unavailable, any Python 3.10 venv works:

```bash
pip install -e ./PythonClient
```

### Verify

```bash
python -c "import airsim; print(airsim.__version__)"
```

## API compatibility

AirSim360 largely inherits the same client-side interface definitions as AirSim (e.g. `MultirotorClient`, movement APIs, and state queries). If you already know AirSim, you can get productive quickly: the same mental model—connect, reset, poll state, command the vehicle—applies here. The sections below call out panoramic-specific calls where AirSim360 extends the usual picture.

## Run the simulator

Start the compiled simulator executable and leave it running; your Python process will attach to it over the RPC channel.

## Connect from Python

```python
client = airsim.MultirotorClient()  # optional: airsim.MultirotorClient(ip="", port=41451)
client.confirmConnection()
client.reset()
```

This follows the standard AirSim pattern: create the client, confirm RPC, and reset the scene.

## Panoramic RGB and depth

These calls cover the AirSim360-specific panorama path: set resolution, trigger capture, then fetch images with `simGetImages` using the panorama camera names.

**Panoramic RGB**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_original", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_original", "")

responses_pano = client.simGetImages([
    airsim.ImageRequest("panorama_original", airsim.ImageType.Scene, False, False)
])
```

**Panoramic depth**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_depth", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_depth", "")

responses_pd = client.simGetImages([
    airsim.ImageRequest("panorama_depth", airsim.ImageType.Scene, pixels_as_float=True, compress=False)
])
```

**Panoramic segmentation**

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_seg", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_seg", "")

responses_seg = client.simGetImages([
    airsim.ImageRequest("panorama_seg", airsim.ImageType.Scene, False, False)
])
```

**Sensor notes**

- Panoramic RGB is a standard 3-channel image.
- Panoramic depth in this path is delivered as a single-channel float buffer via `simGetImages` with `pixels_as_float=True`; interpret values according to your scene units as returned by the simulator.
- Panoramic segmentation follows the same trigger-and-fetch pipeline and returns a 3-channel scene buffer.
- **Performance note:** Set panorama resolution once at startup; do not re-issue resolution calls every control cycle.

## Vehicle state

State access matches the usual AirSim style:

```python
client = airsim.MultirotorClient()
client.confirmConnection()

state = client.getMultirotorState()
p = state.kinematics_estimated.position
q = state.kinematics_estimated.orientation
v = state.kinematics_estimated.linear_velocity
```

The simulator uses NED (North-East-Down). Remap into your own frame if needed.

## Drone control

Control APIs are aligned with classic AirSim (throttle, world/body velocity, position, path, rates, motor PWM).

Throttle-based — roll, pitch, yaw, throttle, duration:

```python
client.moveByRollPitchYawThrottleAsync(r, p, y, t, dt)
```

World-frame velocity (NED) — `vx`, `vy`, `vz` in m/s; `duration` is command length.

```python
client.moveByVelocityAsync(vx, vy, vz, duration)
```

Body-frame velocity — forward / right / down.

```python
client.moveByVelocityBodyFrameAsync(vx, vy, vz, duration)
```

Position — targets in NED; `velocity` is cruise speed.

```python
client.moveToPositionAsync(x, y, z, velocity)
```

Path:

```python
client.moveOnPathAsync(path, velocity)
```

Velocity + altitude hold:

```python
client.moveByVelocityZAsync(vx, vy, z, duration)
```

Body angular rates + throttle:

```python
client.moveByAngleRatesThrottleAsync(roll_rate, pitch_rate, yaw_rate, throttle, duration)
```

Motor PWM:

```python
client.moveByMotorPWMsAsync(front_right_pwm, rear_left_pwm, front_left_pwm, rear_right_pwm, duration)
```

## Algorithms and integration

Everything above stays at the level of operating the simulator and its API. When you are ready for heavier integration—full perception or planning stacks, closed-loop experiments, or examples such as obstacle avoidance tied to this simulator—see the companion repository: https://github.com/Insta360-Research-Team/Fly360
