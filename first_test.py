import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_currectly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_currently(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_calculate_currently(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def test_adding_calculate_currently(self):
        assert self.calc.adding(self, 3, 2) == 5
