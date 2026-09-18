import cv2
import numpy as np


FILTERS = {
    "Gaussian Filter",
    "Median Filter",
    "Bilateral Filter",
}


def apply_filter(img: np.ndarray, filter_type: str) -> np.ndarray:
    """Apply the selected restoration filter."""
    if filter_type not in FILTERS:
        raise ValueError(f"Unsupported filter: {filter_type}")

    if filter_type == "Gaussian Filter":
        return cv2.GaussianBlur(img, (5, 5), 0)

    if filter_type == "Median Filter":
        return cv2.medianBlur(img, 5)

    return cv2.bilateralFilter(img, 9, 75, 75)
