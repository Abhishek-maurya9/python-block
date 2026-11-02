`print()`
Alway display the next output in new line , use `end` keyword for changing the ending and `sep` for changing seperator.

`input()`
Always return string output, so carefull when taking integer as input.

`eval()`
It takes string as input and avaluate the expression if possible.

### STRING
`capitalize()`
This makes the first letter of the string capital.

`find(param)`
This will return the index of passed argument appeared first time in string.

`endswith(param)`
This returns bool value for whether the string ends with passed argument.

`count(param)`
This returns the number of occurence of the passed argument.

`replace('old','new')`
This replaces the old value with new value.

`split(param)`
This will split the string from passed argument and retruns a list of elements.

`upper() & lower()`
This will make string in upper case and lower case.

`strip()`
This will remove all the trailing and leading whitespaces.

### LIST
It stores multiple values of different data types. The values are ordered and indexed.

`insert`
This will insert a new value at the provided index location.

`append`
This will insert an element at last of list.

`extend`
This will combine two existing lists.

`remove`
This will remove a specific element that is passed as argument.

`pop`
This will remove an element whose index is passed.

`del`
This will act same as pop just syntax is changed. If no index passed then complete list is removed

`clear`
This will completely clear the elements of list.Returns the empty list.

### TUPLE
The elements are ordered and can have duplicate values, but are immutable. No direct update is possible.

`add`
It adds one tuple to another tuple at the end.Uses '+' operator

`del`
It completely deletes a tuple and returns nothing.

`Tuple unpacking`
Assigning values to a tuple simply called destructuring. Returns a list if more than one value is passed to one value.
<details>
<summary>Ex.</summary>

```python
fruits = ("banana", "apple", "orange", "chiiko", "grapes")
(yellow, red, orange, grey, green) = fruits

(yellow, red, *orange) = fruits     (This will pass every value to orange.)

(yellow, *red, grey) = fruits  (This will pass every value to red till last subsequent value matches)
```
</details>


<b>If you wanted to update tuple then:</b>

```
                                    TUPLE 
                                      |
                                      |
                                LIST(UPDATE) 
                                      |
                                      |
                                    TUPLE
```

### SET
This is a collection of distinct and unordered elements.User can add or remove elements if needed directly.

`add`
This adds passed value to the set.

`remove`
This will remove the passed element and raises error if element is not found.

`discard`
This will remove the peassed vale and will not raise error if element not exist.

`clear`
This will return an empty set.

`del`
This will delete the complete set.

### DICTIONARY
It stores data in key-value pair. Data is ordered with non duplicate key.

`update`
This helps in both update value of specific key and add other key value pair which not exist(add new data).

`pop`
Removes the item of passed key.Co,pletely remove key-value from dictionary.

`popitem`
This will remove the last element from the dictionary.

`clear`
This will return an empty dictionary.

`copy`
This will copy the dictionary items to new array.

### CONDITION
`match-case`
It check each case and then returns the output of matching case.For default case need to use "_" 
```Python
case 1:
    print()
case _:
    print()
```

### LOOP
`while`
We use a while loop when the number of iterations is unknown and depends on a dynamic condition that changes during execution

`for`
We use a for loop when the number of iterations is known in advance or when iterating over a specific collection, such as a list, array, or range.

`for-else`
Else always executes when the complete for loop is executed. It cannot run on break command.

`range`
Returns a sequence of number starting by deafult from 0.(start, stop, step)

### FUNCTION
Function takes default value of parameter if argument is not passed.
*args and **kwargs allow functions to accept a unknown number of arguments.

`args`
This is passed as parameter and the function will receive a tuple of arguments and can access the items accordingly.
```python
def get(a, b, *args):
    print(args[1])
get(3,5,6,7,8,9,6)
```
`kwargs`
This is passed as parameter and the function will receive a dictionary of arguments and can access the items accordingly.
```python
def getNew(a, **kwargs):
    print(a)
    print(kwargs["name"])
getNew(6, data = 8989, name = "abhishek")
```

### OOPs
`Class` It is a collection of objects. It is a blueprint that provides set of methods and attributes for creating objects.

`Object` It is an instance of class that represents real world entity and used for storing data.

`Inheritance` This is a fundamental concept of OOPs that allows a class to inherit functionality of other calss.<B>Super()<B> keyword is used to call a method of parent class.

`Abstraction` Abstraction hides unnecessary implementation details and exposes only the essential functionality to the user.

`Polymorphism` Polymorphism allows the same interface, method name, or operation to behave differently depending on the object or the arguments involved.

`Encapsulation` Encapsulation bundles data (attributes) and the methods that operate on that data within a class, while controlling how that data is accessed or modified.

EX: BMW class can inherits from Car class.
    In Automatic Car, user's don't need to know what happens with engine while it starts.
    You call move() on each (Car, Bike, Boat), but the behavior depends on the object.
    Mobile phone: Internal hardware state is managed through controlled operations.
    

### Modules
`random`
It generates random values as per random module functions.

```python
random.random()
random.randint(a,b)
random.randrange(start, stop, step)
```
### VIRTUAL ENV
`Create`
This will create a virtual environment.
```"python -m venv name"```

`Activate`
Inside the env folder structure run activate inside Script.
`name/Scripts/activate`

`Deactivate`
In virtual environment CLI just type <b>deactivate</b>.

### FILE HANDLING
`open`
This is used to open file,takes two parameters; filename, and mode.

1. `r` - Read - Default value. Opens a file for reading, error if the file does not exist

2. `a` - Append - Opens a file for appending, creates the file if it does not exist

3. `w` - Write - Opens a file for writing, creates the file if it does not exist

4. `x` - Create - Creates the specified file, returns an error if the file exists

1. `t` - Text - Default value. Text mode

2. `b` - Binary - Binary mode (e.g. images)

```python
f = open("demo.txt")
with open("open.txt") as f: #function
f.close()
```
`opening file using "with" function automatically closes file after complete execution.` 

`read`
This is used to read files. Need to add `r` as mode while opening the file.
1. read() - return complete file data at once, if any index is not passed.
2. readline() - return first line when called first time.It returns line instead of complete file.
3. readlines() - return a list containing lines of file.

`write`
This is used to write in files. Need to add `a`, `w` as mode while opening the file.

```python
f = open("demo.txt", a)
f.write("hello..")
f.close()
```
`When using "w", if file is already there then the content of file is overwritten with new one.`
`While reading the file the cursor points at the last letter it read so, if read next time it will return nothing or empty list if called readlines.`

`delete`
This removes the file completely if file exist.

<hr>

## NUMPY LIBRARY
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.<br>

The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with `ndarray` very easy.
numpy array works on locality of reference, the elements are stored in a continous order.

`create`
We can create a NumPy `ndarray` object by using the `array()` function.We can use either list or tuple.

`Multidimension Array`
We need to use `ndmin` keyword to specify the number of dimensions the array to create.To verify the number of dimension, use `ndim` keyword. 
```python
arr = np.array((2,3,4,5), ndmin=5)
print(arr.ndim)
```

`access`
We can access array elements using their index and we can get list components using slice(start,stop,step).
arr[1,3] = 3rd index element from 1st index array.

`In 0D array and 1D array slice works same as list. But for 2D and 3D array it works like:`
1. 2D Array: 1st value represents the list and second value represents the list elements.
2. 3D Array: 1st & 2D value represents the list and 3rd value represents the list elements.


