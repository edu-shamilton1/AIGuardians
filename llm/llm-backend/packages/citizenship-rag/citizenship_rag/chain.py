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
from langchain.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
#from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np
#from langchain.document_loaders import WebBaseLoader
###from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
import requests
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
#from langchain.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
import faiss
from uuid import uuid4
from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from typing import Any, Callable, Dict, List, Optional, TypedDict

## global config variables
import yaml


GoogleKey = os.environ['GOOGLE_API_KEY']
OpenAIKey = os.environ['OPENAI_API_KEY']
config = yaml.safe_load(open("./config.yaml"))

llm=""
embed=""

if (len(GoogleKey) > 0):
    modelName = config['GOOGLE_MODEL_NAME']
    print("Using Google API {}".format(modelName))
    llm = ChatGoogleGenerativeAI(model=modelName, google_api_key=GoogleKey)
    embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GoogleKey)
if (len(OpenAIKey) > 0):
    modelName = config['OPENAI_MODEL_NAME']
    print("Using OpenAI API {}".format(modelName))
    llm = ChatOpenAI(
      model=modelName,
      temperature=0,
      max_tokens=None,
      timeout=None,
      max_retries=2,
      api_key=OpenAIKey,
    )
    embed = OpenAIEmbeddings(openai_api_key=OpenAIKey)

from langchain.prompts import PromptTemplate
#loader = WebBaseLoader("https://https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/character/character-requirements-for-australian-citizenship/")
#data = loader.load()
#
## Split
#
#text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
#all_splits = text_splitter.split_documents(data)

documents = []
embed_list = []
dimmi_urls = ["https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/character/character-requirements-for-australian-citizenship",
              "https://immi.homeaffairs.gov.au/help-support/meeting-our-requirements/health"
]
for gov_site_url in dimmi_urls :
    # Step 1: Fetch content from the government site
    #gov_site_url = 
    gov_response = requests.get(gov_site_url)
    gov_soup = BeautifulSoup(gov_response.content, 'html.parser')

    for element in gov_soup(["nav", "footer", "header", "aside"]):  # remove nav, footer, header, and aside elements
        element.extract()

    # Extract the content from all paragraphs
    # content = "\n".join([p.get_text() for p in gov_soup.find_all("p")])
    # content = "\n".join([div.get_text() for div in gov_soup.find_all("div")])

    # gov_soup.find(id="content-main") or
    # gov_soup.find(class_="content-main")
    main_content = gov_soup.find(class_="content-main")

    # If the 'content-main' section is found, extract its text
    if main_content:
        content = "\n".join([p.get_text() for p in main_content.find_all("p")])
    else:
        print("[ERROR] no main content section found for url {}".format(gov_site_url))
        content = "Main content section not found."

    print(content)
    ## Step 3: Embed the content
    
    embedded_content = embed.embed_documents([content])

    #
    ## Step 4: Initialize the FAISS index for vector storage
    if embedded_content:
        print("[DEBUG] adding embedded content from {}".format(gov_site_url))
        #dimension = len(embedded_content[0])  # Get the dimension of the embedding vector
        #faiss_index = faiss.IndexFlatL2(dimension)  # L2 distance metric
    #
    #    # Add the embedded content to the FAISS index
    #    # Convert embedded_content to a NumPy array
        embedded_content = np.array(embedded_content)
        embed_list.append(embedded_content)
        #faiss_index.add(embedded_content)
        #faiss_list.append(faiss_index)
        document = Document(page_content=content)
        documents.append(document)

##documents = [document]
uuids = [str(uuid4()) for _ in range(len(documents))]
docstore_index = [{k: uuids[k]} for k in range(len(uuids))]

for x in docstore_index: 
    print("x: {}".format(x))


## Add to vectorDB
#vectorstore = Chroma.from_documents(
#    documents=content,
#    collection_name="rag-private",
#    embedding=embed,
#)
#retriever = vectorstore.as_retriever()


#
# Store in a FAISS wrapper for easier access
# Create a docstore using a dictionary
##docstore = {0: content}
##
### Create a mapping between the index and the docstore
##index_to_docstore_id = {0: 0}
for x in range(len(embed_list)):
    print("- index: {}, len: {}".format(x, len(embed_list[x][0])))

faiss_index = faiss.IndexFlatL2(len(embed_list[0][0]))

# embed.embed_query
##vector_store = FAISS(embed, faiss_index, docstore, index_to_docstore_id)
vector_store = FAISS(
    embedding_function=embed,
    index=faiss_index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

vector_store.add_documents(documents=documents, ids=uuids)

retriever = vector_store.as_retriever()
print("[DEBUG] get retriever from FAISS vector store")
docs = retriever.invoke("What is the minimum age")
print("[DEBUG] got back {} documents".format(len(docs)))
print("[DEBUG] doc[0]: {}".format(docs[0]))
# Prompt
# Optionally, pull from the Hub
# from langchain import hub
# prompt = hub.pull("rlm/rag-prompt")
# Or, define your own:
template = """You are a customer service agent for the Australian Department of Immigration, you can only answer questions about Applying for Australian Citizenship.
Answer the question based only on the following context:
{context}

If there is no context, answer by saying that you can only answer questions about Australian Citizenship.

Question: {question}
"""

#prompt = ChatPromptTemplate.from_template(template)
prompt = ChatPromptTemplate.from_messages([("human", template)])


#rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm
#response = rag_chain.invoke("what checks do I need")
#print(response.content)


# RAG chain
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | llm
)


# Add typing for input
class Question(BaseModel):
    __root__: str

class Input(BaseModel):
    Question: str


chain = chain.with_types(input_type=Question)
