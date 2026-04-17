"""Read an AirSim360 panoramic depth HDF5 file and plot a depth histogram in meters.

Two on-disk formats are supported and detected automatically:

1. float32 metric depth (newer format, e.g. ``Depth_1.h5``)::

    /depth      float32, shape (H, W)
                values are already in meters; no conversion needed.

2. uint16 quantized depth (legacy format, e.g. ``Depth_73.h5``)::

    /depth      uint16, shape (H, W)
                attribute depth_range_m: float (meters), e.g. 1000.0
                metric depth in meters is recovered by:
                    depth_m = depth_uint16.astype(np.float32) / 65535.0 * depth_range_m

The output histogram uses meters on the x axis and is saved next to the input file.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import h5py
import matplotlib.pyplot as plt
import numpy as np

DEPTH_DATASET = "depth"
RANGE_ATTR = "depth_range_m"
UINT16_MAX = 65535.0
DEFAULT_RANGE_M = 1000.0


def load_depth_meters(h5_path: Path) -> tuple[np.ndarray, float]:
    """Return ``(depth_in_meters, depth_range_m)`` for the panoramic depth file.

    Auto-detects the storage format:
      * ``float32`` -> values are taken as meters directly.
      * ``uint16``  -> values are de-quantized using ``depth_range_m`` (default 1000 m).
    """
    with h5py.File(h5_path, "r") as f:
        if DEPTH_DATASET not in f:
            raise KeyError(
                f"Dataset '{DEPTH_DATASET}' not found in {h5_path}. "
                f"Available keys: {list(f.keys())}"
            )
        dset = f[DEPTH_DATASET]
        raw = dset[...]
        depth_range_attr = dset.attrs.get(RANGE_ATTR, None)

    if raw.dtype == np.uint16:
        depth_range_m = float(depth_range_attr) if depth_range_attr is not None else DEFAULT_RANGE_M
        depth_m = raw.astype(np.float32) / UINT16_MAX * depth_range_m
        print(f"format: uint16 (quantized) -> de-quantized to meters using depth_range_m={depth_range_m:.1f} m")
    elif raw.dtype in (np.float32, np.float64, np.float16):
        depth_m = raw.astype(np.float32)
        finite = depth_m[np.isfinite(depth_m)]
        depth_range_m = (
            float(depth_range_attr) if depth_range_attr is not None
            else (float(finite.max()) if finite.size else DEFAULT_RANGE_M)
        )
        print(f"format: {raw.dtype} (already metric) -> values are taken as meters directly, no conversion needed")
    else:
        raise TypeError(
            f"Unsupported depth dtype {raw.dtype}; expected uint16 (quantized) or float32 (metric)."
        )

    return depth_m, depth_range_m


def print_summary(depth_m: np.ndarray, depth_range_m: float) -> None:
    finite = np.isfinite(depth_m)
    valid = depth_m[finite]
    print(f"shape:          {depth_m.shape}")
    print(f"depth range:    0 - {depth_range_m:.1f} m")
    print(f"min / max:      {valid.min():.3f} m / {valid.max():.3f} m")
    print(f"mean / median:  {valid.mean():.3f} m / {np.median(valid):.3f} m")


def plot_depth_histogram(
    depth_m: np.ndarray,
    depth_range_m: float,
    out_path: Path,
    bins: int = 200,
    saturation_eps: float = 1e-3,
) -> None:
    """Plot a histogram of depth values in meters and save it next to the input."""
    values = depth_m[np.isfinite(depth_m)]

    saturation_threshold = depth_range_m * (1.0 - saturation_eps)
    plot_values = values[values < saturation_threshold]
    saturated = int(values.size - plot_values.size)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(plot_values, bins=bins, range=(0.0, depth_range_m), color="#1f77b4")
    ax.set_xlabel("Depth (m)")
    ax.set_ylabel("Pixel count")
    title = f"Panoramic depth histogram (max range {depth_range_m:.0f} m)"
    if saturated > 0:
        title += f"  |  saturated pixels (~{depth_range_m:.0f} m) excluded: {saturated}"
    ax.set_title(title)
    ax.grid(True, linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=here / "Depth_1.h5",
        help="Path to the panoramic depth .h5 file (default: Depth_1.h5 next to this script)",
    )
    parser.add_argument(
        "--bins",
        type=int,
        default=200,
        help="Number of histogram bins (default: 200)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output histogram path (default: <input_stem>_hist.png next to the input)",
    )
    args = parser.parse_args()

    if not args.path.is_file():
        raise SystemExit(f"File not found: {args.path}")

    depth_m, depth_range_m = load_depth_meters(args.path)
    print_summary(depth_m, depth_range_m)

    out_path = args.out or args.path.with_name(f"{args.path.stem}_hist.png")
    plot_depth_histogram(depth_m, depth_range_m, out_path, bins=args.bins)
    print(f"Saved histogram: {out_path}")


if __name__ == "__main__":
    main()
