from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import os
from pydantic import BaseModel, Field
from langchain_core.globals import set_debug

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

set_debug(True)
class Destino(BaseModel):
    filme: str = Field("Filme recomendado")
    motivo: str = Field("Motivo da recomendação")
    
parseador = JsonOutputParser(pydantic_object=Destino)


modelo_prompt = PromptTemplate(
    template="Sugira um filme dado meu {interesse}.{saida}",
    input_variables=["interesse"],
    partial_variables={"saida": parseador.get_format_instructions()}
)

modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

cadeia = modelo_prompt | modelo | parseador

resposta = cadeia.invoke(
    {"interesse": "ficção científica"}
)

print(resposta)