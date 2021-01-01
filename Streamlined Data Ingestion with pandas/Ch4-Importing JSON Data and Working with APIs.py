#Chapter 4 - Importing JSON Data and Working with APIs

#Load JSON data
# Load pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import requests as requests
# Load the daily report to a data frame
pop_in_shelters = pd.read_json('Datasets/dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())
print("=========================================================")


#Work with JSON orientations
try:
    # Load the JSON with orient specified
    df = pd.read_json("Datasets/dhs_report_reformatted.json",
                      orient="split")

    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census",
            y="total_individuals_in_shelter")
    plt.show()

except ValueError:
    print("pandas could not parse the JSON.")
print("=========================================================")


#Get data from an API
api_url = "https://api.yelp.com/v3/businesses/search"
api_key = "B8t6qN3cM_fhFn8vBKsU90isOFle3CTDoH9RRdqN1w1kZT54EKSk9iv_s_wJtsiC_ODPwUzgahk54QdiZaPdnU6N2rwww915NRAoct3pQGCYtRWHn6bAweg6EDDvX3Yx"
headers = {"Authorization": "Bearer {}".format(api_key)}
parameters = {"term": "cafe",
              "location": "NYC"}
# Get data about NYC cafes from the Yelp API
response = requests.get(api_url,
                headers=headers,
                params=parameters)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)
print("=========================================================")


#Set API parameters
# Create dictionary to query API for cafes in NYC
params = {"term": "cafe",
              "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers=headers,
                params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
print("=========================================================")


#Set request headers
# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}
params = {'term': 'cafe', 'location': 'NYC', 'sort_by': 'rating'}
# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers=headers,
                params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)
print("=========================================================")


#Flatten nested JSONs
# Load json_normalize()
from pandas.io.json import json_normalize

api_url = 'https://api.yelp.com/v3/businesses/search'
api_key = "B8t6qN3cM_fhFn8vBKsU90isOFle3CTDoH9RRdqN1w1kZT54EKSk9iv_s_wJtsiC_ODPwUzgahk54QdiZaPdnU6N2rwww915NRAoct3pQGCYtRWHn6bAweg6EDDvX3Yx"
headers = {"Authorization": "Bearer {}".format(api_key)}
parameters = {'location': 'NYC', 'term': 'cafe'}
# Isolate the JSON data from the API response
response = requests.get(api_url,
                headers=headers,
                params=params)
data = response.json()

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
             sep="_")

# View data
print(cafes.columns)
print("=========================================================")


#Handle deeply nested data
# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name',
                                  'alias',
                                  'rating',
                                  'transactions',
                          		  ['coordinates', 'latitude'],
                          		  ['coordinates', 'longitude']],
                    		meta_prefix="biz_")

# View the data
print(flat_cafes.head())
print(flat_cafes.columns)
print("=========================================================")


#Append data frames
# Add an offset parameter to get cafes 51-100
params = {"term": "cafe",
          "location": "NYC",
          "sort_by": "rating",
          "limit": 50,
          "offset" : 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes,ignore_index=True)

# Print shape of cafes
print(cafes.shape)
print("=========================================================")


#Merge data frames

# print(cafes.columns)
# Index(['alias', 'categories', 'coordinates_latitude', 'coordinates_longitude', 'display_phone', 'distance', 'id', 'image_url', 'is_closed', 'location_address1', 'location_address2',
#        'location_address3', 'location_city', 'location_country', 'location_display_address', 'location_state', 'location_zip_code', 'name', 'phone', 'price', 'rating', 'review_count', 'transactions',
#        'url'], dtype='object')
# print(crosswalk.columns)
# Index(['zipcode', 'ziptype', 'postalcity', 'zcta5', 'bcode', 'note', 'puma', 'pumaname'], dtype='object')
# print(pop_data.columns)
# Index(['geo_type', 'geog_name', 'puma', 'borough', 'total_pop_estimate', 'total_pop_moe'], dtype='object')

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk,
                                left_on="location_zip_code",
                                right_on="zipcode")



# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data,
                                left_on="puma",
                                right_on="puma")

# View the data
print(cafes_with_pop.head())
print("=========================================================")
