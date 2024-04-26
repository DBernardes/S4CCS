import os
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time
from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (WS_json, ccd_kw, focuser_json, general_kw, ics_kw,
                   prepare_json, s4gui_json, tcs_json)

# for kw in general_kw.keys():
#     print(f'({kw},{kw}),')
night_dir = r'E:\images\today'
s4gui_json = {k.upper(): v for k, v in general_kw.items()}
tcs = General_KWs(s4gui_json, night_dir)
tcs.fix_keywords()
print(repr(tcs.json_string))
print(repr(tcs.hdr))
