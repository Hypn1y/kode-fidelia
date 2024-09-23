import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write ("Anda memasukkan", x, ' ', sx)
sy = st.text_input("Dikonversi ke", "C")
y = 0
if (sx == 'C'):
  if(sy == 'C'):
    y = x
  elif(sy == 'F'):
    y = (x * 9/5) + 32
  elif sy == 'K'
     y = x + 273.15

elif sx == 'F':  
    if sy == 'C':  
        y = (x - 32) * 5/9
    elif sy == 'F':  
        y = x
    elif sy == 'K':  
        y = (x - 32) * 5/9 + 273.15

elif sx == 'K':  
    if sy == 'C':  
        y = x - 273.15
    elif sy == 'F': 
        y = (x - 273.15) * 9/5 + 32
    elif sy == 'K':  
        y = x
st.write (x, ' ', sx, ' = ', y , sy)
