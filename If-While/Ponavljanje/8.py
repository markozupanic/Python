#7. Napravi program za umnožak dva unesena stringa, bez korištenja integriranih metoda za pretvorbu stringa
#   u int "int()", dozvoljeno je korištenje ascii kodova. Rezultat množenja treba biti u string formatu.


rijec = "neka rijec nesto novo"
asciiRijec = ""
izabranoSlovo = ""
asciiSlovo = ""
counter = 0
brojSlova = len(rijec)


while(counter<brojSlova):
    izabranoSlovo = rijec[counter]
    asciiSlovo = str(ord(izabranoSlovo))
    asciiRijec = asciiRijec + asciiSlovo + " "

    counter = counter + 1

mnozitelj = 10
counter = 0
novaAsciiRijec = ""

while(counter<mnozitelj):
    novaAsciiRijec += asciiRijec # "množenje" stringova (2 puta)
    counter += 1



novaRijec = ""
novaAsciiRijecDuljina = len(novaAsciiRijec)
asciiJedan = ""
counter = 0
print(len(novaAsciiRijec))

while(counter<novaAsciiRijecDuljina):
    if(novaAsciiRijec[counter] == " "):
       
        counter += 1
        novaRijec += chr(int(asciiJedan))
        asciiJedan = ""
        continue
    asciiJedan =  asciiJedan + novaAsciiRijec[counter]    
    counter += 1

print(novaRijec)
    
















