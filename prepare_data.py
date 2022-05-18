import requests
import pandas as pd
from pandas import json_normalize
from constants import URL_GET_SV_CONTENTFUL, ORDERS_PATH, CLIENTS_PATH

pd.set_option('display.max_columns', None)

# Get the SV form Contentful DB 
def get_sv():
    response = requests.get(url = URL_GET_SV_CONTENTFUL)
    data = response.json()
    list_sv = data['items']
    df = json_normalize(list_sv)
    df = df.astype(str)
    df['fields.cedula'] = df['fields.cedula'].astype(int)
    return df

def get_orders():
    df = pd.read_excel(ORDERS_PATH)
    return df

def get_clients():
    df = pd.read_excel(CLIENTS_PATH)
    return df
