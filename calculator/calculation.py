from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    def operate(self) -> Decimal:
        return self.operation(self.a, self.b)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        return Calculation(a, b, operation)
    
    def __strrepr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"