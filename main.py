from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
#cliente = OpenAI(api_key=api_key)



modelo_prompt = PromptTemplate(
    template="Sugira um filme dado meu {interesse}.",
    input_variables=["interesse"]
)



modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

cadeia = modelo_prompt | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {
        "interesse" : " ficção cientifica"
    }
)


print(resposta)