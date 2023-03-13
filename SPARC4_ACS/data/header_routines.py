import astropy.io.fits as fits
import pandas as pd
import json
import os
from datetime import datetime
from utils import get_read_noise, get_ccd_gain, reformat_string, find_index_tab, fix_image_orientation
from utils import values_parameters_ccd as vpc


ss = pd.read_csv('header_content.csv', delimiter='\t')
cards = [(keyword, '', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]


def save_image(file, data, channel_information):
    header_content = fits.Header(cards)
    file = reformat_string(file)
    channel_information = json.loads(reformat_string(channel_information))
    for key, value in channel_information.items():
        header_content[key] = value

    # ---------------------------------------------------
    header_content['OBSLONG'] = -45.5825
    header_content['OBSLAT'] = -22.53444444444445
    header_content['OBSALT'] = 1864.0
    # ---------------------------------------------------
    index = find_index_tab(header_content)
    header_content['GAIN'] = get_ccd_gain(index, header_content['SERN'])
    header_content['RDNOISE'] = get_read_noise(
        index, header_content['SERN'])
    header_content['INSTRUME'] = 'SPARC4'
    header_content['CYCLIND'] += 1
    # ---------------------------------------------------
    header_content['PREAMP'] = vpc['preamps'][header_content['PREAMP']]
    header_content['VSHIFT'] = vpc['vsspeeds'][header_content['VSHIFT']]

    header_content["READRATE"] = vpc['readouts_conv'][header_content['READRATE']]
    if header_content["EMMODE"] == 0:
        header_content["READRATE"] = vpc['readouts_em'][header_content['READRATE']]

    header_content['EMMODE'] = vpc['emmode'][header_content['EMMODE']]
    header_content['SHUTTER'] = vpc['shutter_mode'][header_content['SHUTTER']]
    header_content['VCLKAMP'] = vpc['vertical_clock_amp'][header_content['VCLKAMP']]
    header_content['ACQMODE'] = vpc['acquisition_mode'][header_content['ACQMODE'] - 1]

    header_content['FRAMETRF'] = 'OFF'
    if header_content['FRAMETRF']:
        header_content['FRAMETRF'] = 'ON'

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
            data, invert_x=True, invert_y=False, nrot90deg=1)
    elif header_content['CHANNEL'] == 4:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=1)
    else:
        raise ValueError(
            f'The provided channel does not exit: {header_content["CHANNEL"]}')
    # ---------------------------------------------------
    if os.path.isfile(file):
        now = datetime.utcnow()
        date_time = now.strftime("%Y%m%dT%H%M%S%f")
        image_name = file.split('_')
        img_index = image_name.pop()
        file = ''
        for value in image_name:
            file += value + '_'
        file += f'{date_time[:-4]}' + '_' + img_index

    fits.writeto(file, data, header_content)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
