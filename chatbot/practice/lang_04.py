from langchain.document_loaders.base import Document  # langchain 패키지에서 Document 클래스를 가져옴
from langchain.indexes import VectorstoreIndexCreator  # langchain 패키지에서 VectorstoreIndexCreator 클래스를 가져옴
from langchain.utilities import ApifyWrapper  # langchain 패키지에서 ApifyWrapper 클래스를 가져옴

import os  # os 모듈을 가져옴

from dotenv import load_dotenv  # dotenv 모듈에서 load_dotenv 함수를 가져옴

load_dotenv()  # .env 파일을 로드하여 환경 변수를 설정

openai_api_key = os.getenv("openai_api_key")  # 환경 변수에서 OpenAI API 키를 가져옴
apify_api_key = os.getenv("apify_api_key")  # 환경 변수에서 Apify API 키를 가져옴

apify = ApifyWrapper()  # ApifyWrapper 클래스의 인스턴스를 생성

# Apify 액터를 호출하여 웹 사이트 콘텐츠를 수집하는 작업을 실행
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://python.langchain.com/en/latest/"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

# Document 인스턴스를 생성하는 로더를 사용하여 Vectorstore 인덱스를 생성
index = VectorstoreIndexCreator().from_loaders([loader])

print(index)
query = "What is LangChain?"  # 검색할 질의문을 설정
result = index.query_with_sources(query)  # 인덱스를 사용하여 질의문을 검색하고 결과를 가져옴

print(result["answer"])  # 검색 결과에서 답변을 출력
print(result["sources"])  # 검색 결과에서 소스(문서 출처) 목록을 출력
