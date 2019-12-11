
import matplotlib.pyplot as py
import numpy as np
import sympy as sym
from sympy.abc import t


#sym.integrate() calculating an
def fourier_an(n):
    an = sym.integrate(-2 * t ** 2 * sym.cos(n * t), (t, -sym.pi, sym.pi))
    an = an * 1 / sym.pi
    return an


def fourier_a0():
    a0 = sym.integrate(-2 * t ** 2, (t, -sym.pi, sym.pi))
    a0 = a0 * 1 / sym.pi
    return a0


def fourier_series(l):
    total = 0.0
    for x in range(1, l + 1):
        total += fourier_an(x) * sym.cos(x * 1)
    total = fourier_a0() / 2 + total
   # print(total)
    # print(sym.solve(total, t))

    return total


def fourier_plot(n):
    x = np.linspace(-15, 15, 100)  # 100 linearly spaced numbers between -15 and 15
    y = fourier_series(n)

    print(y)
    # y = 8 * np.cos(x) - 2*np.pi**2/3
    y = 8*np.cos(x) - 2*np.cos(2*x) + 8*np.cos(3*x)/9 - np.cos(4*x)/2 + 8*np.cos(5*x)/25 - 2*np.pi**2/3

    # compose plot
    py.plot(x,y) # sin(x)/x
    py.show()  # show the plot


if "__init__":
    fourier_plot(100)