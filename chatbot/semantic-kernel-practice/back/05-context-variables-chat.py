# 필요한 라이브러리 및 모듈을 가져옵니다.
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion
import asyncio

# Semantic Kernel을 초기화합니다.
kernel = sk.Kernel()

# 사용할 AI 서비스를 구성합니다. (Azure OpenAI 또는 기본 OpenAI)
useAzureOpenAI = False # Azure OpenAI를 사용하려면 True로 설정

if useAzureOpenAI:
    # Azure OpenAI 설정을 사용할 경우
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_chat_service("chat_completion", AzureChatCompletion("gpt-35-turbo", endpoint, api_key))
else:
    # 기본 OpenAI 설정을 사용할 경우
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

# 대화형 챗봇의 동작을 정의하는 프롬프트를 설정합니다.
sk_prompt = """
ChatBot can have a conversation with you about any topic.
It can give explicit instructions or say 'I don't know' if it does not have an answer.

{{$history}}
User: {{$user_input}}
ChatBot: """

# Semantic 함수를 등록합니다.
chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)

# 대화 문맥을 초기화합니다.
context = kernel.create_new_context()
context["history"] = ""


# 메인 함수 정의
async def main():
    # 대화를 시작합니다.
    context["user_input"] = "배고프다 살려줘잉 오늘 점심 뭐먹을까?"
    bot_answer_task = chat_function.invoke_async(context=context)
    bot_answer = await bot_answer_task  # 여기서 결과를 얻기 위해 await를 사용합니다.
    print(bot_answer)
    context["history"] += f"\nUser: {context['user_input']}\nChatBot: {bot_answer}\n"
    
    # 챗봇과 대화를 합니다.
    await chat("나는 한식 중식 양식 일식 가리는 거 없이 잘먹어 뭐먹을까 추천해주라")
    await chat("그거 참 흥미로운 답변이구만? 양재역 근처 식당으로 추천해줄 수 있어?")
    await chat("먹어보고 어땠는지 알려줄게 호호호")
    await chat("다른 식당도 추천해줄 수 있을까?")
    
    # 대화 내역을 출력합니다.
    print(context["history"])

# Chat 함수 정의: 사용자 입력을 처리하고 챗봇의 답변을 생성하는 비동기 함수입니다.
async def chat(input_text: str) -> None:
    # 사용자 입력을 컨텍스트 변수에 저장합니다.
    print(f"User: {input_text}")
    context["user_input"] = input_text

    # 사용자 메시지를 처리하고 답변을 가져옵니다.
    answer = await chat_function.invoke_async(context=context)

    # 답변을 표시합니다.
    print(f"ChatBot: {answer}")

    # 대화 히스토리에 새 상호작용을 추가합니다.
    context["history"] += f"\nUser: {input_text}\nChatBot: {answer}\n"
    
if __name__ == "__main__":
    # 메인 함수를 실행합니다.
    asyncio.run(main())

    # 메인 함수를 실행한 후에는 다음과 같이 사용자 입력을 시뮬레이션할 수 있습니다:
    user_input = "배고프다 살려줘잉 오늘 점심 뭐먹을까?" # 원하는 사용자 입력으로 대체하세요
    asyncio.run(chat(user_input))

