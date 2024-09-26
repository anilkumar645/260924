#write a program that prints the number from 1 to 100 
#for multiple of 3 print "Fizz"
#for multiple of 5 print "Buzz"
#for number both multiple five and three print "FizzBuzz"



def Fizz_Buzz(input):

    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    return input
print(Fizz_Buzz(15))
