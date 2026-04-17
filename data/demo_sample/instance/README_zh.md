# 实例分割标签说明

[English version](README.md)

本目录中的 PNG 标签（如 `panorama_73.png`）存储了与全景图和语义图对齐的实例标注。

这些标签需要结合 `../semantic_lists_nyc.txt` 一起使用。

## 编码规则

1. **Alpha 通道**存储**语义类别 ID**。
2. **RGB 通道**用于区分同一语义类别下的不同实例。
3. 一个实例由 **(Alpha, R, G, B)** 唯一标识。

## 通道顺序

- **OpenCV**（`cv2.imread(..., cv2.IMREAD_UNCHANGED)`）的通道顺序为 **B、G、R、A**。
- **PIL** 的通道顺序通常为 **R、G、B、A**。

## 相关文件

| 文件 | 说明 |
|------|------|
| `panorama_73.png` | 实例标签图 |
| `../semantic_lists_nyc.txt` | 类名到类 ID 的映射 |
| `read_instance_labels_example.py` | 解析示例 |
