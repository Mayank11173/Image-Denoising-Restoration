# Image Denoising and Restoration Tool

## 1. Project Overview
A small Computer Vision project that demonstrates image denoising and restoration using classical filtering techniques.

The application allows a user to upload an image, add simulated noise, apply a restoration filter, compare the results, and evaluate restoration quality using MSE and PSNR.

## 2. Subject
Computer Vision

## 3. Syllabus Topics Used
- Convolution and Filtering
- Image Restoration

## 4. Major Functional Modules
1. Image Input Module
2. Noise Generation Module
3. Image Restoration/Filtering Module
4. Quality Evaluation Module

## 5. Technologies
- Python
- OpenCV
- NumPy
- Pillow
- Streamlit

## 6. Filters
- Gaussian Filter
- Median Filter
- Bilateral Filter

## 7. How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 8. Workflow
Upload image → Add noise → Select restoration filter → View restored image → Calculate MSE/PSNR → Download result.

## 9. Project Structure

```text
Image-Denoising-Restoration/
├── app.py
├── requirements.txt
├── README.md
├── statement.md
├── test_cases.md
├── architecture.md
├── workflow.md
├── use_case.md
├── class_diagram.md
├── sequence_diagram.md
└── report.md
```

## 10. Expected Result
The application displays the original, noisy, and restored images side-by-side and reports MSE and PSNR.

## 11. GitHub
Create a Git repository, add all project files, commit them, and push the repository to GitHub.
