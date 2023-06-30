import streamlit as st
import keytotext
from keytotext import pipeline
Keywords = []
Splited = []
nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")
st.markdown("<h1 style='text-align: center; color: Black;'>Varesh AI</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: Black;'>Sentence Maker</h1>", unsafe_allow_html=True)
st.info("To type the keywords type with comma and space after each comma Example:- Key, Word")
col1, col2, col3 = st.columns(3)

Keywords =  st.text_input("Type the keywords")
Keywords = Keywords.split(",")
Output = nlp(Keywords)

if(st.button("Generate")):
    st.info(Output)

