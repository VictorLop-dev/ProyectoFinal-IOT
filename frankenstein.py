import streamlit as st
from PIL import Image
# Configuración inicial de la página
st.set_page_config(page_title="PokMed App", layout="wide", page_icon="💊")

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
bg_image = "fondo.jpg"
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("{bg_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
#st.markdown("PokMed.jpg", caption="",width=200)

# Estado inicial de la página
if "page" not in st.session_state:
    st.session_state.page = "login"
    
# Inicio de sesión
if st.session_state.page == "login":
   uno,dos,tres,cuatro,cinco,seis,siete = st.columns(7)
   with cinco:
    st.image("PokMed.jpg", caption="",width=250)
    st.markdown("<h1>¡Bienvenido a PokMed App!</h1>", unsafe_allow_html=True)
    
    

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
        st.markdown('<div class="info-box">Fecha de caducidad: 24/07/25</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="info-box">Fecha de apertura: 24/07/25</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<div class="status-good">En buen estado ✅</div>', unsafe_allow_html=True)
        st.markdown('<div class="status-bad">Probable mal estado por: ❌</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="alert-box">Temperatura elevada</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="info-box">Temperatura baja</div>', unsafe_allow_html=True)
        st.write("")
        st.markdown('<div class="purple-box">Exceso de agitación</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Botón de cierre de sesión
    if st.button("Cerrar sesión"):
        st.session_state.page = "login"
        st.rerun()
