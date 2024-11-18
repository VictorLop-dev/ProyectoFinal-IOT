#Aquí estará todo el código que permitirá conectarse con SQL y mostrar las gráficas.
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Configura la URL de tu servidor Flask
URL = 'http://127.0.0.1:5000/get_data'

# Realizar una solicitud GET a la API Flask
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()

    # Crear un DataFrame de pandas
    df = pd.DataFrame(data)
    
    # Convertir la columna 'timestamp' a formato datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Crear un mapa de colores basado en los valores del sensor
    # Normalizamos los valores de los sensores para crear una escala de colores
    norm = plt.Normalize(df['valor'].min(), df['valor'].max())  # Normaliza el rango de valores
    cmap = plt.cm.viridis  # Elige el mapa de colores (puedes probar otros como 'plasma', 'inferno', etc.)
    
    # Asignar colores a los puntos en función del valor del sensor
    colors = cmap(norm(df['valor']))

    # Crear la gráfica
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['timestamp'], df['valor'], c=colors, cmap=cmap)

    # Etiquetas y título
    ax.set_xlabel('Fecha y Hora')
    ax.set_ylabel('Valor del Sensor')
    ax.set_title('Gráfica de Puntos - Sensor')

    # Añadir una barra de color
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Valor del Sensor')

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
else:
    st.error("Error al obtener los datos del servidor.")
