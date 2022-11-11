import astropy.io.fits as fits
import pandas as pd
import json

readouts_em = ['30', '20', '10', '1']
readouts_conv = ['1', '0.1']
vsspeeds = ['0.6', '1.13', '2.2', '4.33']
preamps = ['Gain 1', 'Gain 2']
emmode = ['Electron Multiplying', 'Conventional']
shutter_mode = ['Auto', 'Open', 'Closed']
vertical_clock_amp = ['Normal', '+1', '+2', '+3', '+4']
acquisition_mode = ['Single', 'Accumulate', "Kinetic"]


ss = pd.read_csv('header_content.csv', delimiter='\t')
cards = [(keyword, '', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]
# header_content = fits.Header(cards)


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
    index = find_index_tab(header_content)
    header_content['GAIN'] = get_ccd_gain(index, header_content['SERN'])
    header_content['RDNOISE'] = get_read_noise(
        index, header_content['SERN'])

    header_content['PREAMP'] = preamps[header_content['PREAMP']]
    header_content['VSHIFT'] = vsspeeds[header_content['VSHIFT']] + ' usec'
    if header_content["EMMODE"] == 0:
        header_content["READRATE"] = readouts_em[header_content['READRATE']] + ' MHz'
    else:
        header_content["READRATE"] = readouts_conv[header_content['READRATE']] + ' MHz'
    header_content['EMMODE'] = emmode[header_content['EMMODE']]
    header_content['SHUTTER'] = shutter_mode[header_content['SHUTTER']]
    header_content['VCLKAMP'] = vertical_clock_amp[header_content['VCLKAMP']]
    header_content['ACQMODE'] = acquisition_mode[header_content['ACQMODE'] - 1]
    if header_content['TRIGGER'] == 0:
        header_content['TRIGGER'] = 'Internal'
    else:
        header_content['TRIGGER'] == 'External'
    if header_content['COOLER'] == 0:
        header_content['COOLER'] = 'OFF'
    else:
        header_content['COOLER'] == 'ON'
    if header_content['ACSMODE']:
        header_content['ACSMODE'] = 'Simulated'
    else:
        header_content['ACSMODE'] == 'Real'
    header_content['CYCLIND'] += 1

    # fazer um IF

    fits.writeto(file, data, header_content)
    return


# csv_path = r'C:\Users\observer\Desktop\SPARC4_ACS\SPARC4_ACS\Spreadsheets\header_content.csv'
# ss = pd.read_csv(csv_path, sep='\t')
# write_header('a', ss)
