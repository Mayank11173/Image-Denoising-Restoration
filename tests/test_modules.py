import numpy as np

from modules.noise import add_gaussian_noise, add_salt_pepper_noise
from modules.filters import apply_filter
from modules.metrics import calculate_mse, calculate_psnr


def sample_image():
    return np.full((20, 20, 3), 128, dtype=np.uint8)


def test_gaussian_noise_shape():
    img = sample_image()
    result = add_gaussian_noise(img, 25)
    assert result.shape == img.shape
    assert result.dtype == np.uint8


def test_salt_pepper_shape():
    img = sample_image()
    result = add_salt_pepper_noise(img, 25)
    assert result.shape == img.shape
    assert result.dtype == np.uint8


def test_filters():
    img = sample_image()
    for name in ["Gaussian Filter", "Median Filter", "Bilateral Filter"]:
        result = apply_filter(img, name)
        assert result.shape == img.shape


def test_metrics():
    img = sample_image()
    assert calculate_mse(img, img) == 0.0
    assert np.isinf(calculate_psnr(0.0))
