import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Configuración inicial de la página
st.set_page_config(page_title="Pokmed App", layout="wide", page_icon="💊")

# CSS para personalización
page_bg = """
<style>
body {
    background-color: #1c1e21;
    color: white;
}
div.stButton > button {
    color: white;
    background-color: #d81b60;
    border: none;
    padding: 10px;
    border-radius: 8px;
    font-size: 16px;
    width: 100%;
}
input {
    font-size: 16px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #d3d3d3;
    width: 100%;
    margin-bottom: 10px;
}
h1 {
    font-size: 24px;
    font-weight: bold;
    color: white;
    text-align: center;
}
.header {
    text-align: center;
    color: white;
    font-size: 36px;
    font-weight: bold;
}
.sub-header {
    text-align: center;
    color: white;
    font-size: 24px;
}
.box {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
    color: white;
}
.status-good {
    color: green;
    font-size: 18px;
    font-weight: bold;
}
.status-bad {
    color: red;
    font-size: 18px;
    font-weight: bold;
}
.info-box {
    background-color: #0d6efd;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    color: white;
}
.alert-box {
    background-color: red;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    color: white;
}
.purple-box {
    background-color: purple;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
    color: white;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Estado inicial de la página
if "page" not in st.session_state:
    st.session_state.page = "login"

# Inicio de sesión
if st.session_state.page == "login":
    st.image("PokMed.jpg", caption="",width=250)
    st.markdown("<h1>¡Bienvenido a Pokmed App!</h1>", unsafe_allow_html=True)

    # Formulario de login
    email = st.text_input("Correo electrónico:", value="josepablo83@email.com")
    password = st.text_input("Contraseña:", value="12345678", type="password")

    # Validación de usuario
    if st.button("Iniciar sesión"):
        if email == "josepablo83@email.com" and password == "12345678":
            st.session_state.page = "home"
            st.rerun()  # Recarga segura tras cambio de página
        else:
            st.error("Correo o contraseña incorrectos.")
    st.markdown("---")
    st.markdown("O continúa con:")
    st.button("Google")
    st.button("Facebook")
    st.button("Apple")

# Dashboard
elif st.session_state.page == "home":
    st.markdown('<div class="header">POKMED</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Bienvenido de vuelta, José Pablo</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown("### Recomendación actual de: **INSULINA**")
        st.markdown('<div class="info-box">Fecha esperada de caducidad: 24/07/25</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">Fecha de apertura: 24/07/25</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<div class="status-good">En buen estado ✅</div>', unsafe_allow_html=True)
        st.markdown('<div class="status-bad">Probable mal estado por: ❌</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<div class="alert-box">Temperatura elevada</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">Temperatura baja</div>', unsafe_allow_html=True)
        st.markdown('<div class="purple-box">Exceso de agitación</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Botón de cierre de sesión
    if st.button("Cerrar sesión"):
        st.session_state.page = "login"
        st.rerun()
def fetch_data(host, user, password, database):
        try:
            # Conexión a la base de datos
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=12903
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM medicinav1 where nombre_sensor in ('DHT22')")
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            connection.close()
            return pd.DataFrame(data, columns=columns)
        except pymysql.MySQLError as e:
            st.error(f"Error al conectar a la base de datos: {e}")
            return pd.DataFrame()

    # Conectar a la base de datos con pymysql
    # @st.cache_data(ttl=600)
    def fetch_data_mov(host, user, password, database):
        try:
            # Conexión a la base de datos
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=12903
            )
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM medicinav1 where nombre_sensor in ('MPU6050')")
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Obtener los nombres de las columnas
            connection.close()
            return pd.DataFrame(data, columns=columns)
        except pymysql.MySQLError as e:
            st.error(f"Error al conectar a la base de datos: {e}")
            return pd.DataFrame()



    # Cargar datos de temperatura
    df = fetch_data(host, user, password, database)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp', ascending=True)
    # Cargar datos de movimiento
    df2 = fetch_data_mov(host, user, password, database)
    if 'timestamp' in df2.columns:
        df2['timestamp'] = pd.to_datetime(df2['timestamp'])
        df2 = df2.sort_values(by='timestamp', ascending=True)

    if df['valor'].iloc[-1] > 26:
        st.subheader("Tu insulina esta en malas condiciones en este momento! La temperatura supera los 26°")
    elif df['valor'].iloc[-1] < 2:
        st.subheader("Tu insulina esta en malas condiciones en este momento! La temperatura esta debajo de 2°")
    else:
        st.subheader("Todo parece bien con tu insulina!")
        

    # Crear la gráfica con puntos y colores personalizados
    fig, ax = plt.subplots()

    # Colores según las condiciones
    for i in range(len(df) - 1):  # Iterar sobre los puntos
        # Determinar el color del punto
        if df['valor'].iloc[i] > 26:  # Ajustar a tus valores
            color = '#FF7F3E'
        elif df['valor'].iloc[i] < 2:
            color = '#4335A7'
        else:
            color = '#80C4E9'

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
        if df['valor'].iloc[i + 1] > 26:
            line_color = '#FF7F3E'
        elif df['valor'].iloc[i + 1] < 2:
            line_color = '#4335A7'
        else:
            line_color = '#80C4E9'

        # Graficar la línea hasta el siguiente punto
        ax.plot(
            [df['timestamp'].iloc[i], df['timestamp'].iloc[i + 1]],
            [df['valor'].iloc[i], df['valor'].iloc[i + 1]],
            color=line_color,
            zorder=2
        )

    # Graficar el último punto
    if df['valor'].iloc[-1] > 29:
        last_color = '#FF7F3E'
    elif df['valor'].iloc[-1] < 26:
        last_color = '#4335A7'
    else:
        last_color = '#80C4E9'

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
    # Lo de abajo en teoria amplia el alcance de la grafica en x, pero hasta ahora no ha hecho falta.
    # ax.set_xlim(df['timestamp'].min() - pd.Timedelta(seconds=5), df['timestamp'].max() + pd.Timedelta(seconds=5))  # Espacio horizontal
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


#GRAFICA 2
 # Crear la gráfica con puntos y colores personalizados
    fig2, ax2 = plt.subplots()

    # Colores según las condiciones
    for i in range(len(df2) - 1):  # Iterar sobre los puntos
        # Determinar el color del punto
        if df2['valor'].iloc[i] > 26:  # Ajustar a tus valores
            color = '#FF7F3E'
        elif df2['valor'].iloc[i] < 2:
            color = '#4335A7'
        else:
            color = '#80C4E9'

        # Graficar el punto
        ax2.scatter(df2['timestamp'].iloc[i], df2['valor'].iloc[i], color=color, zorder=3)

        # Agregar el valor debajo del punto
        ax2.text(
            df2['timestamp'].iloc[i],
            df2['valor'].iloc[i] - 0.25,  # Ajustar el valor para que el texto quede debajo
            f"{df2['valor'].iloc[i]:.1f}",  # Formato con dos decimales
            color='white',
            fontsize=8,
            ha='center'  # Centrar el texto horizontalmente
        )

        # Determinar el color de la línea según el punto al que conecta
        if df2['valor'].iloc[i + 1] > 2:
            line_color = '#FF7F3E'
        else:
            line_color = '#80C4E9'

        # Graficar la línea hasta el siguiente punto
        ax2.plot(
            [df2['timestamp'].iloc[i], df2['timestamp'].iloc[i + 1]],
            [df2['valor'].iloc[i], df2['valor'].iloc[i + 1]],
            color=line_color,
            zorder=2
        )

    # Graficar el último punto
    if df2['valor'].iloc[-1] > 2:
        last_color = '#FF7F3E'
    else:
        last_color = '#80C4E9'

    ax2.scatter(df2['timestamp'].iloc[-1], df2['valor'].iloc[-1], color=last_color, zorder=3)

    # Agregar el valor al último punto
    ax2.text(
        df2['timestamp'].iloc[-1],
        df2['valor'].iloc[-1] - 0.25,  # Ajustar el valor para que el texto quede debajo
        f"{df2['valor'].iloc[-1]:.1f}",  # Formato con dos decimales
        color='white',
        fontsize=8,
        ha='center'
    )
    ax2.set_ylim(df2['valor'].min() - 1, df2['valor'].max() + 1)
    # Lo de abajo en teoria amplia el alcance de la grafica en x, pero hasta ahora no ha hecho falta.
    # ax.set_xlim(df['timestamp'].min() - pd.Timedelta(seconds=5), df['timestamp'].max() + pd.Timedelta(seconds=5))  # Espacio horizontal
    # Ajustes del gráfico
    ax2.set_title('Movimiento de la insulina', color='white')  # Título en blanco para destacar
    ax2.set_xlabel('Tiempo', color='white')  # Etiqueta del eje x en blanco
    ax2.set_ylabel('Temperatura (°C)', color='white')  # Etiqueta del eje y en blanco
    plt.xticks(rotation=45, color='white')  # Rotar etiquetas del eje x y ponerlas en blanco
    plt.yticks(color='white')  # Etiquetas del eje y en blanco

    # Invertir el eje x para que las más recientes estén a la izquierda
    ax2.invert_xaxis()

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig2)

    
    col1, col2=st.columns(2)
    with col1:
        st.subheader("Tabla de Temperaturas")
        st.dataframe(df)
    with col2:
        st.subheader("Tabla de Movimiento")
        st.dataframe(df2)
