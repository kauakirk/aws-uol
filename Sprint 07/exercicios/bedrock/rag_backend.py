#1. Importar bibliotecas necessárias: OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws import BedrockLLM
 
#5c. Encapsular o processo de criação do índice em uma função
def hr_index():
    #2. Definir a fonte de dados e carregar os dados usando o PDFLoader (link do documento PDF)
    data_load=PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')  
 
    #3. Dividir o texto com base em caracteres, tokens, etc. - Divisão recursiva por caracteres - ["\n\n", "\n", " ", ""]
    data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100, chunk_overlap=10)
    
    #4. Criar embeddings -- Conexão com o cliente Bedrock
    data_embeddings=BedrockEmbeddings(
        credentials_profile_name= 'default',
        model_id='amazon.titan-embed-text-v1')
    
    #5a. Criar o banco de dados vetorial, armazenar os embeddings e criar o índice para busca - VectorstoreIndexCreator
    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)
    
    #5b. Criar índice para o documento de Política de RH
    db_index=data_index.from_loaders([data_load])
    return db_index

#6a. Escrever uma função para conectar ao modelo de fundação da Bedrock - Modelo Claude
def hr_llm():
    llm=BedrockLLM(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
            "max_tokens_to_sample":3000,
            "temperature": 0.1,
            "top_p": 0.9})
    return llm

#6b. Escrever uma função que busca a pergunta do usuário, encontra a melhor correspondência no banco de dados vetorial e envia ambos para o LLM.
def hr_rag_response(index, question):
    rag_llm=hr_llm()
    hr_rag_query=index.query(question=question, llm=rag_llm)
    return hr_rag_query

# Criação do índice --> https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html