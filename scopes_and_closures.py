#%% Importing libraries
import pandas
import numpy

# %% Question1 - Write a closure that takes a function and then check whether the function 
# passed has a docstring with more than 50 characters. 50 is stored as a free variable

def outer(n):

    def inner(func):
        nonlocal n
        if callable(func):
            if len(func.__doc__) > n:
                print(f"The function passed has more than 50 characters in the doc string")
            else:
                print(f"The function passed has less than 50 characters in the doc string")
        else:
            print(f"Not a function")
    return inner

# %% Test cases:
# 1.Passing non function:
a = "Blah!"

doc_str_check = outer(50)
doc_str_check(a)

# 2.Passing empty doc string
def func1():
    ""
    return

doc_str_check(func1)

# 3.Passing greater than 50 characters
def func2():
    "Is it 50 characters yet? Is it 50 characters yet? Is it 50 characters yet? I guess so"
    return

doc_str_check(func2)


# 4.Passing less than 50 characters 
def func3():
    "Thats not 50 characters"
    return

doc_str_check(func3)

# %% Question2 - Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100

def fib_series():
    a = 0
    b = 1
    def next():
        nonlocal a, b
        z = a
        c = a+b
        a = b
        b = c
        return z
    return next

# %% Test cases:

# 1. First number
fib_next = fib_series()

if fib_next() != 0:
    print("Case failed!")

# 2. Second number

if fib_next() != 1:
    print("Case failed!")

# 3. 10th number

for i in range(7):
    fib_next()

if fib_next() != 34:
    print("Case failed!")


# %% Question3 - We wrote a closure that counts how many times a function was called. 
# Write a new one that can keep a track of how many times add/mul/div functions were called, 
# and update a global dictionary variable with the counts (+ 6 tests) - 250

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

count_dict = {}

def count(func):
    count = 0
    def inner(a,b):
        nonlocal count
        global count_dict
        print(f"{func(a,b)}")
        count += 1
        count_dict[func.__name__] = count
    return inner

add = count(add)
mul = count(mul)
div = count(div)

add(4,5)
add(4,5)
add(4,5)

mul(4,5)
mul(4,5)

div(4,5)

print(count_dict)

# %% Question4 - Modify above such that now we can pass in different dictionary variables 
# to update different dictionaries (+ 6 tests) - 250

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

dic_add = {}
dic_mul = {}
dic_div = {}

def count(func, dic):
    count = 0
    def inner(a,b):
        nonlocal count, dic
        print(f"{func(a,b)}")
        count += 1
        dic[func.__name__] = count
    return inner

add = count(add, dic_add)
mul = count(mul, dic_mul)
div = count(div, dic_div)

add(4,5)
add(4,5)
add(4,5)

mul(4,5)
mul(4,5)

div(4,5)

print(dic_add)
print(dic_mul)
print(dic_div)

