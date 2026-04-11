# Data

## `demo_sample/`

Full documentation: [`demo_sample/README.md`](demo_sample/README.md) (English) · [`demo_sample/README_zh.md`](demo_sample/README_zh.md)（中文）.

One **complete synchronized sample** for the platform (not a training corpus):

| Subfolder   | Content |
|------------|---------|
| `panorama/` | Equirectangular RGB (or your omnidirectional RGB export). |
| `semantic/` | Semantic segmentation map for the same frame index. |
| `depth/`    | Depth / range map (`.npy`, `.exr`, or uint/float image per your pipeline). |
| `instance/` | Instance / entity segmentation map. |
| `scripts/`  | `read_demo_ground_truth.py` loads one frame by stem name across folders. |
