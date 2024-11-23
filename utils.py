import pandas as pd
import os

LISTING_FILE = 'data/listings 2 reduced.csv'
REVIEW_FILE = 'data/reviews 2 reduced.csv'

def load_file(file_to_load = str, data_columns = list(), format_price = False )-> pd.DataFrame:
    try:
        data = pd.read_csv(file_to_load)
        data = data[data_columns]
        if format_price: data['price'] = data['price'].str.replace('[\$,]','', regex=True).astype(float)
        return data
    except:
        raise