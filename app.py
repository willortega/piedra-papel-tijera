import random
import streamlit as st

# 1. Configuración de la página (Debe ser lo primero)
st.set_page_config(
    page_title="Piedra, Papel o Tijera | Enterprise Edition",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Inyección de estilos CSS avanzados para un look profesional y moderno
st.markdown(
    """
    <style>
    /* Estilo general del fondo y tipografía */
    .stApp {
        background-color: #0e1117;
        color: #f0f2f6;
    }
    
    /* Títulos principales con gradiente */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding-bottom: 10px;
    }

    /* Tarjetas de contenedores elegantes */
    .css-1r6slb0, .stContainer {
        border-radius: 12px;
        border: 1px solid #262730;
        padding: 20px;
        background-color: #161b22;
    }

    /* Estilo de los botones de selección */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 1px solid #30363d;
    }
    .stButton>button:hover {
        border-color: #58a6ff;
        box-shadow: 0 0 10px rgba(88, 166, 255, 0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Encabezado de Ingeniería
st.markdown(
    "<h1>⚡ Rock-Paper-Scissors Engine</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #8b949e;'>Sistema interactivo de toma de decisiones estocásticas y lógica de estados finitos.</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# 4. Inicialización del Estado de Sesión (Session State)
if "puntos_usuario" not in st.session_state:
    st.session_state.puntos_usuario = 0
if "puntos_maquina" not in st.session_state:
    st.session_state.puntos_maquina = 0
if "empates" not in st.session_state:
    st.session_state.empates = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

opciones = ["Piedra", "Papel", "Tijera"]
emojis = {"Piedra": "✊", "Papel": "✋", "Tijera": "✌️"}

# 5. Panel de Control / Interfaz de Usuario (Botones)
st.markdown("### 🕹️ Consola de Comandos")
col1, col2, col3 = st.columns(3)

eleccion_usuario = None

with col1:
    if st.button("✊ Piedra", use_container_width=True):
        eleccion_usuario = "Piedra"
with col2:
    if st.button("✋ Papel", use_container_width=True):
        eleccion_usuario = "Papel"
with col3:
    if st.button("✌️ Tijera", use_container_width=True):
        eleccion_usuario = "Tijera"

# 6. Lógica del Algoritmo del Juego
if eleccion_usuario:
    # Generación de la opción de la máquina (modelo aleatorio uniforme)
    eleccion_maquina = random.choice(opciones)

    # Evaluación de resultados
    if eleccion_usuario == eleccion_maquina:
        resultado = "Empate"
        st.session_state.empates += 1
        mensaje_color = "info"
        audio_tag = '<audio src="https://www.myinstants.com/media/sounds/blip.mp3" autoplay></audio>'
    elif (
        (eleccion_usuario == "Piedra" and eleccion_maquina == "Tijera")
        or (eleccion_usuario == "Papel" and eleccion_maquina == "Piedra")
        or (eleccion_usuario == "Tijera" and eleccion_maquina == "Papel")
    ):
        resultado = "Victoria"
        st.session_state.puntos_usuario += 1
        mensaje_color = "success"
        audio_tag = '<audio src="https://www.myinstants.com/media/sounds/tada.mp3" autoplay></audio>'
        # Efecto de confeti profesional para la victoria
        st.balloons()
    else:
        resultado = "Derrota"
        st.session_state.puntos_maquina += 1
        mensaje_color = "error"
        audio_tag = '<audio src="https://www.myinstants.com/media/sounds/erro.mp3" autoplay></audio>'

    # Registrar en el historial de la sesión
    st.session_state.historial.insert(
        0,
        {
            "user": eleccion_usuario,
            "machine": eleccion_maquina,
            "result": resultado,
        },
    )

    # Reproducción de efectos de audio invisibles
    st.markdown(audio_tag, unsafe_allow_html=True)

    # Visualización de la partida actual en contenedores simétricos
    st.markdown("### 📊 Resultado del Ciclo Actual")
    res_col1, res_col2 = st.columns(2)

    with res_col1:
        st.markdown(
            f"""
            <div style="background-color: #21262d; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="color: #8b949e; margin: 0;">USER INPUT</p>
                <h2>{emojis[eleccion_usuario]} {eleccion_usuario}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with res_col2:
        st.markdown(
            f"""
            <div style="background-color: #21262d; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="color: #8b949e; margin: 0;">MACHINE OUTPUT</p>
                <h2>{emojis[eleccion_maquina]} {eleccion_maquina}</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Alerta contextual basada en el resultado
    if resultado == "Empate":
        st.info("⚖️ **Estado:** Resultado neutral (Empate técnico).")
    elif resultado == "Victoria":
        st.success("✅ **Estado:** Ejecución exitosa (¡Victoria del usuario!).")
    else:
        st.error(
            "⚠️ **Estado:** Excepción detectada (La máquina superó la lógica)."
        )

# 7. Panel de Métricas / Dashboard de Rendimiento
st.markdown("---")
st.markdown("### 📈 Dashboard de Rendimiento")

m1, m2, m3, m4 = st.columns(4)
total_partidas = (
    st.session_state.puntos_usuario
    + st.session_state.puntos_maquina
    + st.session_state.empates
)
win_rate = (
    (st.session_state.puntos_usuario / total_partidas * 100)
    if total_partidas > 0
    else 0.0
)

m1.metric("Victorias", st.session_state.puntos_usuario)
m2.metric("Derrotas", st.session_state.puntos_maquina)
m3.metric("Empates", st.session_state.empates)
m4.metric("Win Rate", f"{win_rate:.1f}%")

# 8. Controles de gestión de estado
col_reset, col_space = st.columns([1, 3])
with col_reset:
    if st.button("🔄 Resetear Sistema"):
        st.session_state.puntos_usuario = 0
        st.session_state.puntos_maquina = 0
        st.session_state.empates = 0
        st.session_state.historial = []
        st.rerun()

# 9. Sección de Logs / Historial de Operaciones
if st.session_state.historial:
    with st.expander("🔍 Ver Logs de Auditoría (Historial de Partidas)"):
        for i, h in enumerate(st.session_state.historial[:5]):  # Mostrar los últimos 5
            st.text(
                f"[{i+1}] Usuario: {h['user']} | Máquina: {h['machine']} ---> Resultado: {h['result']}"
            )
