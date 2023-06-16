# Funktion, die Gleichungssysteme erstellt (Variablen könnten durch "Früchte" ersetzt werden)

from random import choice
from random import randrange
from random import uniform
from sympy import primefactors


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


def fruit_math(solution):
    result = ""
    num = randrange(6, 8)
    solution_numbers = split(solution,num)
    variables = [choice(primefactors(x)) * -1 if uniform(0, 1) < 0.5 else 1 for x in solution_numbers]
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
    return result
