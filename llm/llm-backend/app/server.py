# import os module
import os

# langerve imports
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain.prompts import PromptTemplate

#from langchain_community.llms.ollama import Ollama
#from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

##from rag_chroma_private import chain as rag_chroma_private_chain



app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
##add_routes(app, rag_chroma_private_chain, path="/queryLLM")

#llm = Ollama(model='llama3', temperature=0.1)
#llm = ChatOpenAI(
#    model="gpt-4o-mini",
#    temperature=0,
#    max_tokens=None,
#    timeout=None,
#    max_retries=2,
#    api_key="",  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
#)

GoogleKey = os.environ['GOOGLE_API_KEY']
OpenAIKey = os.environ['OPENAI_API_KEY']

llm=""

if (len(GoogleKey) > 0):
    print(f"Using Google API")
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GoogleKey)
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


summaryPrompt = PromptTemplate(
        template='''
        You are a editor adhering to the Australian Style Guide, summarise the following text:
        \n\n {fullText}''',
        
        input_variables=["fullText"]
    )

queryPrompt = PromptTemplate(
        template='''
        {fullText}
        ''',
        input_variables=["fullText"]
    )


add_routes(
    app,
    summaryPrompt | llm,
    path="/summarise"
)

add_routes(
    app,
    queryPrompt | llm,
    path="/queryLLM"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
