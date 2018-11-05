import numpy as np
import matplotlib.pyplot as plt

class bisection:
    def __init__(self, firstLeft, firstRight, tol, f):
        self.firstLeft = firstLeft
        self.firstRight = firstRight
        self.tol = tol
        self.f = f


    def mainCalculation(self):
        left = self.firstLeft
        right = self.firstRight
        i = 0
        while (np.abs(left - right) >= self.tol):
            i += 1
            middle = (left + right)/2.0
            prod = self.f(left) * self.f(middle)
            if prod > self.tol:
                left = middle
            else:
                if prod < self.tol:
                    right = middle

            print ("{}\t\t\t{:f}\t\t\t{:f}\t\t\t{:f}" .format(i - 1, left, right, middle))
        return middle
        print("Bisection Method gives root at x = ", middle)

    print('{}''{:^15}''{:^23}''{:^18}'.format('iteration', 'a', 'b', 'c'))
    print('----\t\t---------\t\t\t --------\t\t\t --------\t')

    def showGraph(self):
        x = np.linspace(self.firstLeft, self.firstRight, 100)
        plt.plot(x, self.f(x))
        plt.grid()
        plt.show()

