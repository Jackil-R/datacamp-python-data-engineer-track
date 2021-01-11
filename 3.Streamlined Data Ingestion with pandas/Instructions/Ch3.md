# Chapter 3 - Importing Data from Databases

## Connect to a database
In order to get data from a database with pandas, you first need to be able to connect to one. In this exercise, you'll practice creating a database engine to manage connections to a database, data.db. To do this, you'll use sqlalchemy's create_engine() function.

create_engine() needs a string URL to the database. For SQLite databases, that string consists of "sqlite:///", then the database file name.
#### Instructions
- Use create_engine() to make a database engine for data.db.
- Run the last line of code to show the names of the tables in the database.

## Load entire tables
In the last exercise, you saw that data.db has two tables. weather has historical weather data for New York City. hpd311calls is a subset of call records made to the city's 311 help line about housing issues.

In this exercise, you'll use the read_sql() function in pandas to load both tables. read_sql() accepts a string of either a SQL query to run, or a table to load. It also needs a way to connect to the database, like the engine in the provided code.
#### Instructions
- Use read_sql() to load the hpd311calls table by name, without any SQL.
- Use read_sql() and a SELECT * ... SQL query to load the entire weather table.

## Selecting columns with SQL
Datasets can contain columns that are not required for an analysis, like the weather table in data.db does. Some, such as elevation, are redundant, since all observations occurred at the same place, while others contain variables we are not interested in. After making a database engine, you'll write a query to SELECT only the date and temperature columns, and pass both to read_sql() to make a data frame of high and low temperature readings.

pandas has been loaded as pd, and create_engine() has been imported from sqlalchemy.

Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.
#### Instructions
- Create a database engine for data.db.
- Write a SQL query that SELECTs the date, tmax, and tmin columns from the weather table.
- Make a data frame by passing the query and engine to read_sql() and assign the resulting data frame to temperatures.

## Selecting rows
SQL WHERE clauses return records whose values meet the given criteria. Passing such a query to read_sql() results in a data frame loaded with only records we are interested in, so there is less filtering to do later on.

The hpd311calls table in data.db has data on calls about various housing issues, from maintenance problems to information requests. In this exercise, you'll use SQL to focus on calls about safety.

pandas has been loaded as pd, and a database engine, engine, has been created for data.db.
#### Instructions
- Create a query that selects all columns of records in hpd311calls that have 'SAFETY' as their complaint_type.
- Use read_sql() to query the database and assign the result to the variable safety_calls.
- Run the last section of code to create a graph of safety call counts in each borough.

## Filtering on multiple conditions
So far, you've selectively imported records that met a single condition, but it's also common to filter datasets on multiple criteria. In this exercise, you'll do just that.

The weather table contains daily high and low temperatures and precipitation amounts for New York City. Let's focus on inclement weather, where there was either an inch or more of snow or the high was at or below freezing (32° Fahrenheit). To do this, you'll need to build a query that uses the OR operator to look at values in both columns.

pandas is loaded as pd, and a database engine, engine, has been created.
#### Instructions
- Create a query that selects records in weather where tmax is less than or equal to 32 degrees OR snow is greater than or equal to 1 inch.
- Use read_sql() to query the database and assign the result to the variable wintry_days.
- View summary statistics with the describe() method to make sure all records in the data frame meet the given criteria.

## Getting distinct values
Sometimes an analysis doesn't need every record, but rather unique values in one or more columns. Duplicate values can be removed after loading data into a data frame, but it can also be done at import with SQL's DISTINCT keyword.

Since hpd311calls contains data about housing issues, we would expect most records to have a borough listed. Let's test this assumption by querying unique complaint_type/borough combinations.

pandas has been imported as pd, and the database engine has been created as engine.

Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.
#### Instructions
- Create a query that gets DISTINCT values for borough and complaint_type (in that order) from hpd311calls.
- Use read_sql() to load the results of the query to a data frame, issues_and_boros.
- Print the data frame to check if the assumption that all issues besides literature requests appear with boroughs listed.

## Counting in groups
In previous exercises, you pulled data from tables, then summarized the resulting data frames in pandas to create graphs. By using COUNT and GROUP BY in a SQL query, we can pull those summary figures from the database directly.

The hpd311calls table has a column, complaint_type, that categorizes call records by issue, such as heating or plumbing. In order to graph call volumes by issue, you'll write a SQL query that COUNTs records by complaint type.

pandas has been imported as pd, and the database engine for data.db has been created as engine.
#### Instructions
- Create a SQL query that gets the complaint_type column and counts of all records from hpd311calls, grouped by complaint_type.
- Create a data frame with read_sql() of call counts by issue, calls_by_issue.
- Run the last section of code to graph the number of calls for each housing issue.

## Working with aggregate functions
If a table contains data with higher granularity than is needed for an analysis, it can make sense to summarize the data with SQL aggregate functions before importing it. For example, if you have data of flood event counts by month but precipitation data by day, you may decide to SUM precipitation by month.

The weather table contains daily readings for four months. In this exercise, you'll practice summarizing weather by month with the MAX, MIN, and SUM functions.

pandas has been loaded as pd, and a database engine, engine, has been created.
#### Instructions
- Create a query to pass to read_sql() that will get months and the MAX value of tmax by monthfrom weather.
- Modify the query to also get the MIN tmin value for each month.
- Modify the query to also get the total precipitation (prcp) for each month.

## Joining tables
Tables in relational databases usually have key columns of unique record identifiers. This lets us build pipelines that combine tables using SQL's JOIN operation, instead of having to combine data after importing it.

The records in hpd311calls often concern issues, like leaks or heating problems, that are exacerbated by weather conditions. In this exercise, you'll join weather data to call records along their common date columns to get everything in one data frame. You can assume these columns have the same data type.

pandas is loaded as pd, and the database engine, engine, has been created.

Note: The SQL checker is picky about join table order -- it expects specific tables on the left and the right.
#### Instructions
- Complete the query to join weather to hpd311calls by their date and created_date columns, respectively.
- Query the database and assign the resulting data frame to calls_with_weather.
- Print the first few rows of calls_with_weather to confirm all columns were joined.

## Joining and filtering
Just as you might not always want all the data in a single table, you might not want all columns and rows that result from a JOIN. In this exercise, you'll use SQL to refine a data import.

Weather exacerbates some housing problems more than others. Your task is to focus on water leak reports in hpd311calls and assemble a dataset that includes the day's precipitation levels from weather to see if there is any relationship between the two. The provided SQL gets all columns in hpd311calls, but you'll need to modify it to get the necessary weather column and filter rows with a WHERE clause.

pandas is loaded as pd, and the database engine, engine, has been created.
#### Instructions
- Complete query to get the prcp column in weather and join weather to hpd311calls on their date and created_date columns, respectively.
- Use read_sql() to load the results of the query into the leak_calls data frame.
- Modify query to get only rows that have 'WATER LEAK' as their complaint_type.

## Joining, filtering, and aggregating
In this exercise, you'll use what you've learned to assemble a dataset to investigate how the number of heating complaints to New York City's 311 line varies with temperature.

In addition to the hpd311calls table, data.db has a weather table with daily high and low temperature readings for NYC. We want to get each day's count of heat/hot water calls with temperatures joined in. This can be done in one query, which we'll build in parts.

In part one, we'll get just the data we want from hpd311calls. Then, in part two, we'll modify the query to join in weather data.

pandas has been imported as pd, and the database engine has been created as engine.
#### Instructions
- Complete the query to get created_date and counts of records whose complaint_type is HEAT/HOT WATER from hpd311calls by date.
- Create a data frame,df, containing the results of the query.
- Modify the query to join tmax and tmin from the weather table. (There is only one record per date in weather, so we do not need SQL's MAX and MIN functions here.) Join the tables on created_date in hpd311calls and date in weather.