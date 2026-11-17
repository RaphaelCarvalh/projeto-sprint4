import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análise de Anúncios de Venda de Veículos')
st.write('Use as caixas de seleção abaixo para explorar os dados de anúncios de carros nos EUA.')

#hist_button = st.button('Criar histograma') # criar um botão
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: 
    st.write('Criando um histograma para a coluna odometer')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter: 
    st.write('Criando um gráfico de dispersão: odometer x price')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
