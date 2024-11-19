import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tu_contraseña',
    database='finalv1'
)
print('Connected')

cursor = connection.cursor()

# Consulta de datos
cursor.execute("SELECT * FROM medicinav1")
data = cursor.fetchall()
columns = cursor.column_names  # Obtener los nombres de las columnas
print(data)

# Mostrar título en Streamlit
st.title('Lecturas del sensor')

# Crear un DataFrame con los datos
df = pd.DataFrame(data, columns=columns)

# Asegurarse de que la columna de tiempo sea datetime y ordenar por tiempo
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ajusta 'timestamp' al nombre real de tu columna de tiempo
df = df.sort_values(by='timestamp', ascending=True)  # Ordenar de más antigua a más reciente

# Mostrar los datos en Streamlit
st.dataframe(df)

# Crear la gráfica con puntos y colores personalizados
plt.style.use('dark_background')
fig, ax = plt.subplots()

# Colores según las condiciones (Configurado solo para pruebas, no para uso final)
for i in range(len(df) - 1):  # Iterar sobre los puntos
    # Determinar el color del punto
    if df['valor'].iloc[i] > 29 :
        #24.5
        color = 'red'
    elif  df['valor'].iloc[i] < 26:
        #2.5
        color = 'blue'
    else:
        color = 'green'

    # Graficar el punto
    ax.scatter(df['timestamp'].iloc[i], df['valor'].iloc[i], color=color, zorder=3)

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
if df['valor'].iloc[i] > 29 :
        #24.5
    last_color = 'red'
elif  df['valor'].iloc[i] < 26:
        #2.5
    last_color = 'blue'
else:
    last_color = 'green'

ax.scatter(df['timestamp'].iloc[-1], df['valor'].iloc[-1], color=last_color, zorder=3)

# Ajustes del gráfico
ax.set_title('Temperatura de la insulina')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Temperatura (°C)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visibilidad

# Invertir el eje x para que las más recientes estén a la izquierda
ax.invert_xaxis()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Cerrar conexión a la base de datos
connection.close()
