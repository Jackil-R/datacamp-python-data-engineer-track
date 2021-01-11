#Chapter 4 - More on Decorators

import time
# Print the return type
def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
    # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))
        return result

    # Return the decorated function
    return wrapper

@print_return_type
def foo(value):
    return value

print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))
print("=========================================================")


# Counter
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func

    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
    print('calling foo()')

foo()
foo()
foo()
print('foo() was called {} times.'.format(foo.count))
print("=========================================================")


# Preserving docstrings when decorating functions
from functools import wraps
def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)

    return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)

print_sum(10, 20)
print(print_sum.__doc__)
print("=========================================================")


# Measuring decorator overhead
def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    #check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    #check_outputs(result)
    return result
  return wrapper

@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))
print("=========================================================")


# Run_n_times()
def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator
@run_n_times(10)
def print_sum(a, b):
    print(a + b)

print_sum(15, 20)

# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)
@run_five_times
def print_sum(a, b):
    print(a + b)

print_sum(4, 100)

# Modify the print() function to always run 20 times
# print = run_n_times(20)(print)

print('What is happening?!?!')
print("=========================================================")


# HTML Generator
def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator


# Make hello() return bolded text
@html("<b>", "</b>")
def hello(name):
    return 'Hello {}!'.format(name)
print(hello('Alice'))


# Make goodbye() return italicized text
@html("<i>", "</i>")
def goodbye(name):
    return 'Goodbye {}.'.format(name)
print(goodbye('Alice'))

# Wrap the result of hello_goodbye() in <div> and </div>
@html("<div>","</div>")
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))
print(hello_goodbye('Alice'))
print("=========================================================")


# Tag your functions
def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)
print("=========================================================")


# Check the return type
def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(value):
        result = value
        assert (type(result) == dict)
        return result
    return wrapper

@returns_dict
def foo(value):
    return value

try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')


def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(return_type):
            result = return_type
            assert (type(result) == type(return_type))
            return result
        return wrapper
    return decorator

@returns(list)
def foo(value):
    return value

try:
    print(foo([1, 2, 3]))
except AssertionError:
    print('foo() did not return a dict!')
print("=========================================================")

def multiply(multipler):
    def decorator(func):
        def wrapper(a):
            return multipler*a
        return wrapper
    return decorator

@multiply(4)
def foo(value):
    return value
print(foo(2))

print("=========================================================")

class Invalid_Arithmetic_Operation_Error(Exception):
   # Constructor method
   def __init__(self, value):
      self.value = value
   # __str__ display function
   def __str__(self):
      return(repr(self.value))

def create_math_function(sign):
    def decorator(func):
        def wrapper(int_a, int_b):
            if sign == '+':
                return int_a+int_b
            elif sign == '-':
                return int_a-int_b
            elif sign == '*':
                return int_a*int_b
            elif sign == '/':
                return int_a/int_b
            else:
                raise Invalid_Arithmetic_Operation_Error(sign)
        return wrapper
    return decorator

@create_math_function("*")
def multiply(a, b):
    pass

@create_math_function("+")
def add(a, b):
    pass

@create_math_function("-")
def subract(a, b):
    pass

@create_math_function("/")
def divide(a, b):
    pass

@create_math_function("§")
def std(a, b):
    pass

try:
    print(multiply(2,2))
    print(add(6, 6))
    print(subract(4, 2))
    print(divide(9, 3))
    print(std(1,1))
except Invalid_Arithmetic_Operation_Error as error:
   print('Invalid arithmetic operation',error.value)

print("=========================================================")