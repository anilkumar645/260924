"write a program that counts the number of even and odd numbers in a list."

n = int(input("Enter input: "))

remainder = (n % 2)

is_even = (remainder == 0)

if is_even:
    print("Even")
else:
    print("odd")
