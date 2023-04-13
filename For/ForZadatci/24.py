#24. Napišite program koji ispisuje koliko ima prostih brojeva između 
#dva proizvoljna broja.


num=int(input("unesi broj: "))
num_veci=int(input("unesi broj: "))

for num in range(num_veci):

 if num > 1:
    # Iterate from 2 to n / 2
     for num in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        num+=1
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
     else:
        print(num, "is a prime number")
 else:
    print(num, "is not a prime number")










