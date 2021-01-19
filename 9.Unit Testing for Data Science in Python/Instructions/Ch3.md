# Chapter 3 - Test Organization and Execution


## How to organize a growing set of tests?

#### Instructions


## Place test modules at the correct location
A data science project without visualization is like pizza without cheese, right? But this has been fixed by creating a package called visualization under the top level application directory src.
``````
src/                                    # All application code lives here
|-- visualization/                      # Package for visualization
    |-- __init__.py
    |-- plots.py                        # Module for plotting
In the package, there is a Python module plots.py, which contain functions related to plotting. These functions should be tested in a test module test_plots.py.
``````
According to pytest guidelines, where should you place this test module within the project structure?
#### Instructions
- src/visualization/test_plots.py.
- src/visualization/tests/test_plots.py.
- tests/test_plots.py.
- Answer: tests/visualization/test_plots.py.


## Create a test class
Test classes are containers inside test modules. They help separate tests for different functions within the test module, and serve as a structuring tool in the pytest framework.

Test classes are written in CamelCase e.g. TestMyFunction as opposed to tests, which are written using underscores e.g. test_something().

You met the function split_into_training_and_testing_sets() in Chapter 2, and wrote some tests for it. One of these tests was called test_on_one_row() and it checked if the function raises a ValueError when passed a NumPy array with only one row.

In this exercise you are going to create a test class for this function. This test class will hold the test test_on_one_row().
#### Instructions
- Declare the test class for the function split_into_training_and_testing_sets(), making sure to give it a name that follows the standard naming convention.
- Fill in the mandatory argument in the test test_on_one_row().


## Mastering test execution

#### Instructions


## One command to run them all
One of your colleagues pushed some changes to the functions row_to_list(), convert_to_int(), get_data_as_numpy_array() and split_into_training_and_testing_sets(). That means that you have to run all the tests again to figure out if something got broken as a result.

The current working directory in the IPython console is the tests directory, which contains all the tests in the same layout as described in the video. You can, at any time, run the tests in the IPython console using the appropriate command.
#### Instructions
- In the IPython console, what is the correct command for running all tests contained in the tests folder? => !pytest
- When you run all tests with the command !pytest, how many of them pass and how may fail? => Passing: 15, Failing: 1
- Assuming that you simply want to answer the binary question "Are all tests passing" without wasting time and resources, what is the correct command to run all tests till the first failure is encountered? =>  !pytest -x
- When you ran the tests using the !pytest -x command, how many tests ran in total before test execution stopped because of the first failing test? => 15

## Running test classes
When you ran the !pytest command in the last exercise, the test test_on_six_rows() failed. This is a test for the function split_into_training_and_testing_sets(). This means that this function is broken.

Short recap in case you forgot: this function takes a NumPy array containing housing area and prices as argument. The function randomly splits the argument array into training and testing arrays in the ratio 3:1, and returns the resulting arrays in a tuple.

A quick look revealed that during the code update, someone inadvertently changed the split from 3:1 to 9:1. This has to be changed back and the unit tests for the function, which now lives in the test class TestSplitIntoTrainingAndTestingSets, needs to be run again. Are you up to the challenge?
#### Instructions
- Fill in with a float between 0 and 1 so that num_training is approximately 3/4 of the number of rows in data_array.
- Now let's see if that modification fixed the broken function. The current working directory in the IPython console is the tests folder that contains all tests. The test class TestSplitIntoTrainingAndTestingSets resides in the test module tests/models/test_train.py. What is the correct command to run all the tests in this test class using node IDs? => !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets
- What is the correct command to run only the previously failing test test_on_six_rows() using node IDs? => !pytest models/test_train.py::TestSplitIntoTrainingAndTestingSets::test_on_six_rows
- What is the correct command to run the tests in TestSplitIntoTrainingAndTestingSets using keyword expressions? => !pytest -k "SplitInto"


## Expected failures and conditional skipping

#### Instructions


## Mark a test class as expected to fail
A new function model_test() is being developed and it returns the accuracy of a given linear regression model on a testing dataset. Test Driven Development (TDD) is being used to implement it. The procedure is: write tests first and then implement the function.

A test class TestModelTest has been created within the test module models/test_train.py. In the test class, there are two unit tests called test_on_linear_data() and test_on_one_dimensional_array(). But the function model_test() has not been implemented yet.

Throughout this exercise, pytest and numpy as np will be imported for you.
#### Instructions
- Run the tests in the test class TestModelTest in the IPython console. What is the outcome?
Answer: The tests fail with NameError since the function model_test() has not yet been defined.
- Mark the whole test class TestModelTest as "expected to fail".
- Add the following reason for the expected failure: "Using TDD, model_test() has not yet been implemented".

## Mark a test as conditionally skipped
In Python 2, there was a built-in function called xrange(). In Python 3, xrange() was removed. Therefore, if any test uses xrange(), it's going to fail with a NameError in Python 3.

Remember the function get_data_as_numpy_array()? You saw it in Chapter 2. It converted data in a preprocessed data file into a NumPy array.

range() has been deliberately replaced with the obsolete xrange() in the function. Evil laughter! But no worries, it will be changed back after you're done with this exercise.

You wrote a test called test_on_clean_file() for this function. This test currently resides in a test class TestGetDataAsNumpyArray inside the test module features/test_as_numpy.py.

pytest, numpy as np and get_data_as_numpy_array() has been imported for you.
#### Instructions
- Run the tests in the test class TestGetDataAsNumpyArray in the IPython console. What is the outcome? => The test test_on_clean_file() fails with a NameError because Python 3 does not recognize the xrange() function.
- Import the sys module.
- Mark the test test_on_clean_file() as skipped if the Python version is greater than 2.7.
- Add the following reason for skipping the test: "Works only on Python 2.7 or lower".


## Reasoning in the test result report
In the last exercises, you marked the test class TestModelTest in the test module models/test_train.py as expected to fail. You also marked the test test_on_clean_file() in the test class TestGetDataAsNumpyArray belonging to the test module features/test_as_numpy.py as skipped if the Python version is greater than 2.7.

In both cases, you provided a reason argument which detailed why they are expected to fail or skipped. In this exercise, your job is to make this reason show up in the test result report when you run all tests in the IPython console.

Feel free to run the !pytest command with different options and flags in the IPython console while doing the exercise.
#### Instructions
- What is the command that would only show the reason for expected failures in the test result report? Answer: !pytest -rx
- What is the command that would only show the reason for skipped tests in the test result report? Answer: !pytest -rs
- What is the command that would show the reason for both skipped tests and tests that are expected to fail in the test result report? Answer: !pytest -rsx


## Continuous integration and code coverage

#### Instructions


## Build failing

#### Instructions


## What does code coverage mean?

#### Instructions
