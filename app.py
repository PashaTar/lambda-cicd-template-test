# https://www.youtube.com/watch?v=3CcGtRidF9c
# https://www.youtube.com/watch?v=6SSLBfOZOtQ
# https://www.youtube.com/watch?v=C99ps_cWp9Y&t=132s ++

import pandas as pd
import json

def handler(event, context):
    data = {"name": "Pasha", "team": "fz"}


    print('[INFO] TABLE CREATED.')
    df = pd.DataFrame(data, index=[0])

    print(df)