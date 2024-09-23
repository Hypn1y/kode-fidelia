import streamlit as st

x1 = st.number_input("Masukkan angka 1")
sx1 = st.text_input("Satuan 1", "C")
st.write ("Anda memasukkan", x1, ' ', sx1)

x2 = st.number_input("Masukkan angka 2")
s2 = st.text_input("Satuan 2", "C")
st.write ("Anda memasukkan", x2, ' ', sx2)
