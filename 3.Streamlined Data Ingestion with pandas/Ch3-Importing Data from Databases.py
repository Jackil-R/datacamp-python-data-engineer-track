#Chapter 3 - Importing Data from Databases

#Connect to a database
# Load matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///Datasets/data.db")

# View the tables in the database
print(engine.table_names())
print("=========================================================")


#Load entire tables
# Create the database engine
engine = create_engine("sqlite:///Datasets/data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql("weather", engine)

# View the first few rows of data
print(weather.head())
print("=========================================================")


#Selecting columns with SQL
# Create database engine for data.db
engine = create_engine("sqlite:///Datasets/data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a data frame by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting data frame
print(temperatures)
print("=========================================================")


#Selecting rows
# Create query to get hpd311calls records about safety
query = """
SELECT *
FROM hpd311calls
WHERE complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query,engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()
print("=========================================================")


#Filtering on multiple conditions
# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query,engine)

# View summary stats about the temperatures
print(wintry_days.describe())
print("=========================================================")


#Getting distinct values
# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query,engine)

# Check assumption about issues and boroughs
print(issues_and_boros)
print("=========================================================")


#Counting in groups
# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     count(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create data frame of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()
print("=========================================================")


#Working with aggregate functions
# Create a query to get month and max tmax by month
query = """
SELECT month, 
       max(tmax),
       min(tmin),
       sum(prcp)
  FROM weather 
  GROUP BY month;"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
print("=========================================================")


#Joining tables
# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create data frame of joined tables
calls_with_weather = pd.read_sql(query,engine)

# View the data frame to make sure all columns were joined
print(calls_with_weather.head())
print("=========================================================")


#Joining and filtering
# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';
"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())
print("=========================================================")


#Joining, filtering, and aggregating
# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       count(*),
       weather.tmax,
       weather.tmin
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
  GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())
print("=========================================================")