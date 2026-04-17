# AirSim360 Pro — Quick User Guide

This document is a simulator usage guide for AirSim360 Pro: how to run the application, attach a Python client, query vehicle state, use panoramic RGB and depth, and issue control commands. It describes the platform in general, so you can treat it as the baseline reference for any work built on this environment.

**📌 Note on AirSim360 Versions and Usage:**

- **Design & Performance:** AirSim360 Pro and Air versions serve different design purposes, which is reflected in their distinct UIs. Crucially, many design choices in the Pro version prioritize maintaining high framerates for developers.
- **Sensor Activation:** In the Pro version, all sensors (including the main and panoramic cameras) must be explicitly activated via code. By default, only the third-person observation view is enabled.
- **Control & Customization:** The Pro version supports sending external control commands (e.g., velocity or position) directly to the UAV via the custom API. Additionally, the panoramic image resolution is fully customizable; however, please note that larger sizes will negatively impact performance.
- **Release Schedule:** Due to the large file size of the software, the first batch of the Pro version and its corresponding scenes, along with other static datasets, will be rolled out by April 17, 2026.

## Table of contents

- [Dependencies](#dependencies)
- [API compatibility](#api-compatibility)
- [Run the simulator](#run-the-simulator)
- [Connect from Python](#connect-from-python)
- [Panoramic RGB and depth](#panoramic-rgb-and-depth)
- [Vehicle state](#vehicle-state)
- [Drone control](#drone-control)
- [Algorithms and integration](#algorithms-and-integration)
- [Operational notes](#operational-notes)


## Dependencies

```bash
python -m pip install -U pip setuptools wheel
```

Install required runtime packages (including NumPy):

```bash
pip install backports.ssl-match-hostname
pip install numpy msgpack-rpc-python opencv-contrib-python
```

Install the local Python client package:

```bash
pip install -e ./PythonClient --no-build-isolation
```

## API compatibility

AirSim360 largely inherits the same client-side interface definitions as AirSim (e.g., `MultirotorClient`, movement APIs, and state queries). If you already know AirSim, you can get productive quickly: the same mental model—connect, reset, poll state, command the vehicle—applies here. The sections below call out panoramic-specific calls where AirSim360 extends the usual picture.

## Run the simulator

Start the compiled simulator executable and leave it running; your Python process will attach to it over the RPC channel.

> **Demo video:**

<video src="../media/videos/airsim360_pro_demo_0410_v1.mp4" controls playsinline width="100%"></video>

## Connect from Python

```python
client = airsim.MultirotorClient()  # optional: airsim.MultirotorClient(ip="", port=41451)
client.confirmConnection()
client.reset()
```

This follows the standard AirSim pattern: create the client, confirm RPC, and reset the scene.

## Panoramic RGB and depth

These calls cover the AirSim360-specific panorama path: set resolution, trigger capture, then fetch images with `simGetImages` using the panorama camera names.

### Panoramic RGB

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_original", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_original", "")

responses_pano = client.simGetImages([
    airsim.ImageRequest("panorama_original", airsim.ImageType.Scene, False, False)
])
```

### Panoramic depth

```python
client = airsim.MultirotorClient()
client.confirmConnection()

client.client.call("simSetPanoramaResolution", "panorama_depth", 512, 256, "")
client.client.call("simTriggerPanoramaCapture", "panorama_depth", "")

responses_pd = client.simGetImages([
    airsim.ImageRequest("panorama_depth", airsim.ImageType.Scene, pixels_as_float=True, compress=False)
])
```

### Panoramic segmentation

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

**Throttle-based** — roll, pitch, yaw, throttle, duration:

```python
client.moveByRollPitchYawThrottleAsync(r, p, y, t, dt)
```

**World-frame velocity (NED)** — `vx`, `vy`, `vz` in m/s; `duration` is command length.

```python
client.moveByVelocityAsync(vx, vy, vz, duration)
```

**Body-frame velocity** — forward / right / down.

```python
client.moveByVelocityBodyFrameAsync(vx, vy, vz, duration)
```

**Position** — targets in NED; `velocity` is cruise speed.

```python
client.moveToPositionAsync(x, y, z, velocity)
```

**Path**:

```python
client.moveOnPathAsync(path, velocity)
```

**Velocity + altitude hold**:

```python
client.moveByVelocityZAsync(vx, vy, z, duration)
```

**Body angular rates + throttle**:

```python
client.moveByAngleRatesThrottleAsync(roll_rate, pitch_rate, yaw_rate, throttle, duration)
```

**Motor PWM**:

```python
client.moveByMotorPWMsAsync(front_right_pwm, rear_left_pwm, front_left_pwm, rear_right_pwm, duration)
```

## Algorithms and integration

Everything above stays at the level of operating the simulator and its API. When you are ready for heavier integration—full perception or planning stacks, closed-loop experiments, or examples such as obstacle avoidance tied to this simulator—see the companion repository: [https://github.com/Insta360-Research-Team/Fly360](https://github.com/Insta360-Research-Team/Fly360)

## Operational notes

**Stop your algorithm before quitting AirSim360.** If Python keeps an RPC session open, the simulator may not exit cleanly and the default RPC port (**41451**) can stay occupied, breaking the next launch.
