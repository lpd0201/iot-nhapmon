"""
Module Calculator - Lê Thiên Ân - MSSV: 25139003
"""

def add(a, b):
    """Cộng hai số"""
    return a + b

def subtract(a, b):
    """Trừ hai số"""
    return a - b

def multiply(a, b):
    """Nhân hai số"""
    return a * b

def divide(a, b):
    """Chia hai số"""
    if b == 0:
        raise ValueError("Không thể chia cho 0!")
    return a / b

# Thông tin cá nhân
AUTHOR = "Lê Thiên Ân"
STUDENT_ID = "25139003"

if __name__ == "__main__":
    print(f"Calculator module - {AUTHOR} - {STUDENT_ID}")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
