
from math import *
import numpy as np
import matplotlib.pyplot as plt

def eulerStep(rhs, dx, x0, y0):
    return y0+dx*rhs(x0, y0)
def myFavouriteRhs(x, y):
    return cos(y-x)
def mySecondRhs(x,y):
    return sqrt(4*x+2*y-1)
def my3Rhs(x,y):
    return sin(x)+1/y

N = 50
dx = 0.1
rhs = my3Rhs
xPrev = 1
yPrev = 1
xs = [xPrev]
ys = [yPrev]

for i in range(N):
    xNext = xs[i] + dx
    yNext = eulerStep(rhs, dx, xs[i], ys[i])
    xs.append(xNext)
    ys.append(yNext)
    print(f"solution({xNext}) = {yNext}")
x = np.array(xs)
y = np.array(ys)
plt.plot(x, y)
plt.show()

