#Chapter 1 - Importing Data from Flat Files

#Get data from CSVs
# Import pandas as pd
import pandas as pd

# Read the CSV and assign it to the variable data
data = pd.read_csv('Datasets/vt_tax_data_2016.csv')

# View the first few lines of data
print(data.head())
print("=========================================================")


#Get data from other flat files
# Import pandas with the alias pd
import pandas as pd
import matplotlib as plt

# Load TSV using the sep keyword argument to set delimiter
# data = pd.read_csv('Datasets/vt_tax_data_2016.csv', sep="\t")

# Plot the total number of tax returns by income group
# counts = data.groupby("agi_stub").N1.sum()
# counts.plot.bar()
# plt.show()
print("=========================================================")

#Import a subset of columns
# Create list of columns to use
cols = ['zipcode','agi_stub','mars1','MARS2','NUMDEP']

# Create data frame from csv using only selected columns
data = pd.read_csv("Datasets/vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
print("=========================================================")


#Import a file in chunks
# Create data frame of next 500 rows with labeled columns
vt_data_first500 = pd.read_csv('Datasets/vt_tax_data_2016.csv', nrows=500)
vt_data_next500 = pd.read_csv('Datasets/vt_tax_data_2016.csv',
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  names = list(vt_data_first500.columns),
                       		  header = None)

# View the Vermont data frames to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())
print("=========================================================")


#Specify data types
# Load csv with no additional arguments
data = pd.read_csv("Datasets/vt_tax_data_2016.csv")

# Print the data types
print(data.dtypes)

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub' : 'category', 'zipcode' : str}

# Load csv using dtype to set correct data types
data = pd.read_csv("Datasets/vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())
print("=========================================================")


#Set custom NA values
# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument
data = pd.read_csv("Datasets/vt_tax_data_2016.csv",
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
print("=========================================================")


#Skip bad data
try:
    # Set warn_bad_lines to issue warnings about bad records
    data = pd.read_csv("Datasets/vt_tax_data_2016_corrupt.csv",
                       error_bad_lines=False,
                       warn_bad_lines=True)

    # View first 5 records
    print(data.head())

except pd.io.common.CParserError:
    print("Your data contained rows that could not be parsed.")
print("=========================================================")