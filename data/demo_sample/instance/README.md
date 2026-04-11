# Instance segmentation ground-truth labels

[中文版说明](README_zh.md)

PNG labels in this folder (for example `panorama_73.png`) are used together with `../semantic_lists_nyc.txt` to represent **semantic class + object instances within each class**.

## Encoding

1. **Alpha channel**: stores the **semantic class ID** (the integer at the end of each line in `semantic_lists_nyc.txt`). **`alpha = 0`** is usually background and can be ignored.
2. **RGB channels**: within one semantic class, **each distinct RGB triple denotes a different object instance**.
3. **Uniqueness**: an instance is uniquely identified by **(Alpha, R, G, B)**. Same alpha and same RGB → same instance; different RGB under the same alpha → different instances.

For each non-zero alpha, all distinct RGB values are listed and each **(Alpha, R, G, B)** gets a per-alpha instance **`Index`** (starting at 0 separately for each alpha). For a **globally** unique ID, use the **(Alpha, R, G, B)** tuple or a hash of it.

## Channel order when reading

- **OpenCV** (`cv2.imread(..., cv2.IMREAD_UNCHANGED)`): array order is **B, G, R, A** — convert to **R, G, B** before matching the design doc column names.
- **PIL** (RGBA PNG): order is typically **R, G, B, A**, which matches the doc columns directly.

## Related files

| File | Role |
|------|------|
| `panorama_73.png` | Instance label image |
| `../semantic_lists_nyc.txt` | Class name ↔ class ID (matches alpha) |
| `read_instance_labels_example.py` | Example parsing code |

## Quick start

With `opencv-python` and `numpy` installed:

```bash
cd data/demo_sample/instance
python read_instance_labels_example.py
```

The script prints semantic classes present, instance counts, and shows how to map pixels to **(Alpha, R, G, B)** and per-class instance indices.
