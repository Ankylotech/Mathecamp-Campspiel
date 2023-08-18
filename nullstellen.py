from random import randint
from random import uniform
import numpy


# Spalte n in k Zufallszahlen, die auf n Summieren
def split(n,k):
    result = []
    left = k
    while left > 1:
        num = randint(-5, n-left+1)
        n -= num
        left -= 1
        result.append(num)
    result.append(n)
    return result


def coef_test(polynomial):
    return 'e' not in str(polynomial)


def nst(solution, i):
    if i <= 2 or len(str(solution)) > 4:
        return "", False
    degree = int(2 + i * 0.75)
    nsts = split(solution, degree)
    polynomial = numpy.polynomial.Polynomial.fromroots(nsts)
    while not coef_test(polynomial):
        nsts = split(solution, degree)
        polynomial = numpy.polynomial.Polynomial.fromroots(nsts)
    result = "Summiere die Ganzzahligen Nullstellen des folgenden Polynoms: \n"
    result += str(polynomial)
    result += "\n"
    return result, True

