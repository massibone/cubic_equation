from cmath import *
from fractions import Fraction
import math

solutions = set()


def cbrt(polynomial):
    solution = set()
    root1 = polynomial ** (1 / 3)
    root2 = (polynomial ** (1 / 3)) * (-1 / 2 + (sqrt(3) * 1j) / 2)
    root3 = (polynomial ** (1 / 3)) * (-1 / 2 - (sqrt(3) * 1j) / 2)
    solution.update({root1, root2, root3})
    return solution


# 'ax^3+bx^2+cx+d=0' 
# esempio 2x^3 -8x^2 -18x +72 = 0 inserisco con spazio 2 -8 -18 72
# le soluzioni dovranno essere arrotondate {(2.9999999999999996+0j), (4+0j), (-3+0j)} 3,4 e -3
a, b, c, d = map(int, input("Enter 4 number with space: ").split())

if a != 0:
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    alpha = cbrt(-q / 2 + sqrt((q / 2) ** 2 + (p / 3) ** 3))
    beta = cbrt(-q / 2 - sqrt((q / 2) ** 2 + (p / 3) ** 3))
    for i in alpha:
        for j in beta:
            if abs((i * j) + p / 3) <= 0.00001:
                x = i + j - b / (3 * a)
                solutions.add(x)

elif b != 0:
    D = c ** 2 - 4 * b * d
    solutions.add((-c - sqrt(D)) / 2 * b)
    solutions.add((-c + sqrt(D)) / 2 * b)

elif c != 0:
    solutions.add(-d / c)

elif d == 0:
    solutions.add("True")

else:
    solutions.add("False")

print(solutions)