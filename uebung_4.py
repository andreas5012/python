#!/usr/bin/python3
# coding: utf-8
# Aufgabenstellung
# Betrachten Sie eine beliebige natürliche Zahl n. Wenn n gerade ist,
# dividieren Sie n durch 2. Wenn n ungerade ist, berechnen Sie 3n + 1. Wie-
# derholen Sie dieses Vorgehen beliebig oft. Wahrscheinlich werden Sie früher
# oder später bei 1 ankommen. – Die Collatz-Vermutung (aufgestellt 1937 vom
# deutschen Mathematiker Lothar Collatz, 1910–1990) besagt, dass man aus-
# gehend von irgendeiner natürlichen Zahl immer bei 1 ankommt. Schreiben
# Sie ein Programm, das für die Zahlen von 2 bis 100 die Collatz-Vermutung
# überprüft.

# Ändern Sie Ihr Programm aus Übung 3 so, dass es für jede getestete
# Zahl die Anzahl der Schritte bestimmt, die nötig sind, um 1 zu erreichen.
# Was ist die größte Anzahl von Schritten, die für Zahlen bis 100 vorkommt?
# Wie sieht es aus für Zahlen bis 1000?
#
n=100
m=n
z=0
while m == 1:
    while n != 1:
        # print (n)
        if n % 2 == 0:
            n = n // 2

        elif n % 2 == 1:
            n = 3 * n + 1
        continue
m -= m
print ("Fertig!")
