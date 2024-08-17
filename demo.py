import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from PIL import Image
import streamlit as st

st.set_page_config(layout='wide')
st.title("Math Problem Solver based on OpenCV and LLM (Google Gemini) ✨")
st.write("""
    This project is based on the MediaPipe library, OpenCV, and generative.ai. 
    You can write a math equation on canvas using one finger and send it to the LLM Gemini to receive a response.
    \n🚀How do I interact with the project:
    \n 1- Use your finger to write the math equation.
    \n 2- To send the input to Gemini, raise all the fourth fingers.
    \n 3- To erase the canvas, raise all five fingers.
""")

column1, column2 = st.columns([2, 1])
with column1:
    frameWindow = st.image([])
with column2:
    st.title("Answer")
    outputText = st.subheader("")

genai.configure(api_key="AIzaSyD-v56sfw_iH0vNJlqLR9fEMAJHNGhiPf4")
#genai.configure(api_key=os.environ["AIzaSyD-v56sfw_iH0vNJlqLR9fEMAJHNGhiPf4"])
model = genai.GenerativeModel('gemini-1.0-pro-latest')

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        fingers = detector.fingersUp(hand1)
        return fingers, lmList
    return None

def draw(info, previousPosition, canvas):
    fingers, lmlist = info
    currentPosition = None
    if fingers == [0, 1, 0, 0, 0]:
        currentPosition = lmlist[8][0:2]
        if previousPosition is None:
            previousPosition = currentPosition
        cv2.line(canvas, currentPosition, previousPosition, (255, 0, 255), 10)
    elif fingers == [1, 1, 1, 1, 1]:
        canvas = np.zeros_like(img)
    return currentPosition, canvas

def sendToGemini(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["solve this math problem", pil_image])
        return response.text
    return ""

previousPosition = None
canvas = None
combinedImage = None
outputResult = ""

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img)
        combinedImage = img.copy()
    info = getHandInfo(img)
    if info:
        fingers, lmlist = info
        previousPosition, canvas = draw(info, previousPosition, canvas)
        outputResult = sendToGemini(model, canvas, fingers)
    combinedImage = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    frameWindow.image(combinedImage, channels="BGR")
    if outputResult:
        outputText.text(outputResult)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()