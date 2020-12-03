import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from getCaseData import getCaseData
from getMaskData import getMaskData
from getPopData  import getPopData
import warnings

# Flag to open all figures created (51 state data including DC) plus the scatter plot
showPlots = True

# Filter out warnings from Pandas about copying to a slice of a DataFrame and from pyplot about opening too many figures
warnings.filterwarnings(action="ignore", category=RuntimeWarning)
pd.options.mode.chained_assignment = None

# Get the DataFrames that contain the data
maskDF = getMaskData()
caseDF = getCaseData()

# Format the case data correctly and sort mask data by state (sorting isn't necessary but I did it for debugging
# purposes)
caseDF['submission_date'] = pd.to_datetime(caseDF['submission_date'], format='%m/%d/%Y')
caseDF = caseDF.loc[caseDF['submission_date'] >= maskDF['time_value'].min()]
stateList = pd.unique(maskDF['geo_value'])
maskDF = maskDF.loc[maskDF['time_value'] <= caseDF['submission_date'].max()]
maskDF.sort_values("geo_value", inplace=True)

print("Showing statistics from ", maskDF['time_value'].min().strftime("%m/%d/%Y"), " to ", \
      maskDF['time_value'].max().strftime("%m/%d/%Y"))

maskMeans = []
caseMeans = []

# Loop through every state
for state in stateList:

    # Get the state population so we can look at cases per capita
    statePop = getPopData(state)
    stateMaskData = maskDF.loc[maskDF['geo_value'] == state]
    stateMaskData.sort_values("time_value", inplace=True)
    stateCaseData = caseDF.loc[caseDF['state'] == state.upper()]
    stateCaseData.sort_values("submission_date", inplace=True)
    stateCaseData = stateCaseData.loc[stateCaseData['submission_date'] >= stateMaskData['time_value'].min()]

    # Set up plot: We will plot mask use, total cases per capita, new cases per capita, and correlation over the time period
    fig, axs = plt.subplots(2,2, figsize=(20,20))
    axs[0,0].plot(stateMaskData['time_value'], stateMaskData['value'], 'b-')
    axs[0,0].set(ylabel='Percentage of People Wearing a Mask in Public', xlabel='Date')
    axs[0,1].plot(stateCaseData['submission_date'], stateCaseData['tot_cases']/statePop, 'r-')
    axs[0,1].set(ylabel='Number of Cases per Capita', xlabel='Date')
    axs[1,0].plot(stateCaseData['submission_date'], stateCaseData['new_case']/statePop, 'm-')
    axs[1,0].set(ylabel='Number of New Cases per Capita', xlabel='Date')

    # Check out the correlation between cases and mask use
    N = len(stateCaseData.index)
    k = np.arange(-N + 1, N, 1)
    maskMean = np.mean(stateMaskData['value'].values)
    caseMean = np.mean(stateCaseData['tot_cases'].values/statePop)

    maskMeans.append(maskMean)
    caseMeans.append(caseMean)
    maskDetrend = stateMaskData['value'].values-maskMean
    caseDetrend = stateCaseData['tot_cases'].values-caseMean

    corrVals = np.correlate(maskDetrend, caseDetrend, mode='full')

    axs[1,1].plot(k, corrVals, 'k-')
    axs[1,1].set(xlabel='Lag (k)', ylabel='Cross-Correlation (Mask Use vs. Total Cases per Capita)')

    plt.suptitle(state.upper())
    plt.savefig(state + '.png')

    if showPlots:
        plt.show(block=True)

# Let's look at what all the means look like in a scatter
fig2 = plt.figure()
plt.scatter(maskMeans, caseMeans, s=10, marker='.')
plt.title('Mean Percentage of Public Mask Use vs. Mean Number of Cases per Capita')
plt.xlabel('Mean Percentage of Mask Use')
plt.ylabel('Mean Cases per Capita')
fig2.savefig('MaskUse-CasePerCapita.png')

if showPlots:
    fig2.show()
