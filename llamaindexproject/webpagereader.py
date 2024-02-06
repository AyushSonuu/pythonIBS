# from llama_index.llms import OpenAI
from llama_index.readers import SimpleWebPageReader
from llama_index import VectorStoreIndex
import os
from dotenv import load_dotenv
load_dotenv()

def main(url:str)->None:
    document = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    index = VectorStoreIndex.from_documents(documents=document)
    query_engine = index.as_query_engine()
    response = query_engine.query("wat is the history of generative ai")
    print(response)


if __name__=="__main__":
    main("https://joinseven.medium.com/blog-series-genai-a-brief-introduction-in-generative-ai-4e11154df3f2")

