# Class / Component Diagram

```text
+----------------------+
| ImageInput           |
+----------------------+
| upload_image()       |
+----------------------+
           |
           v
+----------------------+
| NoiseGenerator       |
+----------------------+
| add_gaussian_noise() |
| add_sp_noise()       |
+----------------------+
           |
           v
+----------------------+
| RestorationFilter    |
+----------------------+
| gaussian_filter()    |
| median_filter()      |
| bilateral_filter()   |
+----------------------+
           |
           v
+----------------------+
| QualityEvaluator     |
+----------------------+
| calculate_mse()      |
| calculate_psnr()     |
+----------------------+
```

Note: The implementation is kept as a compact Streamlit application; this diagram represents the logical components of the system.
