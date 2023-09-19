import os
from dotenv import load_dotenv
# .env 파일에서 API 키를 로드
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

# LLMs : LangChain의 가장 기본 모듈. LLM 모델을 호출하고, input값의 예측값을 받아 오는 모듈
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
text = "What would be a good company name a company that makes colorful socks?"
print(llm(text))


# Prompt Templates : 보통 LLM 모델을 사용할 때, 사용자의 입력을 그대로 input으로 입력하지는 않는다. 템플릿을 미리 정의하고, 원하는 값을 넣을 수 있도록 도와주는 모듈
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
print(prompt.format(product="colorful socks"))
# What is a good name for a company that makes colorful socks?


# Chains : LLM 모델을 불러오고, 프롬프트 템플릿을 만들었다면 이제 이것들을 chain으로 연결할 수 있다. Chain은 LLM 모델 뿐만아니라 다른 chain들과 연결해주는 역할을 하는 모듈이다.
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

chain.run("colorful socks")
# -> '\n\nSocktastic!'