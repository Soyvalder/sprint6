import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis Exploratorio de Datos")

# Cargar tus datos
    
data = pd.read_csv('/home/v4ld3rtest/sprint6')

# Mostrar los datos
st.write(data)

# Crear un gráfico simple
fig = px.scatter(data, x='columna_x', y='columna_y', title='Gráfico de Dispersión')
st.plotly_chart(fig)