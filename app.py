# https://www.youtube.com/watch?v=3CcGtRidF9c

import pandas as pd
import json

def handler(event, context):
    data = {"name": "Pasha", "team": "fz"}


    print('[INFO] TABLE CREATED.')
    df = pd.DataFrame(data)

    print(df)