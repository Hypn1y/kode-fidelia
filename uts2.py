import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Fungsi untuk memeriksa apakah lingkaran kecil berada di dalam lingkaran besar
def is_inside_big_circle(x, y, big_radius):
    return np.sqrt(x**2 + y**2) + 0.1 <= big_radius

# Fungsi untuk menggambar lingkaran besar dan lingkaran-lingkaran kecil di dalamnya
def plot_circles():
    fig, ax = plt.subplots()
    
    # Lingkaran besar dengan radius 1
    big_circle = Circle((0, 0), 1, color='lightblue', fill=False, linewidth=2)
    ax.add_patch(big_circle)
    
    # Lingkaran-lingkaran kecil dengan lokasi, ukuran, dan warna acak
    num_small_circles = 10
    for _ in range(num_small_circles):
        while True:
            # Koordinat acak untuk lingkaran kecil
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
            
            # Memastikan lingkaran kecil berada di dalam lingkaran besar
            if is_inside_big_circle(x, y, 1):
                break
        
        # Ukuran dan warna acak untuk lingkaran kecil
        small_radius = np.random.uniform(0.05, 0.2)
        color = np.random.rand(3,)
        
        # Tambahkan lingkaran kecil
        small_circle = Circle((x, y), small_radius, color=color, fill=True)
        ax.add_patch(small_circle)
    
    # Setting tampilan plot
    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title('Lingkaran dengan Lingkaran Kecil di Dalamnya')
    plt.grid(False)
    plt.axis('off')
    
    st.pyplot(fig)

# Judul aplikasi
st.title("Lingkaran dan Lingkaran-Lingkaran Kecil di Dalamnya")

# Tampilkan lingkaran
plot_circles()
