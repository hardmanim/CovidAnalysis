import pandas as pd


def getPopData(state):

    # Map state abbreviations (which is what is provided as the input) to the state name
    stateAbbrs = {'ak':'Alaska', 'al':'Alabama', 'ar':'Arkansas', 'az':'Arizona', \
                  'ca':'California', 'co':'Colorado', 'ct':'Connecticut', 'de':'Delaware', \
                  'fl':'Florida', 'ga':'Georgia', 'hi':'Hawaii', 'ia':'Iowa', 'id':'Idaho', \
                  'il':'Illinois', 'in':'Indiana', 'ks':'Kansas', 'ky':'Kentucky', \
                  'la':'Louisiana', 'ma':'Massachusetts', 'md':'Maryland', 'me':'Maine', \
                  'mi':'Michigan', 'mn':'Minnesota', 'mo':'Missouri', 'ms':'Mississippi', \
                  'mt':'Montana', 'nc':'North Carolina', 'ne':'Nebraska', 'nh':'New Hampshire', \
                  'nj':'New Jersey', 'nm':'New Mexico', 'nv':'Nevada', 'ny':'New York', \
                  'oh':'Ohio', 'ok':'Oklahoma', 'or':'Oregon', 'pa':'Pennsylvania', \
                  'sc':'South Carolina', 'tn':'Tennessee', 'tx':'Texas', 'ut':'Utah', \
                  'va':'Virginia', 'wa':'Washington', 'wi':'Wisconsin', 'wv':'West Virginia', \
                  'dc':'District of Columbia', 'nd':'North Dakota', 'ri':'Rhode Island', \
                  'sd':'South Dakota', 'vt':'Vermont', 'wy':'Wyoming'}

    stateName = str(stateAbbrs[state])

    popDF = pd.read_csv('csvData.csv')

    popDF.set_index('State', inplace=True)

    population = popDF.loc[stateName, 'Pop']

    return population
