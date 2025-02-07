# calculator.py

class Calculator:
    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность двух чисел."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное двух чисел. Если деление на ноль, вызывает ошибку."""
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b