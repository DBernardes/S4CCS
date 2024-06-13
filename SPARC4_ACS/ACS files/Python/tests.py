# import os
# from datetime import datetime

# import astropy.io.fits as fits
# import pandas as pd
# from astropy.time import Time
# from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
# from utils import (
#     WS_json,
#     ccd_kw,
#     everthing_json,
#     fix_ccd_parameters,
#     focuser_json,
#     general_kw,
#     ics_kw,
#     s4gui_json,
#     tcs_json,
#     test_json,
# )

# night_dir = r"C:\images\today"
# s4gui_json = {k.upper(): v for k, v in test_json.items()}
# s4gui_json = fix_ccd_parameters(s4gui_json)
# del s4gui_json["CMD"]
# s4gui_json["SHUTTER"] = "Closed"
# for cls in [CCD, TCS, Focuser, Weather_Station]:
#     tcs = cls(s4gui_json, night_dir)
#     tcs.fix_keywords()
#     # print(repr(tcs.json_string))
# # print(repr(tcs.hdr))

try:
    for i in range(10):
        print(i)
        try:
            raise ValueError("error")
        except:
            print("intermediate")
except:
    print("final")
