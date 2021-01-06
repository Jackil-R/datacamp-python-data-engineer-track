## Chapter 1 - Best Practices


## Crafting a docstring
You've decided to write the world's greatest open-source natural language processing Python package. It will revolutionize working with free-form text, the way numpy did for arrays, pandas did for tabular data, and scikit-learn did for machine learning.

The first function you write is count_letter(). It takes a string and a single letter and returns the number of times the letter appears in the string. You want the users of your open-source package to be able to understand how this function works easily, so you will need to give it a docstring. Build up a Google Style docstring for this function by following these steps.
#### Instructions
- Copy the following string and add it as the docstring for the function: Count the number of times `letter` appears in `content`.
- Now add the arguments section, using the Google style for docstrings. Use str to indicate a string.
- Add a returns section that informs the user the return value is an int.
- Finally, add some information about the ValueError that gets raised when the arguments aren't correct.

## Retrieving docstrings

You and a group of friends are working on building an amazing new Python IDE (integrated development environment -- like PyCharm, Spyder, Eclipse, Visual Studio, etc.). The team wants to add a feature that displays a tooltip with a function's docstring whenever the user starts typing the function name. That way, the user doesn't have to go elsewhere to look up the documentation for the function they are trying to use. You've been asked to complete the build_tooltip() function that retrieves a docstring from an arbitrary function.

Note that in Python, you can pass a function as an argument to another function. I'll talk more about this in chapter 3, but it will be useful to keep in mind for this exercise.
#### Instructions
- Begin by getting the docstring for the function count_letter(). Use an attribute of the count_letter() function.
- Now use a function from the inspect module to get a better-formatted version of count_letter()'s docstring.
- Use the inspect module again to get the docstring for any function being passed to the build_tooltip() function.

## Docstrings to the rescue!
Some maniac has corrupted your installation of numpy! All of the functions still exist, but they've been given random names. You desperately need to call the numpy.histogram() function and you don't have time to reinstall the package. Fortunately for you, the maniac didn't think to alter the docstrings, and you know how to access them. numpy has a lot of functions in it, so we've narrowed it down to four possible functions that could be numpy.histogram() in disguise: numpy.leyud(), numpy.uqka(), numpy.fywdkxa() or numpy.jinzyxq().

Examine each of these functions' docstrings in the IPython shell to determine which of them is actually numpy.histogram().
#### Instructions


## Extract a function
 Extract a function
While you were developing a model to predict the likelihood of a student graduating from college, you wrote this bit of code to get the z-scores of students' yearly GPAs. Now you're ready to turn it into a production-quality system, so you need to do something about the repetition. Writing a function to calculate the z-scores would improve this code.
``````
# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()
``````
Note: df is a pandas DataFrame where each row is a student with 4 columns of yearly student GPAs: y1_gpa, y2_gpa, y3_gpa, y4_gpa
#### Instructions
- Finish the function so that it returns the z-scores of a column.
- Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.) from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.).

## Split up a function
Split up a function
Another engineer on your team has written this function to calculate the mean and median of a list. You want to show them how to split it into two simpler functions: mean() and median()
``````
def mean_and_median(values):
  """Get the mean and median of a list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median
``````
#### Instructions
- Write the mean() function.
- Write the median() function.

## Mutable or immutable?
Mutable or immutable?
The following function adds a mapping between a string and the lowercase version of that string to a dictionary. What do you expect the values of d and s to be after the function is called?
#### Instructions


## Best practice for default arguments
Best practice for default arguments
One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a panda's DataFrame. Unfortunately, they used a mutable variable as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.
``````
def add_column(values, df=pandas.DataFrame()):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df
``````
#### Instructions
- Change the default value of df to an immutable value to follow best practices.
- Update the code of the function so that a new DataFrame is created if the caller didn't pass one.