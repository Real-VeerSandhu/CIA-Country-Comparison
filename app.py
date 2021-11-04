import streamlit as st
import pandas as pd

st.set_page_config(page_title="CIA Country Comparison", page_icon="🔎", layout='wide', initial_sidebar_state="expanded")

st.write('# CIA Country Comparison')
st.markdown('Compare data between countries based on information from the CIA Factbook')

data = pd.read_csv('data/cia_factbook.csv')

def search(country_name):
    return (data[data['country'] == country_name])

def write_info(country_data, columns):
    st.write(f'**Population**: `{country_data[columns[9]].iloc[0]}`')
    st.write(f'**Population Density (people per km²)**: `{int(country_data[columns[9]].iloc[0] / country_data[columns[1]].iloc[0])}`')
    st.write(f'**Population Growth Rate**: `{country_data[columns[10]].iloc[0]}`')
    st.write(f'**Migration Rate (per 1,000)**: `{country_data[columns[8]].iloc[0]}`')
    st.write(f'**Birth Rate**: `{country_data[columns[2]].iloc[0]}`')
    st.write(f'**Death Rate**: `{country_data[columns[3]].iloc[0]}`')
    st.write(f'**Life Expectancy**: `{country_data[columns[6]].iloc[0]}`')

def main():
    col1, col2 = st.columns(2)

    with col1:
        country1 = st.selectbox('Select Country #1', data['country'], index=2)
        if country1:
            st.markdown(f'## {country1}')
            st.markdown('----')
            data_country1 = search(country1)
            write_info(data_country1, data_country1.columns)
    with col2:
        country2 = st.selectbox('Select Country #2', data['country'], index=1)
        if country2:
            st.markdown(f'## {country2}')
            st.markdown('----')
            data_country2 = search(country2)
            write_info(data_country2, data_country2.columns)
if __name__ == '__main__':
    main()