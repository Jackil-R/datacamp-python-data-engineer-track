# Chapter 3 - Control Statements in Bash Scripting


## IF statements

#### Instructions


## Sorting model results
Sorting model results
You are working as a data scientist in a large corporation. The production environment for your machine learning models writes out text files into the model_results/ folder whenever an experiment is completed. The files have the following structure (example):
``````
Model Name: KNN
Accuracy: 89
F1: 0.87
Date: 2019-12-01
ModelID: 34598utjfddfgdg
``````
You can see the model name, accuracy and F1 scores, the date the experiment completed and a unique ID to link the model experiment back into your experiment system.

The company has a threshold of 90% for accuracy for a model to continue experimentation. Your task is to write a Bash script that takes in an ARGV argument (a filename), extracts the accuracy score and conditionally sorts the model result file into one of two folders: good_models/ for those with accuracy greater than or equal to 90 and bad_models/ for those less than 90. You must run your script from the terminal with the requested arguments before submitting your answer.

NOTE!! If you don't run the script with an argument, it will hang - so make sure to run the script with the requested argument! If you make an error requiring a hint - you may need to refresh the session before submitting as well!
#### Instructions
- Create a variable, accuracy by extracting the "Accuracy" line (and "Accuracy" value) in the first ARGV element (a file).
- Create an IF statement to move the file into good_models/ folder if it is greater than or equal to 90 using a flag, not a mathematical sign.
- Create an IF statement to move the file into bad_models/ folder if it is less than 90 using a flag, not a mathematical sign.
- Run your script from the terminal pane twice (using bash script.sh). Once with model_results/model_1.txt, then once with model_results/model_2.txt as the only argument.

## Moving relevant files
You have recently joined a new startup as one of the few technical employees. Your manager has asked if you can assist to clean up some of the folders on the server. The company has been through a variety of server monitoring software and so there are many files that should be deleted.

Luckily you know that all the files to keep contain both vpt and SRVM_ inside the file somewhere.

Your task is to write a Bash script that will take in file names as ARGV elements and move the file to good_logs/ if it matches both conditions above. Remember from the lecture, the q flag is for 'quiet' so it doesn't return the matched lines like grep normally does. It just returns true if any lines match.

Remember that when you use command-line arguments like grep in IF statements, there is no need for square brackets so don't add them! You must also remember to run your script using each file as an ARGV element. One each time; a total of four times to run your script.
#### Instructions
- Create a variable sfile out of the first ARGV element.
- Use an IF statement and grep to check if the sfile variable contains SRVM_ AND vpt inside.
- Inside the IF statement, move matching files to the good_logs/ directory.
- Try your script on all of the files in the directory (that is, run it four times - once for each file). It should move only one of them.


## FOR loops & WHILE statements

#### Instructions


## A simple FOR loop
You are working as a data scientist in an organization. Due to a recent merge of departments, you have inherited a folder with many files inside. You know that the .R scripts may be useful for your work but you aren't sure what they contain.

Write a simple Bash script to loop through all the files in the directory inherited_folder/ that end in .R and print out their names so you can get a quick look at what sort of scripts you have. Hopefully the file names are useful!
#### Instructions
- Use a FOR statement to loop through files that end in .R in inherited_folder/ using a glob expansion.
- echo out each file name into the console.

## Correcting a WHILE statement
There is a script placed in this directory which has a mistake in it. It is some code to modify some employee files, but only for the first 1000 employees. Do not attempt to run the script as the necessary files are not in this directory.

Using your knowledge of WHILE scripts, can you determine where the mistake is? What will happen if it runs?

You can find the code by using cat emp_script.sh to print it to the console.
#### Instructions
- There is no mistake, this script will run just fine.
- Answer: It will run forever because emp_num isn't incremented inside the loop.
- You cannot cat a .txt file so this will fail.

## Cleaning up a directory
Continuing your work as a data scientist in a large organization, you were told today that a colleague has left for their dream job (lucky them!). Unfortunately, when their logins were terminated, all their files were dumped into a single folder.

The good news is that most of their useful code has been backed up. However, all their python files using the Random Forest algorithm are buried in the file dump.

The task has fallen to you to sift through the hundreds of files to determine if they are both Python files and contain a Random Forest model. This sounds like a perfect opportunity to use your Bash skills, rather than checking every single file manually.

Write a script that loops through each file in the robs_files/ directory to see if it is a Python file (ends in .py) AND contains RandomForestClassifier. If so, move it into the to_keep/ directory.
#### Instructions
- Use a FOR statement to loop through (using glob expansion) files that end in .py in robs_files/.
- Use an IF statement and grep (remember the 'quiet' flag?) to check if RandomForestClassifier is in the file. Don't use a shell-within-a-shell here.
- Move the Python files that contain RandomForestClassifier into the to_keep/ directory.


## CASE statements

#### Instructions


## Days of the week with CASE
In your role as a Data Scientist, it is sometimes useful to associate dates with a 'working day' (Monday, Tuesday, Wednesday, Thursday, Friday) or a 'weekend' (Saturday & Sunday).

Your task is to build a small Bash script that will be useful to call in many areas of your data pipeline. It must take in a single argument (string of a day) into ARGV and use a CASE statement to print out whether the argument was a weekday or a weekend. You only need to account for the capitalized case for now.

You also don't need to worry about words or letters before and after. Just use exact matching for this example.

Remember the basic structure of a case statement is:
``````
case MATCHVAR in
  PATTERN1)
  COMMAND1;;
  PATTERN2)
  COMMAND2;;
  *)
  DEFAULT COMMAND;;
esac
``````
#### Instructions
- Build a CASE statement that matches on the first ARGV element.
- Create a match on each weekday such as Monday, Tuesday etc. using OR syntax on a single line, then a match on each weekend day (Saturday and Sunday) etc. using OR syntax on a single line.
- Create a default match that prints out Not a day! if none of the above patterns are matched.
- Save your script and run in the terminal window with Wednesday and Saturday to test.

## Moving model results with CASE
You are working as a data scientist in charge of analyzing some machine learning model results. The production environment moves files into a folder called model_out/ and names them model_RXX.csv where XX is a random number related to which experiment was run.

Each file has the following structure (example):
``````
Model Name, Accuracy, CV, Model Duration (s)
Logistic,42,4,48
``````
Your manager has told you that recent work in the organization has meant that tree-based models are to be kept in one folder and everything else deleted.

Your task is to use a CASE statement to move the tree-based models (Random Forest, GBM, and XGBoost) to the tree_models/ folder, and delete all other models (KNN and Logistic).
#### Instructions
- Use a FOR statement to loop through (using glob expansion) files in model_out/.
- Use a CASE statement to match on the contents of the file (we will use cat and shell-within-a-shell to get the contents to match against). It must check if the text contains a tree-based model name and move to tree_models/, otherwise delete the file.
- Create a default match that prints out Unknown model in FILE where FILE is the filename then run your script.

## Finishing a CASE statement
What is the correct way to finish a CASE statement?
#### Instructions
- Answer: esac
- fi
- done

