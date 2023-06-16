# Importiere Funktionen, die eine Aufgabe zu einer bestimmten Lösung generieren
from operations import rand_ops
from fruit_math import fruit_math
# Zufällige Auswahl von Lösungen und Generatoren
from random import choice
from random import sample

# Anzahl Probleme und Lösungen
problems = 16
solution_groups = 8

# Welche Funktionen verwendet werden um Aufgaben zu generieren
generators = [rand_ops, fruit_math]
# Verschiedenen Lösungen
# solutions = [1,2,3,4,5,6,7,8]
solutions = sample(range(30, 250), solution_groups)

# Generiere für jede Lösung gleich viele Probleme zufällig aus den Generator-Funktionen
aufgaben = [[(choice(generators)(x), x) for x in solutions] for _ in range(int(problems / len(solutions)))]
aufgaben = [x for sublist in aufgaben for x in sublist]

# Speichere die Aufgaben un einer Datei
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
