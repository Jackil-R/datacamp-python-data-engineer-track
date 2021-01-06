#Chapter 3 - Decorators
import random

import pandas as pd
import numpy as np
#Building a command line data app
def load_data():
    return pd.read_csv("Datasets/input3-1.csv")
def mean(df):
    return np.mean(df)
def std(df):
    return np.str(df)
def maximum(df):
    return np.max(df)
def minimum(df):
    return np.min(df)
# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = 'mean'

# Call the chosen function and pass "data" as an argument
print(function_map[func_name](data))
print("=========================================================")


#Reviewing your co-worker's code
def has_docstring(func):
  """Check to see if the function
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None
def load_and_plot_data():
    """load_and_plot_data
    hello!
    :return:
    """
def as_2D():
    """as_2D
    hello!
    :return:
    """
    return 0
def log_product():
    return 0

# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")
print("=========================================================")


#Returning functions for a math game
def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b
        return subtract
    else:
        print("I don't know that one")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
print("=========================================================")


#Understanding scope

print("=========================================================")


#Modifying variables outside local scope
call_count = 0

def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(
        call_count
    ))

for _ in range(20):
    my_function()


def read_files():
    file_contents = None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents = []
        with open(filename) as fin:
            file_contents.append(fin.read())

    for filename in ['Datasets/1984.txt', 'Datasets/MobyDick.txt', 'Datasets/CatsEye.txt']:
        save_contents(filename)

    return file_contents

print('\n'.join(read_files()))


def wait_until_done():
    def check_is_done():
        # Add a keyword so that wait_until_done()
        # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()


done = False
wait_until_done()

print('Work done? {}'.format(done))
print("=========================================================")


#Checking for closure
def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))

    return new_func


my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(my_func.__closure__[0].cell_contents)
print(my_func.__closure__[1].cell_contents)
# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)
# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])
print("=========================================================")


#Closures keep your values safe
def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
        func()

    return call_func

new_func = get_new_func(my_special_function)

# # Redefine my_special_function() to just print "hello"
# def my_special_function():
#     print('hello')
#
# # Delete my_special_function()
# del my_special_function
# new_func()

# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)
my_special_function()
print("=========================================================")



#Using decorator syntax
def print_args(func):
    def wrapper(a,b,c):
        return func(a,b,c)
    return wrapper

def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)
my_function(1, 2, 3)

def print_args1(func):
    def wrapper(a,b,c):
        return func(a+1,b+1,c+1)
    return wrapper

@print_args1
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)
print("=========================================================")


#Defining a decorator
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)
print("=========================================================")