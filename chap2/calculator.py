"""
간단한 계산기 모듈
기본적인 사칙연산을 수행하는 함수들을 제공합니다.
"""

def add(a, b):
    """두 수를 더합니다."""
    return a + b

def subtract(a, b):
    """첫 번째 수에서 두 번째 수를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

def divide(a, b):
    """첫 번째 수를 두 번째 수로 나눕니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def power(a, b):
    """첫 번째 수를 두 번째 수만큼 거듭제곱합니다."""
    return a ** b

def calculate(operation, a, b):
    """연산을 수행하는 메인 함수"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power
    }
    
    if operation not in operations:
        raise ValueError(f"지원하지 않는 연산입니다: {operation}")
    
    return operations[operation](a, b)

if __name__ == "__main__":
    # 테스트 코드
    print("계산기 테스트")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"2 ^ 8 = {power(2, 8)}")
