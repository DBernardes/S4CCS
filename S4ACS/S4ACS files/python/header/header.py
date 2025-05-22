import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import astropy.io.fits as fits
from datetime import datetime

from astropy.time import Time

from .utils import (
    allowed_kw_values,
    cards,
    expected_kw_names,
    gains,
    keyword_types,
    read_noise,
)


class Header(ABC):

    hdr = fits.Header(cards)
    kw_types = {"integer": int, "boolean": bool, "float": float, "string": str}
    sub_system = "HEADER"

    def __init__(self, dict_header_jsons, log_file) -> None:

        _json = self._load_json(dict_header_jsons)
        self.kw_dataclass = self._initialize_kw_dataclass()
        self.log_file = log_file
        self._json = self.extract_info(_json)
        self._check_type()
        self._check_allowed_values()

        return

    def _load_json(self, dict_header_jsons):
        self.json_string = dict_header_jsons[self.sub_system]
        if self.json_string == "":
            return {}
        try:
            _json = json.loads(self.json_string)
            _json = {k.upper(): v for k, v in _json.items()}
            return _json
        except Exception as e:
            raise Exception(
                f"{self.sub_system}: There was an error when loading the JSON data --> {self.json_string}."
                + repr(e)
            )

    @abstractmethod
    def _initialize_kw_dataclass(self):
        return Keywords_Dataclass()

    def _convert_to_float(self):
        for kw in self.kw_dataclass.to_float_kws:
            try:
                self.hdr[kw] = float(self._json[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_int(self):
        for kw in self.kw_dataclass.to_int_kws:
            try:
                self.hdr[kw] = int(self._json[kw])
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_boolean(self):
        for kw in self.kw_dataclass.to_bool_kws:
            try:
                val = self._json[kw]
                self.hdr[kw] = bool(val)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _convert_to_bool_with_condition(self):
        for kw, (off, on) in self.kw_dataclass.to_bool_with_condition.items():
            try:
                val = self._json[kw]
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
                self._search_unwanted_kw(kw, ",")
                self._json[kw] = self._json[kw].replace(",", ".")
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_str(self):
        for kw, (prev, new) in self.kw_dataclass.replace_str.items():
            try:
                self._search_unwanted_kw(kw, prev)
                self.hdr[kw] = self._json[kw].replace(prev, new)
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _delete_str(self):
        for kw, _str in self.kw_dataclass.delete_str.items():
            try:
                self._search_unwanted_kw(kw, _str)
                self.hdr[kw] = self.hdr[kw].replace(_str, "")
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _replace_empty_str(self):
        for kw, val in self.kw_dataclass.replace_empty_kws.items():
            try:
                if self.hdr[kw] == "":
                    self.hdr[kw] = val
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_any_value(self):
        for kw in self.kw_dataclass.write_any_val:
            try:
                self.hdr[kw] = self._json[kw]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _write_predefined_value(self):
        for kw in self.kw_dataclass.write_predefined_value:
            try:
                val = self._json[kw]
                _list = allowed_kw_values[kw]
                if val in _list:
                    self.hdr[kw] = val
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _substitute_idx_in_dict(self):
        for kw, dict in self.kw_dataclass.idx_in_dict.items():
            try:
                val = self._json[kw]
                self.hdr[kw] = dict[val]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def _subs_idx_in_list(self):
        for kw in self.kw_dataclass.idx_in_list:
            try:
                _list = allowed_kw_values[kw]
                val = self._json[kw]
                self.hdr[kw] = _list[val]
            except Exception as e:
                self._write_log_file(repr(e), kw)

    def extract_info(self, _json):
        new_json = {}
        for hdr_kw in self.kw_dataclass.keywords:
            try:
                json_kw = hdr_kw
                expected_name = expected_kw_names[hdr_kw]
                if expected_name != "":
                    json_kw = expected_name
                new_json[hdr_kw] = _json[json_kw]
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)
        return new_json

    def _check_type(self):
        for hdr_kw in self.kw_dataclass.keywords:
            try:
                val = self._json[hdr_kw]
                _type = keyword_types[hdr_kw]
                if not isinstance(val, self.kw_types[_type]):
                    self._write_log_file(
                        f'Keyword value "{val}" is not an instance of {repr(_type)}.',
                        hdr_kw,
                    )
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)

    def _check_allowed_values(self):
        for hdr_kw in self.kw_dataclass.keywords:
            try:
                _type = keyword_types[hdr_kw]
                if _type in ["integer", "float"]:
                    self._check_number_in_range(hdr_kw)
                elif _type == "string":
                    self._check_string_in_allowed_values(hdr_kw)
            except Exception as e:
                self._write_log_file(repr(e), hdr_kw)

        return

    def _check_number_in_range(self, hdr_kw):
        val = self._json[hdr_kw]
        a_values = allowed_kw_values[hdr_kw]
        min, *max = a_values
        if not isinstance(val, (int, float)):
            return
        if val < min or val > max[-1]:
            self._write_log_file(
                f'The provided keyword value is out of range {a_values}. "{val}" was found.',
                hdr_kw,
            )
        return

    def _check_string_in_allowed_values(self, hdr_kw):
        val = self._json[hdr_kw]
        a_values = allowed_kw_values[hdr_kw]
        if not isinstance(val, str):
            return
        if val not in a_values and a_values != "":
            self._write_log_file(
                f'The expected values for this keyword are {a_values}. "{val}" was found.',
                hdr_kw,
            )
        return

    @abstractmethod
    def fix_keywords(self):
        """Fix header keywords."""
        return

    def _write_log_file(self, message, keyword):
        with open(self.log_file, "a") as file:
            now = str(datetime.now())
            file.write(
                now
                + " - "
                + f"SUB-SYTEM={self.sub_system}, KEYWORD={keyword} - "
                + message
                + "\n"
            )

    def _search_unwanted_kw(self, kw, _str):
        if _str in self._json[kw]:
            self._write_log_file(
                f"An unexpected string was found in the keyword value: {_str}", kw
            )

    def reset_header(self):
        for kw in self.hdr.keys():
            self.hdr[kw] = ""

    def return_empty_header(self):
        return fits.Header(cards)


class Focuser(Header):

    sub_system = "FOCUSER"

    def _initialize_kw_dataclass(self):
        keywords = ["TELFOCUS"]
        to_int_kws = ["TELFOCUS"]
        return Keywords_Dataclass(keywords=keywords, to_int_kws=to_int_kws)

    def fix_keywords(self):
        self._convert_to_int()
        return


class Weather_Station(Header):

    sub_system = "WSTATION"

    def __init__(self, dict_header_jsons, log_file):
        json_string = dict_header_jsons[self.sub_system]
        if 'Weather' in json_string[:7]:
            json_string = json_string.replace('Weather', '')
        dict_header_jsons[self.sub_system] = json_string
        super().__init__(dict_header_jsons, log_file)

    def _initialize_kw_dataclass(self):
        keywords = ["HUMIDITY", "EXTTEMP", "PRESSURE"]
        to_float_kws = ["PRESSURE", "HUMIDITY", "EXTTEMP"]
        comma_kws = ["PRESSURE"]
        return Keywords_Dataclass(
            keywords=keywords, to_float_kws=to_float_kws, comma_kws=comma_kws
        )

    def fix_keywords(self):
        self._replace_comma()
        self._convert_to_float()
        return


class ICS(Header):

    sub_system = "S4ICS"

    def _initialize_kw_dataclass(self):
        keywords = [
            "WPANG",
            "WPPOS",
            "WPROMODE",
            "WPSEL",
            "WPSELPO",
            "WPSEMODE",
            "CALW",
            "CALWMODE",
            "CALWANG",
            "ASEL",
            "ANMODE",
            "ANALANG",
            "GMIR",
            "GMIRMODE",
            "GFOC",
            "GFOCMODE",
            "ICSVRSN",
        ]
        idx_in_dict = {"WPSEL": {"OFF": "None", "L/2": "L2", "L/4": "L4"}}
        to_float_kws = ["GMIR", "GFOC"]
        to_bool_with_condition = {
            "WPROMODE": ("SIMULATED", "ACTIVE"),
            "WPSEMODE": ("SIMULATED", "ACTIVE"),
            "ANMODE": ("SIMULATED", "ACTIVE"),
            "CALWMODE": ("SIMULATED", "ACTIVE"),
            "GMIRMODE": ("SIMULATED", "ACTIVE"),
            "GFOCMODE": ("SIMULATED", "ACTIVE"),
            "ASEL": ("OFF", "ON"),
        }
        write_any_val = ["ICSVRSN"]

        return Keywords_Dataclass(
            keywords=keywords,
            to_float_kws=to_float_kws,
            idx_in_dict=idx_in_dict,
            to_bool_with_condition=to_bool_with_condition,
            write_any_val=write_any_val,
        )

    def fix_keywords(self):
        self._convert_to_float()
        self._substitute_idx_in_dict()
        self._convert_to_bool_with_condition()
        self._write_any_value()
        self._write_WPPOS()
        self._write_CALW()

    def _write_WPPOS(self):
        try:
            val = self._json["WPPOS"]
            if "NONE" in val:
                self.hdr["WPPOS"] = 0
            elif "WP" in val:
                self.hdr["WPPOS"] = int(val[2:])
            else:
                self._write_log_file(
                    f"The expected values for keyword are (NONE, WP1, ..., WP16). {val} was found.",
                    "WPPOS",
                )
        except Exception as e:
            self._write_log_file(repr(e), "WPPOS")

    def _write_CALW(self):
        try:
            val = self._json["CALW"]
            expected_values = ["POLARIZER", "DEPOLARIZER", "NONE", "PINHOLE", "POS5"]
            if val in expected_values:
                self.hdr["CALW"] = val
                if self.hdr["CALW"] == "NONE":
                    self.hdr["CALW"] = "None"
            else:
                if val == "OFF":
                    self.hdr["CALW"] = "None"
                self._write_log_file(
                    f'The expected values for this keyword are {expected_values}. "{val}" was found.',
                    "CALW",
                )
        except Exception as e:
            self._write_log_file(repr(e), "CALW")
        return


class TCS(Header):

    sub_system = "TCS"

    def __init__(self, _json, night_dir) -> None:
        super().__init__(_json, night_dir)
        self._json["TCSDATE"] = self._write_TCSDATE()

    def _initialize_kw_dataclass(self):
        keywords = ["RA", "DEC", "TCSHA", "INSTROT", "AIRMASS"]
        to_float_kws = ["AIRMASS", "INSTROT"]
        write_any_val = ["RA", "DEC", "TCSDATE"]
        comma_kws = ["TCSHA"]

        return Keywords_Dataclass(
            keywords=keywords,
            to_float_kws=to_float_kws,
            write_any_val=write_any_val,
            comma_kws=comma_kws,
        )

    def fix_keywords(self):
        self._convert_to_float()
        self._write_any_value()
        return

    def _write_TCSDATE(self):
        try:
            if self.json_string == "":
                raise KeyError("DATE", "TIME")
            _json = {k.upper(): v for (k, v) in json.loads(self.json_string).items()}
            for kw in ["DATE", "TIME"]:
                if not isinstance(_json[kw], str):
                    self._write_log_file(
                        f'Keyword value "{_json[kw]}" is not an instance of {repr(str)}.',
                        kw,
                    )
                    return
            date, time = _json["DATE"], _json["TIME"]
            date = date.split("/")[::-1]
            time = time.split(":")
            tmp = [int(val) for val in date + time]
            tmp[0] += 2000
            tcsdate = Time(datetime(*tmp)).isot
            return tcsdate
        except Exception as e:
            self._write_log_file(repr(e), "TCSDATE")
            return ""


class S4GUI(Header):

    sub_system = "S4GUI"

    def _initialize_kw_dataclass(self):
        keywords = [
            "CHANNEL1",
            "CHANNEL2",
            "CHANNEL3",
            "CHANNEL4",
            "OBJECT",
            "OBSERVER",
            "PROJID",
            "TCSMODE",
            "FILTER",
            "GUIVRSN",
            "CTRLINTE",
            "SYNCMODE",
            "INSTMODE",
            "OBSTYPE",
            "COMMENT",
        ]
        to_bool_kw = ["CHANNEL1", "CHANNEL2", "CHANNEL3", "CHANNEL4", "TCSMODE"]
        write_any_val = ["OBJECT", "OBSERVER", "PROJID", "GUIVRSN"]
        write_predefined_value = [
            "FILTER",
            "CTRLINTE",
            "SYNCMODE",
            "OBSTYPE",
            "INSTMODE",
        ]
        return Keywords_Dataclass(
            keywords=keywords,
            to_bool_kws=to_bool_kw,
            write_any_val=write_any_val,
            write_predefined_value=write_predefined_value,
        )

    def _write_COMMENT(self):
        kw = "COMMENT"
        try:
            if kw in self.hdr.keys():
                del self.hdr[kw]
            _json = {k.upper(): v for (k, v) in json.loads(self.json_string).items()}
            self.hdr[kw] = _json[kw]
        except Exception as e:
            self._write_log_file(repr(e), kw)
        return

    def fix_keywords(self):
        self._convert_to_boolean()
        self._write_any_value()
        self._write_predefined_value()
        self._write_COMMENT()
        return


class CCD(Header):

    sub_system = "CCD"
    trigger_modes = {0: "Internal", 6: "External"}
    acq_modes = {1: "Single Scan", 3: "Kinetics"}
    em_modes = ["Electron Multiplying", "Conventional"]
    shutter_modes = ["Auto", "Open", "Closed"]
    vclock_modes = ["Normal", "+1", "+2", "+3", "+4"]
    preamp_modes = ["Gain 1", "Gain 2"]
    vshift_modes = [0.6, 1.13, 2.2, 4.33]

    def _load_json(self, dict_header_jsons):
        _json = super()._load_json(dict_header_jsons)
        return self._fix_ccd_parameters(_json)

    def _initialize_kw_dataclass(self):
        keywords = [
            "FRAMEIND",
            "CCDTEMP",
            "TEMPST",
            "CCDSERN",
            "PREAMP",
            "READRATE",
            "EMGAIN",
            "VSHIFT",
            "FRAMETRF",
            "VCLKAMP",
            "ACQMODE",
            "EMMODE",
            "SHUTTER",
            "TRIGGER",
            "VBIN",
            "INITLIN",
            "INITCOL",
            "FINALLIN",
            "FINALCOL",
            "HBIN",
            "EXPTIME",
            "NFRAMES",
            "TGTEMP",
            "COOLER",
            "DATE-OBS",
            "UTTIME",
            "UTDATE",
        ]

        to_bool_kws = ["COOLER", "FRAMETRF"]
        to_float_kws = ["EXPTIME"]
        to_int_kws = [
            "VBIN",
            "HBIN",
            "FINALCOL",
            "FINALLIN",
            "INITCOL",
            "INITLIN",
            "FRAMEIND",
            "CCDSERN",
            "EMGAIN",
            "NFRAMES",
            "CCDTEMP",
            "TGTEMP",
        ]
        write_predefined_value = [
            "TEMPST",
            "TRIGGER",
            "ACQMODE",
            "EMMODE",
            "SHUTTER",
            "VSHIFT",
            "READRATE",
            "PREAMP",
            "VCLKAMP",
        ]
        write_any_val = ["DATE-OBS", "UTDATE", "UTTIME"]

        return Keywords_Dataclass(
            keywords=keywords,
            to_bool_kws=to_bool_kws,
            to_float_kws=to_float_kws,
            to_int_kws=to_int_kws,
            write_predefined_value=write_predefined_value,
            write_any_val=write_any_val,
        )

    def fix_keywords(self):
        self._convert_to_boolean()
        self._convert_to_float()
        self._convert_to_int()
        self._subs_idx_in_list()
        self._substitute_idx_in_dict()
        self._write_any_value()
        self._write_predefined_value()
        self._write_ccd_gain()
        self._write_read_noise()

        return

    def _write_read_noise(self):
        try:
            idx = self.find_index_tab()
            self.hdr["RDNOISE"] = read_noise[f"{self.hdr['CCDSERN']}"][idx]
        except Exception as e:
            self._write_log_file(repr(e), "RDNOISE")

    def _write_ccd_gain(self):
        try:
            idx = self.find_index_tab()
            self.hdr["GAIN"] = gains[f"{self.hdr['CCDSERN']}"][idx]
        except Exception as e:
            self._write_log_file(repr(e), "GAIN")

    def find_index_tab(self):
        _json = self._json
        index = 0
        readout_modes = [30.0, 20.0, 10.0, 1.0]
        if _json["EMMODE"] == "Conventional":
            index += 8
        readout_modes = [1.0, 0.1]
        index += 2 * readout_modes.index(_json["READRATE"])
        index += float(_json["PREAMP"][-1]) - 1
        return index

    def _fix_ccd_parameters(self, _json):
        _json["READRATE"] = self._write_READRATE(_json)
        _json["TRIGGER"] = self.trigger_modes[_json["TRIGGER"]]
        _json["ACQMODE"] = self.acq_modes[_json["ACQMODE"]]
        _json["EMMODE"] = self.em_modes[_json["EMMODE"]]
        _json["SHUTTER"] = self.shutter_modes[_json["SHUTTER"]]
        _json["VCLKAMP"] = self.vclock_modes[_json["VCLKAMP"]]
        _json["PREAMP"] = self.preamp_modes[_json["PREAMP"]]
        _json["VSHIFT"] = self.vshift_modes[_json["VSHIFT"]]
        _json["COOLER"] = _json["COOLER"] == 1
        _json["EXPTIME"] = float(_json["EXPTIME"])
        return _json

    @staticmethod
    def _write_READRATE(_json):
        _list = [30.0, 20.0, 10.0, 1.0]
        if _json["EMMODE"] == 1:
            _list = [1.0, 0.1]
        return _list[_json["READRATE"]]


class General_KWs(Header):

    sub_system = "GENERAL KW"

    def _initialize_kw_dataclass(self):
        keywords = [
            "FILENAME",
            "SEQINDEX",
            "NCYCLES",
            "NSEQ",
            "CYCLIND",
            "ACSVRSN",
            "ACSMODE",
            "CHANNEL",
        ]

        write_any_val = [
            "FILENAME",
            "ACSVRSN",
            "NSEQ",
            "NCYCLES",
            "CHANNEL",
            "SEQINDEX",
            "CYCLIND",
        ]
        to_bool_kw = ["ACSMODE"]
        replace_empty_kws = {
            "NAXIS": 2,
            "OBSLONG": -45.5825,
            "OBSLAT": -22.534,
            "OBSALT": 1864.0,
            "EQUINOX": 2000.0,
            "INSTRUME": "SPARC4",
            "SIMPLE": True,
            "BSCALE": 1,
            "BZERO": 32768,
            "BITPIX": 16,
        }
        return Keywords_Dataclass(
            keywords=keywords,
            replace_empty_kws=replace_empty_kws,
            to_bool_kws=to_bool_kw,
            write_any_val=write_any_val,
        )

    def _load_json(self, dict_header_jsons):
        _json = super()._load_json(dict_header_jsons)
        return self._fix_parameters(_json)

    @staticmethod
    def _fix_parameters(_json):
        _json["SEQINDEX"] = _json["SEQINDEX"] + 1
        _json["CYCLIND"] = _json["CYCLIND"] + 1
        return _json

    def fix_keywords(self):
        self._replace_empty_str()
        self._write_any_value()
        self._convert_to_boolean()


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

    write_any_val: list = field(default_factory=list)
    write_predefined_value: dict = field(default_factory=dict)

    idx_in_dict: dict = field(default_factory=dict)
    idx_in_list: dict = field(default_factory=dict)
    replace_empty_kws: dict = field(default_factory=dict)
