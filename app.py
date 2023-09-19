import streamlit as st 
from lib.utils import run

st.set_page_config(page_title='Anime StyleGAN Generator', layout="wide")
st.header(":hand: Welcome To Anime StyleGAN Generator  ")
n_samples = st.number_input("Enter the number of samples you want to generate :" ,
                             min_value=1 , max_value=30)
img_name = st.text_input("Enter the save Image name :  ")

if st.button("Start generating") : 
    with st.spinner("In progress...") : 
        run(n_samples ,img_name)
        st.image(f"{img_name}.png")