# Load
import os
import requests
from langchain_chroma import Chroma
#from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader
#from langchain_community.embeddings import GPT4AllEmbeddings
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
#from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np
from langchain.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
import requests
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import faiss

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


#loader = WebBaseLoader("https://https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/character/character-requirements-for-australian-citizenship/")
#data = loader.load()
#
## Split
#
#text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
#all_splits = text_splitter.split_documents(data)

# Step 1: Fetch content from the government site
gov_site_url = "https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/character/character-requirements-for-australian-citizenship"
gov_response = requests.get(gov_site_url)
gov_soup = BeautifulSoup(gov_response.content, 'html.parser')

for element in gov_soup(["nav", "footer", "header", "aside"]):  # remove nav, footer, header, and aside elements
    element.extract()

# Extract the content from all paragraphs
# content = "\n".join([p.get_text() for p in gov_soup.find_all("p")])
# content = "\n".join([div.get_text() for div in gov_soup.find_all("div")])

main_content = gov_soup.find(id="content-main") or gov_soup.find(class_="content-main")

# If the 'content-main' section is found, extract its text
if main_content:
    content = "\n".join([p.get_text() for p in main_content.find_all("p")])
else:
    content = "Main content section not found."

print(content)

## Add to vectorDB
#vectorstore = Chroma.from_documents(
#    documents=content,
#    collection_name="rag-private",
#    embedding=embed,
#)
#retriever = vectorstore.as_retriever()


# Step 3: Embed the content
embedded_content = embed.embed_documents([content])

# Step 4: Initialize the FAISS index for vector storage
if embedded_content:
    dimension = len(embedded_content[0])  # Get the dimension of the embedding vector
    faiss_index = faiss.IndexFlatL2(dimension)  # L2 distance metric

    # Add the embedded content to the FAISS index
    # Convert embedded_content to a NumPy array
    embedded_content = np.array(embedded_content)
    faiss_index.add(embedded_content)

# Store in a FAISS wrapper for easier access
# Create a docstore using a dictionary
docstore = {0: content}

# Create a mapping between the index and the docstore
index_to_docstore_id = {0: 0}

vector_store = FAISS(embed.embed_query, faiss_index, docstore, index_to_docstore_id)

retriever = vector_store.as_retriever()
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