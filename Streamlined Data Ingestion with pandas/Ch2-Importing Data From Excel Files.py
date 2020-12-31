#Chapter 2 - Importing Data From Excel Files

#Get data from a spreadsheet
# Load pandas as pd
import pandas as pd

# Load matplotlib as plt
import matplotlib.pyplot as plt

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx" , skiprows=2)

# View the head of the data frame
print(survey_responses.head())
print("=========================================================")


#Load a portion of a spreadsheet
# Create string of lettered columns to load
col_string = 'AD:AW,BA'

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                        skiprows=2,
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)
print("=========================================================")


#Select a single sheet
# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                               skiprows=2,
                               sheet_name='2017')
# responses_2017 = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
#                                skiprows=2,
#                                sheet_name=1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
print("Plot")
print("=========================================================")


#Select multiple sheets
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                                sheet_name=['2016','2017'])

# View the data type of all_survey_data
print(type(all_survey_data))

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                                sheet_name=[0,'2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                                sheet_name=None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())
print("=========================================================")


#Work with multiple spreadsheets
# Create an empty data frame
all_responses = pd.DataFrame()
responses = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                                skiprows=2,
                                sheet_name=None)
# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()
print("=========================================================")


#Set Boolean columns
# Load the data
col_string = ["ID.x" , "AttendedBootcamp","HasDebt" ,"HasFinancialDependents", "HasHomeMortgage", "HasStudentDebt"]
survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                            skiprows=2,
                            nrows=5,
                            usecols=col_string)

# Count NA values in each column
print(survey_data.isna().sum())
# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                            skiprows=2,
                            nrows=5,
                            dtype={"HasDebt": bool},
                            usecols=col_string
                            )

# View financial burdens by Boolean group
print(survey_data.groupby("HasDebt").sum())
print("=========================================================")


#Set custom true/false values
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                              nrows=5,
                              skiprows=2,
                              dtype={"HasDebt": bool,"AttendedBootcamp": bool},
                              false_values=["No",""],
                              true_values=['Yes'],
                              usecols=col_string)

# View the data
print(survey_subset.head())
print("=========================================================")


#Parse simple dates
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                              nrows=5,
                              skiprows=2,
                              parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())
print("=========================================================")


#Get datetimes from multiple columns
# Create dict of columns to combine into new datetime column
datetime_cols = {"PartStartEnd": ["Part2StartTime","Part1EndTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                              nrows=5,
                              skiprows=2,
                              parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.PartStartEnd.describe())
print("=========================================================")


#Parse non-standard date formats

survey_data = pd.read_excel("Datasets/fcc-new-coder-survey.xlsx",
                              nrows=5,
                              skiprows=2,
                              parse_dates=datetime_cols)
# Parse datetimes and assign result back to Part2EndTime
format_string = "%m%d%Y %H:%M:%S"
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],format=format_string)
# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())
print("=========================================================")