#25. napisi funkciju koja prima tri liste popunjene stringovima te ispisuje sve kombinacije stringova.

def kombinacije_stringova():
    lista_jedan=["marko","andrea","dario"]
    lista_dva=["goran","ankica","ante"]
    lista_tri=["ivan","luka","leonarda"]
    
    for i in range(len(lista_jedan)):
        for j in range(len(lista_dva)):
            for k in range(len(lista_tri)):
                print(lista_jedan[i]+lista_dva[j]+lista_tri[k],end=" ")
                print(lista_jedan[i]+lista_tri[k]+lista_dva[j],end=" ")
                print(lista_dva[j]+lista_jedan[i]+lista_tri[k],end=" ")
                print(lista_dva[j]+lista_tri[k]+lista_jedan[i],end=" ")
                print(lista_tri[k]+lista_jedan[i]+lista_dva[j],end=" ")
                print(lista_tri[k]+lista_dva[j]+lista_jedan[i],end=" ")
            



kombinacije_stringova()

















