import cv2
import numpy as np
import streamlit as st

def contours(pathImage):
    image = cv2.imread(pathImage, 0)

    bin = np.zeros(image.shape, np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > 90:
                bin[i, j] = 255

    contours = []
    for i in range(1, bin.shape[0] - 1):
        for j in range(1, bin.shape[1] - 1):
            if bin[i, j] == 255:
                if bin[i - 1, j] == 0 or bin[i + 1, j] == 0 or bin[i, j - 1] == 0 or bin[i, j + 1] == 0:
                    contours.append([(j, i)])

    mask = np.zeros(image.shape[:2], dtype="uint8")
    for contour in contours:
        cv2.drawContours(mask, [np.array(contour)], -1, 255, -1)

    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    # Display the segmented image using Streamlit
    st.image(segmented_image, channels="GRAY")

