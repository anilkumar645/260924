#factorial of a number

number = int(input("Enter a number: "))
factorial = 1 

if number == 0:
    print("Factorial of entered number {} is {}".format(number,factorial))

else:
    for i in range(1,number+1):
        factorial += i 
    print("Factorial of entered number {} is {}".format(number,factorial))
        
