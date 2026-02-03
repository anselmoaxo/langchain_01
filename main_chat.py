
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

lista_perguntas = [
    "Qual a capital da Taiwan?",
    "Qual é a melhor época do ano para visitar?"
]

for pergunta in lista_perguntas:
    resposta = modelo.invoke(pergunta)
    print(f' pergunta : {pergunta} \n resposta : {resposta.content}')

