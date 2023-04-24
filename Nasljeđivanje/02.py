#2. iz prethodne vjezbe iskoristite klasu zivotinja: iz nje izvedite 3 klase (mesojedi, biljojedi, svejedi). 
# iz svake od navedenih klasa izvedite po jednu klasu sa nazivom zivotinje (npr slon, sova, riba).
# osmislite atribute i metode tako da budu smisleni i neka nesto ispisuju - npr. iz klase mesojed, neka ispise: "hranim se mesom!".
from mesojedi import Mesojedi
from biljejedi import Biljojedi
from svejedni import Svejedi

class Zivotinje(Mesojedi,Biljojedi,Svejedi):
    def print_podataka(self):
      print(f"mesojedi: {Mesojedi.ovo_za_print} svejedi:{Svejedi.ovo_za_print} biljojedi: {Biljojedi.ovo_za_print}")
    
Zivotinje.print_podataka()












































