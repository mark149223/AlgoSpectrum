import pandas as pd
import math

class SolvingQuadraticEquationError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f'SolvingQuadraticEquationError {self.message}'


class SettingLeftBorderError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        return f'SettingLeftBorderError {self.message}'


def calculate_spectr_integral(spectr, x_begin, x_end):
    '''
     Считает сумму счета от begin до end включая их.
     x_end должно быть больше x_begin иначе будет ошибка!'''
    if (x_begin >= x_end):
        raise Exception

    integral = 0
    for i, row in spectr.iterrows():
        if i == len(spectr) - 1:
            break
        x_first = spectr['energy'].iloc[i]
        y_first = spectr['N'].iloc[i]


        if x_first >= x_begin and x_first <= x_end:
            integral += y_first
    return integral





