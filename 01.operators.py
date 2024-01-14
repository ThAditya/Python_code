'''Arithmatic operators = it is going to use for calculate the two or more than two 
integers values.e.g;'''
a = 6
b = 5
print("the value of a,b is",(a+b))
print("the value of a,b is",(a-b))
print("the value of a,b is",(a*b))
print("the value of a,b is",(a/b))
print("the value of a,b is",(a%b))

'''Assignment operator = In this operator we can add, multiply, subtract or divide the
value of variable without changing it only taking the help of the using variable.e.g;'''
a = 50
a -= 40    #After the doing any operation in this operator the value will be stored
a *= 25   
a /= 75
a += 50    
print(a)

'''comparison operator = this operator going to be returned Boolean expression after
seeing the condition.e.g;'''
# b = (14>=5)
# b = (14<=5)
# b = (14>5)
b = (14<5)
# b = (14==5)
# b = (14!=5)
print(b)

'''Logical operator = This operator is going to be used for checking the boolean 
expressions like in (1)AND Log. opr.= the condition of both variables is equal or same 
then it will be show true otherwise it will show false (2)OR Log. opr. = The condition 
of any one variable is true so it will be show true if the both variables condition is
false so it will show false (3)NOT Log. opr.=It only work on one variable and it'll 
change the boolean expression .e.g;'''
#for AND log. operator
x = 'hello'
y = 'world'
if(x and y):
    print('yes') 



#index
x = ['apple','bnanana','mango','watermelon']

print(x.index("bnanana"))
    
# count
x = ['apple','cherry','apple']
print(x.count("apple"))    

#copy
x = ["abc","abc","abc"]
print(x.copy())

'''variables in python'''

#None = it is used for showing nothing in any variable which is going to choose.e.g,
a = "Addii"
a = None
b = 1234
b = None
c = 30.798
c = None
print(a)
print(b)
print(c)

#Boolean = it is going to used for show the condition is true or false.e.g,
a = "Addii"
b = 1234
c = True
print(a)
print(b)
print(c)

#Integer = The all real numbers in Python is integers.e.g,
a = 1234
print(a)

#Float = The number which is write by using decimal.e.g,
a = 54.645
print(a)

'''string = The character type values are strings which will going to write in single,
double or triple codes.e.g,'''
a = "Addii"
print(a) 

'''printing the types of variables = it will going to use to know the which type of 
datatype of any variable.e.g,'''
a = "Addii"
b = 1234
c = 56.45
d = None
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))