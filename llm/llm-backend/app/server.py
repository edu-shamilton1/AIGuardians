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
from citizenship_rag import chain as citizenship_rag_chain

# global variables
import yaml


app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")



##add_routes(app, rag_chroma_private_chain, path="/queryLLM")


GoogleKey = os.environ['GOOGLE_API_KEY']
OpenAIKey = os.environ['OPENAI_API_KEY']
config = yaml.safe_load(open("./config.yaml"))


llm=""


if (len(GoogleKey) > 0):
    modelName = config['GOOGLE_MODEL_NAME']
    print("Using Google API {}".format(modelName))
    modelName = modelName   ## "gemini-pro"
    llm = ChatGoogleGenerativeAI(model=modelName, google_api_key=GoogleKey)
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


summaryPrompt = PromptTemplate(
        template='''
        You are a editor adhering to the Australian Style Guide, summarise the following text:
        \n\n {fullText}''',
        
        input_variables=["fullText"]
    )

translatePrompt = PromptTemplate(
    template='''
    Translate the following text to {language}
    \n\n {fullText}''',

    input_variables=["language","fullText"]
)

queryPrompt = PromptTemplate(
        template='''
        {queryText}
        ''',
        input_variables=["queryText"]
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

add_routes(
    app,
    translatePrompt | llm,
    path="/translate"
)


add_routes(app, citizenship_rag_chain, path="/citizenship")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
