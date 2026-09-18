# Test Cases

| ID | Test | Input | Expected Result |
|---|---|---|---|
| TC01 | Upload valid image | JPG/PNG | Image is displayed |
| TC02 | Add Gaussian noise | Valid image | Noisy image is generated |
| TC03 | Add salt-pepper noise | Valid image | Impulse noise is generated |
| TC04 | Gaussian filter | Noisy image | Smoothed/restored image appears |
| TC05 | Median filter | Noisy image | Noise is reduced |
| TC06 | Bilateral filter | Noisy image | Noise is reduced with edge preservation |
| TC07 | Quality calculation | Original + restored | MSE and PSNR are displayed |
| TC08 | Download | Restored image | PNG file is downloaded |
| TC09 | Invalid file type | PDF/TXT | Upload is rejected by file uploader |
