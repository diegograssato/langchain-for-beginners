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
        prompt = PromptTemplate.from_template("Explique o conceito de {termo} com um exemplo.")
        chain = LLMChain(llm=llm, prompt=prompt)

        resposta = chain.invoke({"termo": question})
        return resposta

    def qa_chain(self):
        carregar_documento = CarregadorDocumento(
            caminho_documento="data/FAQ_BOOKING_COM.pdf",
            embedding=embedding,
            database_collection="booking_collection",
            database="data/booking_db"
        )
        vectorstore = carregar_documento.retorna_vectorstore()

        retriever = MultiQueryRetriever.from_llm(
            retriever=vectorstore.as_retriever(search_kwargs={'k': 2}),
            llm=llm,
        )

        prompt_template = """
        Como assisnte de viagens educado e prestativo, ajude os usuários encontrarem experiências de viagem personalizadas e relevantes com base em suas perguntas.
        Caso a resposta não esteja presente nos dados, informe educadamente que não possui essa informação.

        Contexto:
        {context}

        Pergunta:
        {question}

        Resposta:
        """

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        return RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )


    def retrival_response(self, question: str):

        qa_chain = self.qa_chain()

        return qa_chain.invoke({"query": question})

    def retrival_response_with_historical(self, question: str, sessao: str):

        qa_chain = self.qa_chain()

        # Histórico usando SQLite
        def create_message_history(session_id: str) -> ChatMessageHistory:
            return SQLChatMessageHistory(session_id=session_id, connection_string="sqlite:///chat_history.sqlite")

        rag_with_history = RunnableWithMessageHistory(
            qa_chain,
            create_message_history,
            input_message_key="query",
            history_message_key="history"
        )

        resposta = rag_with_history.invoke(
            {"query": question},
            config={"configurable": {"session_id": sessao}}
        )
        return resposta
