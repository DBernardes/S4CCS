import os

import astropy.io.fits as fits
import numpy as np
import pandas as pd

from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (fix_image_orientation, format_string, prepare_json,
                   verify_file_already_exists)


def save_image(file, data, header_json):
    file = format_string(file)
    header_json, hdr = prepare_json(header_json)
    for cls in [Focuser, ICS, S4GUI, TCS, Weather_Station, General_KWs, CCD]:
        obj = cls(header_json, hdr)
        obj.fix_keywords()
        hdr = obj.hdr

    data = fix_image_orientation(hdr['CHANNEL'], data)
    file = verify_file_already_exists(file)
    fits.writeto(file, data, hdr, output_verify='fix')
    return


# path = os.path.join('tttrash', '20240213_s4c1_000001_zero.fitss')
# data = np.zeros((100, 100))
# save_image(path, data, header_json)
