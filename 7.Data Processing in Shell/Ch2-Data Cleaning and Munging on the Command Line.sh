#Chapter 2 - Data Cleaning and Munging on the Command Line


#Installation and documentation for csvkit
# Upgrade csvkit using pip
pip install --upgrade csvkit

# Print manual for in2csv
in2csv -h

# Print manual for csvlook
csvlook -h
print"========================================================="


#Converting and previewing data with csvkit
# Use ls to find the name of the zipped file
ls

# Use Linux's built in unzip tool to unpack the zipped file
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls

# Convert SpotifyData.xlsx to csv
in2csv SpotifyData.xlsx > SpotifyData.csv

# Print a preview in console using a csvkit suite command
csvlook SpotifyData.csv
print"========================================================="


#File conversion and summary statistics with csvkit
# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet1_Popularity" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Datasets/Spotify_Popularity.csv

# Check to confirm name and location of the new CSV file
ls

# Print high level summary statistics for each column
csvstat Datasets/Spotify_Popularity.csv

# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet2_MusicAttributes" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Datasets/Spotify_MusicAttributes.csv

# Check to confirm name and location of the new CSV file
ls

# Print preview of Spotify_MusicAttributes
csvlook Datasets/Spotify_MusicAttributes.csv
print"========================================================="


#Printing column headers with csvkit
# Check to confirm name and location of data file
ls

# Print a list of column headers in data file
csvcut -n Datasets/Spotify_MusicAttributes.csv
print"========================================================="


#Filtering data by column with csvkit
# Print a list of column headers in the data
csvcut -n Datasets/Spotify_MusicAttributes.csv

# Print the first column, by position
csvcut -c 1 Datasets/Spotify_MusicAttributes.csv

# Print the first, third, and fifth column, by position
csvcut -c 1,3,5 Datasets/Spotify_MusicAttributes.csv

# Print the first column, by name
csvcut -c "track_id" Datasets/Spotify_MusicAttributes.csv

# Print the track id, song duration, and loudness, by name
csvcut -c "track_id","duration_ms","loudness" Datasets/Spotify_MusicAttributes.csv
print"========================================================="


#Filtering data by row with csvkit
# Print a list of column headers in the data
csvcut -n Datasets/Spotify_MusicAttributes.csv

# Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki
csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Datasets/Spotify_MusicAttributes.csv

# Filter for row(s) where danceability = 0.812
csvgrep -c "danceability" -m 0.812 Datasets/Spotify_MusicAttributes.csv
print"========================================================="


#Stacking files with csvkit
# Stack the two files and save results as a new file
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv

# Preview the newly created file
csvlook SpotifyPopularity.csv
print"========================================================="


#Chaining commands using operators
# If csvlook succeeds, then run csvstat
csvlook Datasets/Spotify_Popularity.csv && csvstat Datasets/Spotify_Popularity.csv

# Use the output of csvsort as input to csvlook
csvsort -c 2 Datasets/Spotify_Popularity.csv | csvlook

# Take top 15 rows from sorted output and save to new file
csvsort -c 2 Datasets/Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv

# Preview the new file
csvlook Spotify_Popularity_Top15.csv
print"========================================================="


#Data processing with csvkit
# Convert the Spotify201809 sheet into its own csv file
in2csv Spotify_201809_201810.xlsx --sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

csvcut -n Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
csvcut -c "track_id","popularity" Spotify201809.csv > Spotify201809_subset.csv

# While stacking the 2 files, create a data source column
csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv
print"========================================================="