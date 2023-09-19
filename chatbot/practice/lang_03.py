import os
from dotenv import load_dotenv
# .env 파일에서 API 키를 로드
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = "여행지 5가지 추천좀 해줄 수 있어?"
print(llm(text))

from langchain.prompts import PromptTemplate
prompt = PromptTemplate(
    input_variables=["destination"],
    template="{destination}에서 제일 유명한 관광지 추천해줘!",
)
print(prompt.format(destination="제주도"))
print(llm(prompt.format(destination="제주도")))

#Chains: Combine LLMs and prompts in multi-step workflows
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["city"],
    template="{city}에서 뭘 하는게 제일 좋을까?"
)
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("강릉"))

# #Agents: Dynamically call chains based on user input
# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.llms import OpenAI
# os.environ["serpapi_api_key"]="OPENAI_API_KEY"
# # Load the model
# llm = OpenAI(temperature=0)
# tools = load_tools(["serpapi", "llm-math"], llm=llm)

# #llm, tools, agent, agent_type 초기화
# agent = initialize_agent(tools,
#                          llm,
#                          agent="zero-shot-react-description",
#                          verbose=True)
# #실행
# agent.run("한국에서 가장 큰 기업은 어디야? 그 기업의 직원수는 얼마야? 마지막으로 그 기업의 평균연봉은 얼마야?")