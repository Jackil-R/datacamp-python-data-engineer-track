#Chapter 2 - Data Cleaning and Munging on the Command Line


## Installation and documentation for csvkit
First step in learning about any libraries, tools, or suite of tools is to make sure we are using the latest and most stable version.

Second step is to make sure we know how to access the documentation so we know where to go when we get stuck.

Let's do both in this exercise for csvkit and the various commands in this suite of data processing command-line tools.
##### Instructions
- Upgrade csvkit to the latest version using Python package manager pip.
- Print the manual for in2csv on the command line.
- Print the manual for csvlook on the command line.

## Converting and previewing data with csvkit
csvkit is written to process only CSV files. Therefore, the first thing we do is to convert our raw data file into CSV format.

After conversion, it's good practice to take a quick peak into the content of the file for a quick sanity check.
##### Instructions
- Use Linux's built in unzip tool to unpack the zipped file SpotifyData.zip.
- Convert the unzipped Excel file SpotifyData.xslx to csv and name this new file SpotifyData.csv. There is only one sheet (tab) in this file, so there's no need to worry about sheet specifications.
- Print a preview of the newly converted csv file in console using a command that is part of the csvkit suite.

## File conversion and summary statistics with csvkit
It's common for Excel data files to have more than one worksheet (tab) of data. The Excel file SpotifyData.xlsx has two sheets named Worksheet1_Popularity and Worksheet2_MusicAttributes. Each sheet should be treated like its own data file, so we will use csvkit's commands here to convert each sheet to its own CSV file. Then, using the power of the commands we already know, print a high level summary for each column in the CSV files.
##### Instructions
- From SpotifyData.xlsx, convert the sheet "Worksheet1_Popularity" to CSV and call it Spotify_Popularity.csv.
- Print the high level summary statistics for each column in Spotify_Popularity.csv.
- From SpotifyData.xlsx, convert the tab "Worksheet2_MusicAttributes" to CSV and call it Spotify_MusicAttributes.csv.
- Print a preview of Spotify_MusicAttributes.csv using a function in csvkit with Markdown-compatible, fixed-width format.

## Printing column headers with csvkit
There are many ways to preview the data within csvkit alone(e.g. csvlook, csvstat, etc). However, if all we want is to find the position and name of the columns in our data, it is easier to simply print a string of column headers. Let's print the column headers for the data file Spotify_MusicAttributes.csv.
##### Instructions
- Print in console a list of column headers in the data file Spotify_MusicAttributes.csv using a csvkit command.

## Filtering data by column with csvkit
Let's get some hands-on practice for filtering data column using the csvkit command csvcut. Remember that we can filter columns by referring to the position of the column (e.g. 1st column, 2nd column) or by referring to the exact name of the column as it appears in the data file.
##### Instructions
- Print the first column in Spotify_MusicAttributes.csv by referring to the column by its position in the file.
- Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by position.
- Print the first column in Spotify_MusicAttributes.csv by referring to the column by its name.
- Print the first, third, and fifth column in Spotify_MusicAttributes.csv by referring to them by name.

## Filtering data by row with csvkit
Now it's time get some hands-on practice for filtering data by exact row values using -m. Whether it's text or numeric, csvgrep can help us filter by these values.
##### Instructions
- Filter Spotify_MusicAttributes.csv and return the row or rows where track_id equals118GQ70Sp6pMqn6w1oKuki.
- Filter Spotify_MusicAttributes.csv and return the row or rows where danceability equals 0.812.


## Stacking files with csvkit
SpotifyData_PopularityRank6.csv and SpotifyData_PopularityRank7.csv have the same file format, column order, and overall data schema. However, one file contains information for songs ranked #6, and the other contains information for songs ranked #7. Combine the two files together into one unified file by stacking them.
##### Instructions
- Stack SpotifyData_PopularityRank6.csv and SpotifyData_PopularityRank7.csv together. Re-direct the output of this stacking and save as a new file called SpotifyPopularity.csv

## Chaining commands using operators
The more we use command-line tools, the more we start stringing complex commands together. Sometimes it's for convenience, but other times, the output of one command can be used as input to another. Let's get some hands on practice with this by filling in the correct chain operators for the circumstances described in the instructions below.
##### Instructions
- Use the chain operator that allows csvlook to run first, and if it succeeds, then run csvstat.
- Use the chain operator that to pass the output of csvsort as input to csvlook.
- Use the 2 chain operators that takes the top 15 results from the sorted output and saves it to a new file.

## Data processing with csvkit
Once we have assembled a dataset, we still need to process and clean the data prior to more advanced analysis such as predictive modeling. In this capstone exercise, let's make use of various commands in csvkit for some common data processing and cleaning.

The Excel file Spotify_201809_201810.xlsx contains two sheets (tabs), named Spotify201809 and Spotify201810. First, we will split the Excel file down to its individual sheets, preview summary statistics, remove some columns, and then stack the two sheets back together again to form one single csv file, ready for further analysis.
##### Instructions
- Convert the Spotify201809 sheet into its own csv file named Spotify201809.csv
- Familiarize ourselves with the column names by printing a preview of the file using a function in csvkit.
- Find the column names for song track and popularity rank. Create a new CSV containing only these 2 columns.
- Stack Spotify201809_subset.csv and Spotify201810_subset.csv together to form 1 csv file and create a new column with either Sep2018 or Oct2018, depending on original file source. Leave the name of the new column to its default group