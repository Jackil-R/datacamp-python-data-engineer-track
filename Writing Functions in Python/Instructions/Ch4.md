# Chapter 4 - More on Decorators


## Print the return type
You are debugging a package that you've been working on with your friends. Something weird is happening with the data being returned from one of your functions, but you're not even sure which function is causing the trouble. You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing, and it returns something different. For instance, if you expect a function to return a numpy array, but it returns a list, you can get unexpected behavior. To ensure this is not what is causing the trouble, you decide to write a decorator, print_return_type(), that will print out the type of the variable that gets returned from every call of any function it is decorating.
#### Instructions
- Create a nested function, wrapper(), that will become the new decorated function.
- Call the function being decorated.
- Return the new decorated function.


## Counter
Counter
You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.
#### Instructions
- Call the function being decorated and return the result.
- Return the new decorated function.
- Decorate foo() with the counter() decorator.

## Preserving docstrings when decorating functions
Your friend has come to you with a problem. They've written some nifty decorators and added them to the functions in the open-source library they've been working on. However, they were running some tests and discovered that all of the docstrings have mysteriously disappeared from their decorated functions. Show your friend how to preserve docstrings and other metadata when writing decorators
#### Instructions
- Decorate print_sum() with the add_hello() decorator to replicate the issue that your friend saw - that the docstring disappears.
- To show your friend that they are printing the wrapper() function's docstring, not the print_sum() docstring, add the following docstring to wrapper():
"""
Print 'hello' and then call the decorated function.
"""
- Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().
- Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.

## Measuring decorator overhead
Measuring decorator overhead
Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. However, you've noticed that when you use it to decorate your functions, it makes them run much slower. You need to convince your boss that the decorator is adding too much processing time to your function. To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. This is the decorator in question:
``````
def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper
``````
#### Instructions
- Call the original function instead of the decorated version by using an attribute of the function that the wraps() statement in your boss's decorator added to the decorated function.

## Run_n_times()
Run_n_times()
In the video exercise, I showed you an example of a decorator that takes an argument: run_n_times(). The code for that decorator is repeated below to remind you how it works. Practice different ways of applying the decorator to the function print_sum(). Then I'll show you a funny prank you can play on your co-workers.
``````
def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator
``````
#### Instructions
- Add the run_n_times() decorator to print_sum() using decorator syntax so that print_sum() runs 10 times.
- Use run_n_times() to create a decorator run_five_times() that will run any function five times.
- Here's the prank: use run_n_times() to modify the built-in print() function so that it always prints 20 times!

## HTML Generator
HTML Generator
You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, html(), that can take any pair of opening and closing tags.
``````
def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper
``````
``````
def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper
``````
#### Instructions
- Return the decorator and the decorated function from the correct places in the new html() decorator.
- Use the html() decorator to wrap the return value of hello() in <b> and </b> (the HTML tags that mean "bold").
- Use html() to wrap the return value of goodbye() in <i> and </i> (the HTML tags that mean "italics").
- Use html() to wrap hello_goodbye() in a DIV, which is done by adding <div> and </div> tags around a string.

## Tag your functions
Tag your functions
Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:

- Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.
- Labeling functions as "experimental" so that users know that the inputs and outputs might change in the future.
- Marking any functions that you plan to remove in a future version of the code.
- Etc.
#### Instructions
- Define a new decorator, named decorator(), to return.
- Ensure the decorated function keeps its metadata.
- Call the function being decorated and return the result.
- Return the new decorator.

## Check the return type
Check the return type
Python's flexibility around data types is usually cited as one of the benefits of the language. It can occasionally cause problems though if incorrect data types go unnoticed. You've decided that in order to make sure your code is doing exactly what you want it to do, you will explicitly check the return types of all of your functions and make sure they are what you expect them to be. To do that, you are going to create a decorator that checks that the return type of the decorated function is correct.

Note: assert(condition) is a function that you can use to test whether something is true. If condition is True, this function doesn't do anything. If condition is False, this function raises an error. The type of error that it raises is called an AssertionError.
#### Instructions
- Start by completing the returns_dict() decorator so that it raises an AssertionError if the return type of the decorated function is not a dictionary.
- 