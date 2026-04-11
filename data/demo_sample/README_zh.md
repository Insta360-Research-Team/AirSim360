# AirSim360 多模态全景数据介绍及使用说明

[English version](README.md)

本文说明 **`demo_sample`** 目录的组织方式，及其与**即将开源的多模态全景数据集**的对应关系。

## 发布时间与托管方式

即将开源的数据总量**将超过 700 GB**。我们将在 **2026 年 4 月 17 日**前完成**全部数据集**的更新与发布。最终通过 **Google Drive**、**Hugging Face** 分发，或两者组合，将在**项目主页**上统一说明（请参阅本仓库根目录 `README.md` 中的主页链接）。

## 说明

本目录提供 **一套对齐的全景样本**（不是完整训练集），包含四类数据：**全景 RGB**、**全景深度**、**全景语义分割标签**、**全景实例分割标签**，用于展示 **即将发布的数据集** 的组织方式。

## 正式发布数据集（与本示例一致）

正式数据将沿用 **相同的目录结构**。每一帧的四类数据将使用 **相同的文件名前缀（stem）** 建立对应关系，便于脚本直接对齐，例如在各子目录下使用同一前缀的 `000123.png`、`000123.exr` 等。本演示包内文件名可能因历史导出略有差异，但均以 **同一帧编号（如 73）** 对齐；细节以各子目录内文件名为准。

## 四类数据速览

| 类型 | 目录 | 内容说明 | 更多信息 |
|------|------|----------|----------|
| **全景原始图像** | `panorama/` | 等距矩形（equirectangular）彩色全景图。 | 常见为 `.png`、`.jpg` 等。 |
| **全景深度** | `depth/` | 每个像素表示从相机 **光心** 到该像素对应 **场景点** 的 **真实欧氏距离**（沿成像射线的几何距离）。**默认数值单位为米（m）**；**最大支持深度为 1000 米**。一般以浮点格式存储（如 `.exr`、`.npy`）。 | 可使用 `depth/check_depth.py` 做简单交互查看。 |
| **全景语义分割** | `semantic/` | 全景语义标签图。演示脚本 `semantic/read_alpha_unique_values.py` 用于查看 **alpha 通道** 中出现的不同取值（类别 ID）。类别名与 ID 对照见演示根目录的 `semantic_lists_nyc.txt`（与实例标签共用）。 | 请使用保留 alpha 的读取方式（如 `cv2.IMREAD_UNCHANGED`）。 |
| **全景实例分割** | `instance/` | 全景实例标签：**alpha** = 语义大类 ID；同一类别下 **RGB** 区分不同实例。实例由 **(A, R, G, B)** 四元组唯一标识（使用 OpenCV 时注意 **BGRA** 与 PIL **RGBA** 的通道顺序差异）。 | 详见 `instance/README.md`、`instance/README_zh.md` 与 `instance/read_instance_labels_example.py`。 |

## 脚本说明（相对仓库根目录）

| 脚本 | 作用 |
|------|------|
| `scripts/read_demo_ground_truth.py` | 按 **同一 stem** 从四个子目录加载一帧（图像主要用 `imageio`；深度支持 `.npy`、`.exr` 等）。若 OpenCV 未启用 OpenEXR，可为 `.exr` 安装 **`OpenEXR`**（`pip install OpenEXR`）以使用脚本内的回退读取。演示默认 stem：`panorama_73`。 |
| `depth/check_depth.py` | 可选：对深度 `.exr` 做鼠标悬停数值查看（需支持 OpenEXR 的 OpenCV 环境）。 |
| `semantic/read_alpha_unique_values.py` | 打印演示语义图中 alpha 通道的所有不同取值。 |
| `instance/read_instance_labels_example.py` | 解析实例 PNG 与 `semantic_lists_nyc.txt`，输出各类实例数量等。 |

**依赖：** 仓库根目录 `requirements-demo.txt`；部分脚本另需 `opencv-python`（见各子目录 README）。
