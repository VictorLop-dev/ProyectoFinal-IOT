import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Pokmed App", layout="wide", page_icon="💊")

# Fondo personalizado con estilo CSS
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

# Manejo de estado de página
if "page" not in st.session_state:
    st.session_state.page = "login"

# Página de Inicio de Sesión
if st.session_state.page == "login":
    st.markdown("<h1>Bienvenidos a Pokmed</h1>", unsafe_allow_html=True)

    # Formulario de inicio de sesión con valores predeterminados
    st.markdown("### Inicia sesión")
    default_email = "ejemplo@email.com"  # Correo predeterminado
    default_password = "12345678"  # Contraseña predeterminada
    email = st.text_input("Correo electrónico:", value=default_email)
    password = st.text_input("Contraseña:", value=default_password, type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        if email == default_email and password == default_password:
            st.session_state.page = "home"
            #st.experimental_rerun()
        else:
            st.error("Correo o contraseña incorrectos.")

    # Opciones de inicio de sesión con servicios externos
    st.markdown("---")
    st.markdown("O continúa con:")
    st.button("Google")
    st.button("Facebook")
    st.button("Apple")

# Página de Inicio (Dashboard)
elif st.session_state.page == "home":
    # Encabezado
    st.markdown('<div class="header">POKMED</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Bienvenido de vuelta, José Pablo</div>', unsafe_allow_html=True)

    # Diseño del dashboard
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

    # Botón para cerrar sesión
    if st.button("Cerrar sesión"):
        st.session_state.page = "login"
        st.experimental_rerun()
