import io

import cv2
import numpy as np
import streamlit as st
from PIL import Image

from modules.noise import add_gaussian_noise, add_salt_pepper_noise
from modules.filters import apply_filter
from modules.metrics import calculate_mse, calculate_psnr

st.set_page_config(
    page_title="Image Denoising & Restoration",
    page_icon="🖼️",
    layout="wide",
)

st.title("🖼️ Image Denoising and Restoration Tool")
st.caption(
    "Computer Vision mini project using filtering and image restoration techniques."
)

uploaded_file = st.file_uploader(
    "Upload an image", type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    original_rgb = np.array(image)
    original = cv2.cvtColor(original_rgb, cv2.COLOR_RGB2BGR)

    st.sidebar.header("1. Noise Settings")
    noise_type = st.sidebar.selectbox(
        "Noise Type",
        ["Gaussian Noise", "Salt & Pepper Noise"],
    )
    noise_level = st.sidebar.slider("Noise Level", 5, 100, 25)

    if noise_type == "Gaussian Noise":
        noisy = add_gaussian_noise(original, noise_level)
    else:
        noisy = add_salt_pepper_noise(original, noise_level)

    st.sidebar.header("2. Restoration Filter")
    filter_type = st.sidebar.selectbox(
        "Filtering Method",
        ["Gaussian Filter", "Median Filter", "Bilateral Filter"],
    )

    restored = apply_filter(noisy, filter_type)

    noisy_rgb = cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB)
    restored_rgb = cv2.cvtColor(restored, cv2.COLOR_BGR2RGB)

    mse = calculate_mse(original, restored)
    psnr = calculate_psnr(mse)

    st.subheader("Image Results")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("**Original Image**")
        st.image(original_rgb, use_container_width=True)

    with c2:
        st.markdown("**Noisy Image**")
        st.image(noisy_rgb, use_container_width=True)

    with c3:
        st.markdown("**Restored Image**")
        st.image(restored_rgb, use_container_width=True)

    st.subheader("Restoration Quality")
    m1, m2 = st.columns(2)

    with m1:
        st.metric("MSE", f"{mse:.2f}")

    with m2:
        st.metric("PSNR", "∞" if np.isinf(psnr) else f"{psnr:.2f} dB")

    st.info(
        f"Applied method: {filter_type}. "
        "Lower MSE and, generally, higher PSNR indicate closer agreement "
        "with the reference image."
    )

    output = io.BytesIO()
    Image.fromarray(restored_rgb).save(output, format="PNG")

    st.download_button(
        "⬇️ Download Restored Image",
        data=output.getvalue(),
        file_name="restored_image.png",
        mime="image/png",
    )

    with st.expander("About the CV concepts used"):
        st.write(
            """
            • Convolution & Filtering: neighboring pixels are processed using
              a local kernel/window.

            • Image Restoration: noise is reduced to recover a cleaner image.

            • Gaussian Filter: smooths an image and is useful for
              Gaussian-like noise.

            • Median Filter: effective for impulse/salt-and-pepper noise
              while preserving edges.

            • Bilateral Filter: smooths while preserving many edges.

            • MSE: average squared pixel error between reference and restored image.

            • PSNR: quality measure derived from MSE.
            """
        )
else:
    st.info("Upload an image from the sidebar area above to begin.")
