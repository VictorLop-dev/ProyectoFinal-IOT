import pymysql
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title('Visualización de datos de sensores')


host = "autorack.proxy.rlwy.net"
user = "root"
password = "QYruqXDRGGyBxlYXXcoMmaTSExlNQYxZ"
database = "railway"

# Conectar a la base de datos con pymysql
@st.cache_data(ttl=600)
def fetch_data(host, user, password, database):
    try:
        # Conexión a la base de datos
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port = 12903
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM medicinav1")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
        connection.close()
        return pd.DataFrame(data, columns=columns)
    except pymysql.MySQLError as e:
        st.error(f"Error al conectar a la base de datos: {e}")
        return pd.DataFrame()

# Cargar datos
df = fetch_data(host, user, password, database)
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp', ascending=True)

st.subheader("Tabla de datos")
st.dataframe(df)


