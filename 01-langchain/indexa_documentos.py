import os
import shutil
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from langchain_core.embeddings import Embeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

class CarregadorDocumento:
    def __init__(self, caminho_documento: str, embedding: Embeddings, database_collection: str="minha_collection", database: str="data/booking_db"):
        self.caminho_documento = caminho_documento
        self.text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n"],chunk_size=1000, chunk_overlap=200)
        self.embedding_model = embedding
        self.database_collection = database_collection
        self.database = database

        # Verifica se o diretório de persistência existe, caso contrário, cria
        if not os.path.exists(self.database):
            os.makedirs(self.database)

        # Verifica se o arquivo PDF existe
        if not os.path.isfile(self.caminho_documento):
            raise FileNotFoundError(f"O arquivo {self.caminho_documento} não foi encontrado.")


    def carregar_texto(self):
        """Lê e carrega o PDF criando os Documents apenas do texto."""
        print("Carregando base de dados PDF...")
        loader = PyPDFLoader(self.caminho_documento)
        pages_sinc = loader.load()
        return pages_sinc


    def cria_chunks(self, documentos):
        """Função que cria os chunks"""
        print(f"Total de documentos carregados: {len(documentos)}")
        chunks = self.text_splitter.split_documents(documentos)
        return chunks

    def indexar_informacao(self):
        """Função cria os embeddings e armazena no banco cloud Qdrant"""

        # carrega texto:
        documento_lido = self.carregar_texto()
        chunks = self.cria_chunks(documento_lido)

        # Indexar no banco vetorial
        print(f"Total de chunks criados: {len(chunks)}")
        vectordb = Chroma.from_documents(chunks, collection_name=self.database_collection, embedding=self.embedding_model, persist_directory=self.database)
        print(">> Indexação realizada")
        return vectordb

    def retorna_vectorstore(self):
        """Retorna o retriever para ser usado na aplicação"""
        # Reutilizar indexação, se possível
        if os.path.exists(self.database) and os.listdir(self.database):
            vectorstore = Chroma(collection_name=self.database_collection, persist_directory=self.database, embedding_function=self.embedding_model)
        else:
            vectorstore = self.indexar_informacao()
        print(">> Retornando VectorStore")
        return vectorstore


