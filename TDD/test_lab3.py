import pytest

class Calculator:
    def add(self, a, b):
        return a + b
        
calc = Calculator()

#print(calc.add(1, 1))

def test_add_int():
    assert calc.add(1,1) == 2

def test_add_float():
    assert calc.add(1.0,2.5) == 3.5

def test_add_zero():
    assert calc.add(0,0) == 0
    
def test_add_neg():
    assert calc.add(-5,-6) == -11
