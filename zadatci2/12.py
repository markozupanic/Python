x = input("Enter any string: ")
#take input from user

a = x.split()
#use split method to split at whitespaces
print(a)
a.reverse()
#reverse all the elements of the string 
print(a)
print(' '.join(a))
#concatenate them into a string