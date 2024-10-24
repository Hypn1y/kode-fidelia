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
color.append((0.,.7,0.))
size.append(371)

# Fungsi untuk memeriksa apakah lingkaran kecil berada di dalam lingkaran besar
def is_inside_big_circle(x0, y0, radius, big_radius=1):
    return np.sqrt(x0**2 + y0**2) + radius <= big_radius

if st.button("Click"):
    for i in range(111):
        while True:
            # Generate posisi acak untuk lingkaran kecil
            x0 = 2*(random.random() - 0.5)
            y0 = 2*(random.random() - 0.5)
            
            # Radius acak untuk lingkaran kecil
            small_radius = random.uniform(0.05, 0.2)
            
            # Periksa apakah lingkaran kecil berada di dalam lingkaran besar
            if is_inside_big_circle(x0, y0, small_radius):
                break
        
        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713 * small_radius)

# Gambar lingkaran besar dan lingkaran kecil
fig, ax = plt.subplots(figsize=(16, 16))
ax.add_patch(circle)

for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='green', linestyle='--', alpha=0.2)

ax.scatter(x, y, c=color, s=size, alpha=0.5) 

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Data Acak yang berubah setiap tombol ditekan')
ax.grid(True, linestyle='-.')
ax.tick_params(labelcolor='r', labelsize='medium', width=3)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Tambahan keterangan dan pembatas
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")
st.divider()
st.text("UTS menggunakan GitHub dan Streamlit.")
st.divider()
