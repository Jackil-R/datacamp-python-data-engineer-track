# Chapter 4 - Basic pandas optimizations


## Iterating with .iterrows()
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console for convenience.
#### Instructions
- Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.
- Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.
- Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.
- Add a line in the for loop to print the type of each row_tuple.

## Run differentials with .iterrows()
Run differentials with .iterrows()
You've been hired by the San Francisco Giants as an analyst—congrats! The team's owner wants you to calculate a metric called the run differential for each season from the year 2008 to 2012. This metric is calculated by subtracting the total number of runs a team allowed in a season from the team's total number of runs scored in a season. 'RS' means runs scored and 'RA' means runs allowed.

The below function calculates this metric:
``````
def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff
``````
A DataFrame has been loaded into your session as giants_df and printed into the console. Let's practice using .iterrows() to add a run differential column to this DataFrame.
#### Instructions
- Create an empty list called run_diffs that will be used to store the run differentials you will calculate.
- Write a for loop that uses .iterrows() to loop over giants_df and collects each row's runs scored and runs allowed.
- Add a line to the for loop that uses the provided function to calculate each row's run differential.
- Add a line to the loop that appends each row's run differential to the run_diffs list.


## Iterating with .itertuples()
Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax. Let's practice working with namedtuples.

A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').
#### Instructions
- Use .itertuples() to loop over rangers_df and print each row.
- Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.
- Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.

## Run differentials with .itertuples()
Run differentials with .itertuples()
The New York Yankees have made a trade with the San Francisco Giants for your analyst contract— you're a hot commodity! Your new boss has seen your work with the Giants and now wants you to do something similar with the Yankees data. He'd like you to calculate run differentials for the Yankees from the year 1962 to the year 2012 and find which season they had the best run differential.

You've remembered the function you used when working with the Giants and quickly write it down:
``````
def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed
 
    return run_diff
``````
Let's use .itertuples() to loop over the yankees_df DataFrame (which has been loaded into your session) and calculate run differentials.
#### Instructions
- Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.
- Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.
- Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.
- 

## Analyzing baseball stats with .apply()
Analyzing baseball stats with .apply()
The Tampa Bay Rays want you to analyze their data.

They'd like the following metrics:

The sum of each column in the data
- The total amount of runs scored in a year ('RS' + 'RA' for each year)
- The 'Playoffs' column in text format rather than using 1's and 0's
- The below function can be used to convert the 'Playoffs' column to text:
``````
def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 
``````
Use .apply() to get these metrics. A DataFrame (rays_df) has been loaded and printed to the console. This DataFrame is indexed on the 'Year' column.
#### Instructions
- Apply sum() to each column of rays_df to collect the sum of each column. Be sure to specify the correct axis.
- Apply sum() to each row of rays_df, only looking at the 'RS' and 'RA' columns, and specify the correct axis.
- Use .apply() and a lambda function to apply text_playoffs() to each row's 'Playoffs' value of the rays_df DataFrame.

## Settle a debate with .apply()
Settle a debate with .apply()
Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. They'd like for you to help settle a debate amongst the managers. One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. Another manager says this is not true.

Let's use the below function and the .apply() method to see which manager is correct.
``````
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
``````
A DataFrame named dbacks_df has been loaded into your session.
#### Instructions
- Print the first five rows of the dbacks_df DataFrame to see what the data looks like.
- Create a pandas Series called win_percs by applying the calc_win_perc() function to each row of the DataFrame with a lambda function.
- Create a new column in dbacks_df called WP that contains the win percentages you calculated in the above step.
- 

## Replacing .iloc with underlying arrays
Replacing .iloc with underlying arrays
Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. You'll revisit the win percentage calculations you performed row by row with the .iloc method:
``````
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list
``````
Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.
#### Instructions
- Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.
- Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.
- 

## Bringing it all together: Predict win percentage
Bringing it all together: Predict win percentage
A pandas DataFrame (baseball_df) has been loaded into your session. For convenience, a dictionary describing each column within baseball_df has been printed into your console. You can reference these descriptions throughout the exercise.

You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season ('RS') and total runs allowed in a season ('RA') with the following function:
``````
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)
``````
Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.
#### Instructions
- Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.
- 
- 
- 