""" Calculation Test Module """
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add,subtract,multiply,divide


@pytest.mark.parametrize("n1, n2, operation, expected",
[
    (Decimal('8'), Decimal('4'), add, Decimal('12')),
    (Decimal('3'), Decimal('3'), subtract, Decimal('0')),
    (Decimal('12'), Decimal('3'), divide, Decimal('4')),
    (Decimal('2'), Decimal('3'), multiply, Decimal('6')),
    (Decimal('3.0'), Decimal('2.0'), add, Decimal('5.0'))
])


def test_operate(n1, n2, operation, expected):
    """
    test for operate method to encapsulate the decimals and operation to call the operate method to perform arithmetic operation and compare the expected value.
    """
    calc = Calculation(n1, n2, operation)
    assert calc.operate() == expected, "operation failed!"

def test_strrepr():
    """
    Test for string representation
    """
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    str_match = "Calculation(2, 2, add)"
    assert calc.__strrepr__() == str_match, f"Expected {str_match} not equal to {calc.__strrepr__()}."

def test_dividebyzero():
    """
    Test for condition of division by zero
    """
    calc = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Error : Divide By Zero occured!"):
        calc.operate()
