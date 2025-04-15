import os
import traceback

import astropy.io.fits as fits
import numpy as np
from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (
    fix_image_orientation,
    sub_systems,
    verify_file_already_exists,
    write_error_log,
)


def main(night_dir, file, data, tuple_header_jsons, log_file):
    try:
        dict_header_jsons = {k: v for (k, v) in zip(sub_systems, tuple_header_jsons)}
        data = np.asarray(data)
        file = os.path.join(night_dir, file)

        for cls in [Focuser, ICS, S4GUI, TCS, Weather_Station, General_KWs, CCD]:
            obj = cls(dict_header_jsons, log_file)
            obj.fix_keywords()
            hdr = obj.hdr
        data = fix_image_orientation(hdr["CHANNEL"], hdr["EMMODE"], data)
        file = verify_file_already_exists(file)
        fits.writeto(file, data, hdr, output_verify="ignore")
        return 0
    except Exception as e:
        write_error_log(traceback.format_exc(), log_file)
        return 1
