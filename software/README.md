# AirSim360



AirSim360 is a high-fidelity simulation software designed to meet the diverse needs of developers and researchers. We offer two tailored versions: **AirSim360 Air** (a user-friendly, GUI-driven version for direct data collection via keyboard and mouse) and **AirSim360 Pro** (for developers requiring code-based control and API access). 



## 💻 System Requirements



Since AirSim360 features highly realistic environments and rich functional interfaces, it requires capable hardware. 



* **OS:** Windows 11 (Linux support coming in Q2 2026)

* **Minimum Requirements:**

    * NVIDIA GPU with >= 16GB VRAM

    * System RAM >= 16GB

* **Recommended Requirements** *(Crucial for maintaining high framerates when simultaneously rendering panoramic RGB, depth, and semantic maps)*:

    * NVIDIA GPU with >= 24GB VRAM

    * System RAM >= 32GB



---



## 🕹️ AirSim360 Air



Designed for non-programmers and researchers focused on rapid data collection using an intuitive interface.



### Features

* **Zero Setup Required:** Launch the software and manage everything directly through the integrated control panel.

* **Seamless Panoramic Export:** Export panoramic images at customizable resolutions without the need for post-processing stitching algorithms or visible seams.

* **Accurate Depth Mapping:** Export panoramic depth maps based on true point-to-point Euclidean distance.

* **Semantic Segmentation:** Full support for exporting panoramic semantic segmentation masks.

* **Optimized Flight Dynamics:** Integrated with an advanced flight controller to ensure highly stable drone navigation.

* **2-Axis Virtual Gimbal:** All cameras are mounted on a simulated 2-axis gimbal to guarantee stable and smooth image capture.

* **Multi-Viewport Display:** Real-time visual feedback across multiple viewports for immediate rendering perception.

* **One-Click Data Collection:** Dedicated hotkeys to start and stop data collection with automatic file saving.



### Usage Guide

* [AirSim360 Air User Guide (English)](AirSim360_Air_User_Guide_EN.md) — control panel, launch order, preflight steps, navigation, and data capture



---



## 🛠️ AirSim360 Pro



Built for professionals and developers who require programmatic control over the simulation environment.



### Features

* **Out-of-the-box Execution:** No complex environment setup required. Simply run the executable and control it directly via our code API.

* **Seamless Panoramic Export:** Export panoramic images at customizable resolutions without the need for post-processing stitching algorithms or visible seams.

* **Accurate Depth Mapping:** Export panoramic depth maps based on true point-to-point Euclidean distance.

* **Semantic Segmentation:** Full support for exporting panoramic semantic segmentation masks.

* **Optimized Flight Dynamics:** Integrated with an advanced flight controller to ensure highly stable drone navigation.

* **2-Axis Virtual Gimbal:** All cameras are mounted on a simulated 2-axis gimbal to guarantee stable and smooth image capture.

* **View Toggling:** Hotkey support to seamlessly switch between FPV (First-Person View) and TPV (Third-Person View).

* **MetaHuman Integration:** Select environments feature high-fidelity MetaHuman models to enrich your testing scenarios.



### Usage Guide

* [AirSim360 Pro User Guide (English)](AirSim360_Pro_User_Guide_EN.md) — run the simulator, Python client, panoramic RGB/depth, vehicle state, control APIs, and dependencies



---



## 🗺️ Map Update Schedule



Starting in **April 2026**, we will release at least **5 new maps** on the 15th of every month, completely free for the open-source developer community.



| Release Date | Scenario Name | FAB Link |


| April 10, 2026 | `CityDowntown.zip` | [FAB Link](https://www.fab.com/zh-cn/listings/e6bae9e3-10eb-4f9f-aa93-c09608e782f9) |

| April 10, 2026 | `Factory.zip` | [FAB Link](https://www.fab.com/zh-cn/listings/b70e108d-1cb0-41dc-b641-016ba089355b) |

| April 10, 2026 | `SpanishCourtyard.zip` | [FAB Link](https://www.fab.com/zh-cn/listings/ecf3154d-7197-414f-8de4-d06003c63624) |

| April 10, 2026 | `DekogonGym.zip` | [FAB Link](https://www.fab.com/zh-cn/listings/03e76034-abbf-4fc2-aa05-b025996eeb1d) |

| April 10, 2026 | `AtmosphericHouse.zip` | [FAB Link](https://www.fab.com/zh-cn/listings/9b9bfddd-4988-44e0-a4a0-47fda6b7b81c) |

| *Upcoming* | *To be announced...* | *TBA* |



## 🙏 Acknowledgements



### Contributors



The development of AirSim360 has been an extensive journey, and the platform's current capabilities now far exceed those initially presented in our paper.

We would like to express our sincere gratitude to Liu Yan(Harbin Institute of Technology, Shenzhen), Wang Junjie(Insta360), Liu Zihan(Harbin Institute of Technology, Shenzhen) and Hu Xiangping(Zhejiang University) for their exceptional contributions and creative insights, which were fundamental in bringing AirSim360 to fruition.

Finally, we want to thank the global open-source community for your incredible patience and understanding. Your support has been our greatest motivation.

