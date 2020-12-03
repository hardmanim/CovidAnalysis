import pandas as pd
import requests
import io


def getCaseData():

    CSV_URL = 'https://data.cdc.gov/api/views/9mfq-cb36/rows.csv?accessType=DOWNLOAD'

    with requests.Session() as s:
        download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    caseDF = pd.read_csv(io.StringIO(decoded_content))

    return caseDF
