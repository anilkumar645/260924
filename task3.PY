

s = input("Enter a string: ") #abcdef  
#print(s[:]) #abcdef 
#print(s[0:5]) #abcde 
#print(s[0:5:1]) #abcde 
#maprint(s[::]) #abcde 

revstr = (s[::-1]) #edcba reverse string 

if revstr == s:
    print("Palindrome")
else:
    print("Not a palindrome")