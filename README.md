<div align="center">

# 🚁 AirSim360: A Panoramic Simulation Platform within Drone View

[![CVPR 2026](https://img.shields.io/badge/CVPR_2026-%F0%9F%94%A5_Accepted-E3242B?style=flat-square)](YOUR_ARXIV_LINK)
[![arXiv](https://img.shields.io/badge/arXiv-Paper-e05d44?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/pdf/2512.02009)
[![Project Page](https://img.shields.io/badge/Project_Page-Website-97ca00?style=flat-square&logo=googlechrome&logoColor=white)](https://insta360-research-team.github.io/AirSim360-website/)
[![Hugging Face Dataset](https://img.shields.io/badge/Hugging_Face-Dataset-FFD21E?style=flat-square&logo=huggingface&logoColor=171717)](https://huggingface.co/datasets/Insta360-Research/AirSim360)

*AirSim360 is a high-fidelity **omnidirectional (360°)** aerial simulation stack built on Unreal Engine 5.*

</div>

---

<div align="center">

<img src="media/images/teaser.jpg" width="100%" alt="AirSim360 paper teaser figure" />

</div>

---

## 📖 Introduction

AirSim360 addresses the lack of large-scale, diverse equirectangular (ERP) drone data by supporting closed-loop flight with render-aligned multimodal exports. This repository provides release notes, user documentation, one synchronized demo sample, and media for the open release.

<details open>
<summary><b>📑 Table of Contents (Click to expand)</b></summary>

- [🗓️ Update Log & Roadmap](#update-log-roadmap)
- [💻 Hardware Requirements](#hardware-requirements)
- [⚡ Quick Start](#quick-start)
- [⚖️ AirSim360 Air vs. Pro](#airsim360-air-vs-pro)
- [📂 Repository Layout](#repository-layout)
- [🗺️ Available Software Scenes](#available-software-scenes)
- [🌍 Omni360-Scene](#omni360-scene)
- [🛰️ Omni360-WayPoint](#omni360-waypoint)
- [🛣️ Long-Term Open-Source Plan](#long-term-open-source-plan)
- [🤝 Acknowledgement](#acknowledgement)
- [📝 Citation](#citation)
</details>

> 📢 **April 20, 2026 Update:** We have uploaded over **120,000** panoramic frames and their annotations for **Omni360-Scene**, now available via the [Hugging Face](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/Omni360-Scene). More open-source data will be released later this week. Stay tuned.

---

<a id="update-log-roadmap"></a>

## 🗓️ Update Log & Roadmap

This section will be updated continuously so users can track what has been released and what is coming next.

| Date | Type | Status | Details |
| :---: | :---: | :---: | :--- |
| 2026-04-10 | Software scenes | Released | First public scene packages are available: CityDowntown, Factory, SpanishCourtyard, DekogonGym, and AtmosphericHouse. |
| 2026-04-17 | AirSim360 Pro | Released | AirSim360 Pro is now publicly available. |
| 2026-04-20 | Omni360-Scene | Released | The first release includes over 120,000 panoramic frames and annotations from three open-world scenes. |
| 2026-05-15 | Python API environment | Released | Released the patched Python API environment package at [`software/Python_API_Env`](software/Python_API_Env/), bundling the reproducible Conda specification (`environment.yml`), pinned dependency manifest (`requirements.txt`), and the AirSim360-compatible `PythonClient` for programmatic control via the AirSim360 Pro RPC interface. |
| 2026-05-27 | Omni360-Scene | Released | Added camera poses in the Unreal Engine (UE) coordinate system for three Omni360-Scene environments under `data/UE_Raw_sample_pts.zip`, including 6-DoF (x, y, z, pitch, yaw, roll) information for the panoramic cameras. |
| 2026-06-05 | AirSim360 Pro | Released | The Linux binaries for the first public release of AirSim360 Pro (Ubuntu 24.04) are available in the [AirSim360_Pro_Ubuntu](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/AirSim360_Pro_Ubuntu) folder on Hugging Face.|
| From 2026-05 | Monthly updates | Planned | New software scenes and dataset content will be added regularly. |
| Before the end of Q2 2026 | Platform expansion | Planned | Linux support, more dynamic humans, and related calling methods will be added in later releases. |
| TBD | Future release entry | Reserved | Add each new public release note here as the repository grows. |

---

<a id="hardware-requirements"></a>

## 💻 Hardware Requirements

To handle the stunning realism and simultaneous rendering of panoramic RGB, depth, and semantics, you will need a solid rig.

> 🐧 **Linux user?** Support is landing in **Q2 2026**.
> 🪟 **Windows user?** Windows 10 & 11 are supported!

| Specs | Minimum (For casual flights) | Recommended (For high-FPS panoramic data processing) |
| :--- | :--- | :--- |
| **GPU** | NVIDIA GPU with **16GB+ VRAM** | NVIDIA GPU with **24GB+ VRAM** |
| **RAM** | **16GB+** System RAM | **32GB+** System RAM |

---

<a id="quick-start"></a>

## ⚡ Quick Start

### 1. Download and install AirSim360 software

- **AirSim360 Air** — [Download on Hugging Face](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/AirSim360_Air_Beta). Designed for direct use with zero environment setup: download the package, unzip it on Windows, start the remote-control program first, and then launch the main simulator.
- **AirSim360 Pro** — [Download on Hugging Face](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/AirSim360_Pro_Beta). Shipped as a compiled package for professional developer control: download it, unzip it, run the simulator, and connect via Python or RPC to access the custom API for programmatic control.
- Detailed usage guides are available in [`software/AirSim360_Air_User_Guide_EN.md`](software/AirSim360_Air_User_Guide_EN.md) and [`software/AirSim360_Pro_User_Guide_EN.md`](software/AirSim360_Pro_User_Guide_EN.md).

### 2. Start with the currently released datasets

- Current public dataset tracks include **Omni360-Scene** and **Omni360-WayPoint**.
- **Omni360-Scene** — [Download on Hugging Face](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/Omni360-Scene)
- **Omni360-WayPoint** — [Download on Hugging Face](https://huggingface.co/datasets/Insta360-Research/AirSim360/tree/main/Omni360-WayPoint)
- Note: **Omni360-Scene** is now publicly available, and additional open-source data will be released later this week.
- **Omni360-Scene** follows the same structure shown in the [demo sample](data/demo_sample/): every frame is aligned across modalities by a shared file stem.
- The core released modalities are:
  - **Raw (panorama):** Equirectangular RGB images.
  - **Depth:** True Euclidean depth in meters, stored as HDF5 datasets.
  - **Semantic (seg_panorama):** Semantic labels with class IDs carried in the Alpha channel.
  - **Instance (instance_panorama):** Instance labels where `(Alpha, R, G, B)` uniquely identifies an object, with Alpha storing the semantic class ID.
- See [`data/demo_sample/PANORAMIC_DATA_FORMAT.md`](data/demo_sample/PANORAMIC_DATA_FORMAT.md) for the full format specification, and [`data/demo_sample/depth/read_depth_h5.py`](data/demo_sample/depth/read_depth_h5.py) for a minimal depth reader.
- A dedicated **Omni360-WayPoint** section with dataset breakdown and demo scripts will be added in a future update.

---

<a id="airsim360-air-vs-pro"></a>

## ⚖️ AirSim360 Air vs. Pro

| Feature | 🕹️ AirSim360 Air | 🛠️ AirSim360 Pro |
| :---: | :---: | :---: |
| **Target Users** | Researchers who want keyboard-and-mouse data collection with minimal setup. | Developers who need programmatic control, batch capture, and integration. |
| **Control Mode** | Integrated control panel, hotkeys (`W/S`, `A/D`), and multi-viewport feedback (FPV/TPV). | Python / RPC workflow with an AirSim-style client interface. |
| **Panorama and Sensors** | One-click capture with a direct collection workflow. | Sensors are enabled via code; panorama resolution is fully configurable. |
| **API Support** | No | Yes |
| **Typical Strengths** | Fast setup, simple collection, direct operation, zero environment setup. | Automation, external control, code-driven sensors, API-based experiments. |

**Guides:** [Air User Guide](software/AirSim360_Air_User_Guide_EN.md) · [Pro User Guide](software/AirSim360_Pro_User_Guide_EN.md)

### AirSim360 Air Demo

A short demo video of **AirSim360 Air**, showing its direct-use workflow and panoramic data collection interface.

<p align="center">
  <video src="media/videos/airsim360_air_demo_0410_v2.mp4" controls width="100%"></video>
</p>

---

<a id="repository-layout"></a>

## 📂 Repository Layout

| Path | Purpose |
| :--- | :--- |
| [📁 software](software/README.md) | English user guides for AirSim360 Air and AirSim360 Pro. The software packages themselves are not stored in this repository; download links will be provided separately. |
| [📁 data/demo_sample](data/demo_sample/) | One synchronized demo sample plus usage notes that explain the released data format. The full dataset address will be published separately. |
| [📁 media](media/README.md) | Static visuals, figures, UI screenshots, and diagram exports used in the project page and documentation. |
| [📁 scripts](scripts/README.md) | Small cross-cutting utilities (format conversion, batch checks, packaging helpers) that are not tied to a single dataset folder. |

---

<a id="available-software-scenes"></a>

## 🗺️ Available Software Scenes

The following scene packages are currently listed in the public software release. More scenes will be added over time, with monthly updates rolling out on the 15th of each month starting May 2026.

| Scene | Air | Pro | API | Dynamic Actors |
| :---: | :---: | :---: | :---: | :---: |
| CityDowntown | Yes | Yes | Pro only | Planned |
| Factory | Yes | Yes | Pro only | Planned |
| SpanishCourtyard | Yes | Yes | Pro only | Planned |
| DekogonGym | Yes | Yes | Pro only | Planned |
| AtmosphericHouse | Yes | Yes | Pro only | Planned |
| *New scenes coming in May* | Planned | Planned | Planned | Planned |

> **📥 Download Access**: All available scene packages and environment assets can be downloaded directly from the **[AirSim360 Hugging Face Repository](https://huggingface.co/datasets/Insta360-Research/AirSim360)**.

---

<a id="omni360-scene"></a>

## 🌍 Omni360-Scene

**Omni360-Scene** is the current panoramic scene-understanding release in the Omni360-X collection. The sample under [data/demo_sample](data/demo_sample/) shows the core organization used by this dataset: the same frame stem is shared across RGB, depth, semantic, and instance labels, which makes multimodal alignment straightforward.

The current public specification focuses on four aligned outputs:

- **Raw (panorama):** Equirectangular RGB images.
- **Depth:** True Euclidean depth in meters, saved as an HDF5 `/depth` dataset with `float32` values **directly in meters** — no rescaling or de-quantization is needed when reading. Maximum supported distance is 1000 m. For backward compatibility, the reader (`data/demo_sample/depth/read_depth_h5.py`) also accepts the legacy `uint16` format with a `depth_range_m` attribute, recovered via `depth_uint16 / 65535 * depth_range_m`.
- **Semantic (seg_panorama):** Semantic labels aligned pixel-by-pixel with the panorama, where the Alpha channel stores the semantic class ID. The mapping of class names to IDs is recorded in the `semantic_list` text file.
- **Instance (instance_panorama):** Instance labels where the **(Alpha, R, G, B)** tuple identifies a specific object instance, with Alpha storing the semantic class ID.

<p align="center">
  <img src="media/images/demo_img/demo_img/panorama_3080.png" width="24%" alt="Omni360-X panorama RGB (frame 3080)" />
  <img src="media/images/demo_img/demo_img/panorama_3080_depth.png" width="24%" alt="Omni360-X depth visualization (frame 3080)" />
  <img src="media/images/demo_img/demo_img/panorama_3080_seg.png" width="24%" alt="Omni360-X semantic segmentation (frame 3080)" />
  <img src="media/images/demo_img/demo_img/panorama_3080_ins.png" width="24%" alt="Omni360-X instance segmentation (frame 3080)" />
</p>

The current public release covers three main scenes with full support for all four modalities (RGB, depth, semantic, and instance). The corresponding semantic label IDs are shipped alongside each dataset.

| Scene | RGB | Depth | Semantic | Instance | Open-Source Count |
| :--- | :---: | :---: | :---: | :---: | ---: |
| City Park Environment Collection | ✅ | ✅ | ✅ | ✅ | 80,000 |
| Downtown West Modular Pack | ✅ | ✅ | ✅ | ✅ | 24,812 |
| New York City | ✅ | ✅ | ✅ | ✅ | 20,716 |
| **Current public total** | — | — | — | — | **125,528** |

> **Notes:**
> 1. Additional premium/paid scenes will be released and updated on a monthly basis.
> 2. Appropriate randomization has been applied to all 6 degrees of freedom (6-DoF) for the panoramic camera across the provided datasets. This ensures a diverse variety of viewing positions and directions, rather than fixing a single orientation.

<!--
---

<a id="omni360-waypoint"></a>

## 🛰️ Omni360-WayPoint

`Omni360-WayPoint` is the current navigation-oriented release in the Omni360-X collection. It is intended for trajectory learning, control, and evaluation. The detailed dataset composition plus a lightweight demo script will be added in a later update.

Current released scale: `100k+` waypoints in total.

| Scene | Waypoint Count |
| :---: | :---: |
| `CityDowntown` | To be added |
| `Factory` | To be added |
| `SpanishCourtyard` | To be added |
| `DekogonGym` | To be added |
| `AtmosphericHouse` | To be added |
| **Current public total** | 100k+ |

---
-->

<a id="long-term-open-source-plan"></a>

## 🛣️ Long-Term Open-Source Plan

- Starting May 2026, we will release 5 new AirSim360 scenes each month, shared across the Air and Pro editions.
- Starting May 2026, we will also release 2 new dataset scenes each month, each containing 2,000 panoramic images. Data types will be adjusted based on developer feedback, and community suggestions are welcome.
- Before the end of Q2 2026, we will provide additional dynamic human assets inside the AirSim360 software packages, along with the corresponding calling methods and automatic ground attachment for human placement — so developers no longer need to know ground coordinates in advance.
- We welcome feedback on software usage. Adopted suggestions will be acknowledged in a new section at the end of this page.
- The panoramic plugin and other useful features will be published separately on FAB, and will be free for individual developers.

---

<a id="acknowledgement"></a>

## 🤝 Acknowledgement

We gratefully acknowledge the following open-source projects:

* [AirSim](https://microsoft.github.io/AirSim/)
* [Fly360](https://github.com/Insta360-Research-Team/Fly360)
* [Unreal Engine](https://www.unrealengine.com/)

---

<a id="citation"></a>

## 📝 Citation

If you find our work useful in your research, please consider citing:

```bibtex
@article{ge2025airsim360,
  title={Airsim360: A panoramic simulation platform within drone view},
  author={Ge, Xian and Pan, Yuling and Zhang, Yuhang and Li, Xiang and Zhang, Weijun and Zhang, Dizhe and Wan, Zhaoliang and Lin, Xin and Zhang, Xiangkai and Liang, Juntao and others},
  journal={arXiv preprint arXiv:2512.02009},
  year={2025}
}
```