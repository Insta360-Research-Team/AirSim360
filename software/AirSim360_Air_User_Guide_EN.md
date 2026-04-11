# AirSim360 Air — Quick User Guide

The **Air** edition’s data‑collection software is self‑contained: it needs no extra applications or environment setup beyond this package, so it is effectively **plug‑and‑play** on a supported Windows PC.

This guide summarizes how to run **AirSim360 Air** on Windows. Screenshots from the original manual are stored under [`images/`](images/).

---

## 1. Hardware and OS

The simulator relies on **high‑quality real‑time rendering**. Use a machine that meets or exceeds the following:

- **GPU:** NVIDIA GPU, **VRAM ≥ 16 GB** (strongly recommended).
- **System memory:** **RAM ≥ 32 GB** recommended.
- **OS:** Tested on **Windows 11**; **Windows 10** is also supported. 
- **Display:** **Avoid full‑screen** if possible; it noticeably increases GPU load.

---

## 2. Launch order — remote control first

1. Start the **simulation remote control** application **first** (recommended).

![Simulation remote control](images/airsim360_air_doc_01.png)

2. Start the **main simulator** window.

![Main simulator interface](images/airsim360_air_doc_02.png)

3. Keep **both** windows open while you complete the preflight steps below.

---

## 3. Preflight — button order

With both apps running, use the controls in this order:

1. **Connect** (link the remote to the sim).
2. **Select keyboard / mouse control mode.**
3. Press **Start Task** to begin.

![Connect, control mode, Start Task](images/airsim360_air_doc_03.png)

---

## 4. Enter the scene and take off

1. **Click inside the renderer view** on the left (focus the simulation window).
2. Read the **license / usage agreement**. Press **Y** to accept and enter the scene.
3. Click **Take off** when you are ready.

![Agreement and takeoff](images/airsim360_air_doc_04.png)

---

## 5. Panorama previews and multimodal capture

The **three panorama previews** at the bottom use a lot of GPU and are **off by default**.

- **R:** turn previews **on**; press **R** again to turn them **off**.  
  Use this when you work with **panorama multimodal** output (RGB / related streams shown in the UI).

---

## 6. Keyboard and mouse flight controls

| Key | Action |
| --- | --- |
| **W** | Ascend |
| **S** | Descend |
| **A** | Yaw left |
| **D** | Yaw right |
| **↑** (Up arrow) | Move forward |
| **↓** (Down arrow) | Move backward |
| **←** (Left arrow) | Strafe left |
| **→** (Right arrow) | Strafe right |

---

## 7. Switch the aircraft camera view

![Camera / view control hint](images/airsim360_air_doc_05.jpeg)

- **P** — **On:** switch to the aircraft’s **main camera** view.  
- **P** — **Off:** return to the default **third‑person chase** view around the drone.

---

## 8. Where files are saved

Outputs are split into modality folders:

- **`Raw/`** — full **panorama RGB** images  
- **`Depth/`** — **panorama depth** maps  
- **`Seg/`** — **panorama semantic segmentation** labels  

![Save path overview](images/screenshot_5658.png)

If your build uses a different layout, follow the paths shown in the simulator or your project configuration.

---

## 9. Shut down safely

Always exit in this order:

1. **Close the simulation remote control first** (required).
2. Then **close the main simulator** window.

![Shutdown order](images/airsim360_air_doc_07.jpeg)

---