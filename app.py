import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Tport - Medición de Estanques", layout="wide")

st.title("⚓ Registro de Medición de Estanques - Tport")
st.subheader("Formulario Digital N° 0297")

# --- SECCIÓN 1: DATOS GENERALES ---
with st.expander("Datos Generales", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        motivo = st.selectbox("Motivo", ["Inicial", "Final", "Diaria", "Inventario"])
        nave = st.text_input("Nave", placeholder="Ej: Bochem Oslo")
        tk = st.text_input("Estanque TK N°")
    with col2:
        fecha = st.date_input("Fecha", datetime.now())
        hora = st.time_input("Hora", datetime.now())
        sensor = st.number_input("Sensor de Nivel", step=1)

# --- SECCIÓN 2: TEMPERATURAS (CÁLCULO AUTOMÁTICO) ---
with st.expander("Mediciones y Temperaturas"):
    c1, c2, c3 = st.columns(3)
    t_inf = c1.number_input("Temp. Inferior (°C)", format="%.1f")
    t_med = c2.number_input("Temp. Medida (°C)", format="%.1f")
    t_sup = c3.number_input("Temp. Superior (°C)", format="%.1f")
    
    # Cálculo automático del promedio
    promedio = (t_inf + t_med + t_sup) / 3 if (t_inf and t_med and t_sup) else 0.0
    st.info(f"Promedio T° calculado: {promedio:.2f} °C")
    
    densidad = st.number_input("Densidad 20°", format="%.4f")
    toneladas = st.number_input("Toneladas Totales")

# --- SECCIÓN 3: REGISTRO DE SELLOS (CON TK208) ---
st.markdown("### 🔒 Registro de Sellos")
lista_sellos = [
    "Entrada TK201 (01)", "Entrada TK201 (20)", "Entrada TK202 (02)", 
    "Entrada TK202 (17)", "Entrada TK203 (03)", "Entrada TK204 (04)",
    "Entrada TK205 (05)", "Entrada TK206 (06)", "Entrada TK207 (07)",
    "Entrada TK208 (08)", # <-- La nueva entrada que pediste
    "Alim TK207 norte (10)", "Alim TK207 sur (11)", "Salida 12\" TK", "Retorno 6\" TK"
]

sellos_data = {}
cols = st.columns(2)
for i, sello in enumerate(lista_sellos):
    with cols[i % 2]:
        sellos_data[sello] = st.text_input(f"Sello para {sello}")

# --- BOTÓN DE GUARDADO ---
if st.button("Guardar Registro Tport"):
    # Aquí podrías conectar a una base de datos o Google Sheets
    st.success("✅ Datos registrados correctamente para Operador Tport")
    st.balloons()
