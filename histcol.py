import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st

def histcol(pathImage):
  image=cv2.imread(pathImage, 0)
  hist1=cv2.calcHist([image],[0],None,[256],[0,256])
  h,w=image.shape
  for i in range(h):
      for j in range(w):
          if image[i,j]>100 and image[i,j]<256:
              image[i,j]=77

  hist2=cv2.calcHist([image],[0],None,[256],[0,256])
  fig = plt.figure()
  plt.plot(hist2, color='r')
  plt.plot(hist1, color='g')
  plt.xlim([0,256])
  st.pyplot(fig)