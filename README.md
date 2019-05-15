# HW2 - Using Functions

##### Final grade: 7/7  

Grade: 6/7    

-1: passed = data.dtypes.tolist() == types will return False even if all the columns are there but are in a different order

-----

Create a python module (a file with extension ‘.py’) with the following functions:

1. (4 points) Find an on-line data source (e.g., from data.gov). Write python codes that read the on-line file and create a data frame that has at least 3 columns.

1. (3 points) Create the function test_create_dataframe that takes a pandas DataFrame as input and returns True if the following conditions hold:

   1. The DataFrame contains only the columns that you specified in #1.
   1. The columns contain the correct data type
   1. There are at least 10 rows in the DataFrame.

## Usage

This project contains

* df_test.py
* Seattle_Real_Time_Fire_911_Calls.csv

Run 'Python df_test.py' to execute the module to load the dataframe from the datasource (Seattle_Real_Time_Fire_911_Calls.csv from https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj
