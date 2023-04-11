#19. UpiĹĄi 10 cijelih brojeva s tipkovnice koriteÄi while petlju, te ispiĹĄite njihove srednje vrijednosti. 

sumaBrojeva = 0
count = 0

while count < 10:
    
    sumaBrojeva += int(input(f"Upiši broj {count + 1}: "))
    count += 1
 
print(f"Srednja vrijednost brojeva je {sumaBrojeva / 10}")



