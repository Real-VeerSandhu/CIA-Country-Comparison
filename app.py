import streamlit as st
import pandas as pd

st.set_page_config(page_title="CIA Country Comparison", page_icon="🔎", layout='wide', initial_sidebar_state="expanded")

st.write('# CIA Country Comparison')
st.markdown('Compare data between two countries based on information from the CIA Factbook')

data = pd.read_csv('data/cia_factbook.csv')


col1, col2 = st.columns(2)

with col1:
    country1 = st.selectbox('Select Country #1', data['country'])
    if country1:
        st.markdown(f'## {country1}')

with col2:
    country2 = st.selectbox('Select Country #2', data['country'])
    if country1:
        st.markdown(f'## {country1}')
