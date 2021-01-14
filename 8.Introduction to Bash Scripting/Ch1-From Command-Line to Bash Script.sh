# Chapter 1 - From Command-Line to Bash Script


#Introduction and refresher

print"========================================================="


#Extracting scores with shell===

cat start_dir/second_dir/soccer_scores.csv | grep 1959

print"========================================================="


#Searching a book with shell

cat two_cities.txt | grep -E 'Sydney Carton|Charles Darnay' | wc -l

cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay' | wc -l

print"========================================================="


#Your first Bash script===

print"========================================================="


#A simple Bash script
#!/bin/bash

cat soccer_scores

# Now save and run!
print"========================================================="


#Shell pipelines to Bash scripts
#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut -d , -f 2 | tail -n +2 | sort | uniq -c

# Now save and run!
print"========================================================="


#Extract and edit using Bash scripts
#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
print"========================================================="


#Standard streams & arguments===

print"========================================================="


#Using arguments in Bash scripts
#!/bin/bash

# Echo the first and second ARGV arguments
echo $1
echo $2

# Echo out the entire ARGV array
echo $@

# Echo out the size of ARGV
echo $#
print"========================================================="


#Using arguments with HR data
# Echo the first ARGV argument
echo $1

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "$1".csv

print"========================================================="