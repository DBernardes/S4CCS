import os
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time

from header import S4GUI, TCS, Focuser, Weather_Station
from utils import WS_json, focuser_json, prepare_json, s4gui_json, tcs_json

ss = pd.read_csv(os.path.join('csvs', 'header_content.csv'), delimiter='\t')
cards = [(keyword, 'Unknown', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]

hdr = fits.Header(cards)
del focuser_json['cmd']

night_dir = r'E:\images\today'
# header_json, hdr = prepare_json(s4gui_json)
ccd = S4GUI(s4gui_json, hdr, night_dir)
ccd.fix_keywords()
print(ccd.hdr)
