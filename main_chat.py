
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

prompt_sugestao = ChatPromptTemplate(
    [
        ('sytem', 'Você é um assistente de viagem que responde perguntas sobre destinos turísticos, seu nome é Sr.Viagens'),
        ('placeholder', '{historico}'),
        ('human', '{query}'),
    ]
)

cadeia = prompt_sugestao | modelo | StrOutputParser()

lista_perguntas = [
    "Qual a capital da Taiwan?",
    "Qual é a melhor época do ano para visitar?"
]

for pergunta in lista_perguntas:
    resposta = modelo.invoke(pergunta)
    print(f' pergunta : {pergunta} \n resposta : {resposta.content}')

