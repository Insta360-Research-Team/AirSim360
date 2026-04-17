# Instance Segmentation Labels

[中文版说明](README_zh.md)

PNG labels in this folder, such as `panorama_73.png`, store instance annotations aligned with the panorama and semantic maps.

These labels are used together with `../semantic_lists_nyc.txt`.

## Encoding

1. **Alpha channel** stores the **semantic class ID**.
2. **RGB channels** distinguish different object instances within the same semantic class.
3. An instance is uniquely identified by **(Alpha, R, G, B)**.

## Channel order

- **OpenCV** (`cv2.imread(..., cv2.IMREAD_UNCHANGED)`): channel order is **B, G, R, A**.
- **PIL**: channel order is typically **R, G, B, A**.

## Related files

| File | Role |
|------|------|
| `panorama_73.png` | Instance label image |
| `../semantic_lists_nyc.txt` | Class name to class ID mapping |
| `read_instance_labels_example.py` | Parsing example |
