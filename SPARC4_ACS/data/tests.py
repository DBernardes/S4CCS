import os
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time

from header import TCS, Weather_Station
from utils import prepare_json

header_json = {"broker": "Weather160", "version": "1.0.0", "date": "21/02/24", "hour": "10:50", "outTemp": "17.1", "hiTemp": "17.1", "lowTemp": "16.7", "outHumidity": "97", "dewOut": "16.6", "windSpeed": "12.9", "windDirection": "WNW", "windRun": "1.07", "hiSpeed": "22.5", "hiDir": "WNW", "windChill": "16.6", "heatIndex": "17.8", "THWIndex": "17.3", "THSWIndex": "---", "pressure": "753,8", "rain": "0.00", "rainRate": "0.0",
               "solarRad": "1120", "solarEnergy": "8.03", "hiSolarRad": "1120", "UVIndex": "8.3", "UVDose": "0.30", "hiUV": "9.7", "headDD": "0.004", "coolDD": "0.000", "inTemp": "22.2", "inHumidity": "69", "dewIn": "16.3", "inHeat": "22.5", "inEMC": "12.81", "inAirDensity": "1.1642", "2ndTemp": "19.4", "2ndHumidity": "73", "ET": "0.00", "leaf": "0", "windSamp": "115", "windTx": "1", "ISSRecept": "100.0", "arcInt": "5"}
ss = pd.read_csv(os.path.join('csvs', 'header_content.csv'), delimiter='\t')
cards = [(keyword, 'Unknown', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]

hdr = fits.Header(cards)
# del header_json['cmd']
for kw in hdr.keys():
    try:
        if header_json[kw] != "":
            hdr[kw] = header_json[kw]
    except:
        pass
night_dir = r'E:\images\today'
# header_json, hdr = prepare_json(header_json)
ccd = Weather_Station(header_json, hdr, night_dir)
ccd.fix_keywords()
