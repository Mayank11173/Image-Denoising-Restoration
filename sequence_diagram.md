# Sequence Diagram

```text
User          Streamlit App       OpenCV       Evaluator
 |                 |                 |              |
 | Upload Image    |                 |              |
 |---------------->|                 |              |
 |                 | Read Image      |              |
 |                 |---------------->|              |
 |                 |                 |              |
 | Select Noise    |                 |              |
 |---------------->| Generate Noise  |              |
 |                 |---------------->|              |
 |                 |<----------------|              |
 | Select Filter   |                 |              |
 |---------------->| Apply Filter    |              |
 |                 |---------------->|              |
 |                 |<----------------|              |
 |                 | Calculate MSE/PSNR              |
 |                 |------------------------------->|
 |                 |<-------------------------------|
 |                 | Display Results |              |
 |<----------------|                 |              |
```
