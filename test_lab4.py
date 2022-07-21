import pytest

class Calculator:
    def __init__(self, name):
           self.name = name
       
    def add(self, a, b):
        return a + b 
        
    def subtract(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        

        
        
calc = Calculator("Calc 1")
"""
def test_lab4():
    print("This calculator's name is " + calc.name)
    
    
    #change the calculator's name
    calc.name = "Calc 2"
    print("This calculator's name is " + calc.name)
    
    print(calc.add(1,1))
    
    assert True
"""    
@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True
    
def test_lab4_test2(base_calculator):
    print("#2 This calculator's name os " + base_calculator.name)
    
    assert True

def test_calculator_subtract():
    assert calc.subtract(18,19) == -1
    assert calc.subtract(18,19) == 1
    assert calc.subtract(-18,19) == 1
    assert calc.subtract(18,-19) == 1
    assert calc.subtract(-18, -19) == 1
    
def test_calculator_multiply():
    assert calc.multiply(8, 5) == 40
    assert calc.multiply(8,-5) == 40
    assert calc.multiply(-8,5) == 40
    assert calc.multiply(8, 6) == 40
    assert calc.multiply(-6,-5) == 40
    
    