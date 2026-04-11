"""
Read instance-segmentation PNG: alpha = semantic class ID, RGB = instance within class.
Requires: opencv-python, numpy
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import cv2
import numpy as np

IMAGE_NAME = "panorama_73.png"
SEMANTIC_LIST_NAME = "semantic_lists_nyc.txt"


def load_id_to_class_name(list_path: Path) -> dict[int, str]:
    id_to_name: dict[int, str] = {}
    text = list_path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        class_id = int(parts[-1])
        name = parts[0]
        id_to_name[class_id] = name
    return id_to_name


def read_bgra(path: Path) -> np.ndarray:
    img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(path)
    if img.ndim != 3 or img.shape[2] < 4:
        raise ValueError(f"Expected BGRA image; got shape {img.shape}")
    return img


def unique_argb_tuples(bgra: np.ndarray) -> np.ndarray:
    b, g, r, a = cv2.split(bgra)
    stacked = np.stack([a, r, g, b], axis=-1).reshape(-1, 4)
    fg = stacked[:, 0] > 0
    if not np.any(fg):
        return np.empty((0, 4), dtype=np.uint8)
    return np.unique(stacked[fg], axis=0)


def per_alpha_instance_index(argb_rows: np.ndarray) -> dict[tuple[int, int, int, int], int]:
    """For each alpha, assign instance indices 0..N-1 to distinct (R,G,B)."""
    by_alpha: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for row in argb_rows:
        alpha, rv, gv, bv = (int(x) for x in row)
        by_alpha[alpha].append((rv, gv, bv))
    out: dict[tuple[int, int, int, int], int] = {}
    for alpha, rgbs in by_alpha.items():
        unique_rgb = sorted(set(rgbs))
        for idx, (rv, gv, bv) in enumerate(unique_rgb):
            out[(alpha, rv, gv, bv)] = idx
    return out


def build_dense_instance_ids(bgra: np.ndarray, argb_to_index: dict[tuple[int, int, int, int], int]) -> np.ndarray:
    """Dense map: 0 = background; positive ids group (alpha, per-alpha index) for demo visualization."""
    h, w = bgra.shape[:2]
    b, g, r, a = cv2.split(bgra)
    flat_a = a.reshape(-1).astype(np.int32)
    flat_r = r.reshape(-1).astype(np.int32)
    flat_g = g.reshape(-1).astype(np.int32)
    flat_b = b.reshape(-1).astype(np.int32)
    out = np.zeros(h * w, dtype=np.int32)
    fg = flat_a > 0
    if not np.any(fg):
        return out.reshape(h, w)
    pair_to_id: dict[tuple[int, int], int] = {}
    next_id = 1
    for i in np.flatnonzero(fg):
        alpha = int(flat_a[i])
        rv, gv, bv = int(flat_r[i]), int(flat_g[i]), int(flat_b[i])
        idx = argb_to_index[(alpha, rv, gv, bv)]
        key = (alpha, idx)
        if key not in pair_to_id:
            pair_to_id[key] = next_id
            next_id += 1
        out[i] = pair_to_id[key]
    return out.reshape(h, w)


def main() -> None:
    here = Path(__file__).resolve().parent
    demo_root = here.parent
    img_path = here / IMAGE_NAME
    list_path = demo_root / SEMANTIC_LIST_NAME

    id_to_name = load_id_to_class_name(list_path)
    bgra = read_bgra(img_path)

    unique_rows = unique_argb_tuples(bgra)
    argb_to_index = per_alpha_instance_index(unique_rows)

    print("Image:", img_path)
    print("Semantic list:", list_path)
    print("Unique (Alpha, R, G, B) instance keys (alpha > 0):", len(unique_rows))

    by_alpha_count: dict[int, int] = defaultdict(int)
    for row in unique_rows:
        by_alpha_count[int(row[0])] += 1

    print("\nPer semantic class (alpha): distinct RGB instances")
    for alpha in sorted(by_alpha_count):
        name = id_to_name.get(alpha, "?")
        print(f"  alpha={alpha:3d}  {name:20s}  instances={by_alpha_count[alpha]}")

    if len(unique_rows) > 0:
        a0, r0, g0, b0 = (int(x) for x in unique_rows[0])
        idx0 = argb_to_index[(a0, r0, g0, b0)]
        cls = id_to_name.get(a0, "?")
        print("\nExample: first (Alpha,R,G,B) tuple")
        print(f"  (A,R,G,B)=({a0},{r0},{g0},{b0})  class={cls!r}  per-alpha Index={idx0}")

    dense = build_dense_instance_ids(bgra, argb_to_index)
    print("\nDense per-pixel instance map (0=background): max id =", int(dense.max()))


if __name__ == "__main__":
    main()
