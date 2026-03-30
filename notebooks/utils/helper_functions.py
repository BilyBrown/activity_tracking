import pandas as pd
import re

def fix_date(date_val):
    '''
    Fixes and converts the date from my google sheets to datetime.
    '''
    if isinstance(date_val, str):
        regex_pattern = r'(\d{2})[.\s]?(\d{1,2})[.\s]?(\d{1,2})'
        match = re.search(regex_pattern, str(date_val))

        if match:
            year, month, day = match.groups()
            clean_date = f"20{year}-{month.zfill(2)}-{day.zfill(2)}"
            clean_date = pd.to_datetime(clean_date)
            return clean_date
    else:
        return "bugger"
    