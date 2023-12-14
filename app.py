import pandas as pd
import streamlit as st
from PIL import Image

import src.answers as asw
from src.extraction import load_data

st.set_page_config(page_title='Início',
    page_icon='📋',layout="wide"
    )

st.sidebar.markdown('# Xtreme Groovi Bikes Sales')
st.sidebar.markdown("""---""")
image = Image.open( 'logo.png' )
st.sidebar.image( image, width=270)

st.sidebar.markdown('### Revenda de bicicletas')
st.sidebar.markdown("""---""")
st.markdown('## Sobre o projeto')
st.write("#### Diante do aumento constante do valor dos veículos usados, a renomada XGB Sales está em busca de ampliar sua atuação no mercado. Nosso objetivo é facilitar a busca por excelentes oportunidades de negócio, especialmente no segmento de motocicletas para revenda. Comprometidos com a qualidade e satisfação dos nossos clientes, buscamos continuamente as melhores opções disponíveis no mercado. Ressaltamos que todo o contexto, personagens e perguntas apresentados são totalmente fictícios.")

def create_dataframe_section(df):
    
    st.markdown("## - Análise dos Dados")
    
    col_1, col_2 = st.columns(2)

    col_1.header("Base de Dados")
    col_1.dataframe(df, height=530)

    col_2.header("Descrições")

    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | Fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilometros percorrido pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de Quilometros percorridos a cada ano |
                        | km_per_month | Quantidade de Quilometros percorridos por mês |
                        | company | Fabricanete da Motocicleta |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Principais Análises")

    st.subheader(
        "EmpresaS que tem bicicletas mais caras cadastradas e as que possuem maior quantidade de veículos cadastrados"
    )
    asw.rd3_question_5(df)

    st.subheader(
        "Quantas bicicletas estão sendo vendidas pelos seus proprietários e quantas bicicletas estão sendo vendidas pelos distribuidores")
    asw.rd1_question_9(df)

    st.subheader("Quantas bicicletas estão sendo vendidas são de um único proprietário?")
    asw.rd1_question_13(df)

    st.subheader(
        "As bicicletas de alta quilometragem são mais caras do que as bicicletas de menor quilometragem?"
    )
    asw.rd1_question_14(df)

    st.subheader(
        "As bicicletas com um proprietário único são mais caras do que as outras bicicletas?"
    )
    asw.rd2_question_1(df)

    st.subheader(
        "As bicicletas que têm mais proprietários são também as bicicletas com mais quilómetros percorridos em média?"
    )
    asw.rd2_question_2(df)

    st.subheader("Qual empresa tem mais bicicletas cadastradas?")
    asw.rd2_question_7(df)

    st.subheader("Qual empresa tem as bicicletas mais caras do mercado?")
    asw.rd3_question_2(df)

    

    st.subheader("Quais bicicletas são boas para comprar?")
    asw.rd3_question_7(df)


def create_main_layout():
    df = load_data()

    create_dataframe_section(df)

    create_answers_section(df)


if __name__ == "__main__":
    create_main_layout()