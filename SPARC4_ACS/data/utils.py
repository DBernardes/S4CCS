"""This file has all the functions needed to save the acquired images and to edit the image headers"""

import numpy as np
import pandas as pd

values_parameters_ccd = {
    'readouts_em': [30, 20, 10, 1],
    'readouts_conv': [1, 0.1],
    'vsspeeds': [0.6, 1.13, 2.2, 4.33],
    'preamps': ['Gain 1', 'Gain 2'],
    'emmode': ['Electron Multiplying', 'Conventional'],
    'shutter_mode': ['Auto', 'Open', 'Closed'],
    'vertical_clock_amp': ['Normal', '+1', '+2', '+3', '+4'],
    'acquisition_mode': ['Single', 'Accumulate', "Kinetic"]
}


def fix_image_orientation(img_data, invert_x=False, invert_y=False, nrot90deg=0):
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


def reformat_string(string):
    string = str(string)[2:-1]
    return string


def find_index_tab(header_content):
    index = 2 * header_content['READRATE']
    if header_content['EMMODE'] == 1:
        index += 8
    index += header_content['PREAMP']
    return index


def get_ccd_gain(index, serial_number):
    ss = pd.read_csv('preamp_gains.csv')
    values = ss[str(serial_number)]
    ccd_gain = values[index]
    return ccd_gain


def get_read_noise(index, serial_number):
    ss = pd.read_csv('read_noises.csv')
    values = ss[str(serial_number)]
    ccd_gain = values[index]
    return ccd_gain
