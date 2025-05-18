import streamlit as st
import numpy as np
import plotly.graph_objs as go

st.set_page_config(layout="wide")
st.title("Visualisasi Gunung 3D dengan Turunan Parsial")

# Fungsi menyerupai gunung sungguhan
def gunung(x, y):
    return 80 * np.exp(-0.05*(x**2 + y**2)) + 20 * np.exp(-0.5*((x - 3)**2 + (y + 3)**2))

# Turunan parsial
def dfdx(x, y):
    return -0.05 * 2 * x * 80 * np.exp(-0.05*(x**2 + y**2)) - 0.5 * 2 * (x - 3) * 20 * np.exp(-0.5*((x - 3)**2 + (y + 3)**2))

def dfdy(x, y):
    return -0.05 * 2 * y * 80 * np.exp(-0.05*(x**2 + y**2)) - 0.5 * 2 * (y + 3) * 20 * np.exp(-0.5*((x - 3)**2 + (y + 3)**2))

# Input titik dari pengguna
x0 = st.slider("Pilih nilai x", -10.0, 10.0, 2.0)
y0 = st.slider("Pilih nilai y", -10.0, 10.0, 3.0)
z0 = gunung(x0, y0)

dz_dx = dfdx(x0, y0)
dz_dy = dfdy(x0, y0)

st.markdown(f"""
**Titik yang dipilih:** ({x0:.2f}, {y0:.2f})  
**Ketinggian (z):** {z0:.2f} meter  
**Turunan terhadap x (kemiringan timur-barat):** {dz_dx:.2f}  
**Turunan terhadap y (kemiringan utara-selatan):** {dz_dy:.2f}
""")

# Buat permukaan gunung
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
X, Y = np.meshgrid(x, y)
Z = gunung(X, Y)

# Gunakan warna kontur seperti elevasi (hijau ke coklat ke putih)
surface = go.Surface(
    x=X, y=Y, z=Z,
    colorscale=[
        [0, '#2e8b57'],   # hijau
        [0.3, '#a0522d'], # coklat
        [0.6, '#deb887'], # tanah terang
        [1, '#ffffff']    # salju
    ],
    cmin=Z.min(), cmax=Z.max(),
    opacity=0.95,
)

# Titik dipilih pengguna
point = go.Scatter3d(
    x=[x0], y=[y0], z=[z0],
    mode='markers',
    marker=dict(size=6, color='red'),
    name='Titik dipilih'
)

# Layout interaktif
layout = go.Layout(
    title="Gunung 3D Realistik (Interaktif)",
    scene=dict(
        xaxis_title='x (km)',
        yaxis_title='y (km)',
        zaxis_title='Ketinggian (m)',
        aspectratio=dict(x=1, y=1, z=0.5)
    )
)

fig = go.Figure(data=[surface, point], layout=layout)
st.plotly_chart(fig, use_container_width=True)
