#write a program number as input and print sum of numbers 

number = int(input("Number: "))
total = 1 

for i in range(1,number+1):
    total += i 
print(total)