#1. napravite klasu Zivotinja. unutar klase definirajte konstruktor koji sadrzi atribute za 
# naziv, tip, masu, vrstu ishrane. definirajte i metodu unutar klase koja ce ispisati navedene atribute,
# zatim kreirajte dva razlicita objekta te pozovite kreiranu metodu.

from Zivotinje import Zivotinje

pas=Zivotinje("riki","ovčar","15","meso")
macka=Zivotinje("plavko","ruska mačka","7","mačja hrana")

Zivotinje.ispisi_atribute(pas)
Zivotinje.ispisi_atribute(macka)














