import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def translation(pathImage,ecart):

  #chargement de l'image
  img = cv2.imread(pathImage,0)
  h,w = img.shape
  nb_pixels = h*w

  #creation du premier histogramme
  H1 = np.zeros((256,1),np.uint32)
  for i in range(h):
      for j in range(w): 
          H1[img[i,j]]+=1
          
  img_res = img-ecart

  #affichage des deux images
  st.image(img_res)

