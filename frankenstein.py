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

# Establecer una página actual usando session_state
if "page" not in st.session_state:
    st.session_state.page = "login"

# Página de Inicio de Sesión
if st.session_state.page == "login":
    st.markdown("<h1>Bienvenidos a Mi Aplicación</h1>", unsafe_allow_html=True)

    # Formulario de inicio de sesión con valores predeterminados
    st.markdown("### Inicia sesión")
    default_email = "ejemplo@email.com"  # Correo predeterminado
    default_password = "12345678"  # Contraseña predeterminada
    email = st.text_input("Correo electrónico:", value=default_email)
    password = st.text_input("Contraseña:", value=default_password, type="password")

    # Botón de iniciar sesión
    if st.button("Iniciar sesión"):
        # Validar credenciales (opcional)
        if email == default_email and password == default_password:
            # Cambiar a la página siguiente
            st.session_state.page = "home"
            st.experimental_rerun()
        else:
            st.error("Correo o contraseña incorrectos.")

    # Opciones de inicio de sesión con servicios externos
    st.markdown("---")
    st.markdown("O continúa con:")
    st.button("Google")
    st.button("Facebook")
    st.button("Apple")

# Página de inicio tras iniciar sesión
elif st.session_state.page == "home":
    st.markdown("<h1>Página Principal</h1>", unsafe_allow_html=True)
    st.markdown("¡Bienvenido! Has iniciado sesión con éxito.")
    if st.button("Cerrar sesión"):
        st.session_state.page = "login"
        st.experimental_rerun()
