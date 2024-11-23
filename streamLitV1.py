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


    # Procesar y mostrar los datos
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp', ascending=True)

    st.subheader("Tabla de datos")
    st.dataframe(df)

    # Visualización de los datos
    if 'timestamp' in df.columns and 'valor' in df.columns:
        fig, ax = plt.subplots()

        # Colores según las condiciones
        for i in range(len(df) - 1):
            if df['valor'].iloc[i] > 29:
                color = 'red'
            elif df['valor'].iloc[i] < 26:
                color = 'blue'
            else:
                color = 'green'

            ax.scatter(df['timestamp'].iloc[i], df['valor'].iloc[i], color=color, zorder=3)
            ax.text(
                df['timestamp'].iloc[i],
                df['valor'].iloc[i] - 0.25,
                f"{df['valor'].iloc[i]:1f}",
                color='white',
                fontsize=8,
                ha='center'
            )

            if df['valor'].iloc[i + 1] > 29:
                line_color = 'red'
            elif df['valor'].iloc[i + 1] < 26:
                line_color = 'blue'
            else:
                line_color = 'green'

            ax.plot(
                [df['timestamp'].iloc[i], df['timestamp'].iloc[i + 1]],
                [df['valor'].iloc[i], df['valor'].iloc[i + 1]],
                color=line_color,
                zorder=2
            )

        # Último punto
        if df['valor'].iloc[-1] > 29:
            last_color = 'red'
        elif df['valor'].iloc[-1] < 26:
            last_color = 'blue'
        else:
            last_color = 'green'

        ax.scatter(df['timestamp'].iloc[-1], df['valor'].iloc[-1], color=last_color, zorder=3)
        ax.text(
            df['timestamp'].iloc[-1],
            df['valor'].iloc[-1] - 0.25,
            f"{df['valor'].iloc[-1]:.1f}",
            color='white',
            fontsize=8,
            ha='center'
        )

        ax.set_title('Temperatura de la insulina', color='white')
        ax.set_xlabel('Tiempo', color='white')
        ax.set_ylabel('Temperatura (°C)', color='white')
        plt.xticks(rotation=45, color='white')
        plt.yticks(color='white')
        ax.set_ylim(df['valor'].min() - 1, df['valor'].max() + 1)
        ax.invert_xaxis()

        st.pyplot(fig)
    else:
        st.warning("La tabla no tiene las columnas necesarias ('timestamp' y 'valor').")

