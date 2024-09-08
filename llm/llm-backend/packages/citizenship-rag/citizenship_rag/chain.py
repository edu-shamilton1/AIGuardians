# Load
import os
import requests
from langchain_chroma import Chroma
#from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
#from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


GoogleKey = os.environ['GOOGLE_API_KEY']
OpenAIKey = os.environ['OPENAI_API_KEY']

llm=""
embed=""

if (len(GoogleKey) > 0):
    print(f"Using Google API")
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GoogleKey)
    embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GoogleKey)
if (len(OpenAIKey) > 0):
    print(f"Using OpenAI API")
    llm = ChatOpenAI(
      model="gpt-4o-mini",
      temperature=0,
      max_tokens=None,
      timeout=None,
      max_retries=2,
      api_key=OpenAIKey,
    )
    embed = OpenAIEmbeddings(openai_api_key=OpenAIKey)


loader = WebBaseLoader("https://https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/character/character-requirements-for-australian-citizenship/")
data = loader.load()

# Split

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# Add to vectorDB
vectorstore = Chroma.from_documents(
    documents=all_splits,
    collection_name="rag-private",
    embedding=embed,
)
retriever = vectorstore.as_retriever()

# Prompt
# Optionally, pull from the Hub
# from langchain import hub
# prompt = hub.pull("rlm/rag-prompt")
# Or, define your own:
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)



# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | llm
    | StrOutputParser()
)


# Add typing for input
class Question(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Question)