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
#@st.cache_data(ttl=600)
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


plt.style.use('dark_background')  # Activa el modo oscuro

# Crear la gráfica con puntos y colores personalizados
fig, ax = plt.subplots()

# Colores según las condiciones
for i in range(len(df) - 1):  # Iterar sobre los puntos
    # Determinar el color del punto
    if df['valor'].iloc[i] > 29:  # Ajustar a tus valores
        color = 'red'
    elif df['valor'].iloc[i] < 26:
        color = 'blue'
    else:
        color = 'green'

    # Graficar el punto
    ax.scatter(df['timestamp'].iloc[i], df['valor'].iloc[i], color=color, zorder=3)

    # Agregar el valor debajo del punto
    ax.text(
        df['timestamp'].iloc[i],
        df['valor'].iloc[i] - 0.25,  # Ajustar el valor para que el texto quede debajo
        f"{df['valor'].iloc[i]:.1f}",  # Formato con dos decimales
        color='white',
        fontsize=8,
        ha='center'  # Centrar el texto horizontalmente
    )

    # Determinar el color de la línea según el punto al que conecta
    if df['valor'].iloc[i + 1] > 29:
        line_color = 'red'
    elif df['valor'].iloc[i + 1] < 26:
        line_color = 'blue'
    else:
        line_color = 'green'

    # Graficar la línea hasta el siguiente punto
    ax.plot(
        [df['timestamp'].iloc[i], df['timestamp'].iloc[i + 1]],
        [df['valor'].iloc[i], df['valor'].iloc[i + 1]],
        color=line_color,
        zorder=2
    )

# Graficar el último punto
if df['valor'].iloc[-1] > 29:
    last_color = 'red'
elif df['valor'].iloc[-1] < 26:
    last_color = 'blue'
else:
    last_color = 'green'

ax.scatter(df['timestamp'].iloc[-1], df['valor'].iloc[-1], color=last_color, zorder=3)

# Agregar el valor al último punto
ax.text(
    df['timestamp'].iloc[-1],
    df['valor'].iloc[-1] - 0.25,  # Ajustar el valor para que el texto quede debajo
    f"{df['valor'].iloc[-1]:.1f}",  # Formato con dos decimales
    color='white',
    fontsize=8,
    ha='center'
)
ax.set_ylim(df['valor'].min() - 1, df['valor'].max() + 1)
#Lo de abajo en teoria amplia el alcance de la grafica en x, pero hasta ahora no ha hecho falta.
#ax.set_xlim(df['timestamp'].min() - pd.Timedelta(seconds=5), df['timestamp'].max() + pd.Timedelta(seconds=5))  # Espacio horizontal
# Ajustes del gráfico
ax.set_title('Temperatura de la insulina', color='white')  # Título en blanco para destacar
ax.set_xlabel('Tiempo', color='white')  # Etiqueta del eje x en blanco
ax.set_ylabel('Temperatura (°C)', color='white')  # Etiqueta del eje y en blanco
plt.xticks(rotation=45, color='white')  # Rotar etiquetas del eje x y ponerlas en blanco
plt.yticks(color='white')  # Etiquetas del eje y en blanco

# Invertir el eje x para que las más recientes estén a la izquierda
ax.invert_xaxis()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)




