import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# .env 파일에서 API 키를 로드
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

# 번역 채팅 시나리오 설정
chat = ChatOpenAI(temperature=0)  # 번역을 항상 같게 하기 위해서 설정

template = "You are a helpful assisstant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# LLMChain 인스턴스 생성
chatchain = LLMChain(llm=chat, prompt=chat_prompt)

# 번역 실행 및 결과 확인
input_language = "English"
output_language = "Korean"
text_to_translate = "I love programming."

translated_text = chatchain.run(input_language=input_language, output_language=output_language, text=text_to_translate)
print("Translated Text:", translated_text)
