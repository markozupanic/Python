#11. napisi funkciju koja prima listu i vraca jedinstvene elemente prve liste.
#Nerazumijem zadatak 

lista=["bsuks","vdjsnV K","bidsnvlk",[12,14,48],"fsnK"]

def unique_elements(lista):
    jedinstveni = []
    for element in lista:
        if element not in jedinstveni:
            jedinstveni.append(element)
    return jedinstveni


unique_elements(["bsuks","vdjsnV K","bidsnvlk",[12,14,48],"fsnK"])













