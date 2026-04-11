"""
Visualize a float depth map (.exr) with OpenCV. Depth is scalar; this demo reads the R channel from a 3-channel BGR load (see export convention).
Requires OpenCV with OpenEXR enabled: set OPENCV_IO_ENABLE_OPENEXR=1 before import (set below).
"""

from __future__ import annotations

import argparse
import os

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

from pathlib import Path

import cv2
import numpy as np


def read_depth_plane(path: Path) -> np.ndarray:
    img = cv2.imread(str(path), cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    if img is None:
        raise SystemExit(f"Failed to read: {path}")
    if img.ndim == 3:
        return img[:, :, 2].astype(np.float32)
    return img.astype(np.float32)


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Hover to inspect depth EXR values.")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=here / "Depth_73.exr",
        help="Path to depth .exr (default: Depth_73.exr next to this script)",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Divide raw values by this factor (1.0 = file units, typically meters)",
    )
    parser.add_argument("--unit-label", type=str, default="m", help="Label shown next to values")
    args = parser.parse_args()

    if not args.path.is_file():
        raise SystemExit(f"File not found: {args.path}")

    data = read_depth_plane(args.path) / args.scale
    data = np.nan_to_num(data, nan=0.0, posinf=0.0, neginf=0.0)

    print(f"Loaded: {args.path.name}")
    print(f"Max (finite): {np.max(data):.4f} {args.unit_label}")

    display_max = float(np.percentile(data, 95)) or 1.0
    preview = np.clip(data / display_max, 0, 1)
    preview = (preview * 255).astype(np.uint8)
    preview = cv2.cvtColor(preview, cv2.COLOR_GRAY2BGR)

    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            canvas = preview.copy()
            val = float(data[y, x])
            text = f"Val: {val:.3f} {args.unit_label} | Pixel: {x},{y}"
            cv2.putText(canvas, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
            cv2.circle(canvas, (x, y), 4, (0, 0, 255), -1)
            cv2.imshow("Inspector", canvas)

    cv2.namedWindow("Inspector", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Inspector", on_mouse)
    cv2.imshow("Inspector", preview)
    print("Move mouse over the image; press 'q' to quit.")
    while True:
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
