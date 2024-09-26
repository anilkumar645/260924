# largest of 3 numbers using if statement 

#first num1 = 56 
#second num2 = 76
#third num3 = 455 

a = int(input("Enter 1st no: "))
b = int(input("Enter 2st no: "))
c = int(input("Enter 3st no: "))

if a>b and a>c:
    max = a;
elif b>a and b>c:
    max = b;
else:
    max = c;
print("Maximum number: ",max)