# This script downloads data from ACLED and saves the data in a .csv file

# Libraries
import requests
import numpy as np
import pandas as pd
import time
import yaml
import os

# Variables to download from ACLED
acled_vars = ['year', 'event_date', 'event_type', 'country', 'region', 'longitude', 'latitude', 'fatalities', 'notes',
              'geo_precision', 'time_precision', 'inter1', 'inter2', 'source_scale']


def acled_api():
    """Load Data Sets from ACLED API

      Output:
          - acled_hist: downloaded data set
      """
    api_key, email = api_access_tokens()
    appended_data = []
    event_list = ['battle', 'explosions/remote violence', 'violence against civilians', 'protests', 'riots',
                  'strategic developments']
    for event in event_list:
        acled_url = f"https://api.acleddata.com/acled/read?key={api_key}&email={email}&terms=accept&event_type={event}"\
                f"&limit=0"
        r_acled = requests.get(acled_url).json()
        acled_temp = pd.DataFrame(r_acled['data'])
        appended_data.append(acled_temp)
    acled_hist = pd.concat(appended_data)
    return acled_hist


def data_loader_acled(acled_var_set):
    """
    Load ACLED data and add prio grid.

    Output:
          - df_acled_all: ACLED data set
    """

    # Load ACLED Data
    df_acled_all = acled_api()

    # Only take variables of interest
    df_acled = df_acled_all[acled_var_set].copy()

    # Create the new prio grid column according to UCDP transformation
    df_acled['prio_grid'] = ((90 + ((df_acled['latitude'].astype('float') * 2).apply(np.floor) / 2)) * 2 + 1 - 1) * \
        720 + (180 + ((df_acled['longitude'].astype('float') * 2).apply(np.floor) / 2)) * 2 + 1
    # Save as csv
    os.makedirs('data', exist_ok=True)  # make data directory if not exists
    df_acled.to_csv('data/ACLED_data.csv')

    return print('Done!')


def api_access_tokens():
    """
    Load api access key and username from auth.yaml.
    To obtain auth.yaml, contact Adrian Ochs.

    :return:
    - api_key (str): the api access key
    - api_user (str): user name for api
    """
    ACLED_CONFIG_FILE = 'auth.yaml'

    with open(ACLED_CONFIG_FILE, 'r') as config_file:
        config = yaml.full_load(config_file)

    api_key_ = config['acled']['api_key']
    api_user_ = config['acled']['api_user']

    return api_key_, api_user_


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Downloading ACLED Data')
    start = time.time()
    data_loader_acled(acled_vars)
    end = time.time()
    seconds = end - start
    minutes = round(seconds/60, 1)
    print(f"It took {minutes} minutes.")
