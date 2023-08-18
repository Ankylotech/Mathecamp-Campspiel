# Funktion, die Gleichungssysteme erstellt (Variablen könnten durch "Früchte" ersetzt werden)

from random import choice
from random import randrange
from random import uniform
from sympy import primefactors

def factors(n):
    return list(f for i in range(1, int(abs(n)**0.5)+1) if n % i == 0 for f in [i, n//i])
# Spalte n in k Zufallszahlen, die auf n Summieren
def split(n,k):
    result = []
    left = k
    while left > 1:
        num = randrange(max(n // (2*k),1), max((2 * n) // k, 100))
        while num == 0 or num == n:
            num = randrange(max(n // (2 * k), 1), max((2 * n) // k, 100))
        if uniform(0, 1) < 0.5:
            num *= -1

        n -= num
        left -= 1
        result.append(num)
    result.append(n)
    return result


def fruit_math(solution, i):
    result = ""
    num = int(i*0.75 + 3)
    solution_numbers = split(solution, num)
    variables = []
    for x in solution_numbers:
        v = choice(factors(x))
        variables.append(v * (-1 if uniform(0, 1) < 0.5 else 1))
    for _ in range(num):
        mult = [randrange(-75, 75) for _ in range(num)]
        s = 0
        for i in range(num):
            s += variables[i] * mult[i]
            result += str(mult[i]) + " * " + chr(65 + i)
            if i < num - 1:
                result += " + "
            else:
                result += " = "
        result += str(s) + "\n"

    mult = [int(solution_numbers[i] / variables[i]) for i in range(num)]
    s = 0
    for i in range(num):
        s += variables[i] * mult[i]
        result += str(mult[i]) + " * " + chr(65 + i)
        if i < num-1:
            result += " + "
        else:
            result += " = ?\n"
    return result, True
