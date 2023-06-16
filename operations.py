# Generiere Zufällige Rechenaufgabe in Postfix / Reverse polish Notation. Verwendet +,-,*,/

from random import randrange
from random import uniform

from sympy import primefactors


# Get to the number using n operations (in reverse polish/ postfix notation)
# Converter: https://rosettacode.org/wiki/Parsing/RPN_to_infix_conversion#Python
def n_ops(solution, n):
    if n == 0:
        return str(solution)
    factors = primefactors(solution)
    n1 = randrange(0, n)
    n2 = n - n1 - 1
    if len(factors) > 1 and uniform(0, 1) < 0.25:
        i = randrange(len(factors))
        num1 = factors[i]
        num2 = int(solution / num1)
        return n_ops(num1, n1) + " " + n_ops(num2, n2) + " * "
    elif solution > 20 and uniform(0, 1) < 0.33:
        num1 = randrange(5, solution - 4)
        num2 = solution - num1
        return n_ops(num1, n1) + " " + n_ops(num2, n2) + " + "
    elif uniform(0, 1) < 0.5:
        num1 = randrange(15, 150)
        return n_ops(num1 + solution, n1) + " " + n_ops(num1, n2) + " - "
    else:
        num2 = randrange(15, 150)
        return n_ops(solution * num2, n1) + " " + n_ops(num2, n2) + " / "


def rand_ops(solution):
    return n_ops(solution, randrange(5, 8))
