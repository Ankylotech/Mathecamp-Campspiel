# Importiere Funktionen, die eine Aufgabe zu einer bestimmten Lösung generieren
import random

from operations import rand_ops
from fruit_math import fruit_math
from nullstellen import nst
# Zufällige Auswahl von Lösungen und Generatoren
from random import choice
from random import sample

# Anzahl Probleme und Lösungen
problems = 24
solution_groups = 8

# Welche Funktionen verwendet werden um Aufgaben zu generieren
generators = [rand_ops, fruit_math, nst]
# Verschiedenen Lösungen
# solutions = [1,2,3,4,5,6,7,8]
solutions = [0, 1, 314, 2718, 6283, 10, 2, 299792458]

# Generiere für jede Lösung gleich viele Probleme zufällig aus den Generator-Funktionen
aufgaben = [[(choice(generators)(x), x) for x in solutions] for _ in range(int(problems / len(solutions)))]
aufgaben = [x for sublist in aufgaben for x in sublist]

nums = [i for i in range(1, problems+1)]
random.shuffle(nums)
s = {}
for n in solutions:
    s[str(n)] = []

# Speichere die Aufgaben un einer Datei
with open('output.txt', 'w') as f:
    f.write(str(solutions))
    f.write("\n")
    f.write('\n')
    f.write('\n')
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
    f.write(str(s))
