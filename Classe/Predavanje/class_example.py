# import Kutija
from Kutija import Car

vw = Car("vw", "passat", 200)
skoda = Car("skoda", "octavia", 150)
vw.print_something()
Car.print_something(skoda)
print(f"hp skoda {skoda.hp}")
