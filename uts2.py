import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk membuat data acak
def generate_random_data():
    num_points = np.random.randint(10, 100)  # Jumlah titik acak
    x = np.random.uniform(-1, 1, num_points)  # Posisi x acak
    y = np.random.uniform(-1, 1, num_points)  # Posisi y acak
    sizes = np.random.uniform(10, 300, num_points)  # Ukuran acak
    return x, y, sizes

# Judul aplikasi
st.title("Data Acak dengan Lingkaran Berukuran Berbeda 🎨")

# Tombol untuk memperbarui data
if st.button('Generate Data Baru'):
    x, y, sizes = generate_random_data()  # Menghasilkan data baru

    # Membuat plot lingkaran dengan Matplotlib
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, alpha=0.5)
    
    # Mengatur batas sumbu dan lingkaran luar
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='--', alpha=0.3)
    ax.add_artist(circle)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
