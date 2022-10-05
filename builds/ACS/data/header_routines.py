from email import header
import astropy.io.fits as fits
import numpy as np
import pandas as pd
import os
import json


def write_header(file, header_content):
    new_header = fits.PrimaryHDU().header
    header_content = np.asarray(header_content)
    for line in header_content:
        line = [reformat_string(value) for value in line]
        keyword, _type, value, comment = line[0], line[1], line[2], line[3]
        if _type == "INTERGER":
            value = int(value)
        elif _type == "FLOAT":
            try:
                value = float(value)
            except:
                value = float(value.replace(',', '.'))
        elif _type == "BOOLEAN":
            value = bool(value)
        else:
            pass
        new_header[keyword] = (value, comment)
    file = reformat_string(file)
    temp_file = file.split('.fits')[0] + '_temp.fits'
    data = fits.getdata(temp_file)
    fits.writeto(file, data, new_header, overwrite=True)
    os.remove(temp_file)
    return


def reformat_string(string):
    string = str(string)[2:-1]
    return string


def save_image(file, data, header_content):
    file = reformat_string(file)
    header_content = fits.Header(
        cards=json.loads((reformat_string(header_content))))
    fits.writeto(file, data, header_content, overwrite=True)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
