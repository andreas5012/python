# coding: utf-8
# Aufgabenstellung
# Schreiben Sie ein Programm, das die Zahlen 1 bis 50 ausgibt (eine
# pro Zeile), mit den folgenden Ausnahmen:
# • Ist eine Zahl durch 5 teilbar, wird statt der Zahl das Wort »Hopp« aus-
# gegeben.
# • Ist eine Zahl durch 7 teilbar, wird statt der Zahl das Wort »Hipp« aus-
# gegeben.
# • Ist eine Zahl durch 5 und 7 teilbar, wird statt der Zahl die Phrase »Hipp
# Hopp« ausgegeben.

i = 1
while i <= 50:
    if (i % 5 == 0) and (i % 7 == 0):
        print "Hipp Hopp"
    elif i % 5 == 0:
        print "Hipp"
    elif i % 7 == 0:
        print "Hopp"
    else:
        print i
    i += 1
