import astropy.io.fits as fits
import numpy as np
import pandas as pd
import os


def write_header(file, header_content):
    header_content = np.asarray(header_content)
    file = reformat_string(file)
    with fits.open(file, mode='update') as hdu:
        for line in header_content:
            line = [reformat_string(value) for value in line]
            keyword, _type, value, comment = line[0], line[1], line[2], line[3]
            if _type == "INTERGER":
                value = int(value)
            elif _type == "FLOAT":
                value = float(value)
            elif _type == "BOOLEAN":
                value = bool(value)
            else:
                1
            hdu[0].header[keyword] = (value, comment)
    return


def write_header_1(file, header_content):
    header_content = np.asarray(header_content)
    file = reformat_string(file)
    with fits.open(file, mode='update') as hdu:
        for i in range(np.shape(header_content)[0]):
            line = [reformat_string(value) for value in header_content[i]]
            _type = line[1]
            card = tuple(np.delete(line, 1))
            hdu[0].header.append(card)
    return


def reformat_string(string):
    string = str(string)[2:-1]
    return string


def save_image(file, data):
    file = reformat_string(file)
    fits.writeto(file, data, overwrite=True)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
