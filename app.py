import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregar dados
df = pd.read_csv("pizzas.csv")

# Treinamento do modelo
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x, y)

# Layout e estilo da página
st.set_page_config(page_title="Previsão de Preço de Pizzas", page_icon="🍕")

# Estilizando a interface
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f5f5f5;
            color: #333333;
            font-family: Arial, sans-serif;
        }
        .stTitle {
            color: #ff4b4b;
            text-align: center;
            font-size: 3em;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e subtítulo
st.markdown("<h1 class='stTitle'>🍕 Previsão de Preço de Pizzas</h1>", unsafe_allow_html=True)
st.write("Informe o diâmetro da pizza abaixo e veja o preço previsto.")

# Separador
st.divider()

# Entrada do usuário sem limites
diametro = st.number_input("Digite o tamanho da pizza (em polegadas):")

# Previsão e exibição de resultado
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.markdown(f"""
    <div style="text-align: center; font-size: 1.5em;">
        O valor estimado para uma pizza de tamanho <strong>{diametro:.2f}</strong> é de 
        <span style="color: #ff4b4b;"><strong>R${preco_previsto:.2f}</strong></span>.
    </div>
    """, unsafe_allow_html=True)

# Rodapé
st.write("---")
st.markdown("<p style='text-align: center;'>🍕 Aplicação criada para previsão de preço de pizzas 🍕</p>", unsafe_allow_html=True)
