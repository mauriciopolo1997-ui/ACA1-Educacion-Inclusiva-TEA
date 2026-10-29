
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Apoyo Educativo", page_icon="📚")

st.title("Asistente de Apoyo Pedagogico")
st.write("Prototipo academico para explorar estrategias de educacion inclusiva.")

st.info(
    "Esta aplicacion es demostrativa. No diagnostica TEA "
    "ni reemplaza la valoracion de profesionales."
)

modelo = joblib.load("modelo_apoyo_educativo.pkl")

st.subheader("Selecciona las estrategias pedagogicas")

apoyo_visual = st.selectbox(
    "¿Se utilizaran apoyos visuales?", ["Si", "No"]
)

instrucciones_cortas = st.selectbox(
    "¿Se daran instrucciones cortas?", ["Si", "No"]
)

actividad_practica = st.selectbox(
    "¿Se realizaran actividades practicas?", ["Si", "No"]
)

if st.button("Consultar modelo"):
    entrada = pd.DataFrame({
        "apoyo_visual": [1 if apoyo_visual == "Si" else 0],
        "instrucciones_cortas": [
            1 if instrucciones_cortas == "Si" else 0
        ],
        "actividad_practica": [
            1 if actividad_practica == "Si" else 0
        ]
    })

    resultado = modelo.predict(entrada)[0]

    if resultado == 1:
        st.warning("El modelo estima necesidad de apoyo educativo.")
    else:
        st.success("El modelo no identifica necesidad de apoyo en este ejemplo.")

    st.caption(
        "Resultado experimental basado en datos simulados. "
        "Debe ser revisado por el equipo educativo."
    )
