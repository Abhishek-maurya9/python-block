"""
print("hello world!")
print(20,4,50,67,sep="\t")
print(50,44,70,87,sep="\n", end="!!.")
print(20,4,50,67,sep=",", end="\n")
print(40,45,80,17,sep=",", end="nice")
"""

#DATA TYPES
'''
#INTEGER
num = 678
print(type(num), num)

dec = -667.78
print(type(dec), dec)

comp = 3 + 5j
print(type(comp), comp)

cond = num < dec
print(type(cond), cond)

#SEQUENCE
lst = [2,3,4,5]
print(type(lst),lst)

tup = (2,3,4)
print(type(tup), tup)

str = "hello"
print(type(str), str)

#Mappings
dict = {"name":"abhishek", "class": 4, "pass": True}
print(type(dict), dict)

#Set
# data = set(3,4,5,3,4,2,5,3)
# print(type(data),data)

var1 = None
print(type(var1), var1)
'''

#INPUT()
'''
name = input("enter your name ")
print(type(name), name);

x = int(input("enter first number: "))
y = int(input("enter second number: "))
print(type(x) , type(y), x+y)
'''

#EVAL()
'''
sum = eval('10+79')
print(type(sum), sum)

data = eval("78")
print(data)
'''

#ASSIGNING
name, branch, desig, salary = "Abhi", "CSE", "Blockchain Developer", 5000 
print(name, salary)

data = ["Abhi", "DSE", "Blockchain Developer", 6800 ]
name, branch, desig, sal = data
print(name, branch, desig, sal)

data = ("Abhi", "Blockchain Developer", 6800 )
name, desig, sal = data
print(name, desig, sal)