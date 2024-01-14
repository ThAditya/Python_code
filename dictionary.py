#1. dict.keys() - This method returns a view object that contains all the keys of the dictionary. The view object can be used to iterate through the keys of the dictionary or to convert the keys into a list. For example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
for key in keys:
    print(key)
key_list = list(keys)
print(key_list)

'''Output:

a
b
c
['a', 'b', 'c']'''

#2. dict.values() - This method returns a view object that contains all the values of the dictionary. The view object can be used to iterate through the values of the dictionary or to convert the values into a list. For example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
for value in values:
    print(value)
value_list = list(values)
print(value_list)


'''Output:

1
2
3
[1, 2, 3]'''

#3. dict.items() - This method returns a view object that contains all the key-value pairs of the dictionary as tuples. The view object can be used to iterate through the key-value pairs of the dictionary or to convert the key-value pairs into a list. For example:

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
for key, value in items:
    print(key, value)
item_list = list(items)
print(item_list)

'''Output:

a 1
b 2
c 3
[('a', 1), ('b', 2), ('c', 3)]'''

#popitem()
x = {'name':'Aditya', "Roll no.": 102, "Roll id":104 } # type: ignore
x.popitem()
print(x)

#pop()=
x = {'name':'Aditya', "Roll no.": 102, "Roll id":104 } # type: ignore
x.pop('name')
print(x)

#get()=
x = {'name':'Aditya', "Roll no.": 102, "Roll id":104 } # type: ignore
y=x.copy()
print(y.get('name'))

'''Fibonacy series'''

number=int(input("Enter any number: "))
num1 = 0; num2 = 1
print(num1)
print(num2) 
for i in range(1, number):
    num3 = num1 + num2
    print(num3)
    num1, num2 = num2, num3