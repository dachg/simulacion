import streamlit as st
import matplotlib.pyplot as plt
from math import gcd

st.set_page_config(page_title="Desafío: Corte de telas", layout="centered")

st.title("🧩 Desafío guiado: Corte de telas")

st.markdown(
"""
Tienes dos tiras de tela de diferentes longitudes.  
Explora, piensa y descubre *cuál es la pieza más grande* que puedes cortar sin que sobre nada.
"""
)

# --- SLIDERS ---
a = st.slider("Longitud de la tela A", 1, 60, 24)
b = st.slider("Longitud de la tela B", 1, 60, 36)

m = gcd(a, b)

# --- NIVEL 2: PREDICCIÓN ---
st.subheader("✏️ Paso 1: Predice")
pred = st.number_input(
    "¿Cuánto crees que medirá la pieza más grande?",
    min_value=1,
    max_value=60,
    step=1
)

# --- BOTÓN ---
if st.button("Comprobar"):
    st.subheader("🔍 Paso 2: Comprobación")

    if pred == m:
        st.success("¡Correcto! 🎉 Ambas telas se pueden dividir en piezas de esa longitud.")
    else:
        st.error(f"No coincide. La pieza más grande posible mide {m}.")

    st.info(
        "La longitud buscada debe dividir exactamente a ambas telas "
        "y ser lo más grande posible."
    )

    # --- GRÁFICO ---
    fig, ax = plt.subplots(figsize=(8, 2))

    ax.broken_barh([(0, a)], (1, 0.4))
    for i in range(0, a + 1, m):
        ax.plot([i, i], [1, 1.4])

    ax.broken_barh([(0, b)], (0, 0.4))
    for i in range(0, b + 1, m):
        ax.plot([i, i], [0, 0.4])

    ax.set_yticks([0.2, 1.2])
    ax.set_yticklabels(["Tela B", "Tela A"])
    ax.set_xlabel("Longitud")
    ax.set_xlim(0, max(a, b) + 1)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    st.pyplot(fig)

# --- NIVEL 4: REFLEXIÓN ---
st.subheader("🧠 Paso 3: Reflexiona")

opciones = st.multiselect(
    "Marca las afirmaciones que SIEMPRE sean verdaderas:",
    [
        "La pieza divide exactamente a ambas telas",
        "La pieza puede ser mayor que alguna de las telas",
        "La pieza es un divisor común",
        "La pieza es la mayor posible"
    ]
)

if opciones:
    if set(opciones) == {
        "La pieza divide exactamente a ambas telas",
        "La pieza es un divisor común",
        "La pieza es la mayor posible"
    }:
        st.success("¡Excelente! Has descrito correctamente la idea del MCD.")
    else:
        st.warning("Revisa tus elecciones y piensa en los cortes.")