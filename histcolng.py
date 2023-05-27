import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st


def histcolng(pathImage):

  image1=cv2.imread(pathImage,0)
  image2=cv2.imread(pathImage,1)

  histim1=cv2.calcHist([image1],[0],None,[256],[1,256])
  print (histim1)


  r,g,b =cv2.split(image2)
  histim2=cv2.calcHist([r],[0],None,[256],[1,256])
  histim3=cv2.calcHist([g],[0],None,[256],[1,256])
  histim4=cv2.calcHist([b],[0],None,[256],[1,256])

  fig = plt.figure()

  plt.plot(histim2, color='r')
  plt.plot(histim3, color='g')
  plt.plot(histim4, color='b')
  plt.xlim([0,256])
  plt.show()
  st.pyplot(fig)

