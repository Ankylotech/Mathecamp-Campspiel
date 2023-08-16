from random import randrange
from random import uniform
import numpy

# Spalte n in k Zufallszahlen, die auf n Summieren
def split(n,k):
    result = []
    left = k
    while left > 1:
        num = randrange(5,100)
        if uniform(0, 1) < 0.5:
            num *= -1

        n -= num
        left -= 1
        result.append(num)
    result.append(n)
    return result


def coef_test(polynomial):
    for c in polynomial.coef:
        if str(c)[:-2] != str(int(c)):
            return False
    return True


def nst(solution, i):
    degree = int(2 + i * 0.75)
    nsts = split(solution, degree)
    polynomial = numpy.polynomial.Polynomial.fromroots(nsts)
    while not coef_test(polynomial):
        nsts = split(solution, degree)
        polynomial = numpy.polynomial.Polynomial.fromroots(nsts)
    result = "Summiere die Ganzzahligen Nullstellen des folgenden Polynoms: \n"
    result += str(polynomial)
    result += "\n"
    return result

