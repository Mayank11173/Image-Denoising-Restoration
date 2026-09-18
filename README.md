# Image Denoising and Restoration Tool

A Computer Vision mini project that demonstrates image denoising and restoration using classical filtering techniques.

The application allows users to upload an image, add simulated noise, apply restoration filters, compare the original, noisy, and restored images, and evaluate restoration quality using MSE and PSNR.

## 1. Project Overview

Digital images can be affected by unwanted noise during image acquisition, transmission, storage, or processing. This project demonstrates how classical Computer Vision techniques can be used to reduce noise while preserving important image details.

The project focuses on:

- Convolution and Filtering
- Image Enhancement and Restoration
- Noise Reduction
- Image Quality Evaluation

## 2. Subject

Computer Vision

## 3. Major Functional Modules

### 1. Image Input Module

Allows the user to upload an image in JPG, JPEG, or PNG format.

**Input:** Image file  
**Output:** Loaded image

### 2. Noise Generation Module

Allows the user to add controlled noise to the uploaded image.

Supported noise types:

- Gaussian Noise
- Salt-and-Pepper Noise

**Input:** Original image, noise type, and noise level  
**Output:** Noisy image

### 3. Image Restoration Module

Allows the user to select a restoration filter.

Available filters:

- Gaussian Filter
- Median Filter
- Bilateral Filter

**Input:** Noisy image and selected filter  
**Output:** Restored image

### 4. Image Comparison Module

Displays the following images for visual comparison:

- Original Image
- Noisy Image
- Restored Image

### 5. Quality Evaluation Module

Evaluates the quality of the restored image using:

- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)

### 6. Download Module

Allows the user to download the restored image.

## 4. Technologies Used

- Python
- OpenCV
- NumPy
- Pillow
- Streamlit
- Pytest
- Git/GitHub

## 5. Computer Vision Techniques

### Gaussian Filtering

Gaussian filtering is used to smooth the image and reduce noise using a Gaussian kernel.

### Median Filtering

Median filtering replaces a pixel with the median value of its neighborhood and is useful for reducing impulse noise such as Salt-and-Pepper noise.

### Bilateral Filtering

Bilateral filtering reduces noise while preserving important edges in the image.

## 6. Noise Types

### Gaussian Noise

Gaussian noise is randomly generated using a Gaussian distribution and can be added to simulate noise in digital images.

### Salt-and-Pepper Noise

Salt-and-Pepper noise introduces random black and white pixels into an image.

## 7. Quality Evaluation

### Mean Squared Error (MSE)

MSE measures the average squared difference between the original and restored images.

A lower MSE generally indicates a smaller pixel-wise error.

### Peak Signal-to-Noise Ratio (PSNR)

PSNR measures the similarity between the original and restored images in decibels.

A higher PSNR generally indicates closer agreement with the reference image under this metric.

## 8. Workflow

Upload Image
      ↓
Generate Noise
      ↓
Select Restoration Filter
      ↓
Apply Filtering
      ↓
Display Original / Noisy / Restored Images
      ↓
Calculate MSE and PSNR
      ↓
Download Restored Image

9. Project Structure
    Image-Denoising-Restoration/
│
├── app.py
├── requirements.txt
│
├── modules/
│   ├── __init__.py
│   ├── noise.py
│   ├── filters.py
│   └── metrics.py
│
├── tests/
│   └── test_modules.py
│
├── README.md
├── statement.md
├── architecture.md
├── workflow.md
├── use_case.md
├── class_diagram.md
├── sequence_diagram.md
├── test_cases.md
└── report.md

10. Installation

Install the required dependencies using:
   python3 -m pip install -r requirements.txt
11. Running the Application

Run the Streamlit application using:

python3 -m streamlit run app.py

The application will be available at:

http://localhost:8501
12. Testing

The project includes automated tests using Pytest.

Run the tests using:

python3 -m pytest

The current implementation successfully passes all four automated tests:

4 passed
13. Expected Result

The application displays:

Original Image
Noisy Image
Restored Image
MSE
PSNR

The user can experiment with different noise types, noise levels, and restoration filters and download the restored image.

14. Documentation

The repository contains documentation covering:

Problem Statement
Functional Requirements
Non-Functional Requirements
System Architecture
Workflow
Use Case
Class Diagram
Sequence Diagram
Test Cases
Project Report
15. Project Repository

GitHub Repository:

https://github.com/Mayank11173/Image-Denoising-Restoration
   
 
