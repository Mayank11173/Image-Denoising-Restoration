# Image Denoising and Restoration Tool

## 1. Cover Page
**Project Title:** Image Denoising and Restoration Tool  
**Subject:** Computer Vision  
**Project Type:** Mini Project

## 2. Introduction
Digital images may contain unwanted noise caused by sensors, transmission errors, lighting conditions, or environmental factors. Image denoising attempts to reduce this unwanted variation while preserving useful image information.

## 3. Problem Statement
Develop a small computer vision application that introduces controlled noise into an image and uses filtering techniques to reduce the noise and restore the image.

## 4. Objectives
- Demonstrate convolution and filtering.
- Demonstrate basic image restoration.
- Compare noisy and restored images.
- Calculate MSE and PSNR.

## 5. Functional Requirements
1. Upload image.
2. Generate Gaussian or salt-and-pepper noise.
3. Apply Gaussian, Median, or Bilateral filtering.
4. Display original, noisy, and restored images.
5. Calculate MSE and PSNR.
6. Download restored image.

## 6. Non-Functional Requirements
- Usability: simple interface.
- Performance: processing should be fast for normal-sized images.
- Reliability: invalid file types are rejected.
- Maintainability: functions are separated logically and code is documented.

## 7. System Architecture
See `architecture.md`.

## 8. Design Diagrams
- Use Case: `use_case.md`
- Workflow: `workflow.md`
- Sequence: `sequence_diagram.md`
- Component/Class: `class_diagram.md`

## 9. Technical Concepts

### Convolution and Filtering
Filtering processes a pixel using information from its neighboring pixels. A filter kernel/window is moved over the image to smooth noise or modify image characteristics.

### Gaussian Filter
Gaussian filtering performs weighted smoothing. Nearby pixels receive greater weight than pixels farther from the center.

### Median Filter
The median filter replaces a pixel with the median value in its local neighborhood. It is particularly useful for salt-and-pepper noise.

### Bilateral Filter
Bilateral filtering considers both spatial distance and intensity difference, allowing smoothing while retaining many edges.

### Image Restoration
Image restoration attempts to recover a cleaner image from a degraded/noisy observation using a mathematical or algorithmic process.

## 10. Quality Evaluation

### MSE
Mean Squared Error measures the average squared difference between the reference image and restored image.

### PSNR
Peak Signal-to-Noise Ratio is derived from MSE and is commonly used to express reconstruction quality in decibels.

## 11. Implementation
The project uses Python, OpenCV, NumPy, Pillow, and Streamlit. The complete implementation is in `app.py`.

## 12. Results
The application produces:
- Original image
- Noisy image
- Restored image
- MSE value
- PSNR value

Screenshots of the running application should be added here after execution.

## 13. Testing
Testing cases are listed in `test_cases.md`.

## 14. Challenges Faced
- Selecting appropriate filter parameters.
- Maintaining image dimensions and pixel ranges.
- Comparing restoration quality.
- Creating a simple user interface.

## 15. Learnings
- Learned how noise affects digital images.
- Learned basic image filtering.
- Learned practical use of OpenCV.
- Learned MSE and PSNR based evaluation.
- Learned how to create a small CV application using Streamlit.

## 16. Future Enhancements
- Add more restoration algorithms.
- Add interactive filter parameters.
- Add batch image processing.
- Add comparison charts.
- Add automatic selection of a suitable filter.

## 17. References
- OpenCV documentation
- NumPy documentation
- Streamlit documentation
- Course notes and Computer Vision syllabus
