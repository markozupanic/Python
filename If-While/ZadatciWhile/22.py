#23. NapiĹĄite program za koji traĹži najveÄi zajedniÄki djelitelj dvaju brojeva


broj_a = int(input("Unesi broj a: "))
broj_b = int(input("Unesi broj b: "))
counter = 0
nzd = 0

if broj_a > broj_b:
    counter = broj_b
elif broj_a < broj_b:
    counter = broj_a
elif broj_a == broj_b:
    counter = broj_a

# Traži nzd
while counter > 0:
    
    if broj_a % counter == 0 and broj_b % counter == 0:
        nzd = counter
        break
    
    counter -= 1
   
print(f"Najveći zajednički djelitelj brojeva {broj_a} i {broj_b} je {nzd}.")








