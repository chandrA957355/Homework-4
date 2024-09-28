''' Calculations Test Module '''
from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def sample_operations():

    calculations.delete_calculation()

    calculations.add_calculation(Calculation(Decimal('2'), Decimal('3'), add))
    calculations.add_calculation(Calculation(Decimal('4'), Decimal('3'), subtract))
    calculations.add_calculation(Calculation(Decimal('10'), Decimal('3'), multiply))
    calculations.add_calculation(Calculation(Decimal('9'), Decimal('3'), divide))

def test_addcalculation():
    add_obj = Calculation(Decimal('5'),Decimal('3'), add)
    calculations.add_calculation(add_obj)
    assert calculations.get_latest() == add_obj, "History addition failed."

def test_getallhistory(sample_operations):
    history = calculations.print_all_calculation()
    assert len(history) == 4, "All history count is not correct."

def test_deletehistory():
    calculations.delete_calculation()
    assert len(calculations.print_all_calculation()) == 0, "Delete history failed."

def test_getlatestcalculation(sample_operations):
    latest = calculations.get_latest()
    assert latest.a == Decimal('9') and latest.b == Decimal('3'), "Get latest failed."

def test_getlatestafterclear():
    calculations.delete_calculation()
    assert calculations.get_latest() is None, "Get Latest after clear is not working"

def test_findbyoperation(sample_operations):
    add_find = calculations.filter_with_operation("add")
    assert len(add_find) == 1, "count of add operations doesnt match"
    getbymultiply_operation = calculations.filter_with_operation("multiply")
    assert len(add_find) == 1, "count of multiply operations doesnt match"