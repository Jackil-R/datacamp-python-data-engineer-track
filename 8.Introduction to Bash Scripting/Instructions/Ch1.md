## Chapter 1 - From Command-Line to Bash Script


##Introduction and refresher

####Instruction

##Extracting scores with shell
There is a file in either the start_dir/first_dir, start_dir/second_dir or start_dir/third_dir directory called soccer_scores.csv. It has columns Year,Winner,Winner Goals for outcomes of a soccer league.

cd into the correct directory and use cat and grep to find who was the winner in 1959. You could also just ls from the top directory if you like!
####Instruction
- Winner
- Answer: Dunav ()
- Botev

##Searching a book with shell
There is a copy of Charles Dickens's infamous 'Tale of Two Cities' in your home directory called two_cities.txt.

Use command line arguments such as cat, grep and wc with the right flag to count the number of lines in the book that contain either the character 'Sydney Carton' or 'Charles Darnay'. Use exactly these spellings and capitalizations.
####Instruction
- Answer: 77
- 32
- 45

##Your first Bash script

####Instruction


##A simple Bash script
Let's start with a very basic example to practice turning command-line (shell) arguments into a Bash script. In the provided editor, the first line has already been written for you. Remember how that was called the 'hash-bang' or 'shebang'? For this environment bash is not located at /usr/bash but at /bin/bash. You can confirm this with the command which bash.

There is a file in your working directory called server_log_with_todays_date.txt. Your task is to write a simple Bash script that concatenates this out to the terminal so you can see what is inside.
####Instruction
- Create a single-line script that concatenates the mentioned file.
- Save your script and run from the console.


##Shell pipelines to Bash scripts
In this exercise, you are working as a sports analyst for a Bulgarian soccer league. You have received some data on the results of the grand final from 1932 in a csv file. The file is comma-delimited in the format Year,Winner,Winner Goals which lists the year of the match, the team that won and how many goals the winning team scored, such as 1932,Arda,4.

Your job is to create a Bash script from a shell piped command which will aggregate to see how many times each team has won.

Don't worry about the tail -n +2 part, this just ensures we don't aggregate the CSV headers!
####Instruction
- Create a single-line pipe to cat the file, cut out the relevant field and aggregate (sort & uniq -c will help!) based on winning team.
- Save your script and run from the console.

##Extract and edit using Bash scripts
Continuing your work for the Bulgarian soccer league - you need to do some editing on the data you have. Several teams have changed their names so you need to do some replacements. The data is the same as the previous exercise.

You will need to create a Bash script that makes use of sed to change the required team names.
####Instruction
- Create a pipe using sed twice to change the team Cherno to Cherno City first, and then Arda to Arda United.
- Pipe the output to a file called soccer_scores_edited.csv.
- Save your script and run from the console. Try opening soccer_scores_edited.csv using shell commands to confirm it worked (the first line should be changed)!


##Standard streams & arguments

####Instruction


##Using arguments in Bash scripts
Often you will find that your Bash scripts are part of an overall analytics pipeline or process, so it's very useful to be able to take in arguments (ARGV) from the command line and use these inside your scripts.

Your job is to create a Bash script that will return the arguments inputted as well as utilize some of the special properties of ARGV elements in Bash scripts.

Since we are using arguments, you must run your script from the terminal pane, not using the 'run this file' button.
####Instruction
- Echo the first and second ARGV arguments.
- Echo out the entire ARGV array in one command (not each element).
- Echo out the size of ARGV (how many arguments fed in).
- Save your script and run from the terminal pane using the arguments Bird Fish Rabbit. Don't use the ./script.sh method.
  

##Using arguments with HR data
In this exercise, you are working as a data scientist in the HR department of a large IT company. You need to extract salary figures for recent hires, however, the HR IT system simply spits out hundreds of files into the folder /hire_data.

Each file is comma-delimited in the format COUNTRY,CITY,JOBTITLE,SALARY such as Estonia,Tallinn,Javascript Developer,118286

Your job is to create a Bash script to extract the information needed. Depending on the task at hand, you may need to go back and extract data for a different city. Therefore, your script will need to take in a city (an argument) as a variable, filter all the files by this city and output to a new CSV with the city name. This file can then form part of your analytics work.
####Instruction
- Echo the first ARGV argument so you can confirm it is being read in.
- cat all the files in the directory /hire_data and pipe to grep to filter using the city name (your first ARGV argument).
- On the same line, pipe out the filtered data to a new CSV called cityname.csv where cityname is taken from the first ARGV argument.
- Save your script and run from the console twice (do not use the ./script.sh method). Once with the argument Seoul. Then once with the argument Tallinn.
