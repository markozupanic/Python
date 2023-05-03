for i in range(10):
    if(i==0):
      prethodni_broj=i
    else:
        prethodni_broj=i-1
    suma=i+prethodni_broj
    print(f"Current number: {i} Previous number {prethodni_broj}  sum={suma}")