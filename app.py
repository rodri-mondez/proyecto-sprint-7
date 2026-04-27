{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import plotly.express as px\
import streamlit as st\
\
# Leer los datos\
car_data = pd.read_csv('vehicles_us.csv') \
\
# Encabezado de la p\'e1gina\
st.header('An\'e1lisis de Anuncios de Veh\'edculos')\
\
# Crear un bot\'f3n para el histograma\
hist_button = st.button('Construir histograma')\
\
if hist_button: # al hacer clic en el bot\'f3n\
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches')\
    \
    # Crear el histograma\
    fig = px.histogram(car_data, x="odometer")\
    \
    # Mostrar el gr\'e1fico interactivo\
    st.plotly_chart(fig, use_container_width=True)\
\
# EXTRA: Puedes a\'f1adir un checkbox para un gr\'e1fico de dispersi\'f3n\
build_scatter = st.checkbox('Construir un gr\'e1fico de dispersi\'f3n')\
\
if build_scatter:\
    st.write('Creando gr\'e1fico de dispersi\'f3n: Od\'f3metro vs Precio')\
    fig_scatter = px.scatter(car_data, x="odometer", y="price")\
    st.plotly_chart(fig_scatter, use_container_width=True)}