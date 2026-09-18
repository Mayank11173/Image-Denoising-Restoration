import numpy as np


def calculate_mse(original: np.ndarray, restored: np.ndarray) -> float:
    """Return mean squared pixel error between two images."""
    return float(
        np.mean(
            (original.astype(np.float32) - restored.astype(np.float32)) ** 2
        )
    )


def calculate_psnr(mse: float) -> float:
    """Return PSNR in dB for an 8-bit image."""
    if mse == 0:
        return float("inf")
    return float(10 * np.log10((255 ** 2) / mse))
