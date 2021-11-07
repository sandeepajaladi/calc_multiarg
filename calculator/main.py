""" This class is a collection of calculator functions """
class Calculator:
    result = 0
    # Addition of two numbers
    def add(self, num1_a, num2_b):
        self.a =  num1_a
        self.result = self.a + num2_b
        return self.result


    # Subtraction of two numbers
    def subtract(self, num1_a, num2_b):
        self.a = num1_a
        self.result = self.a - num2_b
        return self.result


    # Multiplication of two numbers
    def multiply(self, num1_a, num2_b):
        self.a = num1_a
        self.result = self.a * num2_b
        return self.result

    # Division of numbers and exception for division by 0
    def divide(self, num1_a, num2_b):
        self.a = num1_a
        if b <= 0:
            return "Error: A number cannot be divided by 0"
        else:
            self.result = self.a / num2_b
            return self.result

    # Increment a number by 1
    def increment(self, num1_a):
        self.a = num1_a
        self.result = self.a + 1
        return self.result
