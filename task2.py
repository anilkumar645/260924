"write a program that checks if a given number is prime a prime number is a number greater than 1 that is only divisible 1 and itself"

count = 0 
n = int(input("Enter number: "))

for i in range(1,n+1):
    if n % i == 0:
        count += 1 


if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

