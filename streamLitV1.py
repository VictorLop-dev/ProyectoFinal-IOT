from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
from threading import Thread
import streamlit as st

# Configura la aplicación Flask
app = Flask(__name__)
CORS(app)

# Configura la conexión a MySQL con PyMySQL
def get_db_connection():
    return pymysql.connect(
        host='autorack.proxy.rlwy.net',  # La URL pública de Railway
        user='root',
        password='QYruqXDRGGyBxlYXXcoMmaTSExlNQYxZ',
        database='railway',
        port=12903,  # Asegúrate de incluir el puerto correcto
        cursorclass=pymysql.cursors.DictCursor  # Opcional: para que las filas sean diccionarios
    )

# Ruta para insertar datos
@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()
    nombre_sensor = data.get('nombre_sensor')
    valor_sensor = data.get('valor_sensor')
    if valor_sensor is None or nombre_sensor is None:
        return jsonify({'error': 'No se proporcionó el nombre o valor del sensor'}), 400

    # Conectar con MySQL e insertar el dato
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO medicinav1 (nombre_sensor, valor) VALUES (%s, %s)", (nombre_sensor, valor_sensor))
        connection.commit()
        connection.close()
        return jsonify({'message': 'Datos insertados correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener datos
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM medicinav1 ORDER BY timestamp DESC LIMIT 100")
            rows = cursor.fetchall()
        connection.close()

        # Formatear los datos en JSON
        data = []
        for row in rows:
            data.append({
                'medicion_num': row['medicion_num'],
                'nombre_sensor': row['nombre_sensor'],
                'valor': row['valor'],
                'timestamp': row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            })
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Función para ejecutar la aplicación Flask en segundo plano
def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

# Ejecuta Flask en un hilo separado
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Código de Streamlit
st.title("Aplicación de Streamlit con API Flask")
st.write("La aplicación Flask está ejecutándose en segundo plano.")

if st.button("Consultar datos"):
    response = requests.get("http://localhost:5000/get_data")
    if response.status_code == 200:
        data = response.json()
        st.write(data)
    else:
        st.error("Error al obtener datos de la API Flask")
