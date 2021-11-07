""" This class is a collection of calculator functions """
class Calculator:
    result = 0
    # Addition of two numbers
    def add(self, a, b):
        self.a =  a
        self.result = self.a +b
        return self.result


    # Subtraction of two numbers
    def subtract(self, a, b):
        self.a = a
        self.result = self.a - b
        return self.result


    # Multiplication of two numbers
    def multiply(self, a, b):
        self.a = a
        self.result = self.a * b
        return self.result

    # Division of numbers and exception for division by 0
    def divide(self, a, b):
        self.a = a
        if b <= 0:
            return "Error: A number cannot be divided by 0"
        else:
            self.result = self.a / b
            return self.result

    # Increment a number by 1
    def increment(self, a):
        self.a = a
        self.result = self.a + 1
        return self.result
