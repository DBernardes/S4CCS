"""This file has all the functions needed to save the acquired images and to edit the image headers"""

import json
import os
from datetime import datetime, timezone

import astropy.io.fits as fits
import numpy as np
import pandas as pd

ss = pd.read_csv(os.path.join('csvs', 'header_content.csv'), delimiter='\t')
cards = [(keyword, 'Unknown', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]


def rotate_image(img_data, invert_x=False, invert_y=False, nrot90deg=0):
    """ Tool to fix image orientation of an image array.

    Parameters
    ----------
    img_data : numpy.ndarray (n x m)
        numpy array containing a 2D input image array
    invert_x : bool
        flip image array in the x (horizontal) direction
    invert_y : bool
        flip image array in the y (vertical) direction
    nrot90deg : int
        int to define the number of times image array is rotated by 90 deg counterclockwise

    Returns
    -------
    img_data : numpy.ndarray (n x m)
        numpy array containing the output 2D image array
    """
    if invert_x:
        img_data = np.fliplr(img_data)
    if invert_y:
        img_data = np.flipud(img_data)
    if nrot90deg != 0:
        img_data = np.rot90(img_data, k=nrot90deg)

    return img_data


def format_string(string):
    string = str(string)[2:-1]
    return string


def prepare_json(header_json):
    hdr = fits.Header(cards)
    header_json = format_string(header_json)
    try:
        header_json.replace('true', 'True')
    except:
        pass
    try:
        header_json.replace('false', 'False')
    except:
        pass
    header_json = json.loads(header_json)
    try:
        del header_json['cmd']
    except:
        pass
    for kw in hdr.keys():
        try:
            if header_json[kw] != "":
                hdr[kw] = header_json[kw]
        except:
            pass
    return header_json, hdr


def fix_image_orientation(channel, data):
    setup = {1: [False, True, 2],
             2: [False, False, 0],
             3: [True, False, -1],
             4: [False, False, -1]}
    invert_x, invert_y, nrot = setup[channel]
    return rotate_image(data, invert_x, invert_y, nrot)


def verify_file_already_exists(file):
    if os.path.isfile(file):
        now = datetime.now(timezone.utc)
        date_time = now.strftime("%Y%m%dT%H%M%S%f")
        image_name = file.split('_')
        img_index = image_name.pop()
        file = ''
        for value in image_name:
            file += value + '_'
        file += f'{date_time[:-4]}' + '_' + img_index
    return file
