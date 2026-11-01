#CONDITION:
"""
age = int(input("Enter your age: "))
if(age < 12):
    print("You are Child!")
elif(age < 25):
    print("You are Teenager!")
else:
    print("You are Old!")
"""

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number")
"""
#LOOP

#While loop
num = 1
while(num < 5):
    print("hello", num)
    num += 1

num2 = int(input("enter number"))
i = 1
while(i <= 10):
    print(f'{num} * {i} = ', num * i)
    i += 1


lst = [1,3,5,6,9,23,67,89,34,6,7]
i = 0
while(i < len(lst)):
    print(lst[i])
    i += 1

x = int(input("enter number"))
i = 0
while(i < len(lst)):
    if(lst[i] == x):
        print("elem found", i)
        break
    i += 1


#For loop
lst = [1,3,5,6,9,23,67,89,34,6,7]
for i in lst:
    if(i == 6):
        break
    print(i)
print("breaked")

for i in lst:
    if(i == 6):
        break
    print(i)
else:
    print("breaked")

for i in lst:
    if(i == 6):
        continue
    print(i)
else:
    print("continued")


#Range
for i in range(2,20,2):
    print(i)

for i in range(50, -1, -2):
    print(i)

num = 5
for i in range(1, 11, 1):
    print(f"{num} * {i} = ", num * i)
"""