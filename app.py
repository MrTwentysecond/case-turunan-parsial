# file: cobb_douglas_app.py

import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

st.title("📊 Analisis Fungsi Produksi Cobb-Douglas")

# Input pengguna
st.sidebar.header("Masukkan Parameter:")
A_val = st.sidebar.number_input("Nilai A (Total Faktor Produktivitas)", value=1.0)
alpha_val = st.sidebar.number_input("Nilai α (elastisitas tenaga kerja)", value=0.3)
beta_val = st.sidebar.number_input("Nilai β (elastisitas modal)", value=0.7)
L_val = st.sidebar.number_input("Jumlah Tenaga Kerja (L)", value=100.0)
K_val = st.sidebar.number_input("Jumlah Modal (K)", value=50.0)

# Definisikan simbol dan fungsi
A, L, K, alpha, beta = sp.symbols('A L K alpha beta')
Q = A * L**alpha * K**beta

# Hitung turunan parsial
dQ_dL = sp.diff(Q, L)
dQ_dK = sp.diff(Q, K)

# Substitusi nilai input
subs_dict = {A: A_val, L: L_val, K: K_val, alpha: alpha_val, beta: beta_val}
Q_val = Q.evalf(subs=subs_dict)
dQdL_val = dQ_dL.evalf(subs=subs_dict)
dQdK_val = dQ_dK.evalf(subs=subs_dict)

# Tampilkan hasil
st.subheader("🔣 Fungsi Produksi:")
st.latex(r"Q = A \cdot L^{\alpha} \cdot K^{\beta}")

st.subheader("📉 Hasil Evaluasi:")
st.write(f"Output Produksi (Q) = {Q_val:.2f}")
st.write(f"Turunan Parsial terhadap L (∂Q/∂L) = {dQdL_val:.2f}")
st.write(f"Turunan Parsial terhadap K (∂Q/∂K) = {dQdK_val:.2f}")

# Visualisasi Fungsi Produksi
st.subheader("📈 Visualisasi Fungsi Produksi dalam 3D")

L_range = np.linspace(1, 200, 50)
K_range = np.linspace(1, 200, 50)
L_mesh, K_mesh = np.meshgrid(L_range, K_range)
Q_mesh = A_val * L_mesh**alpha_val * K_mesh**beta_val

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(L_mesh, K_mesh, Q_mesh, cmap='viridis')
ax.set_xlabel("Tenaga Kerja (L)")
ax.set_ylabel("Modal (K)")
ax.set_zlabel("Output (Q)")
st.pyplot(fig)
