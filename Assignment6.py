def greet():
    print("Hello!")

greet() 
#A user-defined function is created by the programmer to perform a specific task


def add():
    print(10 + 20)

add()

 # def is used to define a function, and : marks the beginning of its body.

def hello():      # Definition
    print("Hi")

hello()           # Call
#defining creates the function, calling executes it. A function can be called multiple times.

def future_code():
    pass

print("Done") 
#pass is a placeholder for code that will be written later.

def greet(name):      # Parameter
    print("Hello", name)

greet("Rahul")        # Argument

#A user-defined function is created by the programmer to perform a specific task.

def square(n):
    return n * n

print(square(5))
# return sends the result back to the function caller.

def values():
    return 10, 20

a, b = values()
print(a, b)
#Python returns multiple values by packing them into a tuple.