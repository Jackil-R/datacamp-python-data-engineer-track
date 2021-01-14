# Chapter 2 - Variables in Bash Scripting


## Basic variables in Bash

#### Instructions


## Using variables in Bash
You have just joined a data analytics team at a new company after someone left very quickly to pursue a new job (lucky them!). Unfortunately they left so fast they did not have time to finish the Bash script they were working on as part of a new chatbot project.

There is an error with this script - it is printing out the words yourname rather than the person's name. You know this has something to do with variable assignment - can you help fix this script? Add the necessary components to ensure this script runs correctly.
#### Instructions
- Create a variable, yourname that contains the name of the user. Let's use the test name 'Sam' for this.
- Fix the echo statement so it prints the variable and not the word yourname.
- Run your script.

## Shell within a shell
Which of the following correctly uses a 'shell within a shell' to print out the date? We do not want to select the option that will just print out the string 'date'.

You could try these in the console yourself!
#### Instructions
- echo "Right now it is "date""
- Answer: echo "Right now it is `date`"
- echo "Right now it is $date"



## Numeric variables in Bash

#### Instructions


## Converting Fahrenheit to Celsius
You work in the analytics department for an Australian company that recently purchased an American company. The files and data from the US company are in the imperial system and need to be converted to metric. This sounds like a great opportunity to use your Bash skills to create a program which will assist.

Your task is to write a program that takes in a single number (a temperature in Fahrenheit) as an ARGV argument, converts it to Celsius and returns the new value. There may be decimal places so you will need to undertake calculations using the bc program.

At all times use 2 decimal places using the scale command for bc.

The formula for Fahrenheit to Celsius is:
``````
C = (F - 32) x (5/9)
``````
Remember, since we are using arguments, you will need to run your script from the terminal pane rather than 'run this file' button.
#### Instructions
- Create a variable temp_f from the first ARGV argument.
- Call a shell-within-a-shell to subtract 32 from temp_f and assign to variable temp_f2.
- Using the same method, multiply temp_f2 by 5 and divide by 9, assigning to a new variable temp_c then print out temp_c.
- Save and run your script (in the terminal) using 108 Fahrenheit (the forecast temperature in Parramatta, Sydney this Saturday!).

## Extracting data from files
You are a data scientist for a climate research organization. To update some models, you need to extract temperature data for 3 regions you are monitoring. Unfortunately the temperature reading devices are quite old and can only be configured to dump data each day into a folder called /temps on your server. Each file contains the daily temperature for each region.

Your task is to extract the data from each file (by concatenating) into the relevant variable and print it out. The temperature in the file region_A needs to be assigned to the variable temp_a and so on.

You will later do some more advanced calculations on these variables.
#### Instructions
- Create three variables from the data in the three files within temps by concatenating the content into a variable using a shell-within-a-shell.
- Print out the variables to ensure it worked.
- Save your script and run from the command line.


## Arrays in Bash

#### Instructions


## Creating an array
In this exercise, you will practice building and accessing key properties of an array. Understanding what key properties are built in to Bash is important for fully utilizing arrays. For example, when iterating through arrays, knowing their length is very handy. Similarly, knowing how to easily return all array elements is also important for looping and also for checking your work and printing.

In this exercise, you will firstly build an array using two different methods and then access the length of the array. You will then return the entire array using a different special property.

#### Instructions
- Create a normal array called capital_cities which contains the cities Sydney, New York and Paris. Do not use the declare method; fill the array as you create it. Be sure to put double quotation marks around each element!
- Create a normal array called capital_cities. However, use the declare method to create in this exercise.
- Below, add each city, appending to the array. The cities were Sydney, New York, and Paris. Remember to use double quotation marks.
- Now you have the array created, print out the entire array using a special array property.
- Then print out the length of the array using another special property.



## Creating associative arrays
Associative arrays are powerful constructs to use in your Bash scripting. They are very similar to 'normal' arrays, however they have a few important differences in their creation, manipulation and key properties.

Associative arrays allow you to index using words rather than numbers, which can be important for ease of inputting and accessing properties. For example, rather than accessing 'index 4' of an array about a city's information, you can access the city_population property, which is a lot clearer!

In this exercise we will practice creating and adding to an associative array. We will then access some special properties that are unique to associative arrays. Let's get started!

NOTE if you trigger a hint, you may need to refresh the browser to remove old variables etc that affect the test suite
#### Instructions
- Create an empty associative array on one line called model_metrics. Do not add any elements to it here.
- Add the following key-value pairs; (model_accuracy, 98), (model_name, "knn"), (model_f1, 0.82).
- Create the same associative array (model_metrics) all in one line. (model_accuracy, 98), (model_name, "knn"), (model_f1, 0.82). Remember you must add square brackets* around the keys!
- Print out the array to see what you created.
- Now that you've created an associative array, print out just the keys of this associative array.


## Climate calculations in Bash

#### Instructions