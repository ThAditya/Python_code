#Questions:Write a python program to find the vowel in string?
def find_vowels(string):
    vowels = ['a','e','i','o','u']
    found_vowels = []
    for char in string:
        if char.lower() in vowels:
            found_vowels.append(char)
    return found_vowels
sample_string = "Hello world"
print("vowels found in the string:", find_vowels(sample_string))

#Questions:Write a python program to find the vowel in string?
def find_vowels(string):
    vowels = ['a','e','i','o','u']
    found_vowels = []
    for char in string:
        if char.lower() in vowels:
            found_vowels.append(char)
    return found_vowels
sample_string = "Hello world"
print("vowels found in the string:", find_vowels(sample_string))

#Questions:Write a python program to generate OTP using lambda or random
import random
generate_otp = lambda: random.randint(100000, 999999)
otp = generate_otp()
print("your OTP is:", otp)

''' seudo codes'''
x = int(input("Enter the age"))
if x>= 18:
    print("eligible for vote")
else:
   sum = int(x)-18
   print("You have still" +str(sum)+ "years to vote")
    
#for calculator
import math
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
operation = ('+', '-', '*','/')
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    if b == 0:
        print('Error')
    else:
        result = a/b    
else:
    print("write the operation") 
               
print("result: ", +result)               

'''prime number'''
def is_prime(n):
    i = 0
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        return True
    
num = int(input("enter number"))
if is_prime(num):
    print('prime number') 
else:
    print('not prime number')    
    

#new program
print('enter the integer value') 
x = input()
print('enter the another integer value')
y = input()   
num1 = int(x)
num2 = int(y)
print(num1, '+', num2, '=', num1 + num2 )