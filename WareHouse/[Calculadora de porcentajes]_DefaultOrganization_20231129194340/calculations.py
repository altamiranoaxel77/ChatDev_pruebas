'''
This file contains the PercentageCalculator class which performs the percentage calculation.
'''
class PercentageCalculator:
    def calculate(self, value):
        try:
            value = float(value)
            percentage = (value / 100) * 100
            return percentage
        except ValueError:
            return "Invalid input"