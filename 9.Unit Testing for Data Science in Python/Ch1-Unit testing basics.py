#Chapter 1 - Unit testing basics
import pytest

#Why unit test?

print("=========================================================")


#How frequently is a function tested?

print("=========================================================")


#Manual testing

print("=========================================================")


#Write a simple unit test using pytest

print("=========================================================")


#Your first unit test using pytest
# Import the pytest package
import pytest

# Import the function convert_to_int()
#from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
  # Complete the assert statement
  assert convert_to_int("2,081") == 2081
print("=========================================================")


#Running unit tests

print("=========================================================")


#Understanding test result report

print("=========================================================")


#What causes a unit test to fail?

print("=========================================================")


#Spotting and fixing bugs
def convert_to_int(string_with_comma):
    # Fix this line so that it returns an int, not a str
    return int(string_with_comma.replace(",", ""))
print("=========================================================")


#More benefits and test types

print("=========================================================")


#Benefits of unit testing

print("=========================================================")


#Unit tests as documentation

print("=========================================================")
