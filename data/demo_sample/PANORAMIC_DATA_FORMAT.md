# Panoramic Data Format

[中文说明](PANORAMIC_DATA_FORMAT_zh.md)

This document describes the current panoramic data format used by `Omni360-Scene`.

## Overview

`Omni360-Scene` panoramic data is organized into four parts: **raw images**, **panoramic depth**, **panoramic semantic labels**, and **panoramic instance labels**.

## Directory layout

Subfolders follow the pattern **scene-prefix + function name**. In the examples below, `dtw` is the scene prefix:

- `dtw_Raw/`
- `dtw_Depth/`
- `dtw_seg_panorama/`
- `dtw_instance_panorama/`
- `dtw_semantic_list`

Here, `dtw` is only an example scene prefix. For other scenes, it is replaced by the corresponding scene-specific prefix.

## Modality definitions

| Modality | Example name | Storage | Description |
|----------|--------------|---------|-------------|
| **Raw images** | `dtw_Raw/` | Image files | Equirectangular RGB image data. |
| **Panoramic depth** | `dtw_Depth/` | **HDF5** | Depth is stored as an image-shaped `/depth` dataset with `float32` values **directly in meters (m)** — no rescaling or de-quantization is needed when reading. Each pixel represents the **true Euclidean distance** from the camera center to the corresponding 3D scene point, with a supported maximum distance of **1000 m**. For backward compatibility, the reader (`depth/read_depth_h5.py`) also accepts the legacy `uint16` format, where the dataset additionally carries a `depth_range_m` attribute and metric depth is recovered by `depth_uint16 / 65535 * depth_range_m`. |
| **Panoramic semantic labels** | `dtw_seg_panorama/` | Image files | Per-pixel semantic labels aligned with the panorama image. |
| **Panoramic instance labels** | `dtw_instance_panorama/` | Image files | Per-pixel instance labels aligned with the panorama image and semantic labels. |
| **Semantic label list** | `dtw_semantic_list` | Text file | Semantic class names and their class IDs. |

