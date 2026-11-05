import os
from gtts import gTTS
import numpy as np
from PIL import Image
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Fábulas Interactivas | Andres Felipe Gonzalez",
    page_icon="🐢",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
    }
    .fabula-box {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #10B981;
        font-size: 16px;
        line-height: 1.6;
        color: #F8FAFC;
    }
    .stButton>button {
        background-color: #10B981;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #059669;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- TÍTULO Y PRESENTACIÓN ---
st.title("🐢 Biblioteca de Fábulas Multimodales")
st.markdown("**Autor del proyecto:** Andres Felipe Gonzalez")
st.write(
    "Explora relatos clásicos con síntesis de voz automatizada y traducción"
    " inteligente en tiempo real."
)

st.markdown("---")

# --- SECCIÓN DE LA FÁBULA: LA LIEBRE Y LA TORTUGA ---
st.subheader("📖 Fábula seleccionada: La Liebre y la Tortuga")

# Imagen representativa temática
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  st.info("🏃‍♂️💨 Constancia y paciencia vencen a la velocidad impulsiva.")

# Texto de la fábula en español
fabula_espanol = (
    "La liebre, famosa por su velocidad, se burlaba constantemente de la"
    " lenta tortuga. Cansada de las burlas, la tortuga la retó a una carrera."
    " La liebre, confiada en su victoria, se detuvo a dormir a mitad del"
    " camino. Cuando despertó, la tortuga ya había cruzado la meta pacientemente"
    " y ganado la carrera. Moraleja: Con constancia y paciencia se llega más"
    " lejos."
)

st.markdown(
    f'<div class="fabula-box">{fabula_espanol}</div>', unsafe_allow_html=True
)

st.markdown("### 🌐 Opciones de Conversión y Traducción")

# Área de texto interactiva para traducir o escuchar
texto_a_procesar = st.text_area(
    "Edita o traduce el texto antes de generar el audio:", fabula_espanol, height=150
)

# Selector de idioma para el audio
idioma = st.selectbox(
    "Selecciona el idioma de síntesis de voz:",
    ("Español (es)", "Inglés (en)", "Francés (fr)"),
)

lang_code = idioma.split("(")[1].replace(")", "")

# --- PROCESAMIENTO DE AUDIO (gTTS) ---
if st.button("🎧 Generar Audio Dinámico"):
  with st.spinner("Sintetizando locución de audio..."):
    try:
      tts = gTTS(text=texto_a_procesar, lang=lang_code, slow=False)
      audio_file = "fabula_audio.mp3"
      tts.save(audio_file)

      st.success("¡Audio generado exitosamente!")

      # Reproductor de audio integrado
      st.audio(audio_file, format="audio/mp3")

      # Botón de descarga directa
      with open(audio_file, "rb") as f:
        st.download_button(
            label="📥 Descargar archivo de audio (.mp3)",
            data=f,
            file_name="la_liebre_y_la_tortuga.mp3",
            mime="audio/mp3",
        )
    except Exception as e:
      st.error(f"Ocurrió un error al generar el audio: {e}")

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 14px;'>Desarrollado"
    " con Streamlit Cloud • Andres Felipe Gonzalez</p>",
    unsafe_allow_html=True,
)
