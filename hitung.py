import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write ("Anda memasukkan", x, ' ', sx)

y = st.number_input("Masukkan angka")
sy = st.text_input("Satuan", "C")
st.write ("Anda memasukkan", y, ' ', sy)
