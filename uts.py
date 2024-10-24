import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghasilkan data lingkaran acak
def generate_random_circle_data():
    num_circles = 50
    angles = np.linspace(0, 2 * np.pi, num_circles)
    radii = np.random.rand(num_circles)
    sizes = np.random.rand(num_circles) * 300  # Ukuran lingkaran acak
    return angles, radii, sizes

# Header aplikasi
st.title("Lingkaran Acak yang Berubah Setiap Kali Tombol Ditekan 😄")

# Tombol untuk memperbarui data
if st.button('Generate New Data'):
    angles, radii, sizes = generate_random_circle_data()

    # Membuat plot lingkaran acak
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.scatter(angles, radii, s=sizes, alpha=0.5)

    # Menampilkan plot
    st.pyplot(fig)
