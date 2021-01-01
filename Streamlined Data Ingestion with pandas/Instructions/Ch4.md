# Chapter 4 - Importing JSON Data and Working with APIs

## Load JSON data
Many open data portals make available JSONs datasets that are particularly easy to parse. They can be accessed directly via URL. Each object is a record, all objects have the same set of attributes, and none of the values are nested objects that themselves need to be parsed.

The New York City Department of Homeless Services Daily Report is such a dataset, containing years' worth of homeless shelter population counts. You can view it in the console before loading it to a data frame with pandas's read_json() function.
#### Instructions
- Get a sense of the contents of dhs_daily_report.json, which are printed in the console.
- Load pandas as pd.
- Use read_json() to load dhs_daily_report.json to a data frame, pop_in_shelters.
- View summary statistics about pop_in_shelters with the data frame's describe() method.

## Work with JSON orientations
Work with JSON orientations
JSON isn't a tabular format, so pandas makes assumptions about its orientation when loading data. Most JSON data you encounter will be in orientations that pandas can automatically transform into a data frame.

Sometimes, like in this modified version of the Department of Homeless Services Daily Report, data is oriented differently. To reduce the file size, it has been split formatted. You'll see what happens when you try to load it normally versus with the orient keyword argument. The try/except block will alert you if there are errors loading the data.

pandas has been loaded as pd.
#### Instructions
- Try loading dhs_report_reformatted.json without any keyword arguments.
- Load dhs_report_reformatted.json to a data frame with orient specified.

#Get data from an API
In this exercise, you'll use requests.get() to query the Yelp Business Search API for cafes in New York City. requests.get() needs a URL to get data from. The Yelp API also needs search parameters and authorization headers passed to the params and headers keyword arguments, respectively.

You'll need to extract the data from the response with its json() method, and pass it to pandas's DataFrame() function to make a data frame. Note that the necessary data is under the dictionary key "businesses".

pandas (as pd) and requests have been loaded. Authorization data is in the dictionary headers, and the needed API parameters are stored as params.
#### Instructions
- Get data about New York City cafes from the Yelp API (api_url) with requests.get(). The necessary params and headers information has been provided.
- Extract the JSON data from the response with its json() method, and assign it to data.
- Load the cafe listings to the data frame cafes with pandas's DataFrame() function. The listings are under the "businesses" key in data.
- Print the data frame's dtypes to see what information you're getting.

## Set API parameters
Formatting parameters to get the data you need is an integral part of working with APIs. These parameters can be passed to the get() function's params keyword argument as a dictionary.

The Yelp API requires the location parameter be set. It also lets users supply a term to search for. You'll use these parameters to get data about cafes in NYC, then process the result to create a data frame.

pandas (as pd) and requests have been loaded. The API endpoint is stored in the variable api_url. Authorization data is stored in the dictionary headers.
#### Instructions
- Create a dictionary, parameters, with the term and location parameters set to search for "cafe"s in "NYC".
- Query the Yelp API (api_url) with requests's get() function and the headers and params keyword arguments set. Save the result as response.
- Extract the JSON data from response with the appropriate method. Save the result as data.
- Load the "businesses" values in data to the data frame cafes and print the head.

## Set request headers
Many APIs require users provide an API key, obtained by registering for the service. Keys typically are passed in the request header, rather than as parameters.

The Yelp API documentation says "To authenticate API calls with the API Key, set the Authorization HTTP header value as Bearer API_KEY."

You'll set up a dictionary to pass this information to get(), call the API for the highest-rated cafes in NYC, and parse the response.

pandas (as pd) and requests have been loaded. The API endpoint is stored as api_url, and the key is api_key. Parameters are in the dictionary params.
#### Instructions
- Create a dictionary, headers, that passes the formatted key string to the "Authorization" header value.
- Query the Yelp API (api_url) with get() and the necessary headers and parameters. Save the result as response.
- Extract the JSON data from response. Save the result as data.
- Load the "businesses" values in data to the data frame cafes and print the names column.

#Flatten nested JSONs
A feature of JSON data is that it can be nested: an attribute's value can consist of attribute-value pairs. This nested data is more useful unpacked, or flattened, into its own data frame columns. The pandas.io.json submodule has a function, json_normalize(), that does exactly this.

The Yelp API response data is nested. Your job is to flatten out the next level of data in the coordinates and location columns.

pandas (as pd) and requests have been imported. The results of the API call are stored as response.
#### Instructions
- Load the json_normalize() function from pandas' io.json submodule.
- Isolate the JSON data from response and assign it to data.
- Use json_normalize() to flatten and load the businesses data to a data frame, cafes. Set the sep argument to use underscores (_), rather than periods.
- Show the data head.

## Handle deeply nested data
Last exercise, you flattened data nested down one level. Here, you'll unpack more deeply nested data.

The categories attribute in the Yelp API response contains lists of objects. To flatten this data, you'll employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the data frame. You should also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions. We'll work through this in steps.

pandas (as pd) and json_normalize() have been imported. JSON-formatted Yelp data on cafes in NYC is stored as data.
#### Instructions
- Use json_normalize() to flatten records under the businesses key in data, setting underscores (_) as separators.
- Specify the record_path to the categories data.
- Set the meta keyword argument to get business name, alias, rating, and the attributes nested under coordinates: latitude and longitude.
- Add "biz_" as a meta_prefix to prevent duplicate column names.

## Append data frames
In this exercise, you’ll practice appending records by creating a dataset of the 100 highest-rated cafes in New York City according to Yelp.

APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. The Yelp Business Search API limits the results returned in a call to 50 records. However, the offset parameter lets a user retrieve results starting after a specified number. By modifying the offset, we can get results 1-50 in one call and 51-100 in another. Then, we can append the data frames.

pandas (as pd), requests, and json_normalize() have been imported. The 50 top-rated cafes are already in a data frame, top_50_cafes
#### Instructions
- Add an "offset" parameter to params so that the Yelp API call will get cafes 51-100.
- Append the results of the API call to top_50_cafes, setting ignore_index so rows will be renumbered.
- Print the shape of the resulting data frame, cafes, to confirm there are 100 records.

## Merge data frames
In the last exercise, you built a dataset of the top 100 cafes in New York City according to Yelp. Now, you'll combine that with demographic data to investigate which neighborhood has the most good cafes per capita.

To do this, you'll merge two datasets with the DataFrame merge() method. The first,crosswalk, is a crosswalk between ZIP codes and Public Use Micro Data Sample Areas (PUMAs), which are aggregates of census tracts and correspond roughly to NYC neighborhoods. Then, you'll merge in pop_data, which contains 2016 population estimates for each PUMA.

pandas (as pd) has been imported, as has the cafes data frame from last exercise.
#### Instructions
- Use the DataFrame method to merge cafes and crosswalk on location_zip_code and zipcode, respectively. Assign the result to cafes_with_pumas.
- Merge pop_data into cafes_with_pumas on their puma fields. Save the result as cafes_with_pop.