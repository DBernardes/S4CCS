import os

import astropy.io.fits as fits
import numpy as np
from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (
    fix_image_orientation,
    load_json,
    sub_systems,
    verify_file_already_exists,
    write_error_log,
)


def main(night_dir, file, data, tuple_header_jsons):
    try:
        dict_header_jsons = {k: v for (k, v) in zip(sub_systems, tuple_header_jsons)}
        data = np.asarray(data)
        file = os.path.join(night_dir, file)
        for cls in [Focuser, ICS, S4GUI, TCS, Weather_Station, General_KWs, CCD]:
            obj = cls(dict_header_jsons, night_dir)
            obj.fix_keywords()
            hdr = obj.hdr
        data = fix_image_orientation(hdr["CHANNEL"], hdr["EMMODE"], data)
        file = verify_file_already_exists(file)
        fits.writeto(file, data, hdr, output_verify="ignore")
        return 0
    except Exception as e:
        write_error_log(repr(e), night_dir)
        return 1


def main_1(night_dir, file, data, header_json):
    data = np.asarray(data)
    file = os.path.join(night_dir, file)
    header_json = load_json(header_json)

    if header_json == None:
        hdr = fits.Header()
        error_str = "[WARNNING] A wrong formatting was found for the header content."
        write_error_log(error_str, night_dir)
    else:
        for cls in [Focuser, ICS, S4GUI, TCS, Weather_Station, General_KWs, CCD]:
            obj = cls(header_json, night_dir)
            obj.fix_keywords()
            hdr = obj.hdr
        try:
            data = fix_image_orientation(hdr["CHANNEL"], hdr["EMMODE"], data)
        except Exception as e:
            write_error_log(repr(e), night_dir)

    file = verify_file_already_exists(file)
    fits.writeto(file, data, hdr, output_verify="ignore")
    return
