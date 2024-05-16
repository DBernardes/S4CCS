import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time

csv_path = os.path.join('csvs', 'header_content.csv')
ss = pd.read_csv(csv_path, delimiter=';')
cards = [(keyword, '', comment)
         for keyword, comment in zip(ss['Keyword'], ss['Comment'])]
gains = pd.read_csv(os.path.join('csvs', 'preamp_gains.csv'))
read_noise = pd.read_csv(os.path.join('csvs', 'read_noises.csv'))


class Header(ABC):

    hdr = fits.Header(cards)

    def __init__(self, _json, night_dir) -> None:

        self.kw_dataclass = self._initialize_kw_dataclass()
        self.log_file = os.path.join(night_dir, 'keywords_log.log')
        self.json_string = self.extract_info(_json)

        return

    @abstractmethod
    def _initialize_kw_dataclass(self):
        return Keywords_Dataclass()

    def _convert_to_float(self):
        for kw in self.kw_dataclass.to_float_kws:
            try:
                self.hdr[kw] = float(self.json_string[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_int(self):
        for kw in self.kw_dataclass.to_int_kws:
            try:
                self.hdr[kw] = int(self.json_string[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_comma(self):
        for kw in self.kw_dataclass.comma_kws:
            try:
                self._search_unwanted_kw(kw, ',')
                self.json_string[kw] = self.json_string[kw].replace(',', '.')
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_str(self):
        for kw, (prev, new) in self.kw_dataclass.replace_str.items():
            try:
                self._search_unwanted_kw(kw, prev)
                self.hdr[kw] = self.json_string[kw].replace(prev, new)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _delete_str(self):
        for kw, _str in self.kw_dataclass.delete_str.items():
            try:
                self._search_unwanted_kw(kw, _str)
                self.hdr[kw] = self.hdr[kw].replace(_str, '')
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _substitute_idx_in_dict(self):
        for kw, dict in self.kw_dataclass.idx_in_dict.items():
            try:
                self.hdr[kw] = dict[self.json_string[kw]]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_boolean(self):
        for kw in self.kw_dataclass.to_bool_kws:
            try:
                val = self.json_string[kw]
                self.hdr[kw] = bool(val)                
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_bool_with_condition(self):
        for kw, (off, on) in self.kw_dataclass.to_bool_with_condition.items():
            try:
                val = self.json_string[kw]                
                if val == off:
                    self.hdr[kw] = False
                elif val == on:
                    self.hdr[kw] = True
                else:
                    pass                                 
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _subs_idx_in_list(self):
        for kw, _list in self.kw_dataclass.idx_in_list.items():
            try:
                self.hdr[kw] = _list[self.json_string[kw]]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_empty_str(self):
        for kw, val in self.kw_dataclass.replace_empty_kws.items():
            try:
                if self.hdr[kw] == '':
                    self.hdr[kw] = val
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def extract_info(self, _json):
        new_json = {}
        for json_kw, hdr_kw, _type in self.kw_dataclass.keywords:
            try:
                val = _json[json_kw]
                new_json[hdr_kw] = val
                self._check_type(hdr_kw, val, _type)
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)
        return new_json

    def _write_any_value(self):
        for kw in self.kw_dataclass.write_any_str:
            try:
                self.hdr[kw] = self.json_string[kw]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_predefined_string(self):
        for kw, _list in self.kw_dataclass.write_predefined_str.items():
            try:
                val = self.json_string[kw]
                if val in _list:
                    self.hdr[kw] = val
                else:
                    self._write_log_file(
                        f'The provided keyword value "{val}" is not one of the pre-defined values: {_list}', kw)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    @abstractmethod
    def fix_keywords(self):
        """Fix header keywords.

        """
        return

    def _write_log_file(self, message, keyword):
        with open(self.log_file, 'a') as file:
            now = str(datetime.now())
            file.write(now + ' - ' + f'KEYWORD={keyword} - ' +
                       message + '\n')

    def _check_type(self, kw, val, _type):
        if not isinstance(val, _type):
            self._write_log_file(
                f'Keyword value is not an instance of {repr(_type)}: "{val}" was found.', kw)

    def _search_unwanted_kw(self, kw, _str):
        if _str in self.json_string[kw]:
            self._write_log_file(
                f'An unexpected string was found in the keyword value: {_str}', kw)

    def reset_header(self):
        for kw in self.hdr.keys():
            self.hdr[kw] = ''

    def return_empty_header(self):
        return fits.Header(cards)


class Focuser(Header):

    def _initialize_kw_dataclass(self):
        keywords = [('POSITION', 'TELFOCUS', int)]
        to_int_kws = ['TELFOCUS']
        return Keywords_Dataclass(keywords=keywords, to_int_kws=to_int_kws)

    def fix_keywords(self):
        self._convert_to_int()
        return


class Weather_Station(Header):

    def _initialize_kw_dataclass(self):
        keywords = [('OUTHUMIDITY', 'HUMIDITY', float),
                    ('OUTTEMP', 'EXTTEMP', float),
                    ('PRESSURE', 'PRESSURE', float)]
        to_float_kws = ['PRESSURE', 'HUMIDITY', 'EXTTEMP']
        comma_kws = ['PRESSURE']
        return Keywords_Dataclass(keywords=keywords, to_float_kws=to_float_kws, comma_kws=comma_kws)

    def fix_keywords(self):
        self._replace_comma()
        self._convert_to_float()
        return


class ICS(Header):

    def _initialize_kw_dataclass(self):
        keywords = [
            ("WPROT", "WPPOS", int),
            ("WPROT_MODE", "WPROMODE", bool),
            ("WPSEL", "WPSEL", str),
            ("WPSEL_MODE", "WPSEMODE", bool),
            ("CALW", "CALW", str),
            ("CALW_MODE", "CALWMODE", bool),
            ("ASEL", "ASEL", bool),
            ("ASEL_MODE", "ANMODE", bool),
            ("GMIR", "GMIR", float),
            ("GMIR_MODE", "GMIRMODE", bool),
            ("GFOC", "GFOC", bool),
            ("GFOC_MODE", "GFOCMODE", bool),
            ("ICSVRSN", "ICSVRSN", str),
        ]
        idx_in_dict = {'WPSEL': {'OFF': 'None', 'L/2': 'L2', 'L/4': 'L4'},
                       }
        to_float_kws = ['GMIR', 'GFOC']
        to_bool_with_condition = {'WPROMODE': ('SIMULATED', 'ACTIVE'),
                                  'WPSEMODE': ('SIMULATED', 'ACTIVE'),
                                  'ANMODE': ('SIMULATED', 'ACTIVE'),
                                  'CALWMODE': ('SIMULATED', 'ACTIVE'),
                                  'GMIRMODE': ('SIMULATED', 'ACTIVE'),
                                  'GFOCMODE': ('SIMULATED', 'ACTIVE'),
                                  'ASEL': ('OFF', 'ON')}
        wrtie_any_str = ['ICSVRSN']

        return Keywords_Dataclass(keywords=keywords,
                                  to_float_kws=to_float_kws,
                                  idx_in_dict=idx_in_dict,
                                  to_bool_with_condition=to_bool_with_condition,
                                  write_any_str=wrtie_any_str)

    def fix_keywords(self):
        self._convert_to_float()
        self._substitute_idx_in_dict()
        self._convert_to_bool_with_condition()
        self._write_any_value()
        self._write_WPPOS()
        self._write_CALW()

    def _write_WPPOS(self):
        try:
            val = self.json_string['WPPOS']
            if 'NONE' in val:
                self.hdr['WPPOS'] = 0
            elif 'WP' in val:
                self.hdr['WPPOS'] = int(val[2:])
            else:
                self._write_log_file(
                    f'The expected values for keyword are (NONE, WP1, ..., WP16). {val} was found.', 'WPPOS')
        except Exception as e:
            self._write_log_file(repr(e), 'WPPOS')

    def _write_CALW(self):
        try:
            val = self.json_string['CALW']
            expected_values = ['POLARIZER',
                               'DEPOLARIZER', 'NONE', 'PINHOLE', 'POS5']
            if val in expected_values:
                self.hdr['CALW'] = val
                if self.hdr['CALW'] == 'NONE':
                    self.hdr['CALW'] = 'None'
            else:
                self._write_log_file(
                    f'The expected values for this keyword are {expected_values}. "{val}" was found.', 'CALW')
        except Exception as e:
            self._write_log_file(repr(e), 'CALW')
        return


class TCS(Header):

    def _initialize_kw_dataclass(self):
        keywords = [('RAACQUIS', 'RA', str),
                    ('DECACQUIS', 'DEC', str),
                    ('HOURANGLE', 'TCSHA', str),
                    ('GUIDEANG', 'INSTROT', float),
                    ('AIRMASS', 'AIRMASS', float)]
        to_float_kws = ['AIRMASS', 'INSTROT']
        write_any_str = ['RA', 'DEC', 'TCSHA']

        return Keywords_Dataclass(keywords=keywords,
                                  to_float_kws=to_float_kws,
                                  write_any_str=write_any_str)

    def fix_keywords(self):
        self._convert_to_float()
        self._write_any_value()
        return

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

    def _initialize_kw_dataclass(self):
        keywords = [
            ('CHANNEL 1', 'CHANNEL1', bool),
            ('CHANNEL 2', 'CHANNEL2', bool),
            ('CHANNEL 3', 'CHANNEL3', bool),
            ('CHANNEL 4', 'CHANNEL4', bool),
            ('OBJECT', 'OBJECT', str),
            ('OBSERVER', 'OBSERVER', str),
            ('PROJID', 'PROJID', str),
            ('TCSMODE', 'TCSMODE', bool),
            ('FILTER', 'FILTER', str),
            ('GUIVRSN', 'GUIVRSN', str),
            ('CTRLINTE', 'CTRLINTE', str),
            ('SYNCMODE', 'SYNCMODE', str),
            ('INSTMODE', 'INSTMODE', str),
            ('OBSTYPE', 'OBSTYPE', str),
            ('COMMENT', 'COMMENT', str)]
        to_bool_kw = ['CHANNEL1', 'CHANNEL2',
                      'CHANNEL3', 'CHANNEL4', 'TCSMODE']
        write_any_str = ['OBJECT', 'OBSERVER', 'PROJID']
        write_predefined_str = {'FILTER': ['CLEAR', 'B', 'V', 'R', 'I'],
                                'CTRLINTE': ['S4GUI', 'S4GEI'],
                                'SYNCMODE': ['SYNC', 'ASYNC'],
                                'INSTMODE': ['POL', 'PHOT'],
                                'OBSTYPE': ['ZERO', 'DARK', 'FLAT', 'OBJECT', 'FOCUS']}
        # replace_unknow_kws = {'OBJECT': '', 'OBSERVER': '',
        #                     'PROJID': '', 'TCSMODE': False, 'FILTER': 'CLEAR', 'GUIVRSN': 'v0.0.0'}
        return Keywords_Dataclass(keywords=keywords,
                                  to_bool_kws=to_bool_kw,
                                  write_any_str=write_any_str,
                                  write_predefined_str=write_predefined_str)

    def _write_COMMENT(self):
        kw = 'COMMENT'
        try:
            if kw in self.hdr.keys():
                del self.hdr[kw]
            self.hdr[kw] = self.json_string[kw]
        except Exception as e:
            self._write_log_file(repr(e), kw)
        return

    def fix_keywords(self):
        self._convert_to_boolean()
        self._write_any_value()
        self._write_predefined_string()
        self._write_COMMENT()
        return


class CCD(Header):

    def _initialize_kw_dataclass(self):
        keywords = [('FRAMEIND', 'FRAMEIND', int),
                    ('CCDTEMP', 'CCDTEMP', int),
                    ('TEMPST', 'TEMPST', str),
                    ('CCDSERN', 'CCDSERN', int),
                    ('PREAMP', 'PREAMP', int),
                    ('READRATE', 'READRATE', int),
                    ('EMGAIN', 'EMGAIN', int),
                    ('VSHIFT', 'VSHIFT', int),
                    ('FRAMETRF', 'FRAMETRF', bool),
                    ('VCLKAMP', 'VCLKAMP', int),
                    ('ACQMODE', 'ACQMODE', int),
                    ('EMMODE', 'EMMODE', int),
                    ('SHUTTER', 'SHUTTER', int),
                    ('TRIGGER', 'TRIGGER', int),
                    ('VBIN', 'VBIN', int),
                    ('INITLIN', 'INITLIN', int),
                    ('INITCOL', 'INITCOL', int),
                    ('FINALLIN', 'FINALLIN', int),
                    ('FINALCOL', 'FINALCOL', int),
                    ('HBIN', 'HBIN', int),
                    ('EXPTIME', 'EXPTIME', float),
                    ('NFRAMES', 'NFRAMES', int),
                    ('TGTEMP', 'TGTEMP', int),
                    ('COOLER', 'COOLER', int),
                    ('CHANNEL', 'CHANNEL', int),
                    ('DATE-OBS', 'DATE-OBS', str),
                    ('UTTIME', 'UTTIME', str),
                    ('UTDATE', 'UTDATE', str)]
        idx_in_dict = {'TRIGGER': {0: 'Internal', 6: 'External'},
                       'ACQMODE': {1: 'Single Scan', 2: 'Accumulate', 3: "Kinetic"}, }
        idx_in_list = {
            'EMMODE': ['Electron Multiplying', 'Conventional'],
            'SHUTTER': ['Auto', 'Open', 'Closed'],
            'VCLKAMP': ['Normal', '+1', '+2', '+3', '+4'],
            'VSHIFT': [0.6, 1.13, 2.2, 4.33],
            'PREAMP': ['Gain 1', 'Gain 2'], }
        to_bool_kws = ['COOLER', 'FRAMETRF']
        to_float_kws = ['EXPTIME']
        to_int_kws = ['VBIN', 'HBIN', 'FINALCOL', 'FINALLIN', 'INITCOL',
                      'INITLIN', 'FRAMEIND', 'CCDSERN', 'EMGAIN', 'NFRAMES', 'CHANNEL', 'CCDTEMP', 'TGTEMP']
        write_predefined_str = {'TEMPST': {
            'TEMPERATURE_OFF', 'TEMPERATURE_NOT_REACHED', 'TEMPERATURE_NOT_STABILIZED', 'TEMPERATURE_STABILIZED'
        }}
        write_any_str = ['DATE-OBS', 'UTDATE', 'UTTIME']

        return Keywords_Dataclass(keywords=keywords,
                                  to_bool_kws=to_bool_kws,
                                  to_float_kws=to_float_kws,
                                  to_int_kws=to_int_kws,
                                  idx_in_list=idx_in_list,
                                  idx_in_dict=idx_in_dict,
                                  write_predefined_str=write_predefined_str,
                                  write_any_str=write_any_str)

    def fix_keywords(self):
        self._convert_to_boolean()
        self._convert_to_float()
        self._convert_to_int()
        self._subs_idx_in_list()
        self._substitute_idx_in_dict()
        self._write_any_value()
        self._write_predefined_string()
        self._write_READRATE()
        self._write_ccd_gain()
        self._write_read_noise()

        return

    def _write_read_noise(self):
        try:
            idx = self.find_index_tab()
            self.hdr['RDNOISE'] = read_noise[f"{self.hdr['CCDSERN']}"][idx]
        except Exception as e:
            self._write_log_file(repr(e), 'RDNOISE')

    def _write_ccd_gain(self):
        try:
            idx = self.find_index_tab()
            self.hdr['GAIN'] = gains[f"{self.hdr['CCDSERN']}"][idx]
        except Exception as e:
            self._write_log_file(repr(e), 'GAIN')

    def find_index_tab(self):
        json_string = self.json_string
        index = 2 * json_string['READRATE']
        if json_string['EMMODE'] == 1:
            index += 8
        index += json_string['PREAMP']
        return index

    def _write_READRATE(self):
        try:
            _list = [30., 20., 10., 1.]
            if self.json_string['EMMODE'] == 1:
                _list = [1., 0.1]
            self.hdr['READRATE'] = _list[self.json_string['READRATE']]
        except Exception as e:
            self._write_log_file(repr(e), 'READRATE')


class General_KWs(Header):

    def _initialize_kw_dataclass(self):
        keywords = [
            ('FILENAME', 'FILENAME', str),
            ('SEQINDEX', 'SEQINDEX', int),
            ('NCYCLES', 'NCYCLES', int),
            ('NSEQ', 'NSEQ', int),
            ('CYCLIND', 'CYCLIND', int),
            ('ACSVRSN', 'ACSVRSN', str),
            ('ACSMODE', 'ACSMODE', bool),
        ]

        write_any_str = ['FILENAME', 'ACSVRSN', 'NSEQ', 'NCYCLES']
        to_bool_kw = ['ACSMODE']
        replace_empty_kws = {
            'NAXIS': 2,
            'OBSLONG': -45.5825,
            'OBSLAT': -22.534,
            'OBSALT': 1864.0,
            'EQUINOX': 2000.0,
            'INSTRUME': 'SPARC4',
            'SIMPLE': True,
            'BSCALE': 1,
            'BZERO': 32768,
            'BITPIX': 16}
        return Keywords_Dataclass(keywords=keywords,
                                  replace_empty_kws=replace_empty_kws,
                                  to_bool_kws=to_bool_kw,
                                  write_any_str=write_any_str)

    def fix_keywords(self):
        self._replace_empty_str()
        self._write_any_value()
        self._convert_to_boolean()
        self._write_CYCLIND()
        self._write_SEQINDEX()

    def _write_SEQINDEX(self):
        try:
            self.hdr['SEQINDEX'] = self.json_string['SEQINDEX'] + 1
        except Exception as e:
            self._write_log_file(repr(e), 'SEQINDEX')

    def _write_CYCLIND(self):
        try:
            self.hdr['CYCLIND'] = self.json_string['CYCLIND'] + 1
        except Exception as e:
            self._write_log_file(repr(e), 'CYCLIND')


@dataclass
class Keywords_Dataclass:
    keywords: list = field(default_factory=list)

    to_float_kws: list = field(default_factory=list)
    to_int_kws: list = field(default_factory=list)
    to_bool_kws: list = field(default_factory=list)
    to_bool_with_condition: dict = field(default_factory=dict)

    comma_kws: list = field(default_factory=list)
    replace_str: dict = field(default_factory=dict)
    delete_str: dict = field(default_factory=dict)

    write_any_str: list = field(default_factory=list)
    write_predefined_str: dict = field(default_factory=dict)

    idx_in_dict: dict = field(default_factory=dict)
    idx_in_list: dict = field(default_factory=dict)
    replace_empty_kws: dict = field(default_factory=dict)
