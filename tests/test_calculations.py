''' Calculations Test Module '''
from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def sample_operations():
    '''
    Adding the sample operations into the history for test cases
    '''
    calculations.delete_calculation()

    calculations.add_calculation(Calculation(Decimal('2'), Decimal('3'), add))
    calculations.add_calculation(Calculation(Decimal('4'), Decimal('3'), subtract))
    calculations.add_calculation(Calculation(Decimal('10'), Decimal('3'), multiply))
    calculations.add_calculation(Calculation(Decimal('9'), Decimal('3'), divide))

def test_addcalculation():
    '''
    testing the history for the calculation addition
    '''
    add_obj = Calculation(Decimal('5'),Decimal('3'), add)
    calculations.add_calculation(add_obj)
    assert calculations.get_latest() == add_obj, "History addition failed."

def test_getallhistory(sample_operations):
    '''
    Checking the count of history entries to verify the get history 
    '''
    history = calculations.print_all_calculation()
    assert len(history) == 4, "All history count is not correct."

def test_deletehistory():
    '''
    checking the clear function on the history
    '''
    calculations.delete_calculation()
    assert len(calculations.print_all_calculation()) == 0, "Delete history failed."

def test_getlatestcalculation(sample_operations):
    '''
    Testing if the last calculation is the latest in the history list
    '''
    latest = calculations.get_latest()
    assert latest.a == Decimal('9') and latest.b == Decimal('3'), "Get latest failed."

def test_getlatestafterclear():
    '''
    testing if the history is empty after clear
    '''
    calculations.delete_calculation()
    assert calculations.get_latest() is None, "Get history should be empty"

def test_findbyoperation(sample_operations):
    '''
    Tests the history to get the operations list with given operation
    '''
    add_find = calculations.filter_with_operation("add")
    assert len(add_find) == 1, "count of add operations doesnt match"
    multiply_filter = calculations.filter_with_operation("multiply")
    assert len(multiply_filter) == 1, "count of multiply operations doesnt match"
