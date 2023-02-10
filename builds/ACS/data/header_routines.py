import astropy.io.fits as fits
import pandas as pd
import json
import os
from datetime import datetime
import numpy as np

readouts_em = [30, 20, 10, 1]
readouts_conv = [1, 0.1]
vsspeeds = [0.6, 1.13, 2.2, 4.33]
preamps = ['Gain 1', 'Gain 2']
emmode = ['Electron Multiplying', 'Conventional']
shutter_mode = ['Auto', 'Open', 'Closed']
vertical_clock_amp = ['Normal', '+1', '+2', '+3', '+4']
acquisition_mode = ['Single', 'Accumulate', "Kinetic"]


ss = pd.read_csv('header_content.csv', delimiter='\t')
cards = [(keyword, '', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]


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


def save_image(file, data, channel_information):
    header_content = fits.Header(cards)
    file = reformat_string(file)
    channel_information = json.loads(reformat_string(channel_information))
    for key, value in channel_information.items():
        header_content[key] = value
    # ---------------------------------------------------
    index = find_index_tab(header_content)
    header_content['GAIN'] = get_ccd_gain(index, header_content['SERN'])
    header_content['RDNOISE'] = get_read_noise(
        index, header_content['SERN'])
    # ---------------------------------------------------
    header_content['PREAMP'] = preamps[header_content['PREAMP']]
    header_content['VSHIFT'] = vsspeeds[header_content['VSHIFT']]
    if header_content["EMMODE"] == 0:
        header_content["READRATE"] = readouts_em[header_content['READRATE']]
    else:
        header_content["READRATE"] = readouts_conv[header_content['READRATE']]
    header_content['EMMODE'] = emmode[header_content['EMMODE']]
    header_content['SHUTTER'] = shutter_mode[header_content['SHUTTER']]
    header_content['VCLKAMP'] = vertical_clock_amp[header_content['VCLKAMP']]
    header_content['ACQMODE'] = acquisition_mode[header_content['ACQMODE'] - 1]
    header_content['CYCLIND'] += 1
    header_content['INSTRUME'] = 'SPARC4'
    # ---------------------------------------------------
    if header_content['TRIGGER'] == 0:
        header_content['TRIGGER'] = 'Internal'
    elif header_content['TRIGGER'] == 6:
        header_content['TRIGGER'] = 'External'
    else:
        header_content['TRIGGER'] = 'Uknown'
    # ---------------------------------------------------
    if header_content['COOLER'] == 0:
        header_content['COOLER'] = 'OFF'
    else:
        header_content['COOLER'] == 'ON'
    # ---------------------------------------------------
    if header_content['ACSMODE']:
        header_content['ACSMODE'] = 'Simulated'
    else:
        header_content['ACSMODE'] == 'Real'
    if header_content['OBSTYPE'] == '':
        header_content['OBSTYPE'] = 'NONE'
    # ---------------------------------------------------
    if header_content['TELFOCUS'] != '':
        header_content['TELFOCUS'] = int(
            header_content['TELFOCUS'].replace('S', ''))
    if header_content['EXTTEMP'] != '':
        header_content['EXTTEMP'] = float(
            header_content['EXTTEMP'].replace(',', '.'))
    if header_content['PRESSURE'] != '':
        header_content['PRESSURE'] = float(
            header_content['PRESSURE'].replace(',', '.'))
    if header_content['HUMIDITY'] != '':
        header_content['HUMIDITY'] = float(header_content['HUMIDITY'])
    if header_content['EQUINOX'] != '':
        header_content['EQUINOX'] = float(header_content['EQUINOX'])
    # ---------------------------------------------------
    if header_content['CHANNEL'] == 1:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=True, nrot90deg=0)
    elif header_content['CHANNEL'] == 2:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=2)
    elif header_content['CHANNEL'] == 3:
        data = fix_image_orientation(
            data, invert_x=True, invert_y=False, nrot90deg=3)
    elif header_content['CHANNEL'] == 4:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=3)
    else:
        raise ValueError(
            f'The provided channel does not exit: {header_content["CHANNEL"]}')
    # ---------------------------------------------------
    if os.path.isfile(file):
        now = datetime.utcnow()
        date_time = now.strftime("%Y%m%dT%H%M%S%f")
        file = file.replace('.fits', f'_{date_time[:-4]}.fits')
    fits.writeto(file, data, header_content)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
