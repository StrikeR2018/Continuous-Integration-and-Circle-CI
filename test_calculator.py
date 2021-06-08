"""
Tests for calculator app
"""
import calculator


class TestCalculatorAPP:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_subtract(self):
        assert 5 == calculator.subtract(8, 3)

    def test_mul(self):
        assert 15 == calculator.mulityply(3, 5)

    def test_div(self):
        assert 3 == calculator.divide(15, 5)
