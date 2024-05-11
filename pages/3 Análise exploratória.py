import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

# Carregar e exibir uma imagem JPEG
imagem = open("./pages/images/img_data_explore.jpeg", "rb").read()
st.image(imagem, caption='ANÁLISE', use_column_width=True)

# Carregar e exibir uma imagem JPEG
imagem = open("./pages/images/img_data_explore.jpeg", "rb").read()
st.image(imagem, caption='ANÁLISE', use_column_width=True)

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(credentials=credentials)


@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

def select_view(view_name):  
    rows = run_query(f"SELECT * FROM `postechfiaptc03may2024.microdados_covid19.{view_name}`")
    return pd.DataFrame(rows)
     

aba1, aba2, aba3, aba4, aba5 = st.tabs(['INTRODUÇÃO', 'PERFIL', 'SOCIODEMOGRÁFICO', 'ECONÔMICO', 'ANÁLISE CLÍNICA'])


with aba1:
    st.title('INTRODUÇÃO')

    st.write(''' 
    Neste estudo, será abordado uma análise dos dados fornecidos pelo estudo PNAD-COVID 19 do IBGE.
              Reconhecido por sua abrangência e confiabilidade, o PNAD-COVID 19 do IBGE oferece uma visão
              detalhada das dinâmicas socioeconômicas durante a pandemia, fornecendo insights valiosos 
             para compreender os impactos da crise sanitária em diversas esferas da sociedade brasileira.
             ''')
    
    st.markdown('<h5 style="color: blue;">Seleção dos Meses </h5>', unsafe_allow_html=True)


    st.write(''' 
      A análise dos dados será aprofundada referentes aos meses de maio, junho e julho 
             por diversas razões estratégicas. Primeiramente, esse período coincide com diferentes 
             fases da pandemia, proporcionando uma visão longitudinal que nos permite observar 
             possíveis mudanças e tendências ao longo do tempo. Além disso, esses meses abrangem
              períodos-chave em termos de medidas de controle da pandemia, como a implementação de 
             lockdowns, flexibilizações de restrições e avanços na campanha de vacinação. 
             Essa diversidade temporal nos permitirá capturar nuances importantes das respostas socioeconômicas 
             à crise sanitária, fornecendo insights valiosos para políticas públicas e estratégias de intervenção.
                                ''')
    st.write(''' 
        Portanto, a escolha desses três meses como período de aprofundamento da análise se justifica 
             pela sua representatividade na trajetória da pandemia, oferecendo uma base sólida para 
             compreendermos os desafios e oportunidades enfrentados pela população brasileira diante
              desse contexto sem precedentes.
                                ''')
    
    st.markdown('<h5 style="color: blue;">a.   Caracterização dos sintomas clínicos da população </h5>', unsafe_allow_html=True)

    st.write(''' 
        A compreensão detalhada dos sintomas clínicos relatados pela população nos permitirá não apenas 
                    identificar possíveis tendências e variações ao longo do tempo, mas também estabelecer 
                    conexões importantes entre a presença de sintomas específicos e a progressão da doença.
                    A partir dessas análises, poderemos desenvolver abordagens mais eficazes para o diagnóstico
                    precoce, tratamento adequado e prevenção da disseminação do vírus.
        Quais sintomas foram mais comuns entre a população durante os meses analisados?
        Existem padrões ou correlações entre certos sintomas e a gravidade da doença?
        Como essas informações podem orientar políticas de saúde e estratégias de intervenção diante da pandemia da COVID-19?

                ''')

    st.markdown('<h5 style="color: blue;">b.   Comportamento da população na época da COVID-19 </h5>', unsafe_allow_html=True)

    st.write(''' 
            O objetivo é fornecer uma análise abrangente sobre como diferentes grupos demográficos, como idade, 
             gênero e região geográfica, responderam às recomendações de saúde pública durante o período de análise.
             Existem diferenças no comportamento entre diferentes grupos demográficos, como idade, gênero 
             e região geográfica? Como a população brasileira se comportou em relação às medidas de
              prevenção da COVID-19 durante os meses de maio, junho e julho?
             
                ''')
    
    st.markdown('<h5 style="color: blue;">c.   Características econômicas da Sociedade. </h5>', unsafe_allow_html=True)

    st.write(''' 
            Utilizando os dados fornecidos pelo estudo PNAD-COVID 19 do IBGE, é possível compreender como a 
             crise sanitária afetou os aspectos econômicos do país nesse período desafiador.
             O foco estará em responder a duas perguntas centrais: como as características 
             econômicas da sociedade brasileira foram afetadas pela pandemia da COVID-19 durante
              os meses de maio, junho e julho? Houve variações significativas nos indicadores econômicos?
                          
                ''')
with aba2:
    client = bigquery_client()

    # Perform query.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    #
    # rows = run_query("SELECT * FROM `postechfiaptc03may2024.microdados_covid19.view_dados_por_sexo`")
    #
    # df_dados_por_sexo = pd.DataFrame(rows).set_index("sexo")
    #
    # st.write("# Divisão por sexo")
    # st.write(df_dados_por_sexo) 
    #
    #


    # # Print results.
    # st.write("Some:")
    # for row in rows:
    #     st.write(row)

