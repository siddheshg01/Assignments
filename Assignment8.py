#mymodule.py

#def greet():
    #print("Hello")

main.py

import mymodule

mymodule.greet()
#Create a Python file (module) and import it into another program

import math
from math import sqrt
import math as m

print(math.sqrt(25))
#python modules can  imported in different ways

if True:
    print("Inside")

print("Outside")
# code block starts with : and ends when the indentation ends

from math import *

print(sqrt(16))
#import * is discouraged because it can cause name conflicts

import math

print(math.factorial(5))

#modules help reuse code and make programs easier to maintain

print("Module Loaded")

def hello():
    print("Hello")

    #Statements outside functions execute immediately when the module is imported.


import random

print(random.randint(1, 10))

#Modules organize code into reusable and manageable files.
