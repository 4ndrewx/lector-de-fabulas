from PIL import Image
import streamlit as st

# Configuración de la página con diseño moderno
st.set_page_config(
    page_title="Biblioteca de Fábulas Interactivas",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILOS VISUALES PERSONALIZADOS ---
st.markdown(
    """
    <style>
    .main {
        background-color: #F8FAFC;
    }
    h1 {
        color: #1E293B;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    .fabula-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #3B82F6;
        margin-bottom: 20px;
    }
    .translation-box {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #BFDBFE;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- CABECERA DE LA APP ---
st.title("📚 Biblioteca y Traductor de Fábulas")
st.markdown(
    "### Explora cuentos clásicos, tradúcelos al instante y analiza su"
    " moraleja."
)

# --- SECCIÓN DE IMAGEN / ILUSTRACIÓN ---
# Usamos una imagen representativa o un contenedor estético con texto alternativo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  # Mostramos un contenedor visual atractivo
  st.info("🦊 Fábula del día: La Liebre y la Tortuga")

# --- TEXTO DE LA FÁBULA (ESPAÑOL) ---
st.markdown("### Una gran Fábula de Esopo.")

fabula_espanol = """
En un mundo donde todos corrían tras la velocidad, una orgullosa liebre se burlaba constantemente de la lenta tortuga. 
Cansada de las burlas, la tortuga la retó a una competencia de carrera. 
La liebre, confiada en su velocidad natural, se adelantó rápidamente y, al verse muy lejos, decidió tomar una siesta al borde del camino. 
La tortuga, con paso lento pero constante, siguió caminando sin detenerse jamás, cruzando la meta y ganando la carrera. 
Moralaleja: La perseverancia y la constancia superan con creces al talento natural sin esfuerzo.
"""

st.markdown(
    f'<div class="fabula-box">{fabula_espanol}</div>', unsafe_allow_html=True
)

# --- OPCIÓN DE TRADUCCIÓN ---
st.markdown("### 🌐 Traducir historia")
idioma_destino = st.selectbox(
    "Selecciona el idioma de destino:", ["Inglés", "Francés", "Italiano"]
)

# Diccionario simple de traducción de ejemplo para la fábula
traducciones = {
    "Inglés": (
        "In a world where everyone chased speed, a proud hare constantly mocked"
        " the slow tortoise. Tired of the teasing, the tortoise challenged"
        " her to a race. The hare, confident in her natural speed, sprinted"
        " ahead and, seeing herself far in the lead, decided to take a nap by"
        " the roadside. The tortoise, with slow but steady steps, kept walking"
        " without ever stopping, crossing the finish line and winning the"
        " race. Moral: Perseverance and consistency far outweigh natural"
        " talent without effort."
    ),
    "Francés": (
        "Dans un monde où tout le monde courait après la vitesse, un lièvre"
        " orgueilleux se moquait constamment de la lente tortue. Fatiguée des"
        " railleries, la tortue l'a mise au défi d'une course. Le lièvre, sûr de"
        " sa vitesse naturelle, prit de l'avance et, se voyant très en avance,"
        " décida de faire une sieste au bord de la route. La tortue, d'un pas"
        " lent mais régulier, continua à marcher sans jamais s'arrêter, franchit"
        " la ligne d'arrivée et remporta la course."
    ),
    "Italiano": (
        "In un mondo in cui tutti inseguivano la velocità, una lepre orgogliosa"
        " prendeva costantemente in giro la lenta tartaruga. Stanca delle"
        " prese in giro, la tartaruga la sfidò a una gara di corsa. La lepre,"
        " fiduciosa nella sua velocità naturale, scattò in avanti e, vedendosi"
        " molto in vantaggio, decise di fare un pisolino sul ciglio della strada."
        " La tartaruga, con passo lento ma costante, continuò a camminare"
        " senza fermarsi mai, tagliando il traguardo e vincendo la gara."
    ),
}

if st.button("🔄 Traducir texto"):
  texto_traducido = traducciones[idioma_destino]
  st.markdown("### Texto traducido:")
  st.markdown(
      f'<div class="translation-box">{texto_traducido}</div>',
      unsafe_allow_html=True,
  )

# --- PANEL DE ESTADÍSTICAS DE LECTURA ---
st.markdown("---")
st.markdown("### 📊 Panel de Lectura")
col_a, col_b = st.columns(2)
with col_a:
  st.metric(label="Tiempo estimado de lectura", value="45 segundos")
with col_b:
  st.metric(label="Dificultad del vocabulario", value="Fácil / Infantil")
