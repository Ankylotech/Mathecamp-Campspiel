# Wie funktioniert das ganze?

## Hauptfunktionalität in aufgaben_campspiel.py

In 'aufgaben_campspiel.py' werden Lösungszahlen für Aufgaben generiert. Die Liste 'generators' sammelt Funktionen, die
zu einer bestimmten Lösung Aufgaben generieren. Die Funktionen werden dann zufällig auf die verschiedenen 
Lösungszahlen aufgerufen und die entstehende Liste gespeichert und am Ende in output.txt geschrieben

## Generator-Funktion in operations.py

Die Funktion 'n-ops' nimmt als Parameter eine Lösungszahl und die Anzahl der Operationen. 
Ist die Anzahl der Operationen 0, so wird nur die Zahl ausgegeben. Ansonsten wird die Anzahl der Operationen in einen 
"linken" und in einen "rechten" Teil der Operation aufgeteilt. Dann wird eine der Operationen +,-,*,/ gewählt und die 
Zielnummer entsprechend aufgeteilt. Ist die Operation zum Beispiel '-' wird eine neue zufällige Zahl x generiert und 
die linke Seite generiert dann 'gewollte Lösung + x' und die rechte x. Das Generieren der beiden hälften erfolgt dann
durch einen rekursiven Aufruf der Funktion 'n-ops'.

Um eine Aufgabe zu nur einer bestimmten Lösung zu generieren, gibt es die Funktion 'rand_ops', die 'n_ops' mit einer 
zufälligen Anzahl an Operationen aufruft.

## Generator-Funktion in fruit_math.py

Die Funktion 'fruit_math' generiert ein Gleichungssystem mit einer zufälligen Anzahl an Variablen. Die Lösungszahl wird
dafür zunächst in Summanden aufgeteilt und die Variablen bekommen einen Faktor des jeweiligen Summanden zugeteilt.
Dann werden für das Gleichungssystem zufällige Gleichungen generiert.
Zum Schluss wird nur noch die Gleichung für unsere Lösung angehängt

# Was ist noch zu tun

* Neue Generator-Funktionen hinzufügen
* Ideen für neue Generator-Funktionen finden:
  * ...
* Generator-Funktionen testen und passende Schwierigkeiten finden