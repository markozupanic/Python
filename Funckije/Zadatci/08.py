#8. napisi funkciju koja prima string, provjerava je li string palindrom te ako nije, ispisuje ga unazad (npr. "zadatak" => "katadaz")


def palindrom():
    unos=input("Unesite riječ: ")
    if(unos==unos[::-1]):
        print("Riječ je palindrom")
    else:
        print(unos[::-1])
        
        
palindrom()
























