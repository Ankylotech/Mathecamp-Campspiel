# Importiere Funktionen, die eine Aufgabe zu einer bestimmten Lösung generieren
import random

from operations import rand_ops
from fruit_math import fruit_math
from nullstellen import nst
# Zufällige Auswahl von Lösungen und Generatoren
from random import choice
from random import sample

# Anzahl Probleme und Lösungen
problems = [7, 21, 24, 23, 29, 41]

# Welche Funktionen verwendet werden um Aufgaben zu generieren
generators = [rand_ops, fruit_math, nst]
# Verschiedenen Lösungen
# solutions = [1,2,3,4,5,6,7,8]
solutions = [0, 1, 314159265, 2718, 6283, 10, 2, 299792458]
offset = 0

nums = [i for i in range(1, sum(problems)+1)]
random.shuffle(nums)

s = {}
for n in solutions:
    s[str(n)] = []

for i in range(len(problems)):
    current_problems = problems[i]

    # Generiere für jede Lösung gleich viele Probleme zufällig aus den Generator-Funktionen
    aufgaben = []
    for j in range(current_problems):
        solution = solutions[(j+offset) % len(solutions)]
        result, ok = choice(generators)(solution, i)
        while not ok:
            result, ok = choice(generators)(solution, i)
        aufgaben.append((result, solution))

    offset += current_problems % len(solutions)
    offset %= len(solutions)

    # Speichere die Aufgaben un einer Datei
    with open('output' + str(i + 5) + '.txt', 'w') as f:
        f.write("Klasse " + str(i + 5))
        f.write("\n")
        for aufgabe in aufgaben:
            num = nums.pop()
            s[str(aufgabe[1])].append(num)
            f.write("problem: \n")
            f.write(aufgabe[0])
            f.write('\n')
            f.write("number: ")
            f.write(str(num))
            f.write('\n')
            f.write("solution: ")
            f.write(str(aufgabe[1]))
            f.write('\n')
            f.write('\n')
            f.write('\n')

with open('output.txt', 'w') as f:
    f.write(str(solutions))
    f.write("\n")
    f.write('\n')
    f.write('\n')
    f.write(str(s))
