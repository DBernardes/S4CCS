import astropy.io.fits as fits
import pandas as pd
import json
import os
from datetime import datetime
from utils import get_read_noise, get_ccd_gain, reformat_string, find_index_tab, fix_image_orientation
from utils import values_parameters_ccd as vpc


ss = pd.read_csv('header_content.csv', delimiter='\t')
cards = [(keyword, 'Unknown', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]


def save_image(file, data, channel_information):
    hdr = fits.Header(cards)
    file = reformat_string(file)
    channel_information = json.loads(reformat_string(channel_information))
    for key, value in channel_information.items():
        if value == '':
            continue
        hdr[key] = value

    hdr['NAXIS'] = 2        
    # ---------------------------------------------------
    hdr['OBSLONG'] = -45.5825
    hdr['OBSLAT'] = -22.53444444444445
    hdr['OBSALT'] = 1864.0
    hdr['EQUINOX'] = 2000.0
    # ---------------------------------------------------
    index = find_index_tab(hdr)
    hdr['GAIN'] = get_ccd_gain(index, hdr['CCDSERN'])
    hdr['RDNOISE'] = get_read_noise(
        index, hdr['CCDSERN'])
    hdr['INSTRUME'] = 'SPARC4'
    hdr['CYCLIND'] += 1
    hdr['SEQINDEX'] += 1
    if hdr['INSTMODE'] == 'Unknown':
        hdr['INSTMODE'] = 'PHOT'

    # ---------------------------------------------------
    hdr['PREAMP'] = vpc['preamps'][hdr['PREAMP']]
    hdr['VSHIFT'] = vpc['vsspeeds'][hdr['VSHIFT']]

    if hdr["EMMODE"] == 0:
        hdr["READRATE"] = vpc['readouts_em'][hdr['READRATE']]
    else:
        hdr["READRATE"] = vpc['readouts_conv'][hdr['READRATE']]

    hdr['EMMODE'] = vpc['emmode'][hdr['EMMODE']]
    hdr['SHUTTER'] = vpc['shutter_mode'][hdr['SHUTTER']]
    hdr['VCLKAMP'] = vpc['vertical_clock_amp'][hdr['VCLKAMP']]
    hdr['ACQMODE'] = vpc['acquisition_mode'][hdr['ACQMODE'] - 1]

    if hdr['FRAMETRF']:
        hdr['FRAMETRF'] = True
    else:
        hdr['FRAMETRF'] = False

    # ---------------------------------------------------
    if hdr['TRIGGER'] == 0:
        hdr['TRIGGER'] = 'Internal'
    elif hdr['TRIGGER'] == 6:
        hdr['TRIGGER'] = 'External'
    else:
        hdr['TRIGGER'] = 'Uknown'
    # ---------------------------------------------------
    if hdr['COOLER']:
        hdr['COOLER'] = True
    else:
        hdr['COOLER'] = False
    # ---------------------------------------------------
    if hdr['OBSTYPE'] == 'Unknown':
        hdr['OBSTYPE'] = 'OBJECT'
    # ---------------------------------------------------
    tel_focus = hdr['TELFOCUS']
    if tel_focus != 'Unknown':
        if 'S' in tel_focus:
            tel_focus = int(tel_focus.replace('S', ''))
        elif 'M' in tel_focus:
            tel_focus = int(tel_focus.replace('M', ''))
        else:
            pass
        hdr['TELFOCUS'] = tel_focus
    if hdr['EXTTEMP'] != 'Unknown':
        hdr['EXTTEMP'] = float(
            hdr['EXTTEMP'].replace(',', '.'))
    if hdr['PRESSURE'] != 'Unknown':
        hdr['PRESSURE'] = float(
            hdr['PRESSURE'].replace(',', '.'))
    if hdr['HUMIDITY'] != 'Unknown':
        hdr['HUMIDITY'] = float(hdr['HUMIDITY'])
    if hdr['EQUINOX'] != 'Unknown':
        hdr['EQUINOX'] = float(hdr['EQUINOX'])
    if hdr['AIRMASS'] != 'Unknown':
        hdr['AIRMASS'] = float(hdr['AIRMASS'])
    if hdr['TCSDATE'] != 'Unknown':
        tmp = hdr['TCSDATE'].split('/')
        hdr['TCSDATE'] = f"{hdr['UTDATE'][:2]}{tmp[2][:2]}-{tmp[1]}-{tmp[0]}T{tmp[2][3:]}"
        
    # ---------------------------------------------------
    if hdr['WPSEL'] == 'Unknown':
        hdr['WPSEL'] = 'NONE'
    if hdr['CALW'] == 'Unknown':
        hdr['CALW'] = 'NONE'
    if hdr['ASEL']:
        hdr['ASEL'] = True
    else:
        hdr['ASEL'] = False
    # ---------------------------------------------------
    if hdr['CHANNEL'] == 1:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=True, nrot90deg=2)
    elif hdr['CHANNEL'] == 2:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=0)
    elif hdr['CHANNEL'] == 3:
        data = fix_image_orientation(
            data, invert_x=True, invert_y=False, nrot90deg=-1)
    elif hdr['CHANNEL'] == 4:
        data = fix_image_orientation(
            data, invert_x=False, invert_y=False, nrot90deg=-1)
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

    fits.writeto(file, data, hdr, output_verify='fix')
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
