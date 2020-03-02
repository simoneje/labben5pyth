import pandas as pd
import json
import requests
import csv, sys
import matplotlib.pyplot as plt
import numpy as np

# try:
#     jsonapi = requests.get('http://api.scb.se/OV0104/v1/doris/sv/ssd/START/TK/TK1001/TK1001A/PersBilarA')
#     data = jsonapi.json()
# except: print('error')
# try:
#     with open('data.json', 'w', encoding='utf-8') as datafil:
#         json.dump(data, datafil, ensure_ascii=False, indent=2)
# except: print('error2')
df_taxi = pd.read_csv('nytaxistat.csv', sep=';')
print(df_taxi.head(2))