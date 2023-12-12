import pandas as pd
import json

def handler(event, context):
    data = {"name": "Pasha", "team": "fz"}

    df = pd.DataFrame(data)

    print(df)