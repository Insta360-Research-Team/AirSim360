"""Print distinct alpha-channel values in the demo semantic PNG (class IDs when alpha encodes semantics)."""

from pathlib import Path

import cv2
import numpy as np

IMAGE_NAME = "panorama_73.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    path = here / IMAGE_NAME

    img = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if img is None:
        raise SystemExit(f"Failed to read image: {path}")

    if img.ndim != 3 or img.shape[2] < 4:
        raise SystemExit(
            f"Expected BGRA (4 channels); got shape {img.shape}. No alpha channel."
        )

    alpha = img[:, :, 3]
    unique_values = np.unique(alpha)

    print("Unique alpha channel values:")
    print(unique_values.tolist())


if __name__ == "__main__":
    main()
