# Chapter 4 - Basic pandas optimizations

import numpy as np
import pandas as pd

##Iterating with .iterrows()
pit_df = pd.read_csv('Datasets/input.csv')
print(pit_df)
# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)
# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)
# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))
print("=========================================================")


##Run differentials with .iterrows()
giants_df = pd.read_csv('Datasets/input.csv')
def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff
# Create an empty list to store run differentials
run_diffs= []
# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)
print("=========================================================")


##Iterating with .itertuples()
rangers_df = pd.read_csv('Datasets/input1.csv')
# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)
print("=========================================================")


##Run differentials with .itertuples()
yankees_df = pd.read_csv('Datasets/input2.csv')
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)
# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)
print(max(list(yankees_df['RD'])))
print("=========================================================")


##Analyzing baseball stats with .apply()
rays_df = pd.read_csv('Datasets/input3.csv')
def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'
# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)
# Gather total runs scored in all games per year
RA_RS = rays_df[['RS', 'RA']]
print(RA_RS)
total_runs_scored = RA_RS.apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)
print("=========================================================")


##Settle a debate with .apply()
dbacks_df= pd.read_csv('Datasets/input4.csv')
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])
print(len(dbacks_df))
print(len(dbacks_df[dbacks_df['WP'] >= 0.50]))
print("=========================================================")


##Replacing .iloc with underlying arrays
baseball_df=dbacks_df= pd.read_csv('Datasets/baseball_stats.csv')
baseball_df.drop(['RankSeason','RankPlayoffs','RankSeason','OOBP','OSLG','SLG','BA','OBP'], axis=1, inplace=True)
print(baseball_df)

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())
print("=========================================================")


##Bringing it all together: Predict win percentage
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)
win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds0'] = win_perc_preds_np
print(baseball_df.head())
print(type(win_perc_preds_np))
win_perc_preds_np = baseball_df['RS'].values ** 2 / (baseball_df['RS'].values ** 2 + baseball_df['RA'].values ** 2)
baseball_df['WP_preds1'] = win_perc_preds_np
print(baseball_df.head())
print(type(win_perc_preds_np))
print("=========================================================")