import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

st.title("Fisika Komputasi Awan")
st.title("Enrico Frans Ganya")
circle = Circle((0, 0), 1, color='red', fill=False, linewidth=2, linestyle='-', alpha=0.2)
x = []
y = []
color = []
size = []
x.append(0)
y.append(0)
color.append((0., .7, 0.))
size.append(371)

# Fungsi untuk menempatkan lingkaran kecil agar menyentuh lingkaran besar
def place_touching_big_circle(small_radius, big_radius=1):
    # Pilih sudut acak
    angle = random.uniform(0, 2 * np.pi)
    # Tempatkan lingkaran kecil sehingga menyentuh garis lingkaran besar
    x0 = (big_radius - small_radius) * np.cos(angle)
    y0 = (big_radius - small_radius) * np.sin(angle)
    return x0, y0

if st.button("Click"):
    for i in range(111):
        # Radius acak untuk lingkaran kecil
        small_radius = random.uniform(0.05, 0.2)
        
        # Tempatkan lingkaran kecil tepat menyentuh lingkaran besar
        x0, y0 = place_touching_big_circle(small_radius)
        
        # Tambahkan ke daftar
        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713 * small_radius)

# Gambar lingkaran besar dan lingkaran kecil
fig, ax = plt.subplots(figsize=(16, 16))
ax.add_patch(circle)

for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='green', linestyle='--', alpha=0.2)

ax.scatter(x, y, c=color, s=size, alpha=0) 

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Lingkaran Kecil Menyentuh Garis Lingkaran Besar')
ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Tambahan keterangan dan pembatas
st.caption("Lingkaran kecil menyentuh garis lingkaran besar")
st.divider()
st.text("UTS menggunakan GitHub dan Streamlit.")
st.divider()
