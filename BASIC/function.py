#FUNCTION
def sum(a, b = 5):
    return a + b
print(sum(5))
print(sum(3,9))

#args & kwargs
def get(a, b, *args):
    print(a,b)
    print(args, args[3])
get(3,5,6,7,8,9,6)

def getNew(a, **kwargs):
    print(a)
    print(kwargs["name"])
getNew(6, data = 8989, name = "abhishek")

def func(*nums, **nums1):
    print(nums[1], nums1["desig"])
func(4,5,3,name = "abhi", desig = "dev")

