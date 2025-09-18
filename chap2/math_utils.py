"""
수학 유틸리티 모듈
calculator 모듈을 사용하여 고급 수학 연산을 수행합니다.
"""

from calculator import add, multiply, power, divide
import math

def factorial(n):
    """팩토리얼을 계산합니다."""
    if n < 0:
        raise ValueError("음수는 팩토리얼을 계산할 수 없습니다.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = multiply(result, i)
    return result

def fibonacci(n):
    """피보나치 수열의 n번째 항을 계산합니다."""
    if n < 0:
        raise ValueError("음수 인덱스는 지원하지 않습니다.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, add(a, b)
    return b

def quadratic_formula(a, b, c):
    """이차방정식의 해를 구합니다."""
    discriminant = add(power(b, 2), multiply(-4, multiply(a, c)))
    
    if discriminant < 0:
        return "실근이 없습니다."
    
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = divide(add(-b, sqrt_discriminant), multiply(2, a))
    x2 = divide(add(-b, -sqrt_discriminant), multiply(2, a))
    
    return x1, x2

def geometric_mean(numbers):
    """기하평균을 계산합니다."""
    if not numbers:
        raise ValueError("빈 리스트는 처리할 수 없습니다.")
    
    product = 1
    for num in numbers:
        product = multiply(product, num)
    
    n = len(numbers)
    return power(product, divide(1, n))

def arithmetic_mean(numbers):
    """산술평균을 계산합니다."""
    if not numbers:
        raise ValueError("빈 리스트는 처리할 수 없습니다.")
    
    total = 0
    for num in numbers:
        total = add(total, num)
    
    return divide(total, len(numbers))

if __name__ == "__main__":
    # 테스트 코드
    print("수학 유틸리티 테스트")
    print(f"5! = {factorial(5)}")
    print(f"피보나치 10번째 항: {fibonacci(10)}")
    print(f"이차방정식 x²-5x+6=0의 해: {quadratic_formula(1, -5, 6)}")
    print(f"기하평균 [2, 8, 32]: {geometric_mean([2, 8, 32])}")
    print(f"산술평균 [1, 2, 3, 4, 5]: {arithmetic_mean([1, 2, 3, 4, 5])}")
