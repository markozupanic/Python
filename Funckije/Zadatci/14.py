#14. napisi funkciju koja pronalazi brojeve izmedju 2000 i 3200 djeljive sa 7,
# ali koji nisu djeljivi sa 5. dobiveni brojevi moraju biti ispisani u liniji, odvojeni zarezom

def brojevi_djeljivi_sa_7():
    counter=2000
    for i in range(2000,3201):
        if(i%7==0 and i%5!=0):
            print(i,end=", ")
        

brojevi_djeljivi_sa_7()




































