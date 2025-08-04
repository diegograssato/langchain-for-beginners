import os
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA,LLMChain
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from indexa_documentos import CarregadorDocumento
from langchain.memory import ChatMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()


llm = AzureChatOpenAI(model=os.environ['AZURE_OPENAI_DEPLOYMENT_MODEL'], temperature=0.1)
embedding = AzureOpenAIEmbeddings(
                model=os.environ['AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_MODEL'],
                azure_deployment=os.environ['AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME'])


chat_history = []

class Agente:

    def simple_chain(self, question: str):
        pass



    def qa_chain(self):
        pass

    def retrival_response(self, question: str):

        qa_chain = self.qa_chain()

        return qa_chain.invoke({"query": question})



