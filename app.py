import streamlit as st
import pandas as pd

st.set_page_config(page_title="CIA Country Comparison", page_icon="🔎", layout='wide', initial_sidebar_state="expanded")

st.write('# CIA Country Comparison')
st.markdown('Compare data between two countries based on information from the CIA Factbook')

data = pd.read_csv('data/cia_factbook.csv')

def search(country_name):
    return (data[data['country'] == country_name])

def write_info(country_data, columns):
    # Index(['country', 'area', 'birth_rate', 'death_rate', 'infant_mortality_rate',
    #    'internet_users', 'life_exp_at_birth', 'maternal_mortality_rate',
    #    'net_migration_rate', 'population', 'population_growth_rate'],
    #   dtype='object')
    st.write(f'`Population`: {country_data[columns[9]]}')

def main():
    col1, col2 = st.columns(2)

    with col1:
        country1 = st.selectbox('Select Country #1', data['country'], index=2)
        if country1:
            st.markdown(f'## {country1}')
            x1 = search(country1)
            st.write('Population:', x1['population'].iloc[0])
    with col2:
        country2 = st.selectbox('Select Country #2', data['country'], index=1)
        if country2:
            st.markdown(f'## {country2}')
            st.write(search(country2))
if __name__ == '__main__':
    main()