from random import choice
from random import randrange
from random import sample
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
    variables = [choice(primefactors(x)) for x in solution_numbers]
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


problems = 16
solution_groups = 8
generators = [rand_ops, fruit_math]
solutions = sample(range(30, 250), solution_groups)

# generiere für jede Lösung gleich viele Probleme zufällig aus den Generatorfunktionen
aufgaben = [[(choice(generators)(x), x) for x in solutions] for _ in range(int(problems / len(solutions)))]
aufgaben = [x for sublist in aufgaben for x in sublist]

with open('output.txt', 'w') as f:
    f.write(str(solutions))
    f.write("\n")
    f.write('\n')
    f.write('\n')
    for aufgabe in aufgaben:
        f.write("problem: \n")
        f.write(aufgabe[0])
        f.write('\n')
        f.write("solution: ")
        f.write(str(aufgabe[1]))
        f.write('\n')
        f.write('\n')
        f.write('\n')
