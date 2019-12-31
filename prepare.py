import pandas as pd 

from os import path

import warnings
warnings.filterwarnings('ignore')


def prep_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date').set_index('date')
    df['calories_burned'] = df['calories_burned'].str.replace(',','')
    df['steps'] = df['steps'].str.replace(',','')
    df['minutes_sedentary'] = df['minutes_sedentary'].str.replace(',','')
    df['activity_calories'] = df['activity_calories'].str.replace(',','')
    df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']] = df[['calories_burned', 'steps', 'minutes_sedentary', 'activity_calories']].apply(pd.to_numeric)
    return df