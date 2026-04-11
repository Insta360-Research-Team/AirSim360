# 实例分割真值标签使用说明

[English version](README.md)

本目录下的实例分割 PNG（如 `panorama_73.png`）与 `../semantic_lists_nyc.txt` 配合使用，用于表示「语义大类 + 同类中不同物体实例」。

## 编码规则

1. **Alpha 通道**：存储**语义大类 ID**（与 `semantic_lists_nyc.txt` 中每行末尾的整数一致）。`alpha = 0` 一般表示背景，可忽略。
2. **RGB 通道**：在同一语义大类下，**不同的 RGB 组合表示不同的实例**。  
3. **实例的唯一性**：由四元组 **(Alpha, R, G, B)** 唯一确定。同一 Alpha 下若 RGB 相同，则属于同一实例；若 RGB 不同，则为不同实例。

对每个非零 Alpha，会枚举该 Alpha 下所有不同 RGB，并为每个 **(Alpha, R, G, B)** 分配在该 Alpha 内的实例序号 `Index`（每个 Alpha 各自从 0 递增）。若需**全局**唯一 ID，请直接使用 **(Alpha, R, G, B)** 四元组或对四元组做哈希。

## 读取时注意通道顺序

- 使用 **OpenCV**（`cv2.imread(..., cv2.IMREAD_UNCHANGED)`）时，数组通道顺序为 **B、G、R、A**，需将 B、G、R 转为 R、G、B 后再与文档中的列名对应。
- 使用 **PIL** 读取带透明 PNG 时，通常为 **R、G、B、A**，与文档列名一致。

## 相关文件

| 文件 | 说明 |
|------|------|
| `panorama_73.png` | 实例标签图（BGRA 或 RGBA，取决于读取库） |
| `../semantic_lists_nyc.txt` | 语义类名 ↔ 大类 ID（与 Alpha 对应） |
| `read_instance_labels_example.py` | 解析标签的示例代码 |

## 快速开始

在已安装 `opencv-python`、`numpy` 的环境中执行：

```bash
cd data/demo_sample/instance
python read_instance_labels_example.py
```

脚本会列出图中出现的语义类、实例数量，并演示如何将像素映射到 **(Alpha, R, G, B)** 及每类内的实例序号。
