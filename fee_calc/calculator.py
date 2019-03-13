import pandas as pd
from enum import Enum
import math


class Term(Enum):
    TERM_12 = 12
    TERM_24 = 24


class LoanData:
    def __init__(self, loan, term):
        self.loan = loan
        self.term = term


class FeeCalc:
    def __init__(self):
        table = pd.read_csv('./breakpoints.csv')
        self.table = pd.DataFrame(table)

    def create_diff(self, value):
        diff_list = []
        for loan in self.table.Loans:
            diff_list.append(abs(value - loan))
        return diff_list

    def find_nearest(self, value):
        local = self.table.copy(True)
        local['Differences'] = self.create_diff(value)
        return local.sort_values(by=['Differences']).head(2)

    @staticmethod
    def linear_interpolate(value, x1, x2, y1, y2):
        return y1 + (value - x1) * ((y2 - y1) / (x2 - x1))

    @staticmethod
    def rounding(val, base=5):
        return int(base * math.ceil(float(val) / base))

    def calculate(self, data):
        if type(data.loan) not in [int, float]:
            raise TypeError("The loan amount should only be int or float")

        if 1000 > data.loan or data.loan > 20000:
            raise ValueError("The loan amount should be between 1000 and 20000")

        relevant_table = self.find_nearest(data.loan)

        x1 = relevant_table.Loans.iloc[0]
        x2 = relevant_table.Loans.iloc[1]
        y1 = None
        y2 = None

        if data.term == Term.TERM_12:
            y1 = relevant_table.Fees_12.iloc[0]
            y2 = relevant_table.Fees_12.iloc[1]
        elif data.term == Term.TERM_24:
            y1 = relevant_table.Fees_24.iloc[0]
            y2 = relevant_table.Fees_24.iloc[1]
        else:
            raise ValueError("The Term should be Either Term.TERM_12 or Term.TERM_24")

        return self.rounding(self.linear_interpolate(value=data.loan, x1=x1, x2=x2, y1=y1, y2=y2))



