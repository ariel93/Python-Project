from tkinter import *
import Test
import Test2
root = Tk()
root.title("Numerical analysis")
root.geometry("{}x{}+{}+{}".format(400, 630, 800, 0))

# Bisection method
Label(root, text = "Function: f(x)=").grid(row = 0, column = 0)
entryFunction = Entry(root)
entryFunction.insert(0, "x**3 + x**2 +1")
entryFunction.grid(row = 0, column = 1)
Label(root, text = "Precision").grid(row = 1, column = 0)
entryPrecision = Entry(root)
entryPrecision.insert(0, "0.00001")
entryPrecision.grid(row = 1, column = 1)
Label(root, text = "Left Border ").grid(row = 2, column = 0)
entryLeft = Entry(root)
entryLeft.grid(row = 2, column = 1)
entryLeft.insert(0, "-5")
Label(root, text = "Right  Border ").grid(row = 3, column = 0)
entryRight = Entry(root)
entryRight.grid(row = 3, column = 1)
entryRight.insert(0, "5")
photo=PhotoImage(file="analysis.png")
Label(root, image=photo).grid(row=22,column=0)

def fun():
    function = entryFunction.get()
    Precision = float(entryPrecision.get())
    left = float(entryLeft.get())
    right = float(entryRight.get())

    def f(x):
        return eval(function)

    bis = Test.bisection(left, right, Precision, f)

    answer = bis.mainCalculation()

    Label(root, text="Bisection Method gives root at x = {}".format(answer)).grid(row = 5, columnspan = 10)

    def showGraph():
        bis.showGraph()
    Button(root, text="Show The Graph", command = showGraph, fg = 'blue').grid(row = 6)

Button(root, text="Find the root", command = fun, fg = 'green').grid(row = 4)




# Secant method
Label(root, text = "Function: f(x)=").grid(row = 23, column = 0)
entryFunction2 = Entry(root)
entryFunction2.insert(0, "x**3 + x**2 +1")
entryFunction2.grid(row = 23, column = 1)
Label(root, text = "Precision").grid(row = 24, column = 0)
entryPrecision2 = Entry(root)
entryPrecision2.insert(0, "0.00001")
entryPrecision2.grid(row = 24, column = 1)
Label(root, text = "Left Border ").grid(row = 25, column = 0)
entryLeft2 = Entry(root)
entryLeft2.grid(row = 25, column = 1)
entryLeft2.insert(0, "-5")
Label(root, text = "Right  Border ").grid(row = 26, column = 0)
entryRight2 = Entry(root)
entryRight2.grid(row = 26, column = 1)
entryRight2.insert(0, "5")
photo2=PhotoImage(file="analysis2.png")
Label(root, image=photo2).grid(row=30,column=0)

def fun2():
    function2 = entryFunction2.get()
    Precision2 = float(entryPrecision2.get())
    left2 = float(entryLeft2.get())
    right2 = float(entryRight2.get())

    def f2(x):
        return eval(function2)

    Sec = Test2.Secant(left2, right2, Precision2, f2)

    answer2 = Sec.mainCalculation()

    Label(root, text="Bisection Method gives root at x = {}".format(answer2)).grid(row = 28, columnspan = 10)


Button(root, text="Find the root", command = fun2, fg = 'green').grid(row = 27)

root.mainloop()

