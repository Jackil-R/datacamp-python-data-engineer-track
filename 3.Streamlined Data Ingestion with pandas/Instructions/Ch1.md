# Chapter 1 - Importing Data from Flat Files

## Get data from CSVs
In this exercise, you'll create a data frame from a CSV file. The United States makes available CSV files containing tax data by ZIP or postal code, allowing us to analyze income information in different parts of the country. We'll focus on a subset of the data, vt_tax_data_2016.csv, which has select tax statistics by ZIP code in Vermont in 2016.

To load the data, you'll need to import the pandas library, then read vt_tax_data_2016.csv and assign the resulting data frame to a variable. Then we'll have a look at the data.
#### Instructions
- Import the pandas library as pd.
- Use read_csv() to load vt_tax_data_2016.csv and assign it to the variable data.
- View the first few lines of the data frame with the head() method. This code has been written for you.

## Get data from other flat files
Get data from other flat files
While CSVs are the most common kind of flat file, you will sometimes find files that use different delimiters. read_csv() can load all of these with the help of the sep keyword argument. By default, pandas assumes that the separator is a comma, which is why we do not need to specify sep for CSVs.

The version of Vermont tax data here is a tab-separated values file (TSV), so you will need to use sep to pass in the correct delimiter when reading the file. Remember that tabs are represented as \t. Once the file has been loaded, the remaining code groups the N1 field, which contains income range categories, to create a chart of tax returns by income category.
#### Instructions
- Import pandas with the alias pd.
- Load vt_tax_data_2016.tsv, making sure to set the correct delimiter with the sep keyword argument.

## Import a subset of columns
The Vermont tax data contains 147 columns describing household composition, income sources, and taxes paid by ZIP code and income group. Most analyses don't need all these columns. In this exercise, you will create a data frame with fewer variables using read_csv()s usecols argument.

Let's focus on household composition to see if there are differences by geography and income level. To do this, we'll need columns on income group, ZIP code, tax return filing status (e.g., single or married), and dependents. The data uses codes for variable names, so the specific columns needed are in the instructions.

pandas has already been imported as pd.
#### Instructions
- Create a list of columns to use: zipcode, agi_stub (income group), mars1 (number of single households), MARS2 (number of households filing as married), and NUMDEP (number of dependents).
- Create a data frame from vt_tax_data_2016.csv that uses only the selected columns.

## Import a file in chunks
When working with large files, it can be easier to load and process the data in pieces. Let's practice this workflow on the Vermont tax data.

The first 500 rows have been loaded as vt_data_first500. You'll get the next 500 rows. To do this, you'll employ several keyword arguments: nrows and skiprows to get the correct records, header to tell pandas the data does not have column names, and names to supply the missing column names. You'll also want to use the list() function to get column names from vt_data_first500 to reuse.

pandas has been imported as pd.
#### Instructions
- Use nrows and skiprows to make a data frame, vt_data_next500, with the next 500 rows.
- Set the header argument so that pandas knows there is no header row.
- Name the columns in vt_data_next500 by supplying a list of vt_data_first500's columns to the names argument.

## Specify data types
When loading a flat file, pandas infers the best data type for each column. Sometimes its guesses are off, particularly for numbers that represent groups or qualities instead of quantities.

Looking at the data dictionary for vt_tax_data_2016.csv reveals two such columns. The agi_stub column contains numbers that correspond to income categories, and zipcode has 5-digit values that should be strings -- treating them as integers means we lose leading 0s, which are meaningful. Let's specify the correct data types with the dtype argument.

pandas has been imported for you as pd.
#### Instructions
- Load vt_tax_data_2016.csv with no arguments and view the data frame's dtypes attribute. Note the data types of zipcode and agi_stub.
- Create a dictionary, data_types, specifying that agi_stub is "category" data and zipcode is string data.
- Reload the CSV with the dtype argument and the dictionary to set the correct column data types.
- View the data frame's dtypes attribute.

## Set custom NA values
Part of data exploration and cleaning consists of checking for missing or NA values and deciding how to account for them. This is easier when missing values are treated as their own data type. and there are pandas functions that specifically target such NA values. pandas automatically treats some values as missing, but we can pass additional NA indicators with the na_values argument. Here, you'll do this to ensure that invalid ZIP codes in the Vermont tax data are coded as NA.

pandas has been imported as pd.
#### Instructions
- Create a dictionary, null_values, specifying that 0s in the zipcode column should be considered NA values.
- Load vt_tax_data_2016.csv, using the na_values argument and the dictionary to make sure invalid ZIP codes are treated as missing.

## Skip bad data
In this exercise you'll use read_csv() parameters to handle files with bad data, like records with more values than columns. By default, trying to import such files triggers a specific error, pandas.io.common.CParserError.

Some lines in the Vermont tax data here are corrupted. In order to load the good lines, we need to tell pandas to skip errors. We also want pandas to warn us when it skips a line so we know the scope of data issues.

pandas has been imported as pd. The exercise code will try to read the file. If there is a pandas.io.common.CParserError, the code in the except block will run.

#### Instructions
- Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.
- Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.
- Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.