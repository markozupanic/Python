#4. napravite klasu po zelji. neka jedna metoda prima args, a druga kwargs. objektu predajte odgovarajuce vrijednosti te ih ispisite.

class Hero():

    def init(self):
        pass

    def argsFun(self, a, *args):
        print("a: ", a)
        print("args: ", args)

    def kwargsFun(self, **kwargs):
        print(kwargs["name"])
        print("kwargs: ", kwargs)

Batman = Hero()
#args prima više parametara ali ispisuje prvu po redu
Batman.argsFun(32, 8, 2, 1)

#kwargs funkcionira kao dictionary, prima argument kao kljuc/vrijednost
Batman.kwargsFun(name="Darijan")






























