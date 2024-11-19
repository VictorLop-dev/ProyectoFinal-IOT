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
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ajusta 'tiempo' al nombre real de tu columna de tiempo
df = df.sort_values(by='timestamp', ascending=False)  # Ordenar de más reciente a más antigua

# Mostrar los datos en Streamlit
st.dataframe(df)

# Crear la gráfica
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['valor'], marker='o', linestyle='-', color='b')  # Ajusta 'temperatura' al nombre real
ax.set_title('Temperatura en función del tiempo')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Temperatura (°C)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visibilidad

# Invertir el eje x para que las más recientes estén a la izquierda
ax.invert_xaxis()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Cerrar conexión a la base de datos
connection.close()
