"""
Tests for calculator app
"""
import calculator


class TestCalculatorAPP:
    def test_add(self):
        assert 7 == calculator.add(3, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 6)

    def test_mulityply(self):
        assert 12 == calculator.mulityply(3, 4)

    def test_divide(self):
        assert 2 == calculator.divide(16, 8)
# This is a new line that ends the file.