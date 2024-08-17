# CalcyAI
# Math Problem Solver using OpenCV and Google Gemini LLM

## Project Overview

This project is a unique application that combines computer vision, hand tracking, and a generative AI model to solve handwritten math equations. By leveraging OpenCV, the MediaPipe library, and Google Gemini LLM, users can write math equations using hand gestures on a virtual canvas and receive solutions in real time.

### Key Features

- **Hand Tracking:** Detect and track hand gestures using OpenCV and MediaPipe.
- **Interactive Canvas:** Use hand gestures to write and erase math equations on a virtual canvas.
- **AI-powered Solution:** Submit handwritten equations to the Google Gemini LLM for real-time solutions.

### How to Interact with the Application

1. **Write the Equation:** Use your finger to draw the math equation on the canvas.
2. **Submit the Equation:** Raise all four fingers (except the thumb) to send the equation to Google Gemini for solving.
3. **Clear the Canvas:** Raise all five fingers to erase the current canvas and start fresh.

### Dependencies

Before running the code, ensure that you have the following libraries installed:

- `numpy`
- `opencv-python`
- `cvzone`
- `google-generativeai`
- `Pillow`
- `streamlit`

You can install these libraries using pip:

```bash
pip install numpy opencv-python cvzone google-generativeai Pillow streamlit
```
### API Configuration

The application uses Google Gemini for generating content. You will need to configure the API key by replacing the placeholder in the code with your actual API key:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```
Alternatively, you can set the API key as an environment variable and use it in the code.

### Running the Application

To run the application, execute the script using a Python environment that has access to a webcam. The webcam feed will be used for hand tracking, and the virtual canvas will be displayed on your screen.

```bash
python your_script_name.py
```
### Additional Notes

- The application is designed for simplicity and ease of use, providing an intuitive interface for interacting with math problems.
- Ensure your webcam is functioning properly, as the hand tracking module relies on it.
- The project is ideal for educational purposes, demonstrating the integration of computer vision, AI, and interactive interfaces.

![image](https://github.com/user-attachments/assets/6cd36f5c-08f2-44c0-a67d-1056e6542fe5)

### License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code as needed.
