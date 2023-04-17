#12. napisi funkciju koja prima dvije liste i vraca listu brojeva koje se poklapaju u njima 
# (npr. za unos [1, 2, 3, 4] i [2, 3, 6, 7] vrati [2, 3])


def vraca_zajednicke_brojeve():
    lista_prva=[1, 2, 3, 4]
    lista_druga=[2, 3, 6, 7]
    lista_prva=set(lista_prva)
    lista_druga=set(lista_druga)
    
    print(lista_prva&lista_druga)
    
vraca_zajednicke_brojeve()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
