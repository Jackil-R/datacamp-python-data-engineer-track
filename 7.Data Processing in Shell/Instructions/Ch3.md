#Chapter 3 - Database Operations on the Command Line


## Using sql2csv documentation
Suppose you're trying to run a query with sql2csv but you've been having issues because the error message is not detailed enough to help debug the error. Which optional argument in sql2csv will print detailed tracebacks and logs when errors occur while using sql2csv?
##### Instructions
- -h or --help
- Answer: -v or --verbose
- -l or --linenumber
- -V or --version

## Understand sql2csv connectors
Understand sql2csv connectors
Suppose you have a SQL database you would like to connect to using sql2csv, but you're not sure yet if this particular database can be connected to. sql2csv's manual does not readily have the list of possible database connectors, but csvsql does!

Could you use csvsql's manual to check what SQL database connections are currently NOT supported for sql2csv and for the rest of the csvkit suite?
##### Instructions
- Firebird
- Microsoft SQL Server (mssql)
- MySQL
- Answer: MongoDB
- PostgreSQL

## Practice pulling data from database
With the powers of csvkit, we don't need to download and set up fancy database management software like MS SQL Server, DB2, PgAdmin, or TablePlus to be able to access the data inside a SQL database. We can pull data directly from our command line using csvkit's sql2csv command.

In this practice, let's walk through pulling data step by step, by applying SQL manipulations to the table Spotify_Popularity which dwells inside a SQLite database called SpotifyDatabase and then saving the output of the SQL query to a local .csv file Spotify_Popularity_5Rows.csv.
##### Instructions
- Use sql2csv to access the SQLite database SpotifyDatabase and query and print all data in the table Spotify_Popularity.
- Use a SQL query to print the first 5 rows in the table Spotify_Popularity. Then, preview the results using csvlook.
- Save queried results to a new file Spotify_Popularity_5Rows.csv. Verify and preview the file with ls and csvlook.

## Applying SQL to a local CSV file
Sometimes the data manipulation we want to do is just easier to do with SQL. In this situation, we want to find the shortest duration song in Spotify_MusicAttributes.csv by applying the SQL below directly to the data file.

SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1

Let's go through this step by step.
##### Instructions
- Complete the command to apply the SQL query to Spotify_MusicAttributes.csv.
- Further improve the output by piping the output to csvlook.
- Instead of printing to console, re-direct output and save as new file: LongestSong.csv.

## Cleaner scripting via shell variables
Because SQL queries, by nature, can be long and complex, we will frequently need to deal with line breaks while passing in SQL queries to csvkit commands.

One way to work around this is to store the SQL queries as a shell variable, then pass in the shell variable in place of the SQL query where needed.
##### Instructions
- Fill in the csvsql command by calling upon the bash variable containing the SQL query instead of writing out the SQL query in full.

## Joining local CSV files using SQL
csvsql can be used to join CSV files together even when neither of them are in a database. Here, we have two CSV files Spotify_MusicAttributes.csv and Spotify_Popularity.csv that are both on song level but contain different attributes for each song. We can combine the two files together using a SQL-like JOIN, and we can do so, through the power of csvsql

Explore the data with the commands we have learned so far (e.g. csvstat, csvlook, etc). What is the column that Spotify_MusicAttributes.csv and Spotify_Popularity.csv have in common that can be used as the JOIN key?

csvsql can be used to join CSV files together even when neither of them are in a database. Here, we have two CSV files Spotify_MusicAttributes.csv and Spotify_Popularity.csv that are both on song level but contain different attributes for each song. We can combine the two files together using a SQL-like JOIN, and we can do so, through the power of csvsql
##### Instructions
- popularity
- time_signature
- id
- Answer: track_id

- Join Spotify_MusicAttributes.csv and Spotify_Popularity.csv together to form a new file Spotify_FullData.csv.

## Practice pushing data back to database
It is also possible to go the other way around and push local CSV files back to the database. As long as we specify the database as well as the CSV file to be loaded, csvsql does the rest of the work for us (e.g. inferring table schema), behind the scenes.

In the following exercise, complete the command to upload Spotify_MusicAttributes.csv as its own table in the SQLite database SpotifyDatabase. Then, as a sanity check, re-pull the data from the newly created table in the database.
##### Instructions
- Upload Spotify_MusicAttributes.csv as its own table in the SQLite database SpotifyDatabase.
- Re-pull the data from the newly created table Spotify_MusicAttributes in the SQLite database SpotifyDatabase.

## Database and SQL with csvkit
The addition of csvsql and sql2csv allows us to go through an entire data workflow inside the terminal without needing to install and set up additional SQL clients and software. In this capstone, we will put together and pull data from a SQLite database, merge this data with a locally saved file, and finally, push a final merged file back to the database, all without ever leaving the command line.
##### Instructions
- Download the entire table SpotifyMostRecentData from the SQLite database SpotifyDatabase and save it as a csv file locally as SpotifyMostRecentData.csv.
- Manipulate the two local csv files SpotifyMostRecentData.csv and Spotify201812.csv by passing in the stored UNION ALL SQL query into csvsql. Save the newly created file as UnionedSpotifyData.csv. 
- Push the newly created csv file UnionedSpotifyData.csv back to database SpotifyDatabase as its own table.