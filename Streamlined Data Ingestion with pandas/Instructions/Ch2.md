# Chapter 2 - Importing Data From Excel Files

## Get data from a spreadsheet
In this exercise, you'll create a data frame from a "base case" Excel file: one with a single sheet of tabular data. The fcc_survey.xlsx file here has a sample of responses from FreeCodeCamp's annual New Developer Survey. This survey asks participants about their demographics, education, work and home life, plus questions about how they're learning to code. Let's load all of it.

pandas has not been pre-loaded in this exercise, so you'll need to import it yourself before using read_excel() to load the spreadsheet.
#### Instructions
- Load the pandas library as pd.
- Read in fcc_survey.xlsx and assign it to the variable survey_responses.
- Print the first few records of survey_responses.

## Load a portion of a spreadsheet
Spreadsheets meant to be read by people often have multiple tables, e.g., a small business might keep an inventory workbook with tables for different product types on a single sheet. Even tabular data may have header rows of metadata, like the New Developer Survey data here. While the metadata is useful, we don't want it in a data frame. You'll use read_excel()'s skiprows keyword to get just the data. You'll also create a string to pass to usecols to get only columns AD and AW through BA, about future job goals.

pandas has been imported as pd.
#### Instructions
- Create a single string, col_string, specifying that pandas should load column AD and the range AW through BA.
- Load fcc_survey_headers.xlsx', setting skiprows and usecols to skip the first two rows of metadata and get only the columns in col_string.
- View the selected column names in the resulting data frame.


## Select a single sheet
Select a single sheet
An Excel workbook may contain multiple sheets of related data. The New Developer Survey response workbook has sheets for different years. Because read_excel() loads only the first sheet by default, you've already gotten survey responses for 2016. Now, you'll create a data frame of 2017 responses using read_excel()'s sheet_name argument in a couple different ways.

pandas has been imported as pd.
#### Instructions
- Create a data frame from the second workbook sheet by passing the sheet's position to sheet_name.
- Create a data frame from the 2017 sheet by providing the sheet's name to read_excel().

## Select multiple sheets
So far, you've read Excel files one sheet at a time, which lets you customize import arguments for each sheet. But if an Excel file has some sheets that you want loaded with the same parameters, you can get them in one go by passing a list of their names or indices to read_excel()'s sheet_name keyword. To get them all, pass None. You'll practice both methods to get data from fcc_survey.xlsx, which has multiple sheets of similarly-formatted data.

pandas has been loaded as pd.
#### Instructions
- Load both the 2016 and 2017 sheets by name with a list and one call to read_excel()
- Load the 2016 sheet by its position (0) and 2017 by name. Note the sheet names in the result.
- Load all sheets in the Excel file without listing them all.

## Work with multiple spreadsheets
Workbooks meant primarily for human readers, not machines, may store data about a single subject across multiple sheets. For example, a file may have a different sheet of transactions for each region or year in which a business operated.

The FreeCodeCamp New Developer Survey file is set up similarly, with samples of responses from different years in different sheets. Your task here is to compile them in one data frame for analysis.

pandas has been imported as pd. All sheets have been read into the ordered dictionary responses, where sheet names are keys and data frames are values, so you can get data frames with the values() method.
#### Instructions
- Create an empty data frame, all_responses.
- Set up a for loop to iterate through the values in the responses dictionary.
- Append each data frame to all_responses and reassign the result to the same variable name.

## Set Boolean columns
Datasets may have columns that are most accurately modeled as Boolean values. However, pandas usually loads these as floats by default, since defaulting to Booleans may have undesired effects like turning NA values into Trues.

fcc_survey_subset.xlsx contains a string ID column and several True/False columns indicating financial stressors. You'll evaluate which non-ID columns have no NA values and therefore can be set as Boolean, then tell read_excel() to load them as such with the dtype argument.

pandas is loaded as pd.
#### Instructions
- Count NA values in each column of survey_data with isna() and sum(). Note which columns besides ID.x, if any, have zero NAs.
- Set read_excel()'s dtype argument to load the HasDebt column as Boolean data.
- Supply the Boolean column name to the print statement to view financial burdens by group.

## Set custom true/false values
In Boolean columns, pandas automatically recognizes certain values, like "TRUE" and 1, as True, and others, like "FALSE" and 0, as False. Some datasets, like survey data, can use unrecognized values, such as "Yes" and "No".

For practice purposes, some Boolean columns in the New Developer Survey have been coded this way. You'll make sure they're properly interpreted with the help of the true_values and false_values arguments.

pandas is loaded as pd. You can assume the columns you are working with have no missing values.
#### Instructions
- Load the Excel file, specifying "Yes" as a true value and "No" as a false value.

## Parse simple dates
pandas does not infer that columns contain datetime data; it interprets them as object or string data unless told otherwise. Correctly modeling datetimes is easy when they are in a standard format -- we can use the parse_dates argument to tell read_excel() to read columns as datetime data.

The New Developer Survey responses contain some columns with easy-to-parse timestamps. In this exercise, you'll make sure they're the right data type.

pandas has been loaded as pd.
#### Instructions
- Load fcc_survey.xlsx, making sure that the Part1StartTime column is parsed as datetime data.
- View the first few values of the survey_data.Part1StartTime to make sure it contains datetimes.

#Get datetimes from multiple columns
Sometimes, datetime data is split across columns. A dataset might have a date and a time column, or a date may be split into year, month, and day columns.

A column in this version of the survey data has been split so that dates are in one column, Part2StartDate, and times are in another, Part2StartTime. Your task is to use read_excel()'s parse_dates argument to combine them into one datetime column with a new name.

pandas has been imported as pd
#### Instructions
- Create a dictionary, datetime_cols indicating that the new column Part2Start should consist of Part2StartDate and Part2StartTime.
- Load the survey response file, supplying the dictionary to the parse_dates argument to create a new Part2Start column.
- View summary statistics about the new Part2Start column with the describe() method.

#Parse non-standard date formats
So far, you've parsed dates that pandas could interpret automatically. But if a date is in a non-standard format, like 19991231 for December 31, 1999, it can't be parsed at the import stage. Instead, use pd.to_datetime() to convert strings to dates after import.

The New Developer Survey data has been loaded as survey_data but contains an unparsed datetime field. We'll use to_datetime() to convert it, passing in the column to convert and a string representing the date format used.

For more on date format codes, see this reference. Some common codes are year (%Y), month (%m), day (%d), hour (%H), minute (%M), and second (%S).

pandas has been imported as pd.
#### Instructions
- Parse Part2EndTime using pd.to_datetime(), the format keyword argument, and the format string you just identified. Assign the result back to the Part2EndTime column.
- Print the head of Part2EndTime to confirm the column now contains datetime values.