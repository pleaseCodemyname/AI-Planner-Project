import semantic_kernel as sk  # semantic_kernel 라이브러리를 가져옵니다.
from plugins.MathPlugin.Math import Math  # MathPlugin에서 Math 클래스를 가져옵니다.
import config.add_completion_service  # 서비스 설정 파일을 가져옵니다.

async def main():
    # 커널을 초기화합니다.
    kernel = sk.Kernel()

    # 텍스트 또는 채팅 완성 서비스를 추가합니다. 설정 파일에서 정의한 서비스를 사용합니다.
    kernel.add_completion_service()

    # MathPlugin을 가져와서 math_plugin 변수에 할당합니다.
    math_plugin = kernel.import_skill(Math(), skill_name="MathPlugin")

    # 컨텍스트와 함께 Sqrt 함수를 실행합니다.
    result = await kernel.run_async(
        math_plugin["Sqrt"],  # MathPlugin에서 Sqrt 함수를 가져옵니다.
        input_str="12",  # Sqrt 함수에 전달할 입력 값을 설정합니다.
    )

    print(result)  # 결과를 출력합니다.

# main 함수를 실행합니다.
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
