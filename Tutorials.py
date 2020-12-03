import pandas as pd
from datetime import date
from getMaskData import getMaskData
from getCaseData import getCaseData
from getPopData import getPopData

# This file contains tutorials on how to use the three data retrieval modules included in this project
# These are: getMaskData, getCaseData and getPopData
# It is recommended that you run this file in debug mode if possible and place breakpoints on each line marked as
# debugLine


# getMaskData utilizes the COVIDcast API developed by Carnegie Mellon to import data based on a Facebook survey which
# indicates the percentage of people wearing masks in each state. getMaskData can take 2 inputs, start_date and end_date
# but neither input is required. The survey data begins on 8 September 2020 and as of this writing (3 December 2020),
# contains up-to-date surveys. If a start_date is input that is before the beginning of the survey, the module reverts
# the selection to 8 September 2020. The output is a pandas DataFrame with data from start_date to end_date
# The percentage of people wearing a mask in public is found in the 'value' column

# Examples: To get data for the month of October
maskDF = getMaskData(start_date=date(2020,10,1), end_date=date(2020,10,31))

print(maskDF)

debugLine = -1

# To get all data available, don't include inputs
maskDF = getMaskData()

print(maskDF)

debugLine = -1


# getCaseData downloads a CSV from the CDC website each time it is called and reads the entire CSV into a pandas
# DataFrame. It requires no inputs. Columns of interest in this DataFrame will be 'tot_cases' and 'new_case', but there
# is a lot of other information here. Programs can be created to look at other columns in this DataFrame. The submission
# date column can be used to compare with mask data retrieved using getMaskData

# Example
caseDF = getCaseData()

print(caseDF)

debugLine = -1



# getPopData reads a CSV that is included in the repository into a DataFrame. The module accepts an input of a string
# of the 2 letter abbreviation of each state (including DC). The input can be upper or lower case. The output is the
# the population of the input state.

# Examples:

AKpop = getPopData('ak')

print('The population of Alaska is: ', AKpop)

debugLine = -1

DCpop = getPopData('DC')

print('The population of Washington, D.C. is: ', DCpop)