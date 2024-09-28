from calculator.operations import add, subtract, divide, multiply
from calculator.calculation import Calculation
from calculator.calculations import calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    
    @staticmethod
    def perform(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        calculation = Calculation.create(a, b, operation)
        calculations.add_calculation(calculation)
        return calculation.operate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform(a,b,add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.perform(a,b,subtract)

    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        return Calculator.perform(a,b,multiply)
    
    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        return Calculator.perform(a,b,divide)