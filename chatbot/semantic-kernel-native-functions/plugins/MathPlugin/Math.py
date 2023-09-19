import math  # math 라이브러리를 가져옵니다.
from semantic_kernel.skill_definition import sk_function  # semantic_kernel의 sk_function 데코레이터를 가져옵니다.

class Math:
    @sk_function(
        description="숫자의 제곱근을 계산합니다",
        name="Sqrt",  # 함수의 이름을 설정합니다.
        input_description="제곱근을 계산할 숫자",  # 입력 설명을 설정합니다.
    )
    def square_root(self, number: str) -> str:
        # 입력된 문자열을 실수로 변환한 후 제곱근을 계산하고 문자열로 변환하여 반환합니다.
        return str(math.sqrt(float(number)))
