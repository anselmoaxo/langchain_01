from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
#cliente = OpenAI(api_key=api_key)

numeros_dias = 7
destino = "Gramado, Brasil"
numero_criancas = 1


modelo_prompt = PromptTemplate(
    template="Crie um itinerário detalhado para uma viagem de {dias} dias para {destino}, incluindo atividades adequadas para {criancas} criança(s)."
)

prompt = modelo_prompt.format(
    dias=numeros_dias,
    destino=destino,
    criancas=numero_criancas
)


modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
git
    
resposta = modelo.invoke(prompt)
print(resposta.content)