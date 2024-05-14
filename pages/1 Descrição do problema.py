import streamlit as st
import pandas as pd


#     # Carregar e exibir uma imagem JPEG
imagem = open("./pages/images/img_covid_banner.jpeg", "rb").read()
st.image(imagem, caption='COVID19', use_column_width=True)

st.title('DESCRIÇÃO DO PROBLEMA')

st.write(''' 
Identificação do problema enfrentado pelo hospital: entender o comportamento 
         da população durante a pandemia da COVID-19 e determinar quais
          indicadores são essenciais para o planejamento de um possível novo surto da doença.
          ''')  


st.markdown('<h5 style="color: blue;">ANÁLISE PROPOSTA:</h5>', unsafe_allow_html=True)

st.write(''' 
Descrição da abordagem proposta para análise dos dados, incluindo o uso do estudo 
         PNAD-COVID 19 do IBGE como base confiável de dados.
         ''')


st.write(''' 
Enfatizar a seleção criteriosa de perguntas da pesquisa para abordar os aspectos 
         essenciais do problema.
                   ''')  


st.write(''' 
Mencionar o uso de banco de dados em nuvem para organização e análise dos dados.
                   ''')  


st.markdown('<h5 style="color: blue;">Definir as características-chave a serem analisadas: </h5>', unsafe_allow_html=True)

st.write(''' 
a.   Caracterização dos sintomas clínicos da população;

b.   Comportamento da população na época da COVID-19;

c.   Características econômicas da Sociedade.
           ''')  



