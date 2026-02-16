# Functions
   #=> group related code together so that its reusable


x= 45
y=55
print(f"This is my addition results,{x+y}")
print(f"This is my subtraction results, {x-y}")


#define a fucntion
#1 . In python, functions are first class objects
   # => You can assign them to variables
   # => pass the as arguments
   # => return them from other functions
   # => store them in data structure

# 2. functions can take default parameter
# 3. they are called from other parts of the program


def add(a,b): # function signatur, keyword 'def' and the function_name
    """
     Docstring for add
     parameter are variables in the function defintion

     :parameter a : Description
     :parameter b : Description

     """
    #  return a+b
    

# print(add(4,5))

# 4 & 5 are the arguments, values you pass

# All types of parameters
# 1. positional

def subtraction(x,y):
    return x-y

# print(subtraction(9,0))


# 2. keyword / default parameter

def power_of_eight(x,y=8):
    return x ** y

# the position parameter need to come before the keyword parameter
#dont't pass mutable paramters

def fib(n, memo=[]):
    memo.append(n)
    return memo

def fib_fic(n, meme=None):
    if memo is None:
        memo= []
    memo.append(n)
    return memo

# print(power_of_eight(4))


# 3 *args => variable positional arguments
# here is where a function will utilize a tuples


def function_name(one):
    print(one)

print(function_name(9))


# 4. **kwarg => variable keyword arguments
# the function will utilize a dictionary

def f(**kwargs):
    print(kwargs)

print(f(name= 'koin', age= 'infinity', occupation = "just there", isAdmin = True))


# anon function in python
# a function with no name 
# keyword is lamda

print((lambda i : i ** 9)(5))

power_of_seven = lambda i : i ** 7
print(power_of_seven(9))


numbers= [(91,89),(45,23),(67,44)]


numbers.sort(key=lambda X : X[1])

print(numbers)