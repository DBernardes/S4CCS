import logging
import os
from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd
from astropy.time import Time


class Header(ABC):

    keywords = []
    to_float_kws = []
    to_int_str = []
    comma_kws = []
    subs_to_val_kws = {}
    subs_val_in_list = {}
    boolean_kws = []
    replace_unknow_kws = {}
    replace_str = {}
    delete_str = {}

    def __init__(self, _json, hdr, night_dir) -> None:
        self.json_string = _json
        self.hdr = hdr
        self.log_file = os.path.join(night_dir, 'error_acs.log')
        return

    def _convert_to_float(self):
        for kw in self.to_float_kws:
            try:
                self._check_type(kw, float)
                self.hdr[kw] = float(self.hdr[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_int(self):
        for kw in self.to_int_str:
            try:
                self._check_type(kw, int)
                self.hdr[kw] = int(self.hdr[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_comma(self):
        for kw in self.comma_kws:
            try:
                self._search_unwanted_kw(kw, ',')
                self.hdr[kw] = self.hdr[kw].replace(',', '.')
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_str(self):
        for kw, (prev, new) in self.replace_str.items():
            try:
                self._search_unwanted_kw(kw, prev)
                self.hdr[kw] = self.hdr[kw].replace(prev, new)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _delete_str(self):
        for kw, _str in self.delete_str.items():
            try:
                self._search_unwanted_kw(kw, _str)
                self.hdr[kw] = self.hdr[kw].replace(_str, '')
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _substitute_val_kw(self):
        for kw, dict in self.subs_to_val_kws.items():
            try:
                self.hdr[kw] = dict[self.hdr[kw]]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _boolean_kws(self):
        for kw in self.boolean_kws:
            try:
                val = self.hdr[kw]
                if val == 0:
                    self.hdr[kw] = False
                elif val == 1:
                    self.hdr[kw] = True
                else:
                    pass
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _subs_val_in_list(self):
        for kw, _list in self.subs_val_in_list.items():
            try:
                self.hdr[kw] = _list[self.hdr[kw]]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_unknown_str(self):
        for kw, val in self.replace_unknow_kws.items():
            try:
                if self.hdr[kw] == 'Unknown':
                    self.hdr[kw] = val
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def extract_info(self):
        for json_kw, hdr_kw in self.keywords:
            try:
                self.hdr[hdr_kw] = self.json_string[json_kw]
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)
# TODO: -9999999, strin "",

    def fix_keywords(self):
        """Fix header keywords.

        """
        self.extract_info()
        self._replace_comma()
        self._boolean_kws()
        self._subs_val_in_list()
        self._substitute_val_kw()
        self._replace_str()
        self._delete_str()
        self._replace_unknown_str()
        self._convert_to_float()
        self._convert_to_int()

    def _write_log_file(self, message, keyword):
        with open(self.log_file, 'a') as file:
            now = str(datetime.now())
            file.write(now + ' - ' + f'KEYWORD={keyword} - ' +
                       message + '\n')

    def _check_type(self, kw, tp):
        if not isinstance(self.hdr[kw], tp):
            self._write_log_file(
                f'Keyword value is not an instance of {repr(tp)}', kw)

    def _search_unwanted_kw(self, kw, _str):
        if _str in self.hdr[kw]:
            self._write_log_file(
                f'An unwanted string was found in keyword value: {_str}', kw)


class Focuser(Header):

    keywords = [('POSITION', 'TELFOCUS')]


class Weather_Station(Header):

    keywords = [('OUTHUMIDITY', 'HUMIDITY'),
                ('OUTTEMP', 'EXTTEMP')]
    to_float_kws = ['PRESSURE', 'HUMIDITY', 'EXTTEMP']
    comma_kws = ['PRESSURE']


class ICS(Header):

    keywords = [

        ('WPROT', 'WPPOS'), ('WPROT_MODE', 'WPROMODE'), ('WPSEL_MODE', 'WPSEMODE'),
        ('ASEL_MODE', 'ANMODE'), ('CALW_MODE', 'CALWMODE'), ('GMIR_MODE', 'GMIRMODE'), ('GFOC_MODE', 'GFOCMODE')]

    subs_to_val_kws = {'WPSEL': {'OFF': 'None', 'L/2': 'L2', 'L/4': 'L4'},
                       }
    replace_str = {'CALW': ('OFF', 'None')}

    replace_unknow_kws = {'WPSEL': 'None', 'CALW': 'None', 'ICSVRSN': 'v0.0.0'}
    to_float_kws = ['GMIR', 'GFOC']

    def fix_keywords(self):
        super().fix_keywords()
        self._write_WPPOS()
        self._write_ASEL()
        self._write_ICS_mode()

    def _write_ICS_mode(self):
        for kw in ['WPROMODE', 'WPSEMODE', 'ANMODE', 'CALWMODE', 'GMIRMODE', 'GFOCMODE']:
            try:
                if 'ACTIVE' in self.hdr[kw]:
                    self.hdr[kw] = True
                else:
                    self.hdr[kw] = False
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_ASEL(self):
        try:
            if 'ON' in self.hdr['ASEL']:
                self.hdr['ASEL'] = True
            else:
                self.hdr['ASEL'] = False
        except Exception as e:
            self._write_log_file(repr(e), 'ASEL')

    def _write_WPPOS(self):
        try:
            if 'NONE' in self.hdr['WPPOS']:
                self.hdr['WPPOS'] = 'None'
            elif 'WP' in self.hdr['WPPOS']:
                self.hdr['WPPOS'] = int(self.hdr['WPPOS'][2:])
            else:
                pass
        except Exception as e:
            self._write_log_file(repr(e), 'WPPOS')


class TCS(Header):
    keywords = [('RAACQUIS', 'RA'),
                ('DECACQUIS', 'DEC'), ('HOURANGLE', 'TCSHA'), ('GUIDEANG', 'INSTROT')]

    to_float_kws = ['AIRMASS', 'INSTROT']

    def fix_keywords(self):
        super().fix_keywords()
        self._write_TCSDATE()

    def _write_TCSDATE(self):
        try:
            date, time = self.json_string['DATE'], self.json_string['TIME']
            date = date.split('/')[::-1]
            time = time.split(':')
            tmp = [int(val) for val in date + time]
            tmp[0] += 2000
            self.hdr['TCSDATE'] = Time(datetime(*tmp)).isot
        except Exception as e:
            self._write_log_file(repr(e), 'TCSDATE')


class S4GUI(Header):

    keywords = [
        ('CHANNEL 1', 'CHANNEL1'),
        ('CHANNEL 2', 'CHANNEL2'),
        ('CHANNEL 3', 'CHANNEL3'),
        ('CHANNEL 4', 'CHANNEL4'),]
    replace_unknow_kws = {'OBJECT': '', 'OBSERVER': '',
                          'PROJID': '', 'TCSMODE': False, 'FILTER': 'CLEAR', 'GUIVRSN': 'v0.0.0'}


class CCD(Header):
    subs_to_val_kws = {'TRIGGER': {0: 'Internal', 6: 'External'},
                       'ACQMODE': {1: 'Single Scan', 2: 'Accumulate', 3: "Kinetic"}, }
    subs_val_in_list = {
        'EMMODE': ['Electron Multiplying', 'Conventional'],
        'SHUTTER': ['Open', 'Closed', 'Auto'],
        'VCLKAMP': ['Normal', '+1', '+2', '+3', '+4'],
        'VSHIFT': [0.6, 1.13, 2.2, 4.33],
        'PREAMP': ['Gain 1', 'Gain 2'], }
    boolean_kws = ['COOLER', 'FRAMETRF']
    to_float_kws = ['EXPTIME']

    ss_gains = pd.read_csv(os.path.join('csvs', 'preamp_gains.csv'))
    ss_read_noise = pd.read_csv(os.path.join('csvs', 'read_noises.csv'))

    def fix_keywords(self):
        super().fix_keywords()
        self._write_READRATE()
        idx = self.find_index_tab()
        self.hdr['GAIN'] = self.ss_gains[f"{self.hdr['CCDSERN']}"][idx]
        self.hdr['RDNOISE'] = self.ss_read_noise[f"{self.hdr['CCDSERN']}"][idx]

    def find_index_tab(self):
        json_string = self.json_string
        index = 2 * json_string['READRATE']
        if json_string['EMMODE'] == 1:
            index += 8
        index += json_string['PREAMP']
        return index

    def _write_READRATE(self):
        _list = [30., 20., 10., 1.]
        if self.hdr['EMMODE'] == 'Conventional':
            _list = [1., 0.1]
        try:
            self.hdr['READRATE'] = _list[self.hdr['READRATE']]
        except Exception as e:
            self._write_log_file(repr(e), 'READRATE')


class General_KWs(Header):

    replace_unknow_kws = {'INSTMODE': 'PHOT',
                          'OBSTYPE': 'OBJECT',
                          'NAXIS': 2,
                          'OBSLONG': -45.5825,
                          'OBSLAT': -22.534,
                          'OBSALT': 1864.0,
                          'EQUINOX': 2000.0,
                          'INSTRUME': 'SPARC4', }

    def fix_keywords(self):
        super().fix_keywords()
        try:
            self.hdr['CYCLIND'] += 1
        except Exception as e:
            self._write_log_file(repr(e), 'CYCLIND')
        try:
            self.hdr['SEQINDEX'] += 1
        except Exception as e:
            self._write_log_file(repr(e), 'SEQINDEX')
