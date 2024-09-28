from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable,List

class calculations:
    history = []

    @classmethod
    def add_calculation(cls,Calculation: Calculation):
        cls.history.append(Calculation)
    
    @classmethod
    def delete_calculation(cls):
        cls.history.clear()
        
    
    @classmethod
    def get_latest(cls):
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def print_all_calculation(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def filter_with_operation(cls, operation:str) -> List[Calculation]:
        return [i for i in cls.history if i.operation.__name__ == operation]