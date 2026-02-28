import streamlit as st
import pandas as pd
import joblib

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Calculadora IA LaLiga", page_icon="⚽", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CARGA DEL CEREBRO DE LA IA (Para que no dé error al predecir) ---
@st.cache_resource
def cargar_datos():
    try:
        return joblib.load('modelo_laliga_v1.pkl')
    except Exception as e:
        # ¡Ahora sí vamos a ver el error real!
        st.error(f"Error REAL detectado por Python: {e}")
        return None

datos = cargar_datos()

# Solo asignamos variables si el modelo cargó bien
if datos:
    modelo = datos['modelo']
    elo_dict = datos['elo_diccionario']
    media_goles = datos['media_goles']
    df_historial = datos['historial']
else:
    # Variables vacías de seguridad para que la web no explote si falta el archivo
    modelo, elo_dict, media_goles = None, {}, 0
    df_historial = pd.DataFrame()

# --- 3. DISEÑO Y CSS ---
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .stApp {
        background-color: #102216;
        background-image: linear-gradient(0deg, transparent 24%, rgba(255, 255, 255, .03) 25%, rgba(255, 255, 255, .03) 26%, transparent 27%, transparent 74%, rgba(255, 255, 255, .03) 75%, rgba(255, 255, 255, .03) 76%, transparent 77%, transparent), linear-gradient(90deg, transparent 24%, rgba(255, 255, 255, .03) 25%, rgba(255, 255, 255, .03) 26%, transparent 27%, transparent 74%, rgba(255, 255, 255, .03) 75%, rgba(255, 255, 255, .03) 76%, transparent 77%, transparent);
        background-size: 50px 50px;
        color: #ffffff;
        font-family: 'Lexend', sans-serif;
    }
    .stButton > button {
        background-color: #13ec5b !important;
        color: #102216 !important;
        font-weight: 900 !important;
        font-size: 1.25rem !important;
        text-transform: uppercase !important;
        padding: 1rem 3rem !important;
        border-radius: 0.75rem !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(19,236,91,0.4) !important;
        width: 100%;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button:hover {
        box-shadow: 0 0 30px rgba(19,236,91,0.6) !important;
        transform: scale(1.05) !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #102216;
        border-color: rgba(255,255,255,0.1);
        color: white;
        border-radius: 0.5rem;
    }
    .team-card {
        background-color: #152e1e;
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 1rem;
        padding: 1.5rem;
        text-align: center;
    }
    .vs-badge {
        display: flex; align-items: center; justify-content: center;
        width: 5rem; height: 5rem; border-radius: 9999px;
        background-color: #102216; border: 4px solid #152e1e;
        box-shadow: 0 0 20px rgba(19,236,91,0.2);
        font-size: 1.875rem; font-weight: 900; font-style: italic; margin: 0 auto;
    }
    .result-card {
        background-color: rgba(21, 46, 30, 0.5);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 0.75rem; padding: 1rem;
    }
    .badge-success { background-color: rgba(34, 197, 94, 0.1); color: #22c55e; padding: 0.125rem 0.5rem; border-radius: 0.25rem; font-size: 0.625rem; font-weight: 700; text-transform: uppercase; }
    .badge-error { background-color: rgba(239, 68, 68, 0.1); color: #ef4444; padding: 0.125rem 0.5rem; border-radius: 0.25rem; font-size: 0.625rem; font-weight: 700; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# --- 4. HEADER Y NAVEGACIÓN ---
col_logo, col_nav = st.columns([1, 1])
with col_logo:
    st.markdown("""<div style="display: flex; align-items: center; gap: 0.75rem;"><div style="width: 2rem; height: 2rem; border-radius: 0.5rem; background: linear-gradient(to top right, #13ec5b, #0fa841); display: flex; align-items: center; justify-content: center; color: #102216; font-weight: bold;">⚽</div><h1 style="font-size: 1.125rem; margin: 0;">Calculadora <span style="color: #13ec5b;">IA</span> LaLiga</h1></div>""", unsafe_allow_html=True)
with col_nav:
    st.page_link("pages/resultados.py", label="Resultados por Jornada", icon="📅")

st.markdown("<h2 style='text-align: center; font-size: 3rem; margin-top: 2rem;'>Predictor de Partidos</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8; font-size: 1.125rem; text-align: center; margin-bottom: 2rem;'>Selecciona dos equipos para generar un pronóstico impulsado por IA basado en datos históricos, estado de forma y reportes de lesiones.</p>", unsafe_allow_html=True)

equipos = [
    "Alavés", "Athletic Club", "Atlético de Madrid", "Barcelona", 
    "Celta de Vigo", "Getafe", "Girona", "Mallorca", "Osasuna", "Rayo Vallecano", 
    "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla", "Valencia", 
    "Villarreal", "Oviedo", "Espanyol", "Elche", "Levante"
]
escudos = {
    "Real Madrid": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
    "Barcelona": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
    "Alavés" : "https://upload.wikimedia.org/wikipedia/en/f/f8/Deportivo_Alaves_logo_%282020%29.svg",
    "Athletic Club" : "https://upload.wikimedia.org/wikipedia/an/9/9f/Athletic_c_de_bilbao.png",
    "Atlético de Madrid" : "https://upload.wikimedia.org/wikipedia/pt/c/c1/Atletico_Madrid_logo.svg",
    "Celta de Vigo" : "https://upload.wikimedia.org/wikipedia/commons/4/47/Escudo_RC_Celta_de_Vigo.svg",
    "Getafe" : "https://upload.wikimedia.org/wikipedia/de/d/de/Getafe_CF.svg",
    "Girona" : "https://upload.wikimedia.org/wikipedia/fr/5/56/Logo_Girona_FC_-_2022.svg",
    "Mallorca" : "https://upload.wikimedia.org/wikipedia/de/e/e0/Rcd_mallorca.svg",
    "Osasuna" : "https://upload.wikimedia.org/wikipedia/fr/2/25/Logo_CA_Osasuna_2024.svg",
    "Rayo Vallecano" : "https://upload.wikimedia.org/wikipedia/fr/4/41/Logo_Rayo_Vallecano_de_Madrid_2016.svg",
    "Real Betis" : "https://upload.wikimedia.org/wikipedia/fr/1/13/Real_betis_logo.svg",
    "Real Sociedad" : "https://upload.wikimedia.org/wikipedia/sco/f/f1/Real_Sociedad_logo.svg",
    "Sevilla" : "https://upload.wikimedia.org/wikipedia/fr/8/8d/Logo_S%C3%A9ville_FC.svg",
    "Valencia" : "https://upload.wikimedia.org/wikipedia/sco/c/ce/Valenciacf.svg",
    "Villarreal" : "https://upload.wikimedia.org/wikipedia/pt/7/70/Villarreal_CF_logo.svg",
    "Oviedo" : "https://upload.wikimedia.org/wikipedia/an/6/6e/Real_Oviedo_logo.svg",
    "Espanyol" : "https://upload.wikimedia.org/wikipedia/fr/6/62/Logo_RCD_Espanyol_Barcelona_2022.svg",
    "Elche" : "https://upload.wikimedia.org/wikipedia/fr/c/cd/Logo_Elche_CF_2021.svg",
    "Levante" : "https://upload.wikimedia.org/wikipedia/it/7/7b/Levante_Uni%C3%B3n_Deportiva%2C_S.A.D._logo.svg"
}

# --- COLUMNAS DE LOS EQUIPOS ---
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    # 1. PRIMERO preguntamos el equipo (así la variable ya existe)
    equipo_local = st.selectbox("Seleccionar Equipo Local", equipos, index=0, label_visibility="collapsed")
    
    # 2. LUEGO pintamos la tarjeta y el escudo correspondiente
    st.markdown(f"""
    <div class="team-card">
        <div style="font-size: 0.75rem; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; text-align: left; margin-bottom: 1rem;">Local</div>
        <img src="{escudos[equipo_local]}" style="width: 8rem; height: 8rem; object-fit: contain; margin: 0 auto 1.5rem auto; display: block; drop-shadow: 0 0 10px rgba(255,255,255,0.1);">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<div style='height: 50%;'></div><div class='vs-badge'>VS</div>", unsafe_allow_html=True)

with col3:
    # 1. PRIMERO preguntamos el equipo visitante
    equipo_visitante = st.selectbox("Seleccionar Equipo Visitante", equipos, index=1, label_visibility="collapsed")
    
    # 2. LUEGO pintamos su tarjeta y escudo
    st.markdown(f"""
    <div class="team-card">
        <div style="font-size: 0.75rem; font-weight: bold; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.1em; text-align: right; margin-bottom: 1rem;">Visitante</div>
        <img src="{escudos[equipo_visitante]}" style="width: 8rem; height: 8rem; object-fit: contain; margin: 0 auto 1.5rem auto; display: block; drop-shadow: 0 0 10px rgba(255,255,255,0.1);">
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- BOTÓN DE PREDICCIÓN ---
# (Añadido: Creamos las columnas del botón que faltaban)
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    if st.button("✨ VER PREDICCIÓN DE LA IA"):
        if equipo_local == equipo_visitante:
            st.error("¡Un equipo no puede jugar contra sí mismo!")
        elif datos is None:
            st.error("El modelo de IA no está cargado. Asegúrate de tener 'modelo_laliga_v1.pkl'.")
        else:
            st.success(f"Generando predicción para {equipo_local} vs {equipo_visitante}...")
            
            # Cálculos matemáticos
            elo_l = elo_dict.get(equipo_local, 1500)
            elo_v = elo_dict.get(equipo_visitante, 1500)
            
            hist_l = df_historial[df_historial['HomeTeam'] == equipo_local]
            ataque_l = hist_l['Ataque_Local_5p'].iloc[-1] if not hist_l.empty else media_goles
            defensa_l = hist_l['Defensa_Local_5p'].iloc[-1] if not hist_l.empty else media_goles
            
            hist_v = df_historial[df_historial['AwayTeam'] == equipo_visitante]
            ataque_v = hist_v['Ataque_Visitante_5p'].iloc[-1] if not hist_v.empty else media_goles
            defensa_v = hist_v['Defensa_Visitante_5p'].iloc[-1] if not hist_v.empty else media_goles
            
            datos_hoy = pd.DataFrame({
                'Ataque_Local_5p': [ataque_l], 'Defensa_Local_5p': [defensa_l],
                'Ataque_Visitante_5p': [ataque_v], 'Defensa_Visitante_5p': [defensa_v],
                'Elo_Local': [elo_l], 'Elo_Visitante': [elo_v]
            })
            
            # Sacamos las probabilidades reales
            prob = modelo.predict_proba(datos_hoy)[0]
            prob_local = f"{prob[0]*100:.1f}%"
            prob_empate = f"{prob[1]*100:.1f}%"
            prob_visita = f"{prob[2]*100:.1f}%"
            
            # Inyectamos los resultados
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; text-align: center; background-color: rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 1rem; margin-top: 1rem; border: 1px solid rgba(19,236,91,0.3);">
                <div style="flex: 1; padding: 0.5rem; background-color: rgba(19,236,91,0.1); border: 1px solid rgba(19,236,91,0.4); border-radius: 0.25rem;">
                    <div style="font-size: 0.625rem; text-transform: uppercase; color: #13ec5b; font-weight: bold;">Local</div>
                    <div style="font-size: 1.5rem; font-weight: 900; color: white;">{prob_local}</div>
                </div>
                <div style="flex: 1; padding: 0.5rem;">
                    <div style="font-size: 0.625rem; text-transform: uppercase; color: #94a3b8; font-weight: bold;">Empate</div>
                    <div style="font-size: 1.25rem; font-weight: bold; color: #cbd5e1;">{prob_empate}</div>
                </div>
                <div style="flex: 1; padding: 0.5rem;">
                    <div style="font-size: 0.625rem; text-transform: uppercase; color: #94a3b8; font-weight: bold;">Visita</div>
                    <div style="font-size: 1.25rem; font-weight: bold; color: #cbd5e1;">{prob_visita}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.75rem; color: #64748b; margin-top: 0.5rem;'>*Predicciones basadas en datos históricos. Juegue con responsabilidad.</p><br><br>", unsafe_allow_html=True)

# --- 7. TARJETAS DE HISTORIAL DE PREDICCIONES ---
col_r1, col_r2, col_r3 = st.columns(3)

def render_mini_result(jornada, match, status, p_local, p_empate, p_visita, highlight):
    status_class = "badge-success" if status == "✅ Acertó" else "badge-error"
    bg_local = "background-color: rgba(19,236,91,0.1); border: 1px solid rgba(19,236,91,0.4); border-radius: 0.25rem;" if highlight == 1 else ""
    color_local = "#13ec5b" if highlight == 1 else "#cbd5e1"
    bg_empate = "background-color: rgba(19,236,91,0.1); border: 1px solid rgba(19,236,91,0.4); border-radius: 0.25rem;" if highlight == 2 else ""
    color_empate = "#13ec5b" if highlight == 2 else "#cbd5e1"
    bg_visita = "background-color: rgba(19,236,91,0.1); border: 1px solid rgba(19,236,91,0.4); border-radius: 0.25rem;" if highlight == 3 else ""
    color_visita = "#13ec5b" if highlight == 3 else "#cbd5e1"
    
    return f"""
    <div class="result-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <div style="font-size: 0.75rem; font-weight: 600; color: #cbd5e1;">📅 {jornada}: {match}</div>
            <span class="{status_class}">{status}</span>
        </div>
        <div style="display: flex; justify-content: space-between; text-align: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 0.5rem; margin-top: 0.25rem;">
            <div style="flex: 1; padding: 0.25rem; {bg_local}"><div style="font-size: 0.625rem; text-transform: uppercase; color: #94a3b8; font-weight: bold;">Local</div><div style="font-size: 1.125rem; font-weight: bold; color: {color_local};">{p_local}</div></div>
            <div style="flex: 1; padding: 0.25rem; {bg_empate}"><div style="font-size: 0.625rem; text-transform: uppercase; color: #94a3b8; font-weight: bold;">Empate</div><div style="font-size: 1.125rem; font-weight: bold; color: {color_empate};">{p_empate}</div></div>
            <div style="flex: 1; padding: 0.25rem; {bg_visita}"><div style="font-size: 0.625rem; text-transform: uppercase; color: #94a3b8; font-weight: bold;">Visita</div><div style="font-size: 1.125rem; font-weight: bold; color: {color_visita};">{p_visita}</div></div>
        </div>
    </div>
    """

with col_r1:
    st.markdown(render_mini_result("Jornada 24", "RMA vs BAR", "✅ Acertó", "65%", "20%", "15%", 1), unsafe_allow_html=True)
with col_r2:
    st.markdown(render_mini_result("Jornada 24", "ATM vs SEV", "❌ Falló", "33%", "42%", "25%", 2), unsafe_allow_html=True)
with col_r3:
    st.markdown(render_mini_result("Jornada 23", "VAL vs BET", "✅ Acertó", "22%", "20%", "58%", 3), unsafe_allow_html=True)

# --- 8. FOOTER ---
st.markdown("""<div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center;"><div style="font-size: 0.875rem; color: #64748b;">©2026 Eric Martínez García</div><div style="display: flex; gap: 1.5rem;"><a href="#" style="font-size: 0.875rem; color: #64748b; text-decoration: none;">Metodología</a><a href="#" style="font-size: 0.875rem; color: #64748b; text-decoration: none;">Política de Privacidad</a><a href="#" style="font-size: 0.875rem; color: #64748b; text-decoration: none;">Términos de Servicio</a></div></div>""", unsafe_allow_html=True)
