import os
import pandas as pd
import math
import numpy as np


csv_path = os.path.join('csvs', 'header_content.csv')
ss = pd.read_csv(csv_path, delimiter=';', keep_default_na=False)
cards = [(keyword, '', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]

keyword_types = {k:v for (k,v) in zip(ss['Keyword'], ss['Type'])}
expected_kw_names = {k:v for (k,v) in zip(ss['Keyword'], ss['Expected name'])}
gains = pd.read_csv(os.path.join('csvs', 'preamp_gains.csv'))
read_noise = pd.read_csv(os.path.join('csvs', 'read_noises.csv'))

allowed_kw_values = {k:v for (k,v) in zip(ss['Keyword'], ss['Allowed values'])}
for kw,values in allowed_kw_values.items():    
    if values != '' and keyword_types[kw] in ['interger', 'float', 'string']:
        allowed_kw_values[kw] = allowed_kw_values[kw].split(',')

print(allowed_kw_values)