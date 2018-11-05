import numpy as np
import matplotlib.pyplot as plt



class Secant:
    def __init__(self, start, stop, step, f):
        self.start = start
        self.stop = stop
        self.step = step
        self.f = f

    def mainCalculation(self):
        start = self.start
        stop = self.stop
        sign = self.f(start) > 0
        x = start
        while x <= stop:
            value = self.f(x)
            if value == 0:
                return x
            sign = value > self.step
            x += self.step

