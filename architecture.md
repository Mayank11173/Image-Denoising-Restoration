# System Architecture

```text
+----------------------+
|       User           |
+----------+-----------+
           |
           v
+----------------------+
| Streamlit User       |
| Interface            |
+----------+-----------+
           |
           v
+----------------------+
| Image Input Module   |
+----------+-----------+
           |
           v
+----------------------+
| Noise Generation     |
| Module               |
+----------+-----------+
           |
           v
+----------------------+
| Restoration Module   |
| Gaussian / Median /  |
| Bilateral            |
+----------+-----------+
           |
           +------------------+
           |                  |
           v                  v
+-------------------+  +-------------------+
| Result Display    |  | Quality Evaluation|
| Original/Noisy/   |  | MSE + PSNR        |
| Restored          |  +-------------------+
+-------------------+
```
