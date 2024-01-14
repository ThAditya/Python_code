# WAP to print a pattern  of triangle
n = int(input("enter the number of rows: "))
for i in range(1, n+1):
    print("*"* i)
    
# WAP to print inverted right angled triangle
for i in range(n, 0, -1):
    print("*"* i)
    
#WAP to print equilateral triangle
for i in range(1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# Diamond Pattern
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1, 0, -1):
    print(" " * (n-i) +"*"*(2*i-1))   
    
 # pattern by the help of stars   
print("Pattern of Stars (*): ")
k = 1
for i in range(5):
    for j in range(k):
        print("* ", end="")
    k = k+2
print()

print("Pattern of Stars (*): ")
k = 1
space = 16
for i in range(5):
    for j in range(space):
        print(" ", end="")
    space = space-4
    for j in range(k):
        print("* ", end="")
    k = k + 2
print()    
'''possword'''
import random
import string
def generate_password():
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_symbols = string.punctuation
    uppercase_letters_1 = random.choice(uppercase_letters)
    uppercase_letters_2 = random.choice(uppercase_letters)
    digit = random.choice(digits)
    special_symbol = random.choice(special_symbols)
    remaining_chars = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=6))
    password = uppercase_letters_1 + uppercase_letters_2 + digit + special_symbol + remaining_chars  
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

print(generate_password())

# WAPP to print months of calender
import calendar
year = int(input())
print(calendar.calendar(year))