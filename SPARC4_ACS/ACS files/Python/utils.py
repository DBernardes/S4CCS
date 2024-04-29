"""This file has all the functions needed to save the acquired images and to edit the image headers"""

import json
import os
import warnings
from datetime import datetime, timezone

import astropy.io.fits as fits
import numpy as np
import pandas as pd


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


def load_json(header_json):
    header_json = format_string(header_json)
    header_json.replace("true", "True")
    header_json.replace("false", "False")
    try:
        header_json = json.loads(header_json)
        header_json = {k.upper(): v for k, v in header_json.items()}
        if 'cmd' in header_json.keys():
            del header_json['cmd']
        return header_json
    except:
        return None


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


def write_error_log(message, night_dir):
    log_file = os.path.join(night_dir, 'acs_errors.log')
    with open(log_file, 'a') as file:
        now = str(datetime.now())
        file.write(now + ' - ' + message + '\n')

# --------------------------------------------------------------------------------------------------------------------------


tcs_json = {
    "broker": "TCSPD160",
    "version": "20240131",
    "cmd": "",
    "objectName": "NO_OBJ",
    "raAcquis": "03:19:21",
    "decAcquis": "+03:22:12",
    "epochAcquis": "2000.0",
    "airMass": "1.000",
    "julianDate": "2460368.05207",
    "sideralTime": "20:40:07",
    "hourAngle": "00:00:00",
    "date": "27/02/24",
    "time": "10:14:59",
    "rightAscention": "20 40 07",
    "declination": "-22 35 28",
    "wsDefault": "OFF",
    "guideStr": "27/02/24 20:40:07 20 40 07 -22 35 28",
    "guideAng": "   0.00",
    "guideNor": "  97.00",
    "guideEsp": "S",
    "guideCas": "N",
    "guidePlaca": "0.091",
    "statShutter": "",
    "posCup": "",
    "raOnTarget": True,
    "decOnTarget": True,
    "dome": False,
    "domeOnTarget": True,
    "guider": False,
    "mount": False,
    "grossMovement": False,
    "fineMovement": False,
    "objCentrado": False,
    "varTracking": False,
    "shutter": False
}

focuser_json = {"absolute": True,
                "alarm": 0,
                "broker": "Focuser160",
                "cmd": {"clientId": 0, "clientTransactionId": 0, "clientName": "", "action": ""},
                "connected": True, "controller": "Focuser160", "device": "2ndMirror", "error": "",
                "homing": False, "initialized": True, "isMoving": False, "maxSpeed": 500,
                "maxStep": 50700, "position": 32100, "tempComp": False, "tempCompAvailable": False,
                "temperature": 0, "timestamp": "2024-02-27T10:15:48.255", "version": "1.0.0"}

WS_json = {"broker": "Weather160", "version": "1.0.0", "date": "21/02/24", "hour": "10:50",
           "outTemp": "17.1", "hiTemp": "17.1", "lowTemp": "16.7", "outHumidity": "97",
           "dewOut": "16.6", "windSpeed": "12.9", "windDirection": "WNW", "windRun": "1.07",
           "hiSpeed": "22.5", "hiDir": "WNW", "windChill": "16.6", "heatIndex": "17.8", "THWIndex": "17.3",
           "THSWIndex": "---", "pressure": "753,8", "rain": "0.00", "rainRate": "0.0",
           "solarRad": "1120", "solarEnergy": "8.03", "hiSolarRad": "1120", "UVIndex": "8.3",
           "UVDose": "0.30", "hiUV": "9.7", "headDD": "0.004", "coolDD": "0.000", "inTemp": "22.2",
           "inHumidity": "69", "dewIn": "16.3", "inHeat": "22.5", "inEMC": "12.81", "inAirDensity": "1.1642",
           "2ndTemp": "19.4", "2ndHumidity": "73", "ET": "0.00", "leaf": "0", "windSamp": "115", "windTx": "1",
           "ISSRecept": "100.0", "arcInt": "5"}

s4gui_json = {"OBSERVER": "AAA", "OBJECT": "BBB", "CTRLINTE": "S4GUI", "PROJID": "CCC", "SYNCMODE": "SYNC", "INSTMODE": "POL", "FILTER": "CLEAR",
              "OBSTYPE": "ZERO", "CHANNEL 1": True, "CHANNEL 2": False, "CHANNEL 3": False, "CHANNEL 4": False, "TCSMODE": True, "COMMENT": "DDD", "BROKER": "S4GUI"}
general_kw = {"FILENAME": "20240426_s4c1_000003.fits", "SEQINDEX": 0,
              "NCYCLES": 1, "NSEQ": 1, 'CYCLIND': 1, "ACSVRSN": "v1.46.14", "ACSMODE": False, }
ccd_kw = {"FRAMEIND": 1, "CCDTEMP": 20, "TEMPST": "TEMPERATURE_OFF", "CCDSERN": 9914, "PREAMP": 0, "READRATE": 0, "EMGAIN": 2, "VSHIFT": 3, "FRAMETRF": True, "VCLKAMP": 0, "ACQMODE": 3, "EMMODE": 1, "SHUTTER": 2, "TRIGGER": 0, "VBIN": 1, "INITLIN": 1,
          "INITCOL": 1, "FINALLIN": 1024, "FINALCOL": 1024, "HBIN": 1, "EXPTIME": 1.5, "NFRAMES": 1, "TGTEMP": 20, "COOLER": 0,  "CHANNEL": 1, "DATE-OBS": "2024-04-26T17:35:31.001", "UTTIME": "17:35:31.001", "UTDATE": "2024-04-26"}
ics_kw = {"WPROT": "WP8", "WPROT_MODE": "SIMULATED", "WPSEL": "L/2", "WPSEL_MODE": "SIMULATED", "CALW": "NONE", "CALW_MODE": "SIMULATED",
          "ASEL": "ON", "ASEL_MODE": "SIMULATED", "GMIR": "0.000", "GMIR_MODE": "SIMULATED", "GFOC": "0.000", "GFOC_MODE": "SIMULATED"}
