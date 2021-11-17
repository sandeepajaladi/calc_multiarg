"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self,num1,num2):
        """get the division results"""
        result = 1.0
        self.num_a = num1
	    self.num_b = num2
        for value in self.values:
            self.result = self.num_a / num_b
        return self.result
        
