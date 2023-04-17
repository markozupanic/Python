#5. zadani su tupleovi:
tuple1 = (11, 22)
tuple2 = (99, 88)
#zamijenite im vrijednosti (npr. da tuple1 bude (99, 88), a tuple2 bude (11, 22)

tuple1=list(tuple1)
tuple2=list(tuple2)
tuple1.clear()
tuple1.append(99)
tuple1.append(88)
print(tuple1)
tuple2.clear()
tuple2.append(11)
tuple2.append(22)
print(tuple2)





