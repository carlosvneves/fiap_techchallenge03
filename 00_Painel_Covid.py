import streamlit as st

st.write("# Tech-Challenge 03 - Painel Covid-19 ")

# Carregar e exibir uma imagem JPEG
imagem = open("./pages/images/img_fiap.jpeg", "rb").read()
st.image(imagem, caption='FIAP - Pós-Tech - 3DTAT (maio/2024)', use_column_width=True)

st.write('''
    ---
    ### Grupo: 

    - Carlos Eduardo Veras Neves - RM 353068
    - Emily da Silva Vaculik - RM 352846 
''')



