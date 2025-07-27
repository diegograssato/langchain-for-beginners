import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


client = AzureOpenAI()

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']
prompt = "Este é um teste. Se você recebeu a requisição responda 'Teste OK'."
completion = client.chat.completions.create(
    model=deployment,
    messages=[{'role': 'user', 'content': prompt}]
)


# Executa a chamada ao modelo
# print(completion.model_dump_json())
# print(completion.to_json())
print(completion.choices[0].message.content)
