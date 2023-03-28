import astropy.io.fits as fits
import pandas as pd
import json
import os
from datetime import datetime
from utils import get_read_noise, get_ccd_gain, reformat_string, find_index_tab, fix_image_orientation
from utils import values_parameters_ccd as vpc


ss = pd.read_csv('header_content.csv', delimiter='\t')
cards = [(keyword, 'Unknow', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]


def save_image(file, data, channel_information):
    hdr = fits.Header(cards)
    file = reformat_string(file)
    channel_information = json.loads(reformat_string(channel_information))
    for key, value in channel_information.items():
        if value == '':
            continue
        hdr[key] = value

    # ---------------------------------------------------
    hdr['OBSLONG'] = -45.5825
    hdr['OBSLAT'] = -22.53444444444445
    hdr['OBSALT'] = 1864.0
    # ---------------------------------------------------
    index = find_index_tab(hdr)
    hdr['GAIN'] = get_ccd_gain(index, hdr['SERN'])
    hdr['RDNOISE'] = get_read_noise(
        index, hdr['SERN'])
    hdr['INSTRUME'] = 'SPARC4'
    hdr['CYCLIND'] += 1
    hdr['SEQINDEX'] += 1
    if hdr['INSTMODE'] == 'Unknow':
        hdr['INSTMODE'] = 'PHOT'

    # ---------------------------------------------------
    hdr['PREAMP'] = vpc['preamps'][hdr['PREAMP']]
    hdr['VSHIFT'] = vpc['vsspeeds'][hdr['VSHIFT']]

    hdr["READRATE"] = vpc['readouts_conv'][hdr['READRATE']]
    if hdr["EMMODE"] == 0:
        hdr["READRATE"] = vpc['readouts_em'][hdr['READRATE']]

    hdr['EMMODE'] = vpc['emmode'][hdr['EMMODE']]
    hdr['SHUTTER'] = vpc['shutter_mode'][hdr['SHUTTER']]
    hdr['VCLKAMP'] = vpc['vertical_clock_amp'][hdr['VCLKAMP']]
    hdr['ACQMODE'] = vpc['acquisition_mode'][hdr['ACQMODE'] - 1]

    hdr['FRAMETRF'] = 'OFF'
    if hdr['FRAMETRF']:
        hdr['FRAMETRF'] = 'ON'

    # ---------------------------------------------------
    if hdr['TRIGGER'] == 0:
        hdr['TRIGGER'] = 'Internal'
    elif hdr['TRIGGER'] == 6:
        hdr['TRIGGER'] = 'External'
    else:
        hdr['TRIGGER'] = 'Uknown'
    # ---------------------------------------------------
    if hdr['COOLER'] == 0:
        hdr['COOLER'] = 'OFF'
    else:
        hdr['COOLER'] == 'ON'
    # ---------------------------------------------------
    if hdr['ACSMODE']:
        hdr['ACSMODE'] = 'Simulated'
    else:
        hdr['ACSMODE'] == 'Real'
    if hdr['OBSTYPE'] == '':
        hdr['OBSTYPE'] = 'NONE'
    # ---------------------------------------------------
    if hdr['TELFOCUS'] != 'Unknow':
        hdr['TELFOCUS'] = int(
            hdr['TELFOCUS'].replace('S', ''))
    if hdr['EXTTEMP'] != 'Unknow':
        hdr['EXTTEMP'] = float(
            hdr['EXTTEMP'].replace(',', '.'))
    if hdr['PRESSURE'] != 'Unknow':
        hdr['PRESSURE'] = float(
            hdr['PRESSURE'].replace(',', '.'))
    if hdr['HUMIDITY'] != 'Unknow':
        hdr['HUMIDITY'] = float(hdr['HUMIDITY'])
    if hdr['EQUINOX'] != 'Unknow':
        hdr['EQUINOX'] = float(hdr['EQUINOX'])
    # ---------------------------------------------------
    if hdr['WPSEL'] == 'Unknow':
        hdr['WPSEL'] = 'None'
    if hdr['CALW'] == 'Unknow':
        hdr['CALW'] = 'None'
    if hdr['ASEL']:
        hdr['ASEL'] = 'ON'
    else:
        hdr['ASEL'] = 'OFF'
    # ---------------------------------------------------
    if hdr['CHANNEL'] == 1:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=True, nrot90deg=0)
    elif hdr['CHANNEL'] == 2:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=2)
    elif hdr['CHANNEL'] == 3:
        data = fix_image_orientation(
            data, invert_x=True, invert_y=False, nrot90deg=1)
    elif hdr['CHANNEL'] == 4:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=1)
    else:
        raise ValueError(
            f'The provided channel does not exit: {hdr["CHANNEL"]}')
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

    fits.writeto(file, data, hdr)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
