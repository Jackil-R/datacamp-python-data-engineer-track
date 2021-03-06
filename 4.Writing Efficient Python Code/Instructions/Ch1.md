# Chapter 1 - Foundations for efficiencies

## Pop quiz: what is efficient®

#### Instructions


## A taste of things to come
A taste of things to come
In this exercise, you'll explore both the Non-Pythonic and Pythonic ways of looping over a list.

```
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
```
Suppose you wanted to collect the names in the above list that have six letters or more. In other programming languages, the typical approach is to create an index variable (i), use i to iterate over the list, and use an if statement to collect the names with six letters or more:

```
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
```
    
Let's explore some more Pythonic ways of doing this.
#### Instructions
- Print the list, new_list, that was created using a Non-Pythonic approach.
- A more Pythonic approach would loop over the contents of names, rather than using an index variable. Print better_list.
- The best Pythonic way of doing this is by using list comprehension. Print best_list.

## Zen of Python
Zen of Python
In the video, we covered the Zen of Python written by Tim Peters, which lists 19 idioms that serve as guiding principles for any Pythonista. Python has hundreds of Python Enhancement Proposals, commonly referred to as PEPs. The Zen of Python is one of these PEPs and is documented as PEP20.

One little Easter Egg in Python is the ability to print the Zen of Python using the command import this. Let's take a look at one of the idioms listed in these guiding principles.

Type and run the command import this within your IPython console and answer the following question:

What is the 7th idiom of the Zen of Python?

#### Instructions
What is the 7th idiom of the Zen of Python?

Answer: Readability counts

## Built-in practice: range()
Built-in practice: range()
In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

1) Create a sequence of numbers from 0 to a stop value (which is exclusive). This is useful when you want to create a simple sequence of numbers starting at zero:
```
range(stop)

# Example
list(range(11))


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
2) Create a sequence of numbers from a start value to a stop value (which is exclusive) with a step size. This is useful when you want to create a sequence of numbers that increments by some value other than one. For example, a list of even numbers:
```
range(start, stop, step)

# Example
list(range(2,11,2))

[2, 4, 6, 8, 10]
```
#### Instructions
Create a range object that starts at zero and ends at five. Only use a stop argument.
Convert the nums variable into a list called nums_list.
Create a new list called nums_list2 that starts at one, ends at eleven, and increments by two by unpacking a range object using the star character (*).

## Built-in practice: enumerate()
Built-in practice: enumerate()
In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. For example, suppose you had a list of people that arrived at a party you are hosting. The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):
```
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
```

If you wanted to attach an index representing a person's arrival order, you could use the following for loop:
```
indexed_names = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names.append(index_name)

[(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]
```
But, that's not the most efficient solution. Let's explore how to use enumerate() to make this more efficient.
#### Instructions
- Instead of using for i in range(len(names)), update the for loop to use i as the index variable and name as the iterator variable and use enumerate().
- Rewrite the previous for loop using enumerate() and list comprehension to create a new list, indexed_names_comp.
- Create another list (indexed_names_unpack) by using the star character (*) to unpack the enumerate object created from using enumerate() on names. This time, start the index for enumerate() at one instead of zero.

## Built-in practice: map()
- Built-in practice: map()
- In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. Let's look at a list of party guests:
```
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
```
Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. you could accomplish this with the below for loop:
```
names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
```
Let's explore using the map() function to do this more efficiently in one line of code.
#### Instructions
- Use map() and the method str.upper() to convert each name in the list names to uppercase. Save this to the variable names_map.
- Print the data type of names_map.
- Unpack the contents of names_map into a list called names_uppercase using the star character (*).
- Print names_uppercase and observe its contents.

## Practice with NumPy arrays
Practice with NumPy arrays
Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.

A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience. numpy has been imported into your session as np.
#### Instructions
- Print the second row of nums.
- Print the items of nums that are greater than six.
- Create nums_dbl that doubles each number in nums.
- Replace the third column in nums with a new column that adds 1 to each item in the original column.

## Bringing it all together: Festivus!
Bringing it all together: Festivus!
In this exercise, you will be throwing a party—a Festivus if you will!

You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party in 10-minute increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up 20 minutes into the party, and so on and so forth.

We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and let them know how many minutes late they are to your party. Note that numpy has been imported into your session as np and the names list has been loaded as well.

Let's welcome your guests!
#### Instructions
- Use range() to create a list of arrival times (10 through 50 incremented by 10). Create the list arrival_times by unpacking the range object.
- You realize your clock is three minutes fast. Convert the arrival_times list into a numpy array (called arrival_times_np) and use NumPy broadcasting to subtract three minutes from each arrival time.
- Use list comprehension with enumerate() to pair each guest in the names list to their updated arrival time in the new_times array. You'll need to use the index variable created from using enumerate() on new_times to index the names list.
- A function named welcome_guest() has been pre-loaded into your session. Use map() to apply this function to each element of the guest_arrivals list and save it as the variable welcome_map.
