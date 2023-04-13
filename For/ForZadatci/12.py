#12. Napišite program koji ispisuje zbroj parnih brojeva od 1 do 20

parni_brojevi=0
brojevi=1

for brojevi in range(21):
    if(brojevi%2==0):
        parni_brojevi+=brojevi
        
print(parni_brojevi)

