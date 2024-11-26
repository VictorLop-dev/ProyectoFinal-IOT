import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Pokmed App", layout="centered", page_icon="💊")

# CSS personalizado para estilizar la página
def load_custom_css():
    css = """
    <style>
    body {
        background-color: #f3f4f6;
        color: #333;
        font-family: Arial, sans-serif;
    }
    .stButton > button {
        background-color: #e60023;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
    }
    .stTextInput > div > input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
        width: 100%;
        margin-bottom: 15px;
    }
    h1 {
        font-size: 28px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .login-container {
        background-color: #fff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 400px;
        margin: 0 auto;
    }
    .dashboard-container {
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }
    .card {
        background-color: white;
        border: 1px solid #eaeaea;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
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
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Carga el CSS al inicio
load_custom_css()

# Estado inicial de la página
if "page" not in st.session_state:
    st.session_state.page = "login"

# Inicio de sesión
if st.session_state.page == "login":
    st.markdown("<h1>Bienvenidos a Pokmed</h1>", unsafe_allow_html=True)
    with st.container():
        with st.form("login_form", clear_on_submit=False):
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            email = st.text_input("Correo electrónico:")
            password = st.text_input("Contraseña:", type="password")
            login_button = st.form_submit_button("Iniciar sesión")
            st.markdown('</div>', unsafe_allow_html=True)

            # Validación de usuario
            if login_button:
                if email == "josepablo83@email.com" and password == "12345678":
                    st.session_state.page = "home"
                    st.experimental_rerun()
                else:
                    st.error("Correo o contraseña incorrectos.")

# Dashboard
elif st.session_state.page == "home":
    st.markdown('<h1>POKMED</h1>', unsafe_allow_html=True)
    st.markdown('<h3>Bienvenido de vuelta, José Pablo</h3>', unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("INSULINA")
            st.write("Fecha de apertura: 24/07/25")
            st.write("Fecha de caducidad: 24/07/25")
            st.markdown('<span class="status-good">En buen estado ✅</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Estado")
            st.markdown('<span class="status-bad">Temperatura elevada ❌</span>', unsafe_allow_html=True)
            st.markdown('<span class="status-good">Temperatura baja ✅</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Alerta")
            st.markdown('<span class="status-bad">Exceso de agitación ❌</span>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Cerrar sesión"):
        st.session_state.page = "login"
        st.experimental_rerun()
