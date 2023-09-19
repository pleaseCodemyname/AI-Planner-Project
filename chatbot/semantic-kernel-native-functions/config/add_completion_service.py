import semantic_kernel as sk  # semantic_kernel 라이브러리를 가져옵니다.
from dotenv import dotenv_values  # .env 파일에서 환경 변수를 로드하기 위한 라이브러리를 가져옵니다.
from semantic_kernel.connectors.ai.open_ai import (
    OpenAITextCompletion,
    AzureTextCompletion,
    OpenAIChatCompletion,
    AzureChatCompletion,
)
from semantic_kernel.kernel import Kernel  # 커널 클래스를 가져옵니다.

# AI 서비스를 커널에 추가하는 함수를 정의합니다.
def add_completion_service(self):
    config = dotenv_values(".env")  # .env 파일에서 설정을 읽어옵니다.
    llm_service = config.get("GLOBAL__LLM_SERVICE", None)  # LLM 서비스 이름을 가져옵니다.

    # 커널에서 사용할 AI 서비스를 구성합니다. 설정은 .env 파일에서 가져옵니다.
    if llm_service == "AzureOpenAI":
        deployment_type = config.get("AZURE_OPEN_AI__DEPLOYMENT_TYPE", None)

        if deployment_type == "chat-completion":
            # Azure Chat Completion 서비스를 추가합니다.
            self.add_chat_service(
                "chat_completion",
                AzureChatCompletion(
                    config.get("AZURE_OPEN_AI__CHAT_COMPLETION_DEPLOYMENT_NAME", None),
                    config.get("AZURE_OPEN_AI__ENDPOINT", None),
                    config.get("AZURE_OPEN_AI__API_KEY", None),
                ),
            )
        else:
            # Azure Text Completion 서비스를 추가합니다.
            self.add_text_completion_service(
                "text_completion",
                AzureTextCompletion(
                    config.get("AZURE_OPEN_AI__TEXT_COMPLETION_DEPLOYMENT_NAME", None),
                    config.get("AZURE_OPEN_AI__ENDPOINT", None),
                    config.get("AZURE_OPEN_AI__API_KEY", None),
                ),
            )
    else:
        model_id = config.get("AZURE_OPEN_AI__MODEL_ID", None)

        if model_id == "chat-completion":
            kernel = sk.Kernel()
            # OpenAI Chat Completion 서비스를 추가합니다.
            kernel.add_text_completion_service(
                "chat_completion",
                OpenAIChatCompletion(
                    config.get("OPEN_AI__CHAT_COMPLETION_MODEL_ID", None),
                    config.get("OPEN_AI__API_KEY", None),
                    config.get("OPEN_AI__ORG_ID", None),
                ),
            )
        else:
            kernel = sk.Kernel()
            # OpenAI Text Completion 서비스를 추가합니다.
            kernel.add_text_completion_service(
                "text_completion",
                OpenAITextCompletion(
                    config.get("OPEN_AI__TEXT_COMPLETION_MODEL_ID", None),
                    config.get("OPEN_AI__API_KEY", None),
                    config.get("OPEN_AI__ORG_ID", None),
                ),
            )

# Kernel 클래스에 add_completion_service 함수를 추가합니다.
Kernel.add_completion_service = add_completion_service
