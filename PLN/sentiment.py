import streamlit as st #utilizado para fazer a criação do sistema.
import nltk #criar a maquina preditiva/PLN
from nltk.sentiment.vader import SentimentIntensityAnalyzer #pacote para analisar o input

st.write("Custumer satisfaction analysis")
user_input = st.text_input("Give us your Feedback:") #entrada de dados pelo streamlit

nltk.download("vader_lexicon") #onde vai se usar os dados para identificação de sentimentos.
sentiment = SentimentIntensityAnalyzer() #atribui a função do pacote a uma variavel.
score = sentiment.polarity_scores(user_input) #pede para essa função do pacote analisar o input fonecido pelo usuario.

if score == 0:
    st.write("")
elif score["neg"] != 0:
    st.write("Negative Feedback!")
elif score["pos"] != 0:
    st.write("Positive Feedback!") 