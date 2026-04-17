<div align="center">

# 🚁 AirSim360 Software

**High-fidelity panoramic simulation at your fingertips.**

*Whether you want to fly with a keyboard or code your way to the skies, we've got you covered.*

</div>

---

## 🌟 Choose Your Flavour

AirSim360 comes in two distinct editions tailored for different missions:

- **[🕹️ AirSim360 Air](#️-airsim360-air)**: The plug-and-play GUI edition. Grab your keyboard, fly around, and collect data instantly. 
- **[🛠️ AirSim360 Pro](#️-airsim360-pro)**: The developer's sandbox. Connect via Python, control via API, and automate everything.

---

## 💻 Rig Requirements

To handle the stunning realism and simultaneous rendering of panoramic RGB, depth, and semantics, you'll need a solid rig.

> 🐧 **Linux user?** Hang tight! Support is landing in **Q2 2026**.
> 🪟 **Windows user?** Windows 10 & 11 are good to go!

| Specs | Minimum (For casual flights) | Recommended (For high-FPS panoramic data crunching) |
| :--- | :--- | :--- |
| **GPU** | NVIDIA GPU with **16GB+ VRAM** | NVIDIA GPU with **24GB+ VRAM** |
| **RAM** | **16GB+** System RAM | **32GB+** System RAM |

---

## 🕹️ AirSim360 Air

> **🔥 ZERO ENVIRONMENT SETUP REQUIRED!** 
> 
> No Python, no dependencies, no headaches. Just unzip, double-click, and you're in the air. Perfect for researchers and non-programmers who need rapid data collection without wrestling with code.

### ✨ Highlights

* 🚀 **Plug & Play:** Launch the remote control, start the simulator, connect, and take off. 
* 🎮 **Gamer-Friendly Controls:** Fly naturally using `W/S` (ascend/descend), `A/D` (yaw), and directional arrows (move/strafe).
* 📸 **Flawless Panoramas:** Export seamless 360° images—no messy post-processing stitching required.
* 📏 **True Depth & Semantics:** Get point-to-point Euclidean depth maps and perfectly masked semantic segmentation out of the box.
* 🎥 **Dynamic Views:** Hit **`P`** to seamlessly swap between FPV (onboard) and TPV (chase) cameras.
* ⚡ **Smart Performance:** Press **`R`** to toggle live panorama previews, saving precious GPU cycles when you don't need them.

👉 **Ready to fly?** Check out the **[📖 AirSim360 Air User Guide](AirSim360_Air_User_Guide_EN.md)** for launch sequences, controls, and data capture tips.

---

## 🛠️ AirSim360 Pro

> **🤖 FOR THE CODE WARRIORS**
> 
> Built for professionals who need absolute programmatic control over the drone and the environment.

### ✨ Highlights

* 🐍 **Python-Powered:** Start the executable and attach your script via RPC. If you know the classic AirSim API, you're already a pro here.
* 🎛️ **Absolute Control:** Command velocities, positions, angle rates, and even raw motor PWM directly through the custom API.
* 👁️ **Code-Driven Sensors:** To maximize your framerates, all sensors (including the panoramic array) start *off*. You turn them on via code when *you* need them.
* 📐 **Custom Resolutions:** Dial in your exact panoramic dimensions on the fly (just remember, bigger pixels = bigger GPU load!).
* 👥 **MetaHuman Ready:** Select environments come populated with high-fidelity MetaHuman models to push your algorithms to the limit.

👉 **Ready to code?** Dive into the **[📖 AirSim360 Pro User Guide](AirSim360_Pro_User_Guide_EN.md)** for API endpoints, connection setups, and vehicle state queries.

---

## 🗺️ Map Drop Schedule

Free new maps for the open-source community, dropping on the **15th of every month** starting April 2026!

| Date | Scene | FAB Link |
| :---: | :--- | :--- |
| 📅 **Apr 10, 2026** | 🏙️ `CityDowntown.zip` | [Download on FAB](https://www.fab.com/zh-cn/listings/e6bae9e3-10eb-4f9f-aa93-c09608e782f9) |
| 📅 **Apr 10, 2026** | 🏭 `Factory.zip` | [Download on FAB](https://www.fab.com/zh-cn/listings/b70e108d-1cb0-41dc-b641-016ba089355b) |
| 📅 **Apr 10, 2026** | 🏡 `SpanishCourtyard.zip` | [Download on FAB](https://www.fab.com/zh-cn/listings/ecf3154d-7197-414f-8de4-d06003c63624) |
| 📅 **Apr 10, 2026** | 🏋️ `DekogonGym.zip` | [Download on FAB](https://www.fab.com/zh-cn/listings/03e76034-abbf-4fc2-aa05-b025996eeb1d) |
| 📅 **Apr 10, 2026** | 🏠 `AtmosphericHouse.zip` | [Download on FAB](https://www.fab.com/zh-cn/listings/9b9bfddd-4988-44e0-a4a0-47fda6b7b81c) |
| 🔮 **Coming Soon** | 🤫 *Secret...* | *Stay tuned* |

---

## 🙏 Acknowledgements

This project grew far beyond our initial paper thanks to some incredible people. 

We thank Liu Yan, Leizi, Liu Zihan, and Hugo for their contributions to AirSim360 across its different development stages. 

And to the **global open-source community**: thank you for your patience and support. You keep our rotors spinning! ❤️
