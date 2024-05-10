import streamlit as st
import pandas as pd


def main():

    # Carregar e exibir uma imagem JPEG
    imagem = open("D:\\FIAP\\FASE 3\\TECH CHALLENGE\\STREAMLIT FASE 3\\COVID.jpeg", "rb").read()
    st.image(imagem, caption='COVID19', use_column_width=True)

if __name__ == "__main__":
    main()


aba1, aba2, aba3 = st.tabs(['PNAD-COVID 19', 'PERGUNTAS', 'GOOGLE CLOUD'])

with aba1:
    st.title('BANCO DE DADOS')

    def main():
        st.markdown('<h5 style="color: white;">PNAD-COVID 19 do IBGE </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


    def main():
        st.markdown('<h5 style="color: blue;">O QUE É? </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


    st.write(''' 
    A Pesquisa Nacional por Amostra de Domicílios - PNAD COVID19 é conduzida 
            pelo IBGE e consiste em um levantamento estatístico. Realizada 
            por telefone, abrange aproximadamente 48 mil domicílios semanalmente 
            desde maio de 2020. Divide-se em duas partes: uma enfoca questões de saúde, 
            como sintomas e busca por atendimento médico; e outra aborda aspectos do 
            mercado de trabalho, como ocupação e rendimentos.
            
            ''')



    def main():
     st.markdown('<h5 style="color: blue;">QUAL O OBJETIVO? </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


    st.write(''' 
    O principal objetivo da PNAD COVID19 é estimar o número de pessoas com sintomas gripais 
            e monitorar os impactos da pandemia da COVID-19 no mercado de trabalho brasileiro. 
            Além disso, busca-se oferecer informações cruciais sobre a pandemia e seus efeitos 
            socioeconômicos. Os resultados são divulgados periodicamente, fornecendo insights 
            importantes para atender às necessidades dos usuários do IBGE e para o planejamento 
            de políticas públicas.       
            ''')
    
with aba2:
    st.title('QUESTIONÁRIOS REALIZADOS NA PESQUISA')

    st.write('''
     Na condução da análise dos dados da Pesquisa Nacional por Amostra de Domicílios - PNAD COVID19, 
             optamos por concentrar nosso foco em 20 perguntas principais. Essa abordagem se deve 
             à necessidade de aprofundamento na compreensão dos aspectos mais relevantes da pandemia
              da COVID-19 e de seus impactos no mercado de trabalho brasileiro. Selecionamos cuidadosamente 
             essas perguntas com o objetivo de capturar informações-chave que nos permitam identificar
              tendências, padrões e correlações significativas nos dados coletados.
              ''')
    
    st.write('''
        Essas 20 perguntas foram escolhidas estrategicamente para abordar diferentes aspectos da pandemia,
              desde a prevalência de sintomas gripais até as repercussões econômicas nas ocupações e 
             rendimentos. Ao nos concentrarmos nessas perguntas principais, buscamos otimizar nossa análise,
              garantindo que nossos esforços sejam direcionados para áreas de maior relevância e interesse 
             para o planejamento e tomada de decisões.
    ''')
    
    st.write('''
    Dessa forma, ao limitar nosso escopo a essas perguntas-chave, esperamos obter insights mais
          profundos e acionáveis que contribuam para uma compreensão abrangente da situação atual
          e que possam subsidiar estratégias eficazes de resposta e mitigação dos impactos da pandemia.
    ''')
    
    def main():
        st.markdown('<h5 style="color: blue;">TABELAS DE PERGUNTAS: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    def main():
        st.markdown('<h5 style="color: white;">Parte 1 - Identificação e Controle: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()


    dados = {
        'CÓDIGO': [
            'UF',
            'CAPITAL' ,
            'RM_RIDE' ,
            'V1022' ,
            'V1023' ,
            'A002' ,
            'A003' ,
            'A004' ,
            'A005'],
            
        'QUESTIONÁRIO': [
             'Unidade da Federação',
            'Capital' ,
            'Região Metropolitana e Região Administrativa Integrada de Desenvolvimento' ,
            'Situação do domicílio' ,
            'Tipo de área' ,
            'Idade do morador' ,
            'Sexo' ,
            'Cor ou raça' ,
            'Escolaridade']}
    
    df = pd.DataFrame(dados)
    st.dataframe(df, width=1000, height=350)

    def main():
            st.markdown('<h5 style="color: white;">Parte B - COVID19 - Todos os moradores: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
            main()


    dados2 = {
        'CÓDIGO': [
            'B0011',
            'B0012',
            'B0013',
            'B0014',
            'B0015',
            'B0016',
            'B0017',
            'B0018',
            'B0019',
            'B00111',
            'B00112',
            'B00113',
            'B002',
            'B009A',
            'B009B',
            'B011',
        ],
        'QUESTIONÁRIO': [
            'Na semana passada teve febre?',
            'Na semana passada teve tosse?',
            'Na semana passada teve dor de garganta?',
            'Na semana passada teve dificuldade para respirar?',
            'Na semana passada teve dor de cabeça?',
            'Na semana passada teve dor no peito?',
            'Na semana passada teve náusea?',
            'Na semana passada teve nariz entupido ou escorrendo?',
            'Na semana passada teve fadiga?',
            'Na semana passada teve perda de cheiro ou sabor?',
            'Na semana passada teve dor muscular?',
            'Na semana passada teve diarreia?',
            'Por causa disso, foi a algum estabelecimento de saúde?',
            'Fez o exame coletado com cotonete na boca e/ou nariz (SWAB)?',
            'Qual o resultado?',
            'Qual foi o resultado do teste? Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas?'
        ]
    }

    dados2['CÓDIGO'] = [codigo.ljust(6, '0') for codigo in dados2['CÓDIGO']]

    df = pd.DataFrame(dados2)

    st.dataframe(df, width=1000, height=600)

    def main():
            st.markdown('<h5 style="color: white;">Parte C - Características de trabalho das pessoas de 14 anos ou mais de idade: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
            main()


    dados3 = {
            'CÓDIGO': [
                'C001' ,
                'C002' , 
                'C003' , 
                ],
                
            'QUESTIONÁRIO': [
                'Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?' ,
                'Na semana passada, estava temporariamente afastado de algum trabalho?' ,
                'Qual o principal motivo deste afastamento temporário?' 
                ]}
        
    df = pd.DataFrame(dados3)
    st.dataframe(df, width=1000, height=150)



with aba3:

    st.title('ARMAZENAMENTO EM NUVEM')

    
    def main():
        st.markdown('<h5 style="color: white;">GOOGLE CLOUD </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    def main():
            st.markdown('<h5 style="color: blue;">Explorando o Google Cloud e o BigQuery para Análise de Dados: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    st.write(''' 
            No mundo moderno impulsionado por dados, as organizações estão cada vez mais recorrendo a soluções 
             em nuvem para lidar com grandes volumes de dados e extrair insights valiosos. Uma dessas 
             plataformas líderes é o Google Cloud, que oferece uma ampla gama de serviços e ferramentas 
             poderosas para armazenamento, processamento e análise de dados em escala.
          ''')  


    def main():
            st.markdown('<h5 style="color: blue;">Google Cloud: Uma Visão Geral </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    st.write(''' 
            O Google Cloud é uma plataforma de computação em nuvem abrangente oferecida pelo Google,
              que fornece uma infraestrutura robusta e flexível para empresas de todos os tamanhos.
              Ele oferece uma ampla variedade de serviços, incluindo armazenamento de dados, computação em nuvem,
              machine learning, inteligência artificial, análise de dados e muito mais.

          ''')  

    def main():
            st.markdown('<h5 style="color: blue;">BigQuery: Uma Ferramenta de Análise de Dados em Escala </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    st.write(''' 
            Dentro do ecossistema do Google Cloud, o BigQuery se destaca como uma das ferramentas mais
              poderosas para análise de dados em larga escala. O BigQuery é um banco de dados de 
             data warehouse totalmente gerenciado e altamente escalável, projetado para executar consultas
              SQL em petabytes de dados de forma rápida e eficiente.
          ''') 

    st.write(''' 
            Com o BigQuery, os usuários podem carregar, consultar e analisar grandes conjuntos de dados 
             sem se preocupar com a infraestrutura subjacente. Ele oferece recursos avançados, como consultas
              federadas, integração com ferramentas de visualização de dados, suporte a machine learning e muito mais.
          ''') 

    def main():
            st.markdown('<h5 style="color: blue;">Conexões e Importância para Análise de Dados </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    
    st.write(''' 
        a.   Escalabilidade e Desempenho: O Google Cloud e o BigQuery oferecem uma infraestrutura
              altamente escalável e de alto desempenho, permitindo que as organizações processem 
             grandes volumes de dados de forma eficiente.


        b.   Integração com Ferramentas de Análise: O BigQuery se integra perfeitamente com uma variedade 
             de ferramentas de análise de dados, como Google Data Studio, Tableau e Looker, facilitando a
              visualização e a interpretação de resultados.


        c.   Análise em Tempo Real: Com recursos como streaming de dados e consultas rápidas,
              o BigQuery permite análise em tempo real de dados em constante evolução, fornecendo 
             insights valiosos para tomada de decisões em tempo hábil.

        d.   Machine Learning e Análise Preditiva: A integração do BigQuery com o Google Cloud
              Machine Learning Engine permite a execução de modelos de machine learning diretamente
              nos dados armazenados no BigQuery, abrindo oportunidades para análise preditiva e descoberta
              de padrões complexos.

        e.   Segurança e Conformidade: O Google Cloud oferece robustas medidas de segurança e
              conformidade para proteger os dados dos clientes, garantindo que as análises sejam
              realizadas em um ambiente seguro e em conformidade com regulamentações relevantes.

             ''')

    st.write(''' 
           Em resumo, o Google Cloud e o BigQuery oferecem uma plataforma poderosa e escalável
              para análise de dados em larga escala, permitindo que as organizações extraiam insights
              valiosos de seus dados para impulsionar a inovação, a eficiência operacional e a vantagem competitiva.
          ''') 

    def main():
            st.markdown('<h5 style="color: white;">Abaixo nossa arquitetura de solução e aplicações realizadas: </h5>', unsafe_allow_html=True)

    if __name__ == "__main__":
        main()

    def main():

    # Carregar e exibir uma imagem JPEG
        imagem = open("D:\\FIAP\\FASE 3\\TECH CHALLENGE\\STREAMLIT FASE 3\\ARQUITETURA DO PROJETO.jpg", "rb").read()
        st.image(imagem, caption='ARQUITETURA', use_column_width=True)

    if __name__ == "__main__":
        main()
    