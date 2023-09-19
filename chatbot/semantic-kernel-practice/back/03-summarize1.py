# semantic_kernel 라이브러리와 관련 모듈을 가져옵니다.
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion, OpenAITextCompletion

# Semantic Kernel 인스턴스를 만듭니다.
kernel = sk.Kernel()

# Azure AI OpenAI를 사용할지 여부를 설정합니다.
useAzureOpenAI = False

# 커넥터를 구성합니다. Azure AI OpenAI를 사용하는 경우, 설정을 가져오고 커넥터를 추가합니다.
if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_text_completion_service("dv", AzureTextCompletion(deployment, endpoint, api_key))
else:
    # OpenAI 설정을 가져오고 커넥터를 추가합니다.
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("dv", OpenAITextCompletion("text-davinci-003", api_key, org_id))

# 텍스트 요약을 생성하기 위한 프롬프트를 정의합니다.
prompt = """{{$input}}
Summarize the content above.
"""

# Semantic Function을 만듭니다.
summarize = kernel.create_semantic_function(prompt, max_tokens=2000, temperature=0.2, top_p=0.5)

# 입력 텍스트를 정의합니다.
input_text = """
LLM은 Large Language Model의 약자로, 거대언어모델이라는 뜻이다.

언어모델(LM)을 더욱 확장한 개념으로 인간의 언어를 이해하고 생성하도록 훈련된 인공지능을 통칭한다.

LLM을 활용해 완성된 챗GPT가 출현한 이후 LLM은 딥러닝 알고리즘과 통계 모델을 통한 자연어 처리를 능숙하게 하는데 광범위하게 쓰이고 있다.

LLM은 대규모의 언어 데이터를 학습해 문장 구조나 문법, 의미, 단어 내에 내재된 다른 의미 등을 이해하고 생성할 수 있다.

예를 들면 일정 길이의 한글 문장이 주어진 경우 한 단어가 끝나고 다음 단어를 예측할 때 LLM은 문장 내의 단어들 사이의 유사성과 문맥 형성 등을 파악해 보다 정확하게 의미를 생성할 수 있다.

최근 네이버 등 국내 주요 플랫폼 기업들이 인공지능을 개발하고 서비스를 확장할 때보다 정확한 한국어를 구사하기 위해서는 방대한 데이터를 통한 언어모델 구축이 필수적이다.

최근 국내 주요 기업들이 초거대 인공지능에 주력하고 있는 상황에서 이러한 LLM의 필요성은 더 커지고 있다.
"""

# 텍스트 요약을 생성합니다.
summary = summarize(input_text)

# 요약 내용을 출력합니다.
print(summary)
