import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
import plotly.express as px
from urllib.request import urlopen
import json


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


@st.cache_data(ttl=600)
def get_map():
    with urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson') as response:
        Brazil = json.load(response) # Javascrip object notation 
    state_id_map = {}
    for feature in Brazil ['features']:
        feature['id'] = feature['properties']['name']
        state_id_map[feature['properties']['sigla']] = feature['id']
    return Brazil 

def get_map_df(df):
    siglas = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    nomes = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]
    siglas_map = dict(zip(siglas, nomes))

    df['Estado'] = df['sigla_uf'].map(siglas_map)
    return df

def draw_map(df, var, map):

    fig = px.choropleth(
     df, 
     locations = 'Estado', #define the limits on the map/geography
     geojson = map, #shape information
     color = var, #defining the color of the scale through the database
     hover_name = 'Estado', #the information in the box
     hover_data =[var],
     color_continuous_scale="Viridis",     
     center = {"lat": -17.14, "lon": -57.33},
    )
    # fig.update_layout(margin={'r':0,'t':0,'l':0, 'b':0})
    fig.update_geos(fitbounds = "locations", visible = True)
    return fig 

aba1, aba2, aba3 = st.tabs(['INTRODUÇÃO', 'PERFIL','ANÁLISE CLÍNICA'])


with aba1:
    st.title('INTRODUÇÃO')

    st.write(''' 
    Neste estudo, será abordado uma análise dos dados fornecidos pelo estudo PNAD-COVID 19 do IBGE.
              Reconhecido por sua abrangência e confiabilidade, o PNAD-COVID 19 do IBGE oferece uma visão
              detalhada das dinâmicas socioeconômicas durante a pandemia, fornecendo insights valiosos 
             para compreender os impactos da crise sanitária em diversas esferas da sociedade brasileira.
             ''')
    
    st.markdown('<h5 style="color: white;">Seleção dos Meses </h5>', unsafe_allow_html=True)


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
    
    st.markdown('<h5 style="color: white;">a.   Caracterização dos sintomas clínicos da população </h5>', unsafe_allow_html=True)

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

    st.markdown('<h5 style="color: white;">b.   Comportamento da população na época da COVID-19 </h5>', unsafe_allow_html=True)

    st.write(''' 
            O objetivo é fornecer uma análise abrangente sobre como diferentes grupos demográficos, como idade, 
             gênero e região geográfica, responderam às recomendações de saúde pública durante o período de análise.
             Existem diferenças no comportamento entre diferentes grupos demográficos, como idade, gênero 
             e região geográfica? Como a população brasileira se comportou em relação às medidas de
              prevenção da COVID-19 durante os meses de maio, junho e julho?
             
                ''')
    
    st.markdown('<h5 style="color: white;">c.   Características econômicas da Sociedade. </h5>', unsafe_allow_html=True)

    st.write(''' 
            Utilizando os dados fornecidos pelo estudo PNAD-COVID 19 do IBGE, é possível compreender como a 
             crise sanitária afetou os aspectos econômicos do país nesse período desafiador.
             O foco estará em responder a duas perguntas centrais: como as características 
             econômicas da sociedade brasileira foram afetadas pela pandemia da COVID-19 durante
              os meses de maio, junho e julho? Houve variações significativas nos indicadores econômicos?
                          
            ''')
with aba2: #Perfil
    st.title('PERFIL DOS ENTREVISTADOS')

    st.write(''' 
          Antes de qualquer análise aprofundada, é fundamental compreender o perfil da sociedade entrevistada 
                 em qualquer estudo ou pesquisa. Essa compreensão não apenas fornece insights valiosos 
                 sobre as características demográficas e socioeconômicas dos participantes, mas também é 
                 essencial para garantir a relevância e a eficácia das conclusões obtidas.

        Ao entender o perfil da sociedade entrevistada, somos capazes de capturar uma imagem mais precisa e 
                     abrangente das dinâmicas sociais, culturais e econômicas em jogo. Isso nos permite identificar
                      tendências, padrões e disparidades que podem influenciar diretamente as decisões políticas, 
                     estratégias de negócios, políticas públicas e intervenções sociais.
                 
                    ''')

    # POPULAÇÃO ENTREVISTADA AO LONGO DO TEMPO 
    
    st.markdown('<h5 style="color: white;">a. Período Analisado </h5>', unsafe_allow_html=True)
    st.write(''' 
      Separar três meses para analisar os dados do COVID-19, especificamente maio, junho e julho de 2020,
              é estratégico por várias razões. Primeiramente, esses meses representam um período crítico 
             durante a pandemia, marcado por mudanças significativas nas taxas de infecção, hospitalizações
              e políticas de resposta em muitos países. Ao focalizar nesse intervalo, podemos capturar
              as tendências e os padrões emergentes da doença, assim como avaliar a eficácia das medidas 
             implementadas para controlar sua propagação.
             ''')
    df_dados_por_mes = select_view('view_dados_por_mes')    



    
    fig = px.line(df_dados_por_mes, x="mes", y="pop")
    fig.update_layout(title="Análise da População ao Longo do Tempo",
                      xaxis_title="Mês",
                      yaxis_title="População", xaxis_type='category')
    st.plotly_chart(fig)



    # UNIDADE DA FEDERAÇÃO

    st.markdown('<h5 style="color: white;">b. Divisão da população entrevistada por Unidade da Federação </h5>', unsafe_allow_html=True)

    st.write(''' 
      
    A compreensão da divisão das regiões e unidades da federação durante a análise dos dados
              do COVID-19 nos meses de maio, junho e julho de 2020 é de extrema importância
              por diversas razões. Primeiramente, essa divisão permite uma análise mais 
             granular e específica das tendências da pandemia em diferentes áreas geográficas,
              o que é essencial para identificar disparidades regionais e entender como a doença
              se espalhou e impactou diferentes comunidades.

    Além disso, compreender a distribuição geográfica dos casos de COVID-19 ao longo desses três meses
              pode fornecer insights valiosos sobre a eficácia das medidas de controle e resposta 
             adotadas em diferentes regiões. Por exemplo, podemos identificar áreas onde as taxas 
             de transmissão foram mais altas e onde as medidas de mitigação foram mais eficazes, 
             ajudando a informar futuras estratégias de saúde pública.

    Essa análise regional também é crucial para entender as necessidades específicas de cada região 
             em termos de recursos médicos, capacidade hospitalar e intervenções de saúde pública.
              Ao compreender as diferenças regionais nos padrões de infecção e nas respostas à pandemia, 
             podemos direcionar recursos de forma mais eficiente e eficaz para onde são mais necessários, 
             contribuindo para uma resposta mais coordenada e adaptável à crise.
             
             
                ''')

    df_uf = select_view('view_dados_por_uf')

    # fig = px.bar(df_uf, x="sigla_uf", y="pop", 
    #              labels={"sigla_uf": "Unidade da Federação", "pop": "População"},
    #              title="Divisão da População Entrevistada por Unidade da Federação")
    # fig.update_xaxes(type='category')  # Define o eixo X como categórico para evitar a ordenação automática das UF
    # fig.update_layout(xaxis={'categoryorder':'total descending'})  # Ordena as UF por população decrescente
    # 
    # st.plotly_chart(fig)

    #print(get_map_df(df_uf)) 
    brazil_map = get_map()
    fig = draw_map(get_map_df(df_uf), 'pop', brazil_map)
    fig.update_layout(title="Divisão da População Entrevistada por Unidade da Federação")
    fig.update_layout(height = 1080, width = 920)
    st.plotly_chart(fig, theme = "streamlit", use_container_width = False)


    # DOMICILIO 

    st.markdown('<h5 style="color: white;">c. Divisão da população entrevistada por Unidade da Federação/Domicilio</h5>', unsafe_allow_html=True)

    # Carregar os dados
    df_uf_por_domicilio = select_view('view_dados_uf_por_domicilio') 
    # Mapear os valores numéricos para as legendas correspondentes
    situacao_map = {
        1: 'Urbana',
        2: 'Rural'
    }
    df_uf_por_domicilio['situacao_domicilio'] = df_uf_por_domicilio['situacao_domicilio'].astype('int32')
    df_uf_por_domicilio['situacao_domicilio'] = df_uf_por_domicilio['situacao_domicilio'].map(situacao_map)

    # Exibir os dados (opcional)
    # st.write(df_uf_por_domicilio)

    # Criar um gráfico de barras
    
    fig = px.bar(df_uf_por_domicilio, x="sigla_uf", 
                 y="contagem", 
                 title="Divisão da população entrevistada por Unidade da Federação/Domicilio", 
                 color="situacao_domicilio",)
    st.plotly_chart(fig)

    st.write(''' 
      
   Ao analisar os gráficos apresentados, observamos que os estados de São Paulo (SP), Minas Gerais (MG)
          e Rio de Janeiro (RJ) se destacam como os mais entrevistados durante os meses de maio, junho
          e julho de 2020 em relação à situação do domicílio dos entrevistados. Esses estados, como 
         centros populacionais significativos, refletem a representatividade de suas respectivas regiões
          e a densidade populacional, o que pode influenciar nas políticas de saúde pública e nas estratégias 
         de mitigação da pandemia.

Além disso, é interessante notar a predominância dos moradores da zona urbana de São Paulo e da zona
          rural de Minas Gerais entre os entrevistados. Essa disparidade pode refletir as características
          socioeconômicas e demográficas dessas regiões, bem como as diferenças no acesso aos serviços de
          saúde e nas condições de vida entre áreas urbanas e rurais.
         
                        ''')

    # SEXO

    st.markdown('<h5 style="color: white;">d. Divisão da população entrevistada por Sexo </h5>', unsafe_allow_html=True)
    
    st.write(''' 
      
   Ao examinar a divisão de sexo nos entrevistados durante os meses de maio, junho e julho de 2020,
              notamos que o gráfico revela uma distribuição relativamente equilibrada entre homens e
              mulheres. Com cerca de 48% dos entrevistados sendo homens e aproximadamente 52% mulheres,
              essa divisão de gênero proporciona uma visão abrangente da amostra estudada.

    A paridade na participação entre homens e mulheres é um achado importante, pois reflete uma representação
              mais justa e inclusiva da população. Essa distribuição equitativa nos permite obter insights
              mais robustos sobre como o COVID-19 afeta diferentes segmentos da sociedade, considerando as
              possíveis diferenças de gênero em termos de exposição ao vírus, acesso aos cuidados de saúde
              e impactos socioeconômicos.
             
         
                        ''')
    
    df_sexo = select_view('view_dados_por_sexo')

    # Substitua os valores 1 e 2 pelos rótulos "Homem" e "Mulher"
    df_sexo['sexo'] = df_sexo['sexo'].astype('int32')
    df_sexo['sexo'] = df_sexo['sexo'].replace({1: 'Homem', 2: 'Mulher'})


    
    fig = px.pie(df_sexo, values="pop", names="sexo", title="População por sexo", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

    # RAÇA

    st.markdown('<h5 style="color: white;">e. Divisão da população entrevistada por Raça </h5>', unsafe_allow_html=True)
    
   
    df_raca = select_view('view_dados_por_raca') 
    df_raca['raca'] = df_raca['raca'].astype('int32')
    # Mapeie os valores numéricos para os rótulos correspondentes
    raca_map = {1: 'Branca', 2: 'Preta', 3: 'Amarela', 4: 'Parda', 5: 'Indígena', 9: 'Ignorado'}
    df_raca['raca'] = df_raca['raca'].map(raca_map)

    # st.write(df_raca)

    # Crie um gráfico de barras
    fig = px.bar(df_raca, x='raca', y='pop', title="População por raça", color='raca')

    # Defina o título dos eixos
    fig.update_xaxes(title_text='Raça')
    fig.update_yaxes(title_text='População')

    st.plotly_chart(fig)

    st.write(''' 
      
   Essa diversidade racial é um reflexo da complexidade da sociedade brasileira e ressalta a
              importância de uma abordagem inclusiva e sensível à raça na análise dos dados do
              COVID-19. É fundamental reconhecer as disparidades de saúde existentes entre diferentes 
             grupos raciais e étnicos, considerando fatores como acesso aos serviços de saúde, condições
              socioeconômicas e exposição ao vírus.
             
                        ''')

    # IDADE 

    st.markdown('<h5 style="color: white;">f. Distribuição de Idades e Escolaridade dos Entrevistados </h5>', unsafe_allow_html=True)
    
    st.write(''' 
      
            A análise da idade e do nível de escolaridade dos entrevistados nos 
             oferece uma visão abrangente das características demográficas e educacionais
              da amostra estudada. Esses insights são fundamentais para entender como diferentes
              grupos populacionais estão sendo impactados pela pandemia e para informar a formulação 
             de políticas e estratégias de resposta que sejam sensíveis às necessidades específicas de 
             cada segmento da população, de acordo com o seu nível de escolaridade. Também é de se notar que, 
             com a pandemia, necessariamente ocorre algum prejuízo para o desempenho das atividades educacionais formais.
             
             
                        ''')
    
    df_idades = select_view('view_dados_por_idade')

    st.write(df_idades.describe().T)

    # Criar um histograma com paleta de cores Viridis
    fig = px.histogram(df_idades, x='a002', title="Distribuição de Idades dos Entrevistados", nbins=30, 
                       color_discrete_sequence=px.colors.sequential.Viridis)

    # Definir o título dos eixos
    fig.update_xaxes(title_text='Idade')
    fig.update_yaxes(title_text='Contagem')
    fig.update_traces(opacity=0.85, selector=dict(type='histogram'))

    st.plotly_chart(fig)

    # ESCOLARIDADE 
    # st.markdown('<h5 style="color: white;">Distribuição da Escolaridade dos Entrevistados</h5>', unsafe_allow_html=True)
    
    df_escolaridade = select_view('view_dados_por_escolaridade') 

    df_escolaridade['escolaridade'] = df_escolaridade['escolaridade'].astype('int32')                                                       

    # Mapear os valores numéricos para as legendas correspondentes
    escolaridade_map = {
        1: 'Sem instrução',
        2: 'Fundamental incompleto',
        3: 'Fundamental completo',
        4: 'Médio incompleto',
        5: 'Médio completo',
        6: 'Superior incompleto',
        7: 'Superior completo',
        8: 'Pós-graduação, mestrado ou doutorado'
    }
    df_escolaridade['escolaridade'] = df_escolaridade['escolaridade'].map(escolaridade_map)

    # st.write(df_escolaridade)

    # Criar um gráfico de pizza
    fig_pizza = px.pie(df_escolaridade, values='pop_escolaridade', names='escolaridade', title="Distribuição da Escolaridade dos Entrevistados", 
                    color_discrete_sequence=px.colors.qualitative.Dark24)

    # # Adicionar rótulos de título aos gráficos
    fig_pizza.update_layout(title_x=0.5)
    # fig_barras.update_layout(title_x=0.5)

    # Configurar o layout para exibir os gráficos lado a lado
    fig_pizza.update_layout(showlegend=True)
    # fig_barras.update_layout(showlegend=False)

    st.plotly_chart(fig_pizza, use_container_width=True)


    st.markdown('<h5 style="color: white;">g. Relação entre a Covid e o Mercado de trabalho </h5>', unsafe_allow_html=True)


    # MERCADO DE TRABALHO
    df_dados_c001 = select_view('view_dados_c001_semana_passada_trabalho').set_index('MES')
    df_dados_c002 = select_view('view_dados_c002_afastamento_temp').set_index('MES')
    df_dados_c003 = select_view('view_dados_c003_motivo_afastamento').set_index('MES')
    df_dados_c007d = select_view('view_dados_afastamento_serv_esfera').set_index('MES')

    df_trabalho_afastamento = df_dados_c001[['pop_semana_passada_trabalho_sim']].join(df_dados_c002[['pop_semana_passada_afastado_temp_sim']])

    fig = px.line(df_trabalho_afastamento,  x = df_trabalho_afastamento.index, 
            y = df_trabalho_afastamento.columns, 
                title = 'Trabalho e Afastamento',)
    fig.update_layout(xaxis_title="Mês",
                        yaxis_title="População", xaxis_type='category')
    
    st.plotly_chart(fig, use_container_width=True)
     
    st.write('''
        Entre maio e julho de 2020 houve um aumento no número de pessoas trabalhando na semana anterior, ao passo em que houve uma redução no número de afastamentos.
    ''')

    fig = px.bar(df_dados_c003, x = df_dados_c003.index, y = df_dados_c003.columns[1:9], title = 'Motivo do afastamento')
    fig.update_layout(xaxis_title="Mês",
                      yaxis_title="População", xaxis_type='category')
    st.plotly_chart(fig, use_container_width=True)

    st.write('''
        Nos mesmo período, o número de entrevistados alegando afastamento em face da quarentena foi diminuindo ao longo do tempo. Por outro lado, os afastados 
             em função de licença saúde aumentou.''')

    fig = px.bar(df_dados_c007d, x = df_dados_c007d.index, y = df_dados_c007d.columns[1:], title = 'Trabalhava em qual esfera de governo na semana anterior', barmode = 'group')
    fig.update_layout(xaxis_title="Mês",
                      yaxis_title="População", xaxis_type='category')
    st.write('''
        A quantidade de pessoas que não trabalhavam em qualquer esfera de governo foi aumentando ao longo do tempo.
             
        ''')
    st.plotly_chart(fig, use_container_width=True)


with aba3: #ANÁLISE CLÍNICA


    st.title('IDENTIFICAÇÃO DE CASOS POSITIVOS')

    st.write(''' 
      Ademais do perfil socio-econômico da população, é importante entender qual foi o comportamento da população quanto à realização de exames para identificação da COVID-19. Afinal, a evolução da pandemia só pode ser compreendida a partir de dados sobre casos confirmados. 
      Assim, os casos positivos de COVID-19 em cada estado, juntamente com informações sobre
              idades e distribuição entre zonas rurais e urbanas, é crucial para uma resposta eficaz
              à pandemia. Essa abordagem detalhada permite uma análise mais completa dos padrões de 
             propagação da doença e das características demográficas das áreas afetadas.
      Ao examinar os casos positivos em cada estado, podemos identificar áreas de maior incidência da doença,
              permitindo uma alocação mais eficiente de recursos de saúde e a implementação de medidas
              de controle mais direcionadas. Além disso, entender a distribuição por idade nos casos 
             positivos nos fornece informações sobre grupos populacionais mais vulneráveis, orientando 
             a priorização de campanhas de vacinação e medidas de proteção para essas faixas etárias específicas.
             
             
    ''')

    st.markdown('<h5 style="color: white;">a. Sintomas relatados ao longo dos meses </h5>', unsafe_allow_html=True)
    
    df_dados_b00111 = select_view('view_dados_b00111_perda_olfato_paladar').set_index('MES')
    df_dados_b00112 = select_view('view_dados_b00112_dor_muscular').set_index('MES')
    df_dados_b00113 = select_view('view_dados_b00113_diarreia').set_index('MES')
    df_dados_b0011 = select_view('view_dados_b0011_febre').set_index('MES')
    df_dados_b0012 = select_view('view_dados_b0012_tosse').set_index('MES')
    df_dados_b0013 = select_view('view_dados_b0013_dor_garganta').set_index('MES')
    df_dados_b0014 = select_view('view_dados_b0014_dificuldade_respirar').set_index('MES')
    df_dados_b0016 = select_view('view_dados_b0016_dor_peito').set_index('MES')
    df_dados_b0017 = select_view('view_dados_b0017_nausea').set_index('MES')
    df_dados_b0018 = select_view('view_dados_b0018_coriza').set_index('MES')
    
    # primeiro conjunto de sintomas
    df_sintomas_1 = (df_dados_b00111[['pop_semana_passada_perda_olfato_paladar_sim']]
                 .join(df_dados_b00112['pop_semana_passada_dor_muscular_sim'])
                 .join(df_dados_b00113[ 'pop_semana_passada_diarreia_sim'])
                 .join(df_dados_b0017['pop_semana_passada_nausea_sim']))

    fig = px.line(df_sintomas_1, x = df_sintomas_1.index, 
        y = ['pop_semana_passada_perda_olfato_paladar_sim', 
             'pop_semana_passada_dor_muscular_sim', 
             'pop_semana_passada_diarreia_sim', 
             'pop_semana_passada_nausea_sim'])
    fig.update_layout(title="Sintomas relacionados a perda de olfato, paladar, diarreia e dores musculares na semana anterior",
                      xaxis_title="Mês",
                      yaxis_title="População", xaxis_type='category')
    st.plotly_chart(fig, use_container_width=True)

    # segundo conjunto de sintomas
    df_sintomas_2 = (df_dados_b0011[['pop_semana_passada_febre_sim']]                        
                 .join(df_dados_b0012['pop_semana_passada_tosse_sim'])
                 .join(df_dados_b0013[ 'pop_semana_passada_dor_garganta_sim']))

    fig = px.line(df_sintomas_2, x = df_sintomas_1.index, 
            y = df_sintomas_2.columns, 
                title = 'Sintomas relacionados a febre e tosse na semana anterior',)
    fig.update_layout(xaxis_title="Mês",
                        yaxis_title="População", xaxis_type='category')
    st.plotly_chart(fig, use_container_width=True)

    # terceiro conjunto de sintomas
    df_sintomas_3 = (df_dados_b0014[['pop_semana_passada_dificuldade_respirar_sim']]
                 .join(df_dados_b0016['pop_semana_passada_dor_peito_sim'])
                 .join(df_dados_b0018[ 'pop_semana_passada_coriza_sim']))

    fig = px.line(df_sintomas_3, x = df_sintomas_1.index, 
        y = df_sintomas_3.columns, 
              title = 'Sintomas relacionados a dificuldade de Respiração')
    fig.update_layout(xaxis_title="Mês",
                      yaxis_title="População", xaxis_type='category')
    st.plotly_chart(fig, use_container_width=True)
 
    st.write('''
        De maio a julho de 2020, apenas os sintomas relacionados a perda de olfato, paladar, diarreia e dores musculares na semana anterior 
              tiveram uma tendência de alta a partir do mês 6. Em todos os outros grupos de sintomas, houve a redução no relato de 
              sua ocorrência na semana anterior.
    ''')
    
    st.markdown('<h5 style="color: white;">a. Realização de teste por Swab (entre maio e julho de 2020)</h5>', unsafe_allow_html=True)

    
    st.write('''

    De maio a julho de 2020, a maior parte dos entrevistados não realizou o exame de Swab (66,8%).


    ''')

    df_dados_b009a_swab = select_view('view_dados_b009a_swab').T

    df_dados_b009a_swab['resultado'] = ['Sim', 'Não', 'Ignorado']
    df_dados_b009a_swab.columns.values[0] = 'pop'

    st.write(df_dados_b009a_swab)



    fig =px.pie(df_dados_b009a_swab, values = 'pop', names='resultado', title="Realização de teste por Swab (entre maio e julho de 2020)")
    #
    st.plotly_chart(fig)

    st.write('''

    No mesmo período, De maio a julho de 2020, a maior parte dos entrevistados não realizou o exame de Swab (66,8%).


    ''')
    
    # Mapear os valores numéricos para as legendas correspondentes
    rotulos_map = {
        1: 'Positivo',
        2: 'Negativo',
        3: 'Inconclusivo',
        4: 'Ainda não recebeu o resultado',
        9: 'Ignorado',
        # Adicione outras entradas conforme necessário
    }

    df_dados_b009b_swab = select_view('view_dados_b009b_swab_resultado')
    df_dados_b009b_swab = df_dados_b009b_swab.loc[2, :]
    df_dados_b009b_swab = df_dados_b009b_swab.iloc[2:7].reset_index()
    df_dados_b009b_swab['resultado'] = rotulos_map.values()

    df_dados_b009b_swab.columns.values[1] = 'pop'


    fig =px.pie(df_dados_b009b_swab, values = 'pop', names='resultado', title="Resultados do teste por Swab (entre maio e julho de 2020)")
    # #
    st.plotly_chart(fig)

    st.write('''

    Entre aqueles que fizeram o teste, 26,9% testou positivo. Este resultado deve ser avaliado com cuidado, visto que a maior parte daqueles que respondeu a pergunta não fez o teste.

    ''')
