import streamlit as st
from PIL import Image
from io import BytesIO
import egalisation as histEgalisation
import histcol 
import histcolng
import contoures as cont
import translation as trans

st.set_page_config(layout="wide", page_title="Image Tools Analyser")

st.write("## Tools Image")
st.write(
    "The project aims to develop advanced imaging tools for histogram analysis and image segmentation. These tools will provide robust and efficient methods to analyze image data, extract meaningful information, and facilitate accurate segmentation of objects or regions of interest within the images."
)
st.sidebar.write("## Upload and download :gear:")




my_upload = st.sidebar.file_uploader("Upload first image", type=["png", "jpg", "jpeg"])

if my_upload is not None :
    
    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["🖼️ Image","📈 Histograme Egaliser", "📈 Histogramme cumulé","📈 Histogramme cumulé égaliser","Segmentation","Translation"])

    
    with tab1:

        st.subheader(" 🖼️ Image Utiliser")
        st.image(my_upload)

    with tab2 :
        st.subheader("📈 Histograme Egaliser")
        st.write(histEgalisation.egalisationImage(my_upload.name))
    
    with tab3 :
        st.subheader("📈 Histogramme cumulé")
        st.write(histcol.histcol(my_upload.name))

    with tab4 :
        st.subheader("📈 Histogramme cumulé égaliser")
        st.write(histcolng.histcolng(my_upload.name))
    
    
    with tab5 :
        st.subheader("Sgementation")
        cont.contours(my_upload.name)
    

    with tab6 :
        st.subheader("Translation")
        ecart =  st.sidebar.slider("Ecart de la translation",0,255,1)
        st.write(trans.translation(my_upload.name,ecart))
       
   





