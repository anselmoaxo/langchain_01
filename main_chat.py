from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Modelo de linguagem
modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5
)

# Prompt correto usando from_messages
prompt_sugestao = ChatPromptTemplate.from_messages([
    # system estava escrito errado (sytem)
    ("system", "Você é um assistente de viagem que responde perguntas sobre destinos turísticos. Seu nome é Sr. Viagens."),
    ("placeholder", "{historico}"),
    # Mensagem do usuário
    ("human", "{query}")
])

# Cadeia: Prompt → Modelo → Parser
cadeia = prompt_sugestao | modelo | StrOutputParser()

memoria =  {}
sessao = 'lanchain'

def historioco_de_sessao(sessao : str):
    if sessao not in memoria:
        memoria[sessao] = InMemoryChatMessageHistory()
    return memoria[sessao]


# Perguntas
lista_perguntas = [
    "Qual a capital da Taiwan?",
    "Qual é a melhor época do ano para visitar?"
]

cadeia_com_memoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=historioco_de_sessao,
    input_message_key="query",
    history_message_key="historico"
)

# Execução correta
for pergunta in lista_perguntas:
    resposta = cadeia_com_memoria.invoke(
        {"query": pergunta}, # invoke precisa de dicionário
        config={"session_id": sessao}
    )
    
    print(f"Pergunta: {pergunta}")
    print(f"Resposta: {resposta}\n")  # resposta já é string
