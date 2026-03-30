import pandas as pd

def fix_date(df):
    '''
    Fixes and converts the date from my google sheets to datetime.
    '''
    regex_pattern = r'(\d{2})[.\s]?(\d{1,2})[.\s]?(\d{1,2})'
    extracted_date = df['date'].str.extract(regex_pattern)
    extracted_date.columns = ['year', 'month', 'day']
    df['clean_date'] = ("20" + 
                        extracted_date['year'] +
                        "-" + extracted_date['month'].str.zfill(2) + 
                        "-" + extracted_date['day'].str.zfill(2))
    df['date'] = df['clean_date']
    df['date'] = pd.to_datetime(df['date'])
    return df