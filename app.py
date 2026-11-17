import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

#hist_button = st.button('Criar histograma') # criar um botão
# criar uma caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um histograma para a coluna odometer')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter: # se a caixa de seleção for selecionada
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão: odometer x price')

    # criar um gráfico de dispersão (quilometragem x preço)
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
