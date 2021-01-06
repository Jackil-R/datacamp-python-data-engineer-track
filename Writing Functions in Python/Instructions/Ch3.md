# Chapter 3 - Decorators


## Building a command line data app
You are building a command line tool that lets a user interactively explore a data set. We've defined four functions: mean(), std(), minimum(), and maximum() that users can call to analyze their data. Help finish this section of the code so that your users can call any of these functions by typing the function name at the input prompt.

Note: The function get_user_input() in this exercise is a mock version of asking the user to enter a command. It randomly returns one of the four function names. In real life, you would ask for input and wait until the user entered a value.
#### Instructions
- Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
- The name of the function the user wants to call is stored in func_name. Use the dictionary of functions, function_map, to call the chosen function and pass data as an argument.

## Reviewing your co-worker's code
Reviewing your co-worker's code
Your co-worker is asking you to review some code that they've written and give them some tips on how to get it ready for production. You know that having a docstring is considered best practice for maintainable, reusable functions, so as a sanity check you decide to run this has_docstring() function on all of their functions.
``````
def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None
``````
#### Instructions
- Call has_docstring() on your co-worker's load_and_plot_data() function.
- Check if the function as_2D() has a docstring.
- Check if the function log_product() has a docstring.

## Returning functions for a math game
You are building an educational math game where the player enters a math term, and your program returns a function that matches that term. For instance, if the user types "add", your program returns a function that adds two numbers. So far you've only implemented the "add" function. Now you want to include a "subtract" function.
#### Instructions
- Define the subtract() function. It should take two arguments and return the first argument minus the second argument.

## Understanding scope


## Modifying variables outside local scope
Sometimes your functions will need to modify a variable that is outside of the local scope of that function. While it's generally not best practice to do so, it's still good to know-how in case you need to do it. Update these functions so they can modify variables that would usually be outside of their scope.
#### Instructions
- Add a keyword that lets us update call_count from inside the function.
- Add a keyword that lets us modify file_contents from inside save_contents().
- Add a keyword to done in check_is_done() so that wait_until_done() eventually stops looping.

## Checking for closure
You're teaching your niece how to program in Python, and she is working on returning nested functions. She thinks she has written the code correctly, but she is worried that the returned function won't have the necessary information when called. Show her that all of the nonlocal variables she needs are in the new function's closure.
#### Instructions
- Use an attribute of the my_func() function to show that it has a closure that is not None.
- Show that there are two variables in the closure.
- Get the values of the variables in the closure so you can show that they are equal to [2, 17], the arguments passed to return_a_func().



## Closures keep your values safe
You are still helping your niece understand closures. You have written the function get_new_func() that returns a nested function. The nested function call_func() calls whatever function was passed to get_new_func(). You've also written my_special_function() which simply prints a message that states that you are executing my_special_function().

You want to show your niece that no matter what you do to my_special_function() after passing it to get_new_func(), the new function still mimics the behavior of the original my_special_function() because it is in the new function's closure.
#### Instructions
- Show that you still get the original message even if you redefine my_special_function() to only print "hello".
- Show that even if you delete my_special_function(), you can still call new_func() without any problems.
- Show that you still get the original message even if you overwrite my_special_function() with the new function.

## Decorators

## Using decorator syntax
You have written a decorator called print_args that prints out all of the arguments and their values any time a function that it is decorating gets called.
#### Instructions
- Decorate my_function() with the print_args() decorator by redefining my_function().
- Decorate my_function() with the print_args() decorator using decorator syntax.

## Defining a decorator
Your buddy has been working on a decorator that prints a "before" message before the decorated function is called and prints an "after" message after the decorated function is called. They are having trouble remembering how wrapping the decorated function is supposed to work. Help them out by finishing their print_before_and_after() decorator.
#### Instructions
- Call the function being decorated and pass it the positional arguments *args.
- Return the new decorated function.