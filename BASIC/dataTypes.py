#STRING
"""
str1 = "hello World!"
print(str1)
str2 = "I'm Abhishek"
print(str2)

greet = "Hello guys,\n I am a developer"
print(greet)

name = "I am Abhishek "
desig = "I am a developer"
print(name + desig)

print(len(greet))
print(len(name))
print(len(desig))

#INDEXING & SLICING

str1 = "Abhishek"
print(str1[2])
print(str1[5] == 'h')

str2 = "I am Abhishek and a blockchain developer"
print(str2[:5])
print(str2[2:8])
print(str2[::2])
print(str2[::-1])

print(str2[-5:-1])
print(str2[-12:])

#METHODS:
str = "I am Abhishek and a blockchain developer"

print(str.endswith('per'))
print(str.capitalize())
print(str.count("e"))
print(str.replace('a', 'e'))
print(str.replace("developer", "engineer"))
print(str.find('a'))
print(str.upper())
print(str.lower())
print(str.strip())
print(str.split("a"))


#Format String:
 
age = 24
print(f"I am Abhishek. I am {age} years")

price = 26.89867
print(f"The price of PC is {price:.3f} only")
"""

#LIST:
"""
lst = [1, "ABHISHEK", 20, True]
print(lst)
print(type(lst))
print(len(lst))

print(lst[1])
print("till 20:", lst[:3])
print("from 1st till last:",lst[1:])

lst[2] = 21
print(lst)

lst[1:4] = ["hello", 26]
print(lst)

del lst[0]
print(lst)

new_list = list(("abhishek", 21, "blockchain"))
print(new_list)

if "ABHISHEK" in lst:
    print("found")

lst = ["abhishek", 21, "blockchain", True, "hello"]

#insert()
lst.insert(2, "Python Developer")
print(lst)

#append()
lst.append("apple")
print(lst)

#extends()
lst2 = [1, "akash", 22]
lst.extend(lst2)
print(lst)

#remove()
lst.remove('apple')
print(lst)

#pop()
lst.pop(2)
print(lst)

#del()
del lst[1]
print(lst)

#clear
lst.clear()
print(lst)

#Loop
lst = ["abhishek", 21, "blockchain", True, "hello"]
for x in lst:
    print(x)

[print(x) for x in lst]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if 'a' in x]
print(newList)
"""

#TUPLE
"""
tup = ("abhishek", 22, True)
print(tup)

tup2 = "abhi", 24, "fullstack"
print(tup2)
print(type(tup2))
print(len(tup2))

tup3 = tuple(tup2)
print(tup3)

print(tup3[0])
print(tup[:3])

# tup[0] = "abhi" will fail

#add tuple
tup3+= tup
print(tup3)

del tup3

tup = ("Abhishek")
print(type(tup))

tup = ("Abhishek", )
print(type(tup))

#Tuple Unpacking
fruits = ("banana", "apple", "orange", "chiiko", "grapes")
(yellow, red, orange, grey, green) = fruits
print(red, yellow, orange)

(yellow, red, *orange) = fruits
print(orange)

(yellow, *red, grey) = fruits
print(red, grey)
"""

#SET:
"""
data = {"apple", "cherry", "cherry", True, 1, False, 0}
print(data)

data = set(("apple", "cherry", "cherry", True))
print(data)

print(len(data))
print(type(data))

#access
for x in data:
    print(x)

#add()
data.add("orange")
print(data)

#remove()
data.remove("orange")
print(data)

#discard()
data.discard("apple")
print(data)

#clear()
data.clear()
print(data)

del data

#loop
data = set(("apple", "cherry", "cherry", True))
for x in data:
    print(x, end="\t")
"""

#DICTIONARY
"""
data = {
    "name" : "Abhi",
    "branch" : "CSE",
    "age" : 21,
    "desig" : "dev"
}
print(data)
print(data["name"])
print(data.get("age"))
print(data.items())
print(data.keys())
print(data.values())

print(len(data))
print(type(data))

data = dict(name = "abhi", age = 21, branch = "CSE")
print(data)

data["name"] = "Abhishek"
print(data)

data.update({"branch" : "CSD"})
print(data)

data.update({"dev" : "Blockchain"})
print(data)

data["marks"] = 45
print(data)

data.pop("age")
print(data)

data.popitem()
print(data)

del data["name"]
print(data)

data.clear()
print(data)

data = dict(name = "abhi", age = 21, branch = "CSE")
for x, y in data.items():
    print(x, y)

"""