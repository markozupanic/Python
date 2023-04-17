#19. napisi funkciju koja pronalazi brojeve izmedju 1000 i 3000, 
# u kojima je svaka znamenka paran broj ili nula te ih ispisuje odvojene zarezom (npr. 2000, 2002, 2004...)


def pronalazi_brojeve_1000_3000():
    rezultat = []

    for broj in range(1000, 3001):
        
        broj_str = str(broj)
       
        sve_pare = True
        for znamenka in broj_str:
            if int(znamenka) % 2 != 0 and znamenka != '0':
                sve_pare = False
                break
        if sve_pare:
            rezultat.append(broj)
    
    print(", ".join(map(str, rezultat)))





pronalazi_brojeve_1000_3000()









