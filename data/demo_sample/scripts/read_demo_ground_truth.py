"""Load one synchronized demo frame: panorama, semantic, depth, instance (see demo_sample/README.md or README_zh.md)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np

try:
    import imageio.v3 as iio
except ImportError:  # pragma: no cover
    iio = None


@dataclass
class DemoFrame:
    stem: str
    panorama: Optional[np.ndarray]
    semantic: Optional[np.ndarray]
    depth: Optional[np.ndarray]
    instance: Optional[np.ndarray]


def _repo_demo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _read_exr_float_r(path: Path) -> np.ndarray:
    """Depth in EXR: float plane (prefers R channel via OpenEXR; else imageio)."""
    try:
        import Imath
        import OpenEXR

        exr = OpenEXR.InputFile(str(path))
        header = exr.header()
        dw = header["dataWindow"]
        width = dw.max.x - dw.min.x + 1
        height = dw.max.y - dw.min.y + 1
        pt = Imath.PixelType(Imath.PixelType.FLOAT)
        channels = header["channels"]
        ch = "R" if "R" in channels else ("Y" if "Y" in channels else next(iter(channels)))
        raw = exr.channel(ch, pt)
        return np.frombuffer(raw, dtype=np.float32).reshape((height, width))
    except ImportError:
        pass
    except Exception:
        pass
    if iio is None:
        raise RuntimeError("Install imageio or OpenEXR to read .exr: pip install imageio OpenEXR")
    arr = iio.imread(path)
    if arr.ndim == 3:
        return arr[..., 0].astype(np.float32)
    return arr.astype(np.float32)


def _read_image(path: Path) -> Optional[np.ndarray]:
    if not path.is_file():
        return None
    if iio is None:
        raise RuntimeError("Install imageio to load demo images: pip install imageio")
    if path.suffix.lower() == ".exr":
        return _read_exr_float_r(path)
    return iio.imread(path)


def _depth_to_h_w(depth: np.ndarray) -> np.ndarray:
    if depth.ndim == 3:
        return depth[..., 0].astype(np.float32)
    return depth.astype(np.float32)


def _load_depth(dep_dir: Path, stem: str) -> Optional[np.ndarray]:
    dep_npy = dep_dir / f"{stem}.npy"
    if dep_npy.is_file():
        return _depth_to_h_w(np.load(dep_npy))
    for ext in (".exr", ".png", ".tif", ".tiff"):
        p = dep_dir / f"{stem}{ext}"
        if p.is_file():
            depth = _read_image(p)
            return _depth_to_h_w(depth) if depth is not None else None
    m = re.fullmatch(r"panorama_(\d+)", stem, flags=re.IGNORECASE)
    if m:
        p = dep_dir / f"Depth_{m.group(1)}.exr"
        if p.is_file():
            depth = _read_image(p)
            return _depth_to_h_w(depth) if depth is not None else None
    return None


def load_demo_frame(stem: str = "panorama_73") -> DemoFrame:
    """Load ``{stem}.*`` from panorama/, semantic/, depth/, instance/ (see README for depth naming)."""
    root = _repo_demo_root()
    pan_dir = root / "panorama"
    sem_dir = root / "semantic"
    dep_dir = root / "depth"
    ins_dir = root / "instance"

    panorama = None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = pan_dir / f"{stem}{ext}"
        if p.is_file():
            panorama = _read_image(p)
            break

    semantic = None
    for ext in (".png", ".tif", ".tiff"):
        p = sem_dir / f"{stem}{ext}"
        if p.is_file():
            semantic = _read_image(p)
            break

    depth = _load_depth(dep_dir, stem)

    instance = None
    for ext in (".png", ".tif", ".tiff"):
        p = ins_dir / f"{stem}{ext}"
        if p.is_file():
            instance = _read_image(p)
            break

    return DemoFrame(
        stem=stem,
        panorama=panorama,
        semantic=semantic,
        depth=depth,
        instance=instance,
    )


if __name__ == "__main__":
    frame = load_demo_frame()
    print(frame.stem)
    for name, arr in (
        ("panorama", frame.panorama),
        ("semantic", frame.semantic),
        ("depth", frame.depth),
        ("instance", frame.instance),
    ):
        if arr is None:
            print(f"{name}: (missing file)")
        else:
            print(f"{name}: shape={arr.shape}, dtype={arr.dtype}")
