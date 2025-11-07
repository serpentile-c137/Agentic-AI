from agno.tools import Toolkit

class MathToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="math_toolkit")
        self.register(self.multiply_numbers)
        self.register(self.add_numbers)
        self.register(self.subtract_numbers)
        self.register(self.divide_numbers)


    def add_numbers(self, a: float, b: float) -> float:
        """Adds two numbers and returns the result."""
        return a + b
    
    def subtract_numbers(self, a: float, b: float) -> float:
        """Subtracts the second number from the first and returns the result."""
        return a - b
    
    def multiply_numbers(self, a: float, b: float) -> float:
        """Multiplies two numbers and returns the result."""
        return a * b
    
    def divide_numbers(self, a: float, b: float) -> float:
        """Divides the first number by the second and returns the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b