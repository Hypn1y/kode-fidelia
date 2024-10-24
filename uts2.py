import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghasilkan data lingkaran acak dengan radius 1
def generate_random_circle_data():
    num_circles = 50
    x = np.random.uniform(-1, 1, num_circles)
    y = np.random.uniform(-1, 1, num_circles)
    sizes = np.random.rand(num_circles) * 300  # Ukuran lingkaran acak
    colors = np.random.rand(num_circles, 3)    # Warna acak (RGB)
    return x, y, sizes, colors

# Header aplikasi
st.title("Lingkaran Acak Berwarna-warni yang Berubah Setiap Kali Tombol Ditekan 🌈")

# Tombol untuk memperbarui data
if st.button('Generate New Data'):
    x, y, sizes, colors = generate_random_circle_data()

    # Membuat plot lingkaran acak dengan radius 1
    fig, ax = plt.subplots()
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    # Plot lingkaran dengan warna acak
    ax.scatter(x, y, s=sizes, c=colors, alpha=0.6)

    # Menampilkan plot
    st.pyplot(fig)
