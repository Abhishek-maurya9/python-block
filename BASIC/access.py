#import module
import module as mod
from module import mul
import json
"""
mod.greeting("Abhi")

sum = mod.sum(4,5)
print(sum)

div = mod.div(99,0)
print(div)

country = mod.person1["country"]
print(country)

mul = mul(6,9.4)
print(mul)

print(dir(mod))
"""
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["age"])

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))