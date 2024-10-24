import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghasilkan data lingkaran kecil yang berada di dalam lingkaran besar
def generate_inner_circle_data():
    num_circles = 50
    angles = np.random.uniform(0, 2 * np.pi, num_circles)
    radii = np.random.uniform(0, 1, num_circles)  # Radius di dalam lingkaran besar
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    sizes = np.random.rand(num_circles) * 100  # Ukuran lingkaran kecil
    colors = np.random.rand(num_circles, 3)  # Warna acak (RGB)
    return x, y, sizes, colors

# Header aplikasi
st.title("Lingkaran Besar dengan Lingkaran Kecil di Dalamnya 🔵")

# Tombol untuk memperbarui data
if st.button('Generate New Data'):
    # Data lingkaran kecil
    x, y, sizes, colors = generate_inner_circle_data()

    # Membuat plot dengan lingkaran besar di tengah
    fig, ax = plt.subplots()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])

    # Plot lingkaran besar
    big_circle = plt.Circle((0, 0), 1, color='lightblue', fill=False, linewidth=2)
    ax.add_artist(big_circle)

    # Plot lingkaran-lingkaran kecil di dalam lingkaran besar
    ax.scatter(x, y, s=sizes, c=colors, alpha=0.6)

    # Menampilkan plot
    st.pyplot(fig)
