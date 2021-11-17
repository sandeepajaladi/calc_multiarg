"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        for value in self.values:
            result = result / value
        return result
        
