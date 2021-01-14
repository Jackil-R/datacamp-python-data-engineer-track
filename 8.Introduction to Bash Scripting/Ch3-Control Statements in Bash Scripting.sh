#Chapter 3 - Control Statements in Bash Scripting


#IF statements

print"========================================================="


#Sorting model results
# Extract Accuracy from first ARGV element
accuracy=$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -gt 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi
print"========================================================="


#Moving relevant files
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on sfile's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi
print"========================================================="


#FOR loops & WHILE statements

print"========================================================="


#A simple FOR loop
# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do
    # Echo out each file
    echo $file
done

print"========================================================="


#Correcting a WHILE statement

print"========================================================="


#Cleaning up a directory
# Create a FOR statement on files in directory
for file in robs_files/*.py
do
    # Create IF statement using grep
    if grep -q 'RandomForestClassifier' $file ; then
        # Move wanted files to to_keep/ folder
        mv $file to_keep/
    fi
done

print"========================================================="


#CASE statements

print"========================================================="


#Days of the week with CASE
# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday|Tuesday|Wednesday|Thursday|Friday)
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  *)
  echo "Not a day!";;
esac
print"========================================================="


#Moving model results with CASE
# Use a FOR loop for each file in 'model_out/'
for file in model_out/*
do
    # Create a CASE statement for each file's contents
    case $(cat $file) in
      # Match on tree and non-tree models
      *"Random Forest"*|*GBM*|*XGBoost*)
      mv $file tree_models/ ;;
      *KNN*|*Logistic*)
      rm $file ;;
      # Create a default
      *)
      echo "Unknown model in $file" ;;
    esac
done
print"========================================================="


#Finishing a CASE statement

print"========================================================="