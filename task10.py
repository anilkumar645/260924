number = int(input("Enter the number : "))

length = len(str(number))

temp = number 
sum = 0 
while temp >0:
    digit = temp % 10 
    sum += digit ** length 
    temp = temp // 10

print("Number is {} and sum is {}".format(number, sum ))
if sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    