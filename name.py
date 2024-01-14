name= "aDITYA"
print(name.swapcase())

#factorial number
n = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# If the input is negative, print an error message
if n < 0:
    print("Factorial does not exist for negative numbers")
# If the input is 0, the factorial is 1
elif n == 0:
    print("Factorial of 0 is 1")
# Otherwise, calculate the factorial
else:
    for i in range(1, n+1):
        factorial *= i
        print("Factorial of", n, "is",factorial)
        
x = "hello"
print(len(x))

#string function REPLACE
y = "hello"
print(x.replace("l","w"))

#string function FIND
x = "hello"
print(x.find("l"))

#string function COUNT
x = "This is my house"
print(x.count("i"))

#string fuction UPPERCASE
x = "helloo"
print(x.upper())

#string function LOWERCASE
x = "HELLO"
print(x.lower())        

'''modules in python'''

#Random module: it is going to use return floating values b/w 0 to 1
import random
x= random.random()
print(x)

#Randint module: it is return integar values b/w given range(argument1 and argument2)
import random
x= random.randint(2, 9) # type: ignore
print(x)

#randrange module: it is return integer value b/w given range but not included argument2
import random
x= random.randrange(2,8)
print(x)

#choice module: it is return random element of list 
import random
a= ['Aditya','GLA','Manshi']
print(random.choice(a))

#choices module: it is return multiple elements from list
import random
a= ['Aditya','GLA','Manshi']
print(random.choices(a))

#sample module: it si return specific no. of element from a list
import random
a= ['GLA','Amit', 'NIT']
print(random.sample(a, ))

#uniform module: it is return decimal value b/w given range
import random
x = random.uniform(2.1, 3.9)
print(x)

'''math in python'''
import math
print(math.sqrt(4))
print(math.factorial(4))
print(math.pow(2,2))
print(math.fabs(-4))
print(math.fsum(1,2))
print(math.prod(3,2)) # type: ignore
print(math.ceil(54.56))
print(math.floor(54.56))
