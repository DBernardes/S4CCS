# Hardware

This section presents the hardware components used to run an S4CCS instace. These components are the detectors, the acquisition computers, and the optical fiber set.

## Detectors

The detectors used by SPARC4 are four Frame Transfer (FT) iXon Ultra 888 Electron Multiplying CCD (EMCCD) cameras, of 1024 x 1024 pixels of 13 &mu;m, produced by Oxford Instruments company. These cameras have a window and a coating optimized for the spectral band where they operate, which are similar to the g, r, i, and z bands of the Sloan Digital Sky Survey (SDSS) photometric system. These devices have the Electron Multiplying option, which allows the amplification of the acquired signal. Also, they have the FT option, which allows the acquisition of an exposure happens simultaneously with the reading of the previous one. For this reason, date acqiosition can be done with a maximum acquisition rate of 27 fps, for full-frame images. 

Tabela Below, all the parameters of the cameras operation mode are presented. These parameters are presented in the engineering tab of the S4GUI. Each line lists the keyword that represents a given parameter, the possible values in the first brackets, the default value in the second brackets, and a brief description of the parameter. 

Table 1: operation mode parameters of the SPARC4 cameras. In the table, the name, allowed values, default value, and a brief description are presented.
|Parameter|Type| Unit |Allowed values|Default value|Description|
|-|-|-|-|-|-|
|INITIAL_LINE   | integer | 1-1024 | 1 | Initial image line.|
|INITIAL_COLUMN | integer |1-1024| 1 | Initial image column.|
|FINAL_LINE| integer |1-1024 | 1024 | Final image line of the image.|
|FINAL_COLUMN |integer |1-1024| 1024| The final column of the image.|
|VBIN |integer |1-1024| 1 | Vertical binning of the pixels. The number of lines of the image (FINAL_LINE - INITIAL_LINE)  must be a multiple of the chosen value for the VBIN.|
|HBIN |integer |1-1024| 1 | Horizontal binning of the pixels. The number of columns of the image (FINAL_COLUMN - INITIAL_COLUMN) must be a multiple of the chosen value for the |HBIN.
|PREAMP |Gain 1, Gain 2| Gain 1| Type of the pre-amplification gain of the CCD (see Table 1).|
|EM_GAIN | 2-300| 2 | EM gain of the CCD. This parameter can be used only in the EM mode.|
|EM_MODE |Electron Multiplying, Conventional| Conventional| Output amplifier mode. This parameter constrains the possible values of the EM_GAIN and the READOUT_RATE.|
|READOUT_RATE |0.1, 1, 10, 20, 30| 1 MHz | Pixel readout rate (horizontal shift speed) in MHz. For the Conventional mode, the allowed values are 0.1 MHz and 1 MHz. For the EM mode, the allowed values are 1, 10, 20, and 30 MHz.|
|SHUTTER_MODE |Open, Closed| Open | Shutter operation mode.|
|SHUTTER_TTL |High, Low| Low |: signal to open shutter.|
|SHUTTER_OPENING_TIME |1-2E9| 50 | Time to open the shutter in milliseconds.|
|SHUTTER_CLOSING_TIME |1-2E9| 50| Time to close the shutter in milliseconds.|
|TRIGGER_MODE |Internal, External | External| Trigger mode for the start of the exposure.|
|VERTICAL_SHIFT_SPEED |0.6, 1.13, 2.2, 4.33| 0.6| Shift speed of the lines of CCD in MHz (see this link).|
|READ_MODE |Image| Image | Image read mode.|
|FRAME_TRANSFER |ON, OFF| ON | Frame transfer mode.|
|VERTICAL_CLOCK_VOLTAGE |Normal, +1, +2, +3, +4| Normal| Amplitude of the clock signal (see this link).|
|ACQUISITION_MODE |Single Scan, Kinetic| Kinetic| Image acquisition mode. |
|AD_CHANNEL |0 | 0 | Analogical-to-digital converter. The iXon cameras have only one AD channel.|

Besides these parameters, there is another set of parameters that can be set only by using the SET command (see Section 3.2). These parameters are:

|Parameter|Allowed values|Default value|Description|
|-----|-----|-----|-----|
|COOLER_POWER_STATUS |ON, OFF | OFF| CCD cooler status. |
|TEMP |-80, 20|20| CCD temperature. To set the temperature, the cooler of the CCD must be on.|
|EXPTIME |1e-5-2E9| 1| Exposure time in seconds.|
|#FRAMES |1- 2E9| 1| The number of frames in the cube. The number of frames can be set only if Kinetic mode is selected.|
|#CUBES |1 - 2E9| 1| The number of cubes in the series.|
|SUFFIX |string| ''| The suffix of the image name.|
|OBSTYPE |string|‘NONE’| The observation type (FLAT, DARK, ZERO, OBJECT, or NONE).|
|COMMENT |string|''| Comment of the image header.|
|OBJECT |string|''| The name of the observed object.|
|OBSERVER |string|''| Observer’s name.|
|FILTER|string|''| Filter used during acquisition (UBVRI).|
|CTRLINTE|string|''| Graphical interface used to control S4CCS.|
|INSTMODE|string|''| Instrument mode (photometric or polarimetric).|
|WAVEPLATE_POS|string|''| An integer related to the positions of the waveplate. |


Table 1. Gain and readout noise values for the four SPARC4 cameras as a function of the operation mode of the CCD.

|Em Mode |Readout Rate|Pre-amp|Gain||||Readout Noise|||
|--|--|--|--|--|--|--|--|--|--|
||(MHz)||(e-/ADU)||||(e-)|
|||9914|9915|9916|9917|9914|9915|9916|9917|
| EM | 30 | 1 | 17.2 | 17.9 | 17.2 | 17.6 | 197 | 219 | 209 | 188 |
| EM | 30 | 2 | 5.27 | 5.58 | 5.27 | 5.38 | 106 | 130 | 119 | 111 |
| EM | 20 | 1 | 16.4 | 16.8 | 16.4 | 16.8 | 141 | 138 | 158 | 148 |
| EM | 20 | 2 | 4.39 | 4.57 | 4.39 | 4.51 | 65.5 | 73.2 | 67.9 | 67.5 |
| EM | 10 | 1 | 16 | 15.9 | 16 | 16.2 | 77.5 | 80 | 76.1 | 78.6 |
| EM | 10 | 2 | 3.96 | 3.94 | 3.96 | 4 | 39.5 | 40 | 40 | 39.2 |
| EM | 1 | 1 | 15.9 | 16 | 15.9 | 16.1 | 24.9 | 24.4 | 24.8 | 25.1 |
| EM | 1 | 2 | 3.88 | 3.88 | 3.96 | 3.92 | 12.4 | 12.3 | 12.2 | 12.2 |
| Conv | 1 | 1 | 3.37 | 3.3 | 3.37 | 3.36 | 6.66 | 6.57 | 6.67 | 6.55 |
| Conv | 1 | 2 | 0.8 | 0.79 | 0.8 | 0.8 | 4.82 | 4.84 | 4.76 | 4.65 |
| Conv | 0.1 | 1 | 3.35 | 3.32 | 3.35 | 3.37 | 8.87 | 8.7 | 8.78 | 8.43 |
| Conv | 0.1 | 2 | 0.8 | 0.79 | 0.8 | 0.8 | 3.47 | 3.4 | 3.46 | 3.21 |

## Computers
There are four acquisition computers. They have been acquired using Fapemig funds and their model is Dell Server Poweredge R440: Intel 4108; RAM 16GB; 3 HDD 2TB; OME Server ConfigMgmt; Win Ser 2016; iDRAC9 Enterprise. 

## Fiber optic set 
The fiber optic set is composed of a cable of 50 m of optical fiber, a converter from fiber cable to USB 3.0 cable, and the PCI Express plate. The specifications of the fiber set can be viewed in this link.
If the PCI Express plate is installed in a computer, the converter should be energized, otherwise the computer is not able to start. Also, the converter should not be turned off while the computer is on. If this happens, the computer will freeze and reboot. For more information, see this link.

## Related links

- [Characterization of the SPARC4 CCDs](https://arxiv.org/abs/1806.02191)
- [Optimization of EMCCD operating parameters for the acquisitionsystem of SPARC4](https://arxiv.org/abs/2107.14769)

