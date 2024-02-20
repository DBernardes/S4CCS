from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time

from header import CCD
from utils import prepare_json

header_json = {"CYCLIND": 0, "FILENAME": "20240220_s4c1_000001.fits", "FRAMEIND": 1, "CCDTEMP": 20, "TEMPST": "TEMPERATURE_OFF", "CCDSERN": 9914, "SEQINDEX": 0, "WPPOS": 0, "PREAMP": 0, "READRATE": 0, "EMGAIN": 2, "VSHIFT": 3, "FRAMETRF": True, "VCLKAMP": 0, "ACQMODE": 3, "EMMODE": 1, "SHUTTER": 2, "TRIGGER": 0, "VBIN": 1, "INITLIN": 1, "INITCOL": 1, "FINALLIN": 1024, "FINALCOL": 1024, "HBIN": 1, "EXPTIME": 1.5, "COMMENT": "", "OBSTYPE": "", "OBJECT": "", "OBSERVER": "", "FILTER": "", "CTRLINTE": "GEI", "INSTMODE": "", "TCSMODE": True, "INSTROT": 0, "NFRAMES": 1, "NCYCLES": 1, "NSEQ": 1, "TGTEMP": 20, "ACSVRSN": "v1.43.0", "CHANNEL": 1, "ACSMODE": True, "WPSEMODE": True, "CALWMODE": True, "ANMODE": True, "GMIRMODE": True, "GFOCMODE": True, "WPROMODE": True, "absolute": True, "alarm": 0, "broker": "Focuser160", "cmd": {"clientId": 0, "clientTransactionId": 0, "clientName": "", "action": ""}, "connected": True, "controller": "Focuser160", "device": "2ndMirror", "error": "", "homing": True, "initialized": True, "isMoving": True, "maxSpeed": 500, "maxStep": 50700, "position": 66134, "tempComp": True, "tempCompAvailable": True, "temperature": 0, "timestamp": "2024-02-20T14:33:48.226", "version": "1.0.0", "broker": "Weather160", "version": "1.0.0", "date": "20/02/24", "hour": "14:30", "outTemp": "17.7", "hiTemp": "17.7", "lowTemp": "17.7", "outHumidity": "96", "dewOut": "17.1", "windSpeed": "9.7", "windDirection": "WNW", "windRun": "0.80", "hiSpeed": "20.9", "hiDir": "NW", "windChill": "17.7", "heatIndex": "18.4", "THWIndex": "18.4", "THSWIndex": "---", "pressure": "751.0", "rain": "0.00", "rainRate": "0.0", "solarRad": "497", "solarEnergy": "3.56", "hiSolarRad": "512", "UVIndex": "3.3", "UVDose": "0.12", "hiUV": "4.3", "headDD": "0.002", "coolDD": "0.000", "inTemp": "23.2", "inHumidity": "71", "dewIn": "17.6", "inHeat": "23.8", "inEMC": "13.30", "inAirDensity": "1.1541", "2ndTemp": "20.0", "2ndHumidity": "76", "ET": "0.00", "leaf": "0", "windSamp": "114", "windTx": "1", "ISSRecept": "100.0", "arcInt": "5",
               "broker": "TCSPD160",
               "version": "20240131",
               "cmd": "",
               "objectName": "               ",
               "raAcquis": "        ",
               "decAcquis": "        ",
               "epochAcquis": "",
               "airMass": "2.857",
               "julianDate": "2460361.23181",
               "sideralTime": "00:32:04",
               "hourAngle": "-1:38:48",
               "date": "20/02/24",
               "time": "14:33:49",
               "rightAscention": "02 10 53",
               "declination": "43 18 41,",
               "wsDefault": "OFF",
               "guideStr": "20/02/24 00:32:04 02 10 53 43 18 41,",
               "guideAng": "   0.00",
               "guideNor": " 180.00",
               "guideEsp": "S",
               "guideCas": "S",
               "guidePlaca": "0.100",
               "statShutter": "",
               "posCup": "",
               "raOnTarget": True,
               "decOnTarget": True,
               "dome": True,
               "domeOnTarget": True,
               "guider": True,
               "mount": True,
               "grossMovement": True,
               "fineMovement": True,
               "objCentrado": True,
               "varTracking": True,
               "shutter": True, "DATE-OBS": "2024-02-20T17:33:49.000", "UTTIME": "17:33:49.000", "UTDATE": "2024-02-20"}

header_json, hdr = prepare_json(header_json)
ccd = CCD(header_json, hdr)
ccd.fix_keywords()
print(ccd.hdr['trigger'])
