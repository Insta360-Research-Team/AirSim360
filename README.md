# 🚁 AirSim360: A Panoramic Simulation Platform within Drone View

AirSim360 is the first platform to systematically model the 4D real world under an omnidirectional setting for UAVs. Built on a cutting-edge rendering engine (Unreal Engine 5 series), it addresses the critical lack of large-scale and diverse 360-degree aerial data.

The platform enables closed-loop simulation for omnidirectional aerial systems and offers an integrated toolchain for intelligent data acquisition across diverse flight scenarios.

---

## ✨ Core Capabilities

AirSim360's design focuses on three key components for high-quality data generation:

### 1. 🖼️ Render-Aligned Data and Label Generation
* **Panoramic Image:** Adopts the Equirectangular Projection (ERP) as the omnidirectional representation. It uses a GPU-side texture copying mechanism (based on RHI) to quickly and seamlessly stitch six cube-face views for one-time image stitching.
* **Depth Information:** Defined as the distance (slant range) from the camera center to the point along the viewing ray, aligning with the omnidirectional perspective.
* **Segmentation:** Provides pixel-level Semantic Segmentation and Entity Segmentation annotations. Entity segmentation ensures complete coverage of all entities (static mesh actors, skeleton mesh actors, and landscape elements) across the entire image.
* **Synchronous Rendering:** A custom Event Dispatcher synchronizes all sensors with a unified trigger signal to ensure simultaneous data acquisition.

### 2. 🚶 Interactive Pedestrian-Aware System (IPAS)
* **Human Behavior Modeling:** Simulates movable pedestrians with various actions and realistic interactions.
* **Autonomous Interaction:** Combines NPC Behavior Trees with State Machines for autonomous interaction, such as switching from walking to chatting when agents meet.
* **3D Human Keypoints:** Generates keypoints in real time, ensuring temporally consistent annotations for downstream perception tasks, such as 3D monocular human localization.

### 3. 🗺️ Automated Trajectory Generation Paradigm
* **Minimum Snap Planning:** Adopts the Minimum Snap trajectory planning method to automatically generate a smooth, realistic trajectory from sparse user-defined waypoints.
* **Dynamic Feasibility:** The generated trajectory adheres to realistic dynamic constraints on maximum velocity ($v_{max}$) and acceleration ($a_{max}$) of the UAV, making it directly applicable to real quadrotors.

---

## 💾 Omni360-X Dataset Collection

Built on AirSim360, we collected the large-scale **Omni360-X** dataset (more than **60K** non-duplicate frames), structured into three subsets:

| Subset | Focus | Samples/Frames | Key Annotations |
| :--- | :--- | :--- | :--- |
| **Omni360-Scene** | Panoramic scene parsing | ~61,000 images | Depth, Semantic/Entity Segmentation |
| **Omni360-Human** | Pedestrian behavior understanding | ~100,700 frames | 3D Human Keypoints |
| **Omni360-WayPoint** | UAV Navigation and Control | $>100,000$ waypoints | Physics-consistent trajectories ($p(t)$, $v(t)$, $a(t)$) |

---

## 🔗 Links

* **Project Website, Toolkit, Plugins, and Datasets:** [https://insta360-research-team.github.io/AirSim360-website/](https://insta360-research-team.github.io/AirSim360-website/)

---
