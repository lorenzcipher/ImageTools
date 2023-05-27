import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st



def egalisationImage(pathImage):
  # Chargement de l'image en niveau de gris
  image = cv2.imread(pathImage, 0)

  # Vérification si le chargement de l'image a échoué
  if image is None:
      print("Erreur: Impossible de charger l'image.")
      exit()

  # Application de la transformation d'égalisation à l'image
  image_equalized = cv2.equalizeHist(image)

  # Calcul de l'histogramme de l'image égalisée
  hist_equalized, bins_equalized = np.histogram(image_equalized.flatten(), 256, [0, 256])

  # Affichage de l'histogramme de l'image égalisée
  fig = plt.figure()
  plt.plot(hist_equalized, color='black')
  plt.xlabel('Niveau de gris')
  plt.ylabel('Fréquence')
  plt.title("Histogramme de l'image égalisée")
  plt.show()
  st.pyplot(fig)