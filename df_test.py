"""
This module loads a public dataset into a dataframe, then tests the dataframe
according to the instructions given for DATA 515 HW2.

The dataset loaded is Seattle Real Time Fire 911 calls from:
https://data.seattle.gov/Public-Safety/Seattle-Real-Time-Fire-911-Calls/kzjm-xkqj

The tests are:
    The DataFrame contains only the columns that specified for the loaded data
    The columns contain the correct data type.
    There are at least 10 rows in the DataFrame

As specified in the assignment:
https://github.com/UWSEDS/hw2-using-functions-PKing70
"""
import pandas as pd

def test_create_dataframe(data, columns, types, rows_allowed):
    """
    Tests whether the data in a dataframe match the column name, data type,
    and row count constraints.

    Extended description of function.

    Parameters:
    data (pandas.dataframe): Data loaded from a publicdata source (911 CSV
    from data.seattle.gov, in this case).

    columns(list): The header columns expected from the given data.

    types(list): The data types (after loading from CSV) from the given data.

    row_allowed(int): A row count that the dataframe must equal or surpass.
    In this case, 10 is tested.

    Returns:
    Boolean: Whether data passes all tests.

    """
    passed = (sorted(data.columns.values.tolist()) == sorted(columns))
    if passed:
        passed = data.dtypes.tolist() == types
    if passed:
        passed = data.shape[0] >= rows_allowed
    return passed

DF = pd.read_csv('Seattle_Real_Time_Fire_911_Calls.csv', delimiter=',')
COLUMN_NAMES = DF.columns.values.tolist()
COLUMN_TYPES = DF.dtypes.tolist()
MAX_ROW_COUNT = 10

print(test_create_dataframe(DF, COLUMN_NAMES, COLUMN_TYPES, MAX_ROW_COUNT))
