import os
import logging
from langchain_openai import AzureChatOpenAI, AzureOpenAI, ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import LLMResult
from langchain_openai import AzureOpenAIEmbeddings

from typing import Any, Dict, List

from dotenv import load_dotenv

# import dotenv
load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "").strip()
assert API_KEY, "ERROR: Azure OpenAI Key is missing"

class LoggingHandler(BaseCallbackHandler):
    def on_chat_model_start(
        self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], **kwargs
    ) -> None:
        print("Chat model started")

    def on_llm_end(self, response: LLMResult, **kwargs) -> None:
        print(f"Chat model ended, response: {response}")

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs
    ) -> None:
        print(f"Chain {serialized.get('name')} started")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs) -> None:
        print(f"Chain ended, outputs: {outputs}")


callbacks = [LoggingHandler()]

# O ChatModel é um componente LangChain então ele possui o protocolo invoke()
# logging.basicConfig(
#     stream=sys.stdout,
#     format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
#     level=logging.INFO,
# )
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i + 1}:\n\n" +
                d.page_content for i, d in enumerate(docs)]
        )
    )


def pretty_print(response):
    try:
        print(
            f"\n{'-' * 100}\n" +
            f"\n{response.content}" if response.content else str(
                response)
        )
    except Exception as e:
        print(
            f"\n{'-' * 100}\n" +
            f"\n{response}" if response else str(e)
        )


def initialize_llm(agent_type: str = "azure") -> BaseChatOpenAI:

    load_dotenv()

    match agent_type:
        case "azure":
            logger.info("Using AzureOpenAI.")
            # O ChatModel é um componente LangChain então ele possui o protocolo invoke()
            """
            model: o nome do modelo
            temperature: a temperatura de amostragem
            timeout: tempo limite da solicitação
            max_tokens: máximo de tokens para gerar
            stop: sequências de parada padrão
            max_retries: número máximo de vezes para repetir solicitações
            api_key: Chave de API para o provedor do modelo
            base_url: ponto final para enviar solicitações
            """
            llm = AzureChatOpenAI(model=os.environ['AZURE_OPENAI_DEPLOYMENT_MODEL'], temperature=0.1)

            openia = OpenAI(model=os.environ['AZURE_OPENAI_DEPLOYMENT_MODEL'], temperature=0.1)

            embeddings = AzureOpenAIEmbeddings(
                model=os.environ['AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_MODEL'],
                azure_deployment=os.environ['AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME']
            )

    return llm, openia, embeddings
