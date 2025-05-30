import json
import os
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time
from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (
    WS_json,
    ccd_kw,
    everthing_json,
    focuser_json,
    general_kw,
    ics_kw,
    s4gui_json,
    tcs_json,
    test_json,
)

dicts = {
    # "CCD": ccd_kw,
    # "WSTATION": WS_json,
    # "FOCUSER": focuser_json,
    "GENERAL KW": general_kw,
    # "S4ICS": ics_kw,
    # "TCS": tcs_json,
    # "S4GUI": s4gui_json,
}

dicts = {k: json.dumps(v) for (k, v) in dicts.items()}
night_dir = "C:\\images\\today"
for cls in [General_KWs]:
    tcs = cls(dicts, night_dir)
    tcs.fix_keywords()

