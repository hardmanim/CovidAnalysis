import covidcast
from datetime import date
from datetime import timedelta


def getMaskData(start_date=date(2020, 9, 8), end_date=date.today()-timedelta(days=1)):

    if start_date < date(2020, 9, 8):
        start_date = date(2020, 9, 8)
        print("Mask data not available before 8 Sept 2020.")

    maskDF = covidcast.signal(data_source="fb-survey", signal="smoothed_wearing_mask", geo_type='state',
                              start_day=start_date, end_day=end_date)
    return maskDF
