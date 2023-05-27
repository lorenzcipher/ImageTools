import streamlit as st
from PIL import Image
from io import BytesIO
import egalisation as histEgalisation
import histcol 
import histcolng

st.set_page_config(layout="wide", page_title="Image Tools Analyser")

st.write("## Tools Image")
st.write(
    "The project aims to develop advanced imaging tools for histogram analysis and image segmentation. These tools will provide robust and efficient methods to analyze image data, extract meaningful information, and facilitate accurate segmentation of objects or regions of interest within the images."
)
st.sidebar.write("## Upload and download :gear:")




my_upload = st.sidebar.file_uploader("Upload first image", type=["png", "jpg", "jpeg"])

if my_upload is not None :
    
    tab1,tab2,tab3,tab4 = st.tabs(["🗃 Image","📈 Histograme Egaliser", "📈 Histogramme colonnes","📈 Histogramme colonnes lignes"])

    tab1.subheader("Image Utiliser")
    tab1.image(my_upload)

    tab2.subheader("📈 Histograme Egaliser")
    tab2.write(histEgalisation.egalisationImage(my_upload.name))
    
    tab3.subheader("📈 Histogramme colonnes")
    tab3.write(histcol.histcol(my_upload.name))

    tab4.subheader("📈 Histogramme colonnes lignes")
    tab4.write(histcolng.histcolng(my_upload.name))
     
       

  





