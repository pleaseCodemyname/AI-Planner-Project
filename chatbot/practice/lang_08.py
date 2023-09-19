import os
from dotenv import load_dotenv
# .env 파일에서 API 키를 로드
load_dotenv()
openai_api_key = os.getenv("openai_api_key")


from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path="https://ko.wikipedia.org/wiki/NewJeans")
documents = loader.load()

from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
len(docs)

print(docs[:1])
