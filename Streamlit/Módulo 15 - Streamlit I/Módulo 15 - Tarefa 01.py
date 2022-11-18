# Imports

import streamlit as st
import numpy as np
import pandas as pd

# st.title

st.title('Uber pickups in NYC')

st.write('----')

# Nomenado variáveis

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Criando uma função

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Imprimindo texto na tela

data_load_state = st.text('Loading data...')

# Utilizando a função

data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

st.write('----')

# st.checkbox

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.write('----')

# Histogram / st.bar_chart

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.write('----')

# st.map e st.slider

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
