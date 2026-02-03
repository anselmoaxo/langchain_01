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

set_debug(Falsegit)
class Destino(BaseModel):
    cidade: str = Field("cidade recomendada")
    motivo: str = Field("Motivo da recomendação")
    
class Restaurantes(BaseModel):
    cidade: str = Field("cidade recomendada")
    restaurantes : str = Field("Restaurante recomendados")
    
parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)


destino_prompt = PromptTemplate(
    template="Sugira uma cidade para visitar {interesse}.{saida}",
    input_variables=["interesse"],
    partial_variables={"saida": parseador_destino.get_format_instructions()}
)


restaurante_prompt = PromptTemplate(
    template="Sugira uma restaurantes para visitar {cidade}.{saida}",
    input_variables=["interesse"],
    partial_variables={"saida": parseador_restaurantes.get_format_instructions()}
)

prompt_cutural =PromptTemplate(
    template="Sugira atividades culturais {cidade}."
)

modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

cadeia1 = destino_prompt | modelo | parseador_destino
cadeia2 = restaurante_prompt | modelo | parseador_restaurantes
cadeia3 = prompt_cutural | modelo | StrOutputParser()

cadeia = (cadeia1 | cadeia2 | cadeia3)

resposta = cadeia.invoke(
    {"interesse": "interior de São Paulo"}
)

print(resposta)