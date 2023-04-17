
# globalna varijabla; mozemo ju dohvatiti u funkciji
something = "123"
def fit(x_train, y_train, epochs=1, batch_size=32):
    global something
    something = "hey, it's something"
    print(f"data consists of {x_train} features and {y_train} labels")
    print(f"training for {epochs} epochs with batch size {batch_size}")


# poziv funkcije; prvo positional argumenti pa onda kw argumenti!
fit(1650, 9, epochs=15)
# buduci da je something definiran i izvan i unutar funkcije, gleda se onaj
# koji je posljednji put pozvan, jer "overwrite"-a vrijednost
print(something)
# *rest oznacava niz i mozemo predati bilo koji broj argumenata
def my_new_function(a, b, *rest):
    print(a, b)
    print(rest)


my_new_function(22, 33, 55, 66, 77, 99)

# **kwargs oznacava keyword arguments i radi dict od vrijednosti
def my_kw_function(a, b, **kwargs):
    print(a, b)
    print(f"ja sam {kwargs.get('name')} i imam {kwargs['age']} godina")
    print(kwargs)


# predajemo positional argumente i kwargs u obliku key=value
my_kw_function(27, 12, name="dani", age=30)
