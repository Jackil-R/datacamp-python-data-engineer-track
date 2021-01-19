# Chapter 2 - Intermediate unit testing


## Mastering assert statements

#### Instructions

## Write an informative test failure message
The test result reports become a lot easier to read when you make good use of the optional message argument of the assert statement.

In a previous exercise, you wrote a test for the convert_to_int() function. The function takes an integer valued string with commas as thousand separators e.g. "2,081" as argument and should return the integer 2081.

In this exercise, you will rewrite the test called test_on_string_with_one_comma() so that it prints an informative message if the test fails.
#### Instructions
- Format the message string so that it shows the actual return value.
- Write the assert statement that checks if actual is equal to expected and prints the message message if they are not equal.


## Testing float return values
The get_data_as_numpy_array() function (which was called mystery_function() in one of the previous exercises) takes two arguments: the path to a clean data file and the number of data columns in the file . An example file has been printed out in the IPython console. It contains three rows.

The function converts the data into a 3x2 NumPy array with dtype=float64. The expected return value has been stored in a variable called expected. Print it out to see it.

The housing areas are in the first column and the housing prices are in the second column. This array will be the features that will be fed to the linear regression model for learning.

The return value contains floats. Therefore you have to be especially careful when writing unit tests for this function.
#### Instructions
- Complete the assert statement to check if get_data_as_numpy_array() returns expected, when called on example_clean_data_file.txt with num_columns set to 2.

## Testing with multiple assert statements
You're now going to test the function split_into_training_and_testing_sets() from the models module.

It takes a n x 2 NumPy array containing housing area and prices as argument. To see an example argument, print the variable example_argument in the IPython console.

The function returns a 2-tuple of NumPy arrays (training_set, testing_set). The training set contains int(0.75 * n) (approx. 75%) randomly selected rows of the argument array. The testing set contains the remaining rows.

Print the variable expected_return_value in the IPython console. example_argument had 6 rows. Therefore the training array has int(0.75 * 6) = 4 of its rows and the testing array has the remaining 2 rows.

numpy as np, pytest and split_into_training_and_testing_sets have been imported for you. 
#### Instructions
- Calculate the expected number of rows of the training array using the formula int(0.75*n), where n is the number of rows in example_argument, and assign the variable expected_training_array_num_rows to this number.
- Calculate the expected number of rows of the testing array using the formula n - int(0.75*n), where n is the number of rows in example_argument, and assign the variable expected_testing_array_num_rows to this number.
- Write an assert statement that checks if training array has expected_training_array_num_rows rows.
- Write an assert statement that checks if testing array has expected_testing_array_num_rows rows.

## Testing for exceptions instead of return values

#### Instructions


## Practice the context manager
In pytest, you can test whether a function raises an exception by using a context manager. Let's practice your understanding of this important context manager, the with statement and the as clause.

At any step, feel free to run the code by pressing the "Run Code" button and check if the output matches your expectations.
#### Instructions
- Complete the with statement by filling in with a context manager that will silence the ValueError raised in the context.
- Complete the with statement with a context manager that raises Failed if no OSError is raised in the context.
- Extend the with statement so that any raised ValueError is stored in the variable exc_info.
- Write an assert statement to check if the raised ValueError contains the message "Silence me!".

## Unit test a ValueError
Sometimes, you want a function to raise an exception when called on bad arguments. This prevents the function from returning nonsense results or hard-to-interpret exceptions. This is an important behavior which should be unit tested.

Remember the function split_into_training_and_testing_sets()? It takes a NumPy array containing housing area and prices as argument. The function randomly splits the array row wise into training and testing arrays in the ratio 3:1, and returns the resulting arrays in a tuple.

If the argument array has only 1 row, the testing array will be empty. To avoid this situation, you want the function to not return anything, but raise a ValueError with the message "Argument data_array must have at least 2 rows, it actually has just 1".
#### Instructions
- Fill in with the correct context manager that checks if split_into_training_and_testing_sets() raises a ValueError when called on test_argument, which is a NumPy array with a single row.
- Complete the with statement so that information about any raised ValueError will be stored in the variable exc_info.
- Write an assert statement to check if the raised ValueError contains the correct message stored in the variable expected_error_msg.
-


## The well tested function

#### Instructions


## Testing well: Boundary values
Remember row_to_list()? It takes a row containing housing area and prices e.g. "2,041\t123,781\n" and returns the data as a list e.g. ["2,041", "123,781"].

A row can be mapped to a 2-tuple (m, n), where m is the number of tab separators. n is 1 if the row has any missing values, and 0 otherwise.

For example,
``````
"123\t456\n"  -> (1, 0).

"\t456\n" -> (1, 1).

"\t456\t\n" -> (2, 1).
``````
The function only returns a list for arguments mapping to (1, 0). All other tuples correspond to invalid rows, with either more than one tab or missing values. The function returns None in all these cases. See the plot.

This mapping shows that the function has normal behavior at (1, 0), and special behavior everywhere else.
#### Instructions
- Which are the boundary values for this function, according to the plot? Answer: 
(0, 0), (2, 0) and (1, 1).
- Assign actual to the return value of row_to_list() on the argument "123\n", which is an instance of the boundary value (0, 0).
- Complete the assert statement to check if row_to_list() indeed returns None for the instance "123\t4,567\t89\n" of the boundary value (2, 0).
- In the test test_on_one_tab_with_missing_value(), format the failure message with the actual return value.

## Testing well: Values triggering special logic
Look at the plot. The boundary values of row_to_list() are now marked in orange. The normal argument is marked in green and the values triggering special behavior are marked in blue.

In the last exercise, you wrote tests for boundary values. In this exercise, you are going to write tests for values triggering special behavior, in particular, (0, 1) and (2, 1). These are values triggering special logic since the function returns None instead of a list.
#### Instructions
- Assign the variable actual to the actual return value for "\n".
- Complete the assert statement for test_on_no_tab_with_missing_value(), making sure to format the failure message appropriately.
- Assign the variable actual to the actual return value for "123\t\t89\n".
- Complete the assert statement for test_on_two_tabs_with_missing_value(), making sure to format the failure message appropriately.

## Testing well: Normal arguments
This time, you will test row_to_list() with normal arguments i.e. arguments mapping to the tuple (1, 0). The plot is provided to you for reference.

Remembering that the best practice is to test for two to three normal arguments, you will write two tests in this exercise.
#### Instructions
- How many normal arguments is it recommended to test? At least two or three.
- Assign the variable expected to the expected return value for the normal argument "123\t4,567\n".
- Complete the correct assert statement for test_on_normal_argument_2(), making sure to format the failure message appropriately.
- The tests for boundary values, values triggering special behavior and normal arguments have been written to a test module test_row_to_list.py. Run the tests in the IPython shell. Which bugs does the function have?
Answer: The function does not have any bugs.

## Test Driven Development (TDD)

#### Instructions


## TDD: Tests for normal arguments
In this and the following exercises, you will implement the function convert_to_int() using Test Driven Development (TDD). In TDD, you write the tests first and implement the function later.

Normal arguments for convert_to_int() are integer strings with comma as thousand separators. Since the best practice is to test a function for two to three normal arguments, here are three examples with no comma, one comma and two commas respectively.

Argument value	| Expected return value
------------- | -------------------
"756"	| 756
"2,081"	| 2081
"1,034,891"	|1034891

Since the convert_to_int() function does not exist yet, you won't be able to import it. But you will use it in the tests anyway. That's how TDD works.

pytest has already been imported for you.
#### Instructions
- Complete the assert statement for test_with_no_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_one_comma() by inserting the correct boolean expression.
- Complete the assert statement for test_with_two_commas() by inserting the correct boolean expression.

## TDD: Requirement collection
What should convert_to_int() do if the arguments are not normal? In particular, there are three special argument types:

Arguments that are missing a comma e.g. "178100,301".
Arguments that have the comma in the wrong place e.g. "12,72,891".
Float valued strings e.g. "23,816.92".
Also, should convert_to_int() raise an exception for specific argument values?

When your boss asked you to implement the function, she didn't say anything about these cases! But since you want to write tests for special and bad arguments as a part of TDD, you go and ask your boss.

She says that convert_to_int() should return None for every special argument and there are no bad arguments for this function.

pytest has been imported for you.
#### Instructions
- Give a name to the test by using the standard name prefix that pytest expects followed by on_string_with_missing_comma.
- Assign actual to the actual return value for the argument "12,72,891".
- Complete the assert statement.

## TDD: Implement the function
convert_to_int() returns None for the following:

1) Arguments with missing thousands comma e.g. "178100,301". If you split the string at the comma using "178100,301".split(","), then the resulting list ["178100", "301"] will have at least one entry with length greater than 3 e.g. "178100".

2) Arguments with incorrectly placed comma e.g. "12,72,891". If you split this at the comma, then the resulting list is ["12", "72", "891"]. Note that the first entry is allowed to have any length between 1 and 3. But if any other entry has a length other than 3, like "72", then there's an incorrectly placed comma.

3) Float valued strings e.g. "23,816.92". If you remove the commas and call int() on this string i.e. int("23816.92"), you will get a ValueError.
#### Instructions
- Complete the if statement that checks if the i-th element of comma_separated_parts has length greater than 3.
- 
- 
- 