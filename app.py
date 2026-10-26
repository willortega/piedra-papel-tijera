import random
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Piedra, Papel o Tijera", page_icon="🎮", layout="centered"
)

st.title("🎮 Piedra, Papel o Tijera con Sonido")
st.write(
    "¡Juega contra la computadora y escucha los efectos en cada ronda!"
)

# Inicializar el estado de la sesión para el marcador
if "puntos_usuario" not in st.session_state:
    st.session_state.puntos_usuario = 0
if "puntos_maquina" not in st.session_state:
    st.session_state.puntos_maquina = 0
if "empates" not in st.session_state:
    st.session_state.empates = 0

opciones = ["Piedra", "Papel", "Tijera"]
emojis = {"Piedra": "✊", "Papel": "✋", "Tijera": "✌️"}

# Botones de selección
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

# Lógica del juego
if eleccion_usuario:
    eleccion_maquina = random.choice(opciones)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Tú elegiste:")
        st.markdown(
            f"### {emojis[eleccion_usuario]} {eleccion_usuario}"
        )

    with c2:
        st.subheader("La computadora eligió:")
        st.markdown(
            f"### {emojis[eleccion_maquina]} {eleccion_maquina}"
        )

    # Determinar ganador, mostrar mensajes y reproducir sonidos automáticos
    if eleccion_usuario == eleccion_maquina:
        st.info("¡Empate! 🤝")
        st.session_state.empates += 1
        # Sonido corto para empate (reproductor oculto)
        st.markdown(
            '<audio src="https://www.myinstants.com/media/sounds/blip.mp3" autoplay></audio>',
            unsafe_allow_html=True,
        )

    elif (
        (eleccion_usuario == "Piedra" and eleccion_maquina == "Tijera")
        or (eleccion_usuario == "Papel" and eleccion_maquina == "Piedra")
        or (eleccion_usuario == "Tijera" and eleccion_maquina == "Papel")
    ):
        st.success("¡Ganaste esta ronda! 🎉")
        st.session_state.puntos_usuario += 1
        # Sonido de victoria o campana (reproductor oculto)
        st.markdown(
            '<audio src="https://www.myinstants.com/media/sounds/tada.mp3" autoplay></audio>',
            unsafe_allow_html=True,
        )

    else:
        st.error("¡Perdiste esta ronda! 🤖")
        st.session_state.puntos_maquina += 1
        # Sonido de error o derrota (reproductor oculto)
        st.markdown(
            '<audio src="https://www.myinstants.com/media/sounds/erro.mp3" autoplay></audio>',
            unsafe_allow_html=True,
        )

# Marcador global
st.markdown("---")
st.subheader("📊 Marcador")
m1, m2, m3 = st.columns(3)
m1.metric("Tus Puntos", st.session_state.puntos_usuario)
m2.metric("Computadora", st.session_state.puntos_maquina)
m3.metric("Empates", st.session_state.empates)

# Botón para reiniciar
if st.button("🔄 Reiniciar Marcador"):
    st.session_state.puntos_usuario = 0
    st.session_state.puntos_maquina = 0
    st.session_state.empates = 0
    st.rerun()
