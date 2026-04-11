# AirSim360 Pro — Quick User Guide

This document is a **simulator usage guide** for AirSim360 Pro: how to run the application, attach a Python client, query vehicle state, use panoramic RGB and depth, and issue control commands. It describes the **platform in general**, so you can treat it as the baseline reference for any work built on this environment.

**📌 Note on AirSim360 Versions and Usage:**

* **Design & Performance:** AirSim360 Pro and Air versions serve different design purposes, which is reflected in their distinct UIs. Crucially, many design choices in the Pro version prioritize maintaining high framerates for developers.
* **Sensor Activation:** In the Pro version, all sensors (including the main and panoramic cameras) must be explicitly activated via code. By default, only the third-person observation view is enabled.
* **Control & Customization:** The Pro version supports sending external control commands (e.g., velocity or position) directly to the UAV via our custom API. Additionally, the panoramic image resolution is fully customizable; however, please note that larger sizes will negatively impact performance.
* **Release Schedule:** Due to the large file size of the software, the first batch of the Pro version and its corresponding scenes, along with other static datasets, will be rolled out by **April 17, 2026**.

## Table of contents

- [API compatibility](#api-compatibility)
- [Run the simulator](#run-the-simulator)
- [Connect from Python](#connect-from-python)
- [Panoramic RGB and depth](#panoramic-rgb-and-depth)
- [Vehicle state](#vehicle-state)
- [Drone control](#drone-control)
- [Algorithms and integration](#algorithms-and-integration-companion-repository)
- [Operational notes](#operational-notes)
- [Dependencies](#dependencies)

## API compatibility

AirSim360 **largely inherits the same client-side interface definitions as AirSim** (e.g. `MultirotorClient`, movement APIs, and state queries). If you already know AirSim, you can **get productive quickly**: the same mental model—connect, reset, poll state, command the vehicle—applies here. The sections below call out **panoramic-specific** calls where AirSim360 extends the usual picture.


## Run the simulator

Start the compiled simulator executable and leave it running; your Python process will attach to it over the RPC channel.

> **Demo video:**

<video src="videos/airsim360_pro_demo_0410_v1.mp4" controls playsinline width="100%"></video>


## Connect from Python

```python
client = airsim.MultirotorClient()  # specify the port if necessary
client.confirmConnection()
print("AirSim connected successfully!")
client.reset()
print("Vehicles:", client.listVehicles())
```

This follows the standard AirSim pattern: create the client, confirm RPC, reset the scene, and list vehicles.


## Panoramic RGB and depth

These calls cover the **AirSim360-specific** panorama path: set resolution, trigger capture, then fetch images with `simGetImages` using the panorama camera names.

### Panoramic RGB

```python
# Set panorama RGB resolution
result_pano = client.client.call("simSetPanoramaResolution", "panorama_original", 448, 224, "")
result_pano = client.client.call("simTriggerPanoramaCapture", "panorama_original", "")
if result_pano:
    print("Set pano successfully.")

# Get RGB image
responses_pano = client.simGetImages([
    airsim.ImageRequest("panorama_original", airsim.ImageType.Scene, False, False)
])
rp = responses_pano[0]
img_pano = np.frombuffer(rp.image_data_uint8, dtype=np.uint8).reshape(rp.height, rp.width, 3)
img_pano = cv2.resize(img_pano, (448, 224), interpolation=cv2.INTER_AREA)
img_pano = cv2.cvtColor(img_pano, cv2.COLOR_BGR2RGB)  # BGR -> RGB
erp_rgb = torch.from_numpy(img_pano).permute(2, 0, 1).float().to(device).unsqueeze(0)
```

### Panoramic depth

```python
# Set panorama depth resolution
result_pd = client.client.call("simSetPanoramaResolution", "panorama_depth", 448, 224, "")
result_pd = client.client.call("simTriggerPanoramaCapture", "panorama_depth", "")
if result_pd:
    print("Set pano depth successfully.")

# Get depth image
responses_pd = client.simGetImages([
    airsim.ImageRequest("panorama_depth", airsim.ImageType.Scene, False, False)
])
rpd = responses_pd[0]
img_pd = np.frombuffer(rpd.image_data_uint8, dtype=np.uint8).reshape(rpd.height, rpd.width, 3).copy()
erp_depth = torch.from_numpy(img_pd[:, :, 0]).float().to(device).unsqueeze(0).unsqueeze(0) / 100.0  # cm -> m
```

**Sensor notes**

- Panoramic RGB is a standard **3-channel** image.
- Depth is stored in **centimeters** in the buffer; scale to meters when feeding planners or learning code (e.g. divide by `100.0` as above).

**Performance note:** Set panorama resolution **once** at startup; do not re-issue resolution calls every control cycle (see [Operational notes](#operational-notes)).

## Vehicle state

State access matches the usual AirSim style:

```python
state = client.getMultirotorState()
p = state.kinematics_estimated.position
q = state.kinematics_estimated.orientation
v = state.kinematics_estimated.linear_velocity
```

The simulator uses **NED** (North-East-Down). 
Remap into your own frame if needed, e.g.:

```python
p_remap = torch.as_tensor([p.x_val, -p.y_val, -p.z_val])
v_remap = torch.as_tensor([v.x_val, -v.y_val, -v.z_val])
q_remap = torch.as_tensor([q.w_val, q.x_val, -q.y_val, -q.z_val])
```

## Drone control

Control APIs are **aligned with classic AirSim** (throttle, world/body velocity, position, path, rates, motor PWM).

**Throttle-based**

```python
# roll, pitch, yaw, throttle, duration
client.moveByRollPitchYawThrottleAsync(r, p, y, t, dt)
```

**World-frame velocity (NED)** — `vx, vy, vz` in m/s; `duration` is command length.

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

**Path**

```python
client.moveOnPathAsync(path, velocity)
```

**Body angular rates + throttle**

```python
client.moveByAngleRatesThrottleAsync(roll_rate, pitch_rate, yaw_rate, throttle, duration)
```

**Motor PWM**

```python
client.moveByMotorPWMsAsync(m1, m2, m3, m4, duration)
```

## Algorithms and integration

Everything above stays at the level of **operating the simulator and its API**. When you are ready for **heavier integration**—full perception or planning stacks, closed-loop experiments, or examples such as obstacle avoidance tied to this simulator—see the companion repository:
**https://github.com/Insta360-Research-Team/Fly360**


**Operational notes**

**Stop your algorithm before quitting AirSim360.** If Python keeps an RPC session open, the simulator may not exit cleanly and the default RPC port (**41451**) can stay occupied, breaking the next launch.

