import cv2
import numpy as np


def add_gaussian_noise(img: np.ndarray, level: float) -> np.ndarray:
    """Add Gaussian noise with the requested standard-deviation level."""
    noise = np.random.normal(0, level, img.shape)
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def add_salt_pepper_noise(img: np.ndarray, amount: float) -> np.ndarray:
    """Add salt-and-pepper impulse noise to an image."""
    noisy = img.copy()
    probability = amount / 1000.0

    salt = np.random.random(img.shape[:2]) < probability
    pepper = np.random.random(img.shape[:2]) < probability

    noisy[salt] = 255
    noisy[pepper] = 0
    return noisy
