#14. NapiÅ¡i program koji Äe unositi iznos odobreno g potroÅ¡aÄkog kredita c, godiÅ¡nju kamatnu 
#stopu p, broj mjeseci m, a ispisivati kamate prema formuli: k=cp(m+a)/2400 
#primjer: 
#unos:1000, 8, 12 
#ispis: 43.33

kredit=int(input("Dozvoljeni kredit: "))
kamatna_stopa=int(input("Kamatna stopa: "))
broj_mjeseci=int(input("Broj mjeseci: "))

kamata=kredit*kamatna_stopa*(broj_mjeseci+kredit)/2400
print(kamata)