# multiplication table for a given number 

n = int(input("Enter number: "))

for i in range(1,11):
    a = n* i 
    print(str(n) +" X " + str(i) + " = " + str(a))