import os

import astropy.io.fits as fits
from header import CCD, ICS, S4GUI, TCS, Focuser, General_KWs, Weather_Station
from utils import (fix_image_orientation, format_string, load_json,
                   prepare_json, set_image_header, verify_file_already_exists)


def main(night_dir, file, data, header_json):
    file = format_string(file)
    night_dir = format_string(night_dir)
    file = os.path.join(night_dir, file)

    header_json = load_json(header_json)
    header_json = prepare_json(header_json)

    error_str = ''
    if hdr == {}:
        hdr = fits.Header()
        error_str = 'Warning: a wrong formatting was found in the header content.'
    else:
        for cls in [Focuser, ICS, S4GUI, TCS, Weather_Station, General_KWs, CCD]:
            obj = cls(header_json, night_dir)
            obj.fix_keywords()
            hdr = obj.hdr
        data = fix_image_orientation(hdr['CHANNEL'], data)

    file = verify_file_already_exists(file)
    fits.writeto(file, data, hdr, output_verify='fix')
    return error_str


# path = os.path.join('tttrash', '20240213_s4c1_000001_zero.fitss')
# data = np.zeros((100, 100))
# save_image(path, data, header_json)
