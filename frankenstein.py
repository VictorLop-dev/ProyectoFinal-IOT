import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Inicio de Sesión", layout="centered")

# Fondo personalizado con estilo
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
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Contenido principal
st.markdown("<h1>Bienvenidos a Mi Aplicación</h1>", unsafe_allow_html=True)

# Formulario de inicio de sesión
st.markdown("### Inicia sesión")
email = st.text_input("Correo electrónico:", value="jospablo1895@gmail.com")
password = st.text_input("Contraseña:", value="contraseña", type="password")

st.button("Iniciar sesión")

# Opciones de inicio de sesión con servicios externos
st.markdown("---")
st.markdown("O continúa con:")
st.button("Google")
st.button("Facebook")
st.button("Apple")

