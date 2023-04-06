#9. IzraÄunati sumu prirodnih brojeva u intervalu od 1 do n koji nisu djeljivi sa a.

n=int(input("Unesi broj: "))
a=1

while(a<n):
    if(n&a==0):
        n=n+1
        print(n)
    a+=1






