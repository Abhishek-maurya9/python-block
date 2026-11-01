import os
file = open("demo.txt")
print(file.read())
file.close()

with open("demo.txt") as f:
    print(f.read(3))

with open("demo.txt") as f:
    print(f.readline())

with open("demo.txt") as f:
    print(f.readlines())

with open("demo.txt") as f:
  for x in f:
    print(x)

#Write()

with open("demo.txt", "a") as f:
  f.write("\nNow the file has more content!")
with open("demo.txt") as f:
  print(f.read())

with open("demo.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
with open("demo.txt") as f:
  print(f.read())

#delete
os.remove("demo.txt")
