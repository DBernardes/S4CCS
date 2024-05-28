import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

import astropy.io.fits as fits
import pandas as pd
from astropy.time import Time
from .utils import cards, gains, read_noise, keyword_types, expected_kw_names, allowed_kw_values
import math



class Header(ABC):

    hdr = fits.Header(cards)
    kw_types = {'integer': int, 'boolean':bool, 'float':float, 'string':str}

    def __init__(self, _json, night_dir) -> None:

        self.kw_dataclass = self._initialize_kw_dataclass()
        self.log_file = os.path.join(night_dir, 'keywords_log.log')
        self.json_string = self.extract_info(_json)
        self._check_type()

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
    
    def _replace_empty_str(self):
        for kw, val in self.kw_dataclass.replace_empty_kws.items():
            try:
                if self.hdr[kw] == '':
                    self.hdr[kw] = val
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_any_value(self):
        for kw in self.kw_dataclass.write_any_str:
            try:
                self.hdr[kw] = self.json_string[kw]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_predefined_string(self):
        for kw in self.kw_dataclass.write_predefined_str:
            try:
                val = self.json_string[kw]
                _list = allowed_kw_values[kw]
                if val in _list:
                    self.hdr[kw] = val
                else:
                    self._write_log_file(
                        f'The provided keyword value "{val}" is not one of the pre-defined values: {_list}', kw)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _substitute_idx_in_dict(self):
        for kw, dict in self.kw_dataclass.idx_in_dict.items():
            try:
                val = self.json_string[kw]
                self.hdr[kw] = dict[val]
                self._write_log_file(f'The expected values for this keyword are ({dict.values()}). "{val}" was found.', kw)
            except Exception as e:
                self._write_log_file(repr(e), kw)


    def _subs_idx_in_list(self):
        for kw in self.kw_dataclass.idx_in_list:
            try:
                _list = allowed_kw_values[kw]
                val = self.json_string[kw]
                self.hdr[kw] = _list[val]
                self._write_log_file(f'The expected values for this keyword are ({_list}). "{val}" was found.', kw)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    

    def extract_info(self, _json):
        new_json = {}
        for hdr_kw in self.kw_dataclass.keywords:
            try:
                json_kw = hdr_kw
                expected_name = expected_kw_names[hdr_kw]
                if not math.isnan(expected_name):
                    json_kw = expected_name
                new_json[hdr_kw] = _json[json_kw]                
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)
        return new_json

    def _check_type(self):
        for hdr_kw in self.kw_dataclass.keywords:
            try:
                val = self.json_string[hdr_kw]
                _type = keyword_types[hdr_kw]
                if not isinstance(val, self.kw_types[_type]):
                    self._write_log_file(
                        f'Keyword value "{val}" is not an instance of {repr(_type)}.', hdr_kw)
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)
    
    # def _check_allowed_values(self):
    #     for hdr_kw in self.kw_dataclass.keywords:
    #         _type = self.kw_types[hdr_kw]
    #         if _type

        
    #     return

 

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
        keywords = ['TELFOCUS']
        to_int_kws = ['TELFOCUS']
        return Keywords_Dataclass(keywords=keywords, to_int_kws=to_int_kws)

    def fix_keywords(self):
        self._convert_to_int()
        return


class Weather_Station(Header):

    def _initialize_kw_dataclass(self):
        keywords = ['HUMIDITY', 'EXTTEMP','PRESSURE']
        to_float_kws = ['PRESSURE', 'HUMIDITY', 'EXTTEMP']
        comma_kws = ['PRESSURE']
        return Keywords_Dataclass(keywords=keywords, to_float_kws=to_float_kws, comma_kws=comma_kws)

    def fix_keywords(self):
        self._replace_comma()
        self._convert_to_float()
        return


class ICS(Header):

    def _initialize_kw_dataclass(self):
        keywords = ["WPANG","WPPOS","WPROMODE","WPSEL","WPSELPO","WPSEMODE","CALW",
                    "CALWMODE","CALWANG","ASEL","ANMODE","ANALANG","GMIR","GMIRMODE","GFOC","GFOCMODE","ICSVRSN"]
        idx_in_dict = {'WPSEL': {'OFF':'None', 'L/2':'L2', 'L/4':'L4'}}
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
                if val == 'OFF':
                    self.hdr['CALW'] = 'None'
                self._write_log_file(
                    f'The expected values for this keyword are {expected_values}. "{val}" was found.', 'CALW')
        except Exception as e:
            self._write_log_file(repr(e), 'CALW')
        return


class TCS(Header):

    def _initialize_kw_dataclass(self):
        keywords = ['RA', 'DEC','TCSHA','INSTROT','AIRMASS','DATE','TIME']
        to_float_kws = ['AIRMASS', 'INSTROT']
        write_any_str = ['RA', 'DEC', 'TCSHA']

        return Keywords_Dataclass(keywords=keywords,
                                  to_float_kws=to_float_kws,
                                  write_any_str=write_any_str)

    def fix_keywords(self):
        self._convert_to_float()
        self._write_any_value()
        self._write_TCSDATE()
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
        keywords = ['CHANNEL1','CHANNEL2','CHANNEL3','CHANNEL4','OBJECT','OBSERVER','PROJID',
                    'TCSMODE','FILTER','GUIVRSN','CTRLINTE','SYNCMODE','INSTMODE','OBSTYPE','COMMENT','GUIVRSN']
        to_bool_kw = ['CHANNEL1', 'CHANNEL2', 'CHANNEL3', 'CHANNEL4', 'TCSMODE']
        write_any_str = ['OBJECT', 'OBSERVER', 'PROJID', 'GUIVRSN']
        write_predefined_str = ['FILTER','CTRLINTE','SYNCMODE', 'OBSTYPE','INSTMODE']
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
        keywords = ['FRAMEIND','CCDTEMP','TEMPST','CCDSERN','PREAMP','READRATE','EMGAIN','VSHIFT',
                    'FRAMETRF','VCLKAMP','ACQMODE','EMMODE','SHUTTER','TRIGGER','VBIN','INITLIN',
                    'INITCOL','FINALLIN','FINALCOL','HBIN','EXPTIME','NFRAMES','TGTEMP','COOLER',
                    'CHANNEL','DATE-OBS','UTTIME','UTDATE']
        idx_in_dict = {'TRIGGER': {0: 'Internal', 6:'External'},
                       'ACQMODE': {1: 'Single Scan', 3: 'Kinetics'}}
        idx_in_list = ['EMMODE','SHUTTER','VCLKAMP','VSHIFT','PREAMP']
        to_bool_kws = ['COOLER', 'FRAMETRF']
        to_float_kws = ['EXPTIME']
        to_int_kws = ['VBIN', 'HBIN', 'FINALCOL', 'FINALLIN', 'INITCOL',
                      'INITLIN', 'FRAMEIND', 'CCDSERN', 'EMGAIN', 'NFRAMES', 'CHANNEL', 'CCDTEMP', 'TGTEMP']
        write_predefined_str = ['TEMPST']
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
        keywords = ['FILENAME','SEQINDEX','NCYCLES','NSEQ','CYCLIND','ACSVRSN','ACSMODE']

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
