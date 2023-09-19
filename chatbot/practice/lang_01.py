import os
from dotenv import load_dotenv
from langchain.agents import load_tools, initialize_agent

# .env 파일에서 API 키를 로드
load_dotenv()
serpapi = os.getenv("SERPAPI_API_KEY")  

# Load the model
from langchain.llms import OpenAI
llm = OpenAI(temperature=0)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# 실행
agent.run("한국에서 가장 큰 기업은 어디야? 그 기업의 직원수는 얼마야? 마지막으로 그 기업의 평균연봉은 얼마야?")