# AirSim360 multimodal panoramic data: overview and usage

[中文版说明](README_zh.md)

This document describes the **`demo_sample`** layout and how it relates to the **upcoming open-source multimodal omnidirectional dataset**.

## Release schedule and hosting

The full open-source release will **total more than 700 GB**. We aim to have **all dataset parts published by 17 April 2026**. Whether distribution uses **Google Drive**, **Hugging Face**, or a combination will be stated on the **project homepage** (see the root `README.md` of this repository for the link).

## Purpose

This folder ships **one synchronized omnidirectional sample** (not a training corpus): **panorama RGB**, **panorama depth**, **panorama semantic labels**, and **panorama instance labels**. It previews how the **upcoming public dataset** will be organized.

## Upcoming dataset layout (same as this sample)

The full release will follow the **same directory layout**. For each captured frame, the four modalities use the **same file name stem (prefix)** so you can align them without extra metadata—for example `000123.png` / `000123.exr` under `panorama/`, `semantic/`, `depth/`, and `instance/` respectively. In this demo, modalities are aligned by the **same frame index** (see file names in each subfolder).

## Modality guide (short)

| Modality | Folder | What it is | More detail |
|----------|--------|------------|-------------|
| **Panorama RGB** | `panorama/` | Equirectangular (360°) color image for the frame. | Typical formats: `.png`, `.jpg`. |
| **Depth** | `depth/` | Per-pixel **true Euclidean distance** from the camera **optical center** to the **3D scene point** imaged at that pixel (not “z-only” in a local tangent plane unless your renderer defines it that way in export docs). **Default unit: meters (m)**. **Maximum range supported: 1000 m.** Stored as floating-point (e.g. `.exr` or `.npy`). | See `depth/check_depth.py` for a small OpenCV-based inspector. |
| **Semantic** | `semantic/` | Panorama **semantic segmentation** label image. The demo helper `semantic/read_alpha_unique_values.py` inspects the **alpha channel** (distinct class IDs present in the map). Class names and IDs are listed in `semantic_lists_nyc.txt` at the demo root (same file referenced by instance labels). | Open PNG with an alpha-aware reader (`cv2.IMREAD_UNCHANGED` or equivalent). |
| **Instance** | `instance/` | Panorama **instance segmentation**: **alpha** = semantic class ID; **RGB** (within one class) distinguishes different object instances. Unique object identity is the **(A, R, G, B)** tuple (mind **BGR vs RGB** when using OpenCV vs PIL). | See `instance/README.md` / `instance/README_zh.md` and `instance/read_instance_labels_example.py`. |

## Scripts (repo root–relative)

| Script | Role |
|--------|------|
| `scripts/read_demo_ground_truth.py` | Loads one frame by **stem** across `panorama/`, `semantic/`, `depth/`, and `instance/` (`imageio` for most images; depth from `.npy` or `.exr`). For `.exr` without OpenCV OpenEXR, install **`OpenEXR`** (`pip install OpenEXR`) so depth can be read via the bundled fallback. Default demo stem: `panorama_73`. |
| `depth/check_depth.py` | Optional: mouse-hover preview of a depth `.exr` (expects OpenCV built with OpenEXR or compatible stack). |
| `semantic/read_alpha_unique_values.py` | Lists unique alpha values in the demo semantic PNG. |
| `instance/read_instance_labels_example.py` | Parses instance PNG + `semantic_lists_nyc.txt`; prints per-class instance counts. |

**Python deps (minimal):** see `requirements-demo.txt` in the repository root; some scripts additionally need `opencv-python` where noted in subfolder READMEs.
