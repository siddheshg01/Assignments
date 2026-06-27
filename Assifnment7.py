x = 10      # Global

def demo():
    y = 20  # Local
    print(x, y)

demo()
#A local variable exists inside a function, while a global variable is accessible throughout the program.

count = 0

def increase():
    global count
    count += 1

increase()
print(count)
#Too many global variables make the program difficult to manage and debug.

x = 5

def change():
    global x
    x = 10

change()
print(x)
#The global keyword allows a function to modify a global variable.

def outer():
    return inner

def inner():
    print("Hello")

f = outer()
f()

#A function can return another function as its result.

import math

print(math.sqrt(25))
#A module is a Python file, while a function is a block of code inside it.

def demo():
    x = 10
    y = 20
    return x, y

a, b = demo()
print(a, b)

# return x returns one value, return x, y returns multiple values, and return returns nothing (None)