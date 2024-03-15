import os
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time

from header import TCS, Focuser, Weather_Station
from utils import WS_json, focuser_json, prepare_json, tcs_json

# ss = pd.read_csv(os.path.join('csvs', 'header_content.csv'), delimiter='\t')
# cards = [(keyword, 'Unknown', comment)
#          for keyword, comment in zip(ss['Keyword'], ss['Comment'])]

# hdr = fits.Header(cards)
# del focuser_json['cmd']

# night_dir = r'E:\images\today'
# header_json, hdr = prepare_json(header_json)
# ccd = Focuser(focuser_json, hdr, night_dir)
# ccd.fix_keywords()


# header_json = {"CYCLIND":0,"FILENAME":"20240227_s4c1_000016.fits","FRAMEIND":1,"CCDTEMP":20,"TEMPST":"TEMPERATURE_OFF","CCDSERN":9914,"SEQINDEX":0,"WPPOS":0,"PREAMP":1,"READRATE":0,"EMGAIN":2,"VSHIFT":3,"FRAMETRF":false,"VCLKAMP":0,"ACQMODE":3,"EMMODE":1,"SHUTTER":1,"TRIGGER":0,"VBIN":1,"INITLIN":1,"INITCOL":1,"FINALLIN":1024,"FINALCOL":1024,"HBIN":1,"EXPTIME":1.5,"COMMENT":"","OBSTYPE":"","OBJECT":"","OBSERVER":"","FILTER":"","CTRLINTE":"","INSTMODE":"","TCSMODE":false,"INSTROT":0,"NFRAMES":1,"NCYCLES":1,"NSEQ":1,"TGTEMP":20,"COOLER":0,"ACSVRSN":"v1.43.1","CHANNEL":1,"ACSMODE":false,"WPSEMODE":false,"CALWMODE":false,"ANMODE":false,"GMIRMODE":false,"GFOCMODE":false,"WPROMODE":false,"absolute": true, "alarm": 0, "broker": "Focuser160", "cmd": {"clientId": 0, "clientTransactionId": 0, "clientName": "", "action": ""}, "connected": true, "controller": "Focuser160", "device": "2ndMirror", "error": "", "homing": false, "initialized": true, "isMoving": false, "maxSpeed": 500, "maxStep": 50700, "position": 32100, "tempComp": false, "tempCompAvailable": false, "temperature": 0, "timestamp": "2024-02-27T16:00:32.256", "version": "1.0.0","broker": "Weather160", "version": "1.0.0", "date": "27/02/24", "hour": "15:55", "outTemp": "20.7", "hiTemp": "21.1", "lowTemp": "20.7", "outHumidity": "84", "dewOut": "17.9", "windSpeed": "4.8", "windDirection": "WSW", "windRun": "0.40", "hiSpeed": "6.4", "hiDir": "WSW", "windChill": "20.7", "heatIndex": "21.6", "THWIndex": "21.6", "THSWIndex": "---", "pressure": "754.9", "rain": "0.00", "rainRate": "0.0", "solarRad": "78", "solarEnergy": "0.56", "hiSolarRad": "88", "UVIndex": "0.5", "UVDose": "0.02", "hiUV": "0.6", "headDD": "0.000", "coolDD": "0.008", "inTemp": "24.4", "inHumidity": "68", "dewIn": "18.2", "inHeat": "25.1", "inEMC": "12.51", "inAirDensity": "1.1545", "2ndTemp": "23.9", "2ndHumidity": "62", "ET": "0.00", "leaf": "0", "windSamp": "115", "windTx": "1", "ISSRecept": "100.0", "arcInt": "5","broker": "TCSPD160","version": "20240131","cmd": "","objectName": "NO_OBJ         ","raAcquis": "03:19:21","decAcquis": "+03:22:12","epochAcquis": "2000.0","airMass": "1.000","julianDate": "2460368.29173","sideralTime": "02:26:12","hourAngle": "00:00:00","date": "27/02/24","time": "16:00:06","rightAscention": "02 26 12","declination": "-23 22 32","wsDefault": "OFF","guideStr": "27/02/24 02:26:12 02 26 12 -23 22 32","guideAng": "   0.00","guideNor": "  97.00","guideEsp": "S","guideCas": "N","guidePlaca": "0.091","statShutter": "","posCup": "","raOnTarget": true,"decOnTarget": true,"dome": false,"domeOnTarget": true,"guider": false,"mount": false,"grossMovement": false,"fineMovement": false,"objCentrado": false,"varTracking": false,"shutter": false,"DATE-OBS":"2024-02-27T19:00:5.001","UTTIME":"19:00:5.001","UTDATE":"2024-02-27"}


# header_json, hdr = prepare_json(header_json)
# print(header_json)

path = r'E:\images\20230604'
files = os.listdir(path)
for file in files:
    try:
        hdr = fits.getheader(path + '\\' + file, ignore_missing_simple=True)
        if 'hilt' in hdr['OBJECT']:
            print(file)
    except:
        continue
