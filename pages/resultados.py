import streamlit as st

st.set_page_config(page_title="Historial de Resultados - LaLiga IA", page_icon="📅", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    .stApp { background-color: #102216; color: #ffffff; font-family: 'Lexend', sans-serif; }
    .stButton > button {
        background-color: #13ec5b !important; color: #102216 !important; font-weight: bold !important;
        border-radius: 0.75rem !important; border: none !important; box-shadow: 0 4px 14px 0 rgba(19,236,91,0.39) !important;
        transition: all 0.2s ease-in-out !important;
    }
    .stButton > button:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(19,236,91,0.5) !important; }
    div[data-baseweb="select"] > div { background-color: #162e1e; border-color: #23482f; color: white; border-radius: 0.75rem; padding: 0.25rem; }
    .match-card {
        background-color: #162e1e; border: 1px solid #23482f; border-radius: 1rem; overflow: hidden; position: relative;
        transition: all 0.3s ease; height: 100%; display: flex; flex-direction: column;
    }
    .match-card:hover { border-color: rgba(19,236,91,0.5); box-shadow: 0 10px 25px -5px rgba(19,236,91,0.1); }
    .match-card.failed:hover { border-color: rgba(239, 68, 68, 0.5); box-shadow: 0 10px 25px -5px rgba(239, 68, 68, 0.1); }
    .card-header-success { position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(to right, transparent, #13ec5b, transparent); opacity: 0.75; }
    .card-header-error { position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(to right, transparent, #ef4444, transparent); opacity: 0.75; }
    .team-logo { width: 4rem; height: 4rem; background-color: rgba(255,255,255,0.05); border-radius: 50%; border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin: 0 auto 0.5rem auto; }
    .score-box { background-color: rgba(16,34,22,0.5); border: 1px solid rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 0.25rem 1rem; font-size: 1.875rem; font-weight: 900; letter-spacing: 0.1em; }
    .prediction-bar { background-color: rgba(255,255,255,0.05); border-radius: 0.5rem; padding: 0.25rem; display: flex; gap: 0.25rem; font-size: 0.75rem; }
    .pred-item { flex: 1; text-align: center; padding: 0.25rem 0; color: rgba(255,255,255,0.5); border-radius: 0.25rem; }
    .pred-item.active { background-color: rgba(19,236,91,0.3); color: white; font-weight: bold; }
    .status-badge-success { display: flex; align-items: center; gap: 0.375rem; color: #13ec5b; background-color: rgba(19,236,91,0.1); border: 1px solid rgba(19,236,91,0.2); padding: 0.375rem 0.75rem; border-radius: 0.5rem; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .status-badge-error { display: flex; align-items: center; gap: 0.375rem; color: #ef4444; background-color: rgba(239,68,68,0.1); border: 1px solid rgba(239,68,68,0.2); padding: 0.375rem 0.75rem; border-radius: 0.5rem; font-size: 0.75rem; font-weight: bold; text-transform: uppercase; }
    .stat-box { background-color: #162e1e; border: 1px solid #23482f; border-radius: 0.75rem; padding: 0.5rem 1.25rem; display: flex; align-items: center; gap: 0.75rem; }
</style>
""", unsafe_allow_html=True)

col_logo, col_nav = st.columns([1, 1])
with col_logo:
    st.markdown("""<div style="display: flex; align-items: center; gap: 0.75rem;"><div style="width: 2rem; height: 2rem; border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; color: #13ec5b;">⚽</div><h2 style="font-size: 1.125rem; margin: 0; color: white;">LaLiga IA</h2></div>""", unsafe_allow_html=True)
with col_nav:
    st.page_link("app.py", label="Volver al Predictor", icon="⬅️")

st.markdown("<h1 style='font-size: 2.25rem; margin-top: 1rem; margin-bottom: 0.5rem;'>Historial de Resultados</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #92c9a4; font-size: 1.125rem; max-width: 42rem; margin-bottom: 2rem;'>Analiza el rendimiento pasado. Revisa la precisión de la IA en jornadas anteriores y sigue la evolución del algoritmo.</p>", unsafe_allow_html=True)

col_ctrl1, col_ctrl2, col_ctrl3, col_ctrl4 = st.columns([2, 1.5, 1.5, 2])
with col_ctrl1:
# Generamos una lista del 1 al 38 automáticamente
    lista_jornadas = [f"Jornada {i}" for i in range(1, 39)]
# Guardamos lo que elija el usuario en una variable
    jornada_seleccionada = st.selectbox("Seleccionar Jornada", lista_jornadas, index=23, label_visibility="collapsed")
with col_ctrl2:
    st.markdown("""<div class="stat-box"><div style="background-color: rgba(19,236,91,0.2); color: #13ec5b; padding: 0.375rem; border-radius: 0.5rem;">✅</div><div><div style="font-size: 0.625rem; color: #92c9a4; text-transform: uppercase; font-weight: bold; letter-spacing: 0.05em;">Precisión</div><div style="font-size: 1.125rem; font-weight: bold; color: white;">80%</div></div></div>""", unsafe_allow_html=True)
with col_ctrl3:
    st.markdown("""<div class="stat-box"><div style="background-color: rgba(59,130,246,0.2); color: #60a5fa; padding: 0.375rem; border-radius: 0.5rem;">📊</div><div><div style="font-size: 0.625rem; color: #92c9a4; text-transform: uppercase; font-weight: bold; letter-spacing: 0.05em;">Partidos Totales</div><div style="font-size: 1.125rem; font-weight: bold; color: white;">10</div></div></div>""", unsafe_allow_html=True)
with col_ctrl4:
    st.button("📥 Exportar Informe", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

def render_match_card(t1, t2, score, p_1, p_x, p_2, is_success, active_pred):
    card_class = "match-card" if is_success else "match-card failed"
    header_class = "card-header-success" if is_success else "card-header-error"
    status_badge = f'<div class="status-badge-success">✅ Acertó</div>' if is_success else f'<div class="status-badge-error">❌ Falló</div>'
    a1 = "active" if active_pred == 1 else ""
    ax = "active" if active_pred == 2 else ""
    a2 = "active" if active_pred == 3 else ""
    
    return f"""
    <div class="{card_class}">
        <div class="{header_class}"></div>
        <div style="padding: 1.5rem 1.5rem 1rem 1.5rem; flex-grow: 1;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="width: 33%; text-align: center;"><div class="team-logo">🛡️</div><div style="font-size: 0.875rem; font-weight: bold;">{t1}</div></div>
                <div style="width: 33%; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 0.25rem;"><div class="score-box">{score}</div><div style="font-size: 0.75rem; color: #92c9a4; text-transform: uppercase; font-weight: 500; letter-spacing: 0.1em;">Final</div></div>
                <div style="width: 33%; text-align: center;"><div class="team-logo">🛡️</div><div style="font-size: 0.875rem; font-weight: bold;">{t2}</div></div>
            </div>
        </div>
        <div style="height: 1px; background-color: #23482f; width: 100%;"></div>
        <div style="padding: 1rem; background-color: rgba(16,34,22,0.3); display: flex; justify-content: space-between; align-items: center;">
            <div style="width: 65%;">
                <div style="font-size: 0.625rem; text-transform: uppercase; letter-spacing: 0.1em; color: #92c9a4; font-weight: bold; margin-bottom: 0.25rem;">Predicción IA (1-X-2)</div>
                <div class="prediction-bar"><div class="pred-item {a1}">{p_1}</div><div class="pred-item {ax}">{p_x}</div><div class="pred-item {a2}">{p_2}</div></div>
            </div>
            <div>{status_badge}</div>
        </div>
    </div>
    """

r1c1, r1c2, r1c3 = st.columns(3)
with r1c1: st.markdown(render_match_card("Real Madrid", "Barcelona", "3 - 1", "85%", "10%", "5%", True, 1), unsafe_allow_html=True)
with r1c2: st.markdown(render_match_card("Atlético", "Sevilla", "0 - 1", "25%", "45%", "30%", False, 2), unsafe_allow_html=True)
with r1c3: st.markdown(render_match_card("Valencia", "Sociedad", "1 - 2", "20%", "18%", "62%", True, 3), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
r2c1, r2c2, r2c3 = st.columns(3)
with r2c1: st.markdown(render_match_card("Real Betis", "Villarreal", "2 - 2", "33%", "35%", "32%", True, 2), unsafe_allow_html=True)
with r2c2: st.markdown(render_match_card("Athletic", "Getafe", "0 - 0", "70%", "20%", "10%", False, 1), unsafe_allow_html=True)
with r2c3: st.markdown(render_match_card("Mallorca", "Osasuna", "2 - 0", "55%", "30%", "15%", True, 1), unsafe_allow_html=True)

st.markdown("""<div style="margin-top: 4rem; padding: 2rem 0; border-top: 1px solid #23482f; background-color: #0f1b14; display: flex; justify-content: space-between; align-items: center;"><div style="font-size: 0.875rem; color: #92c9a4;">© 2026 Eric Martínez García</div><div style="display: flex; gap: 1.5rem;"><a href="#" style="font-size: 0.875rem; color: #92c9a4; text-decoration: none;">Privacidad</a><a href="#" style="font-size: 0.875rem; color: #92c9a4; text-decoration: none;">Términos</a><a href="#" style="font-size: 0.875rem; color: #92c9a4; text-decoration: none;">Ayuda</a></div></div>""", unsafe_allow_html=True)
