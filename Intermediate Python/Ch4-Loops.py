#Basic while loop
# Initialize offset
offset = 8

# Code the while loop
while(offset != 0):
    print("correcting...")
    offset = offset -1
    print(offset)
print('========================================')


#Add conditionals
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else :
      offset = offset + 1
    print(offset)
print('========================================')


#Loop over a list
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)

print('========================================')


#Indexes and values (1)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room "+ str(index) + ": "+ str(area))
print('========================================')



#Indexes and values (2)
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
print('========================================')


#Loop over list of lists
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x in house:
    print("the " + str(x[0]) + " is " + str(x[1]) + " sqm")
print('========================================')


#Loop over dictionary
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print("the capital of " + k + " is " + v)
print('========================================')


#Loop over Numpy array
# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height) :
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(str(x))
print('========================================')


#Loop over DataFrame (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for i, car in cars.iterrows() :
    print(i)
    print(str(car))
print('========================================')


#Loop over DataFrame (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
print('========================================')


#Add column (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = str.upper(row["country"])

# Print cars
print(cars)
print('========================================')


#Add column (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars['COUNTRY'] = cars["country"].apply(str.upper)
print('========================================')