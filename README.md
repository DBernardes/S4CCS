 ![LabVIEW](https://a11ybadges.com/badge?logo=labview)
 ![Windows](https://img.shields.io/badge/Windows-0078D6?style=Flat&logo=windows&logoColor=white)
 [![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
 [![DOI](https://zenodo.org/badge/295755182.svg)](https://zenodo.org/doi/10.5281/zenodo.12796063)
 [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

 # SPARC4 Acquisition Control System

The Simultaneous Polarimeter and Rapid Camera in Four Bands ([SPARC4](https://coast.lna.br/home/sparc4)) is a new astronomical instrument developed by the *Instituto Nacional de Pesquisas Espaciais* (INPE), in collaboration with the *Laboratório Nacional de Astrofísica* (LNA), that is currently installed on the Perkin-Elmer 1.6 m telescope of Picos dos Dias Observatory (in Portuguese, OPD). SPARC4 was developed to allow simultaneous photometric and polarimetric acquisitions in the g, r, i and, z bands of the Sloan Digital Sky Survey ([SDSS](https://www.sdss.org/)). The acquisition of data is done using four Electron Multplying CCD cameras, one for each optical band of the instrument, produced by Oxford Instruments. 

The control of SPARC4 is done by a set of dedicated softwares. These softwares are the Acquisition Control System (S4ACS), the Instrument Control Software (S4ICSoft), and the Graphical User Interface (S4GUI). S4ACS is responsible for controlling the scientific cameras of the instrument, S4ICSoft controls its moving mechanisms, and S4GUI is an user interface that coordinates all the subsystems of the instrument.

S4ACS, in particular, was developed using the graphical programming language Laboratory Virtual Instrument Engineering Workbench (LabVIEW) 2018, together with the Software Development Kit (SDK) made available by the Oxford Instruments for the control of the cameras. The data acquired by the detectors are saved in the Flexible Image Transport System (FITS) files, created using python scripts. These scripts are run in the LabVIEW platform using a native library for creting Python environments. With the current version of S4ACS, a series of 1400 images of 1024 x 1024 pixels can be acquired with an overhead of 1.7 ms between images. Besides, several images series can be acquired with an overhead of 120 ms between series. 

This document provides a step-by-step guide to help you obtain a copy of the S4ACS executable on your local machine. Please note that S4ACS requires several dependencies to be installed beforehand: the Python interpreter, the Andor SDK, and the LabVIEW Runtime Engine. This tutorial assumes that these dependencies are already properly installed. If they are not, we recommend reaching out to the development team for assistance.


### Installing S4ACS
1. Download and extract the S4ACS .zip file found in this [link](https://github.com/DBernardes/S4ACS/releases/latest). 
1. Inside the extracted folder, there is a file name `acs_config_TEMPLATE.cgf`, which has the configuration that S4ACS needs when initializing. This file should be renamed to `acs_config.cfg` (without the `_TEMPLATE` string) and placed into the `C:\Users\<user_name>\SPARC4\ACS` directory. For more details about the content of this file, see the description presented in this [section](https://github.com/DBernardes/S4ACS?tab=readme-ov-file#description-of-the-inital-configuration-parameters).
1. Similarly, another important file is `socket_TEMPLATE.cfg`, which contains a default IP address for all the applications that S4ACS communicates with. This file should be renamed to `socket.cfg` (without the `_TEMPLATE` string) and placed into the `C:\Users\<user_name>\SPARC4\COMMAN` directory. However, note that the IP addresses of the instrument and/or observatory applications may have changed since the last S4ACS release. For this reason, it's recommended to review the contents of this file before launching S4ACS.
1. When running the S4ACS executable, an interface (see figure below) will show up. If everything was properly installed, you should be able to execute the software by pressing the white arrow at the top of the window.

<p align="center"><img src="docs/images/S4ACS_front_panel.png" alt="S4ACS front panel" width="500"/></p>


### Description of the inital configuration parameters

|Parameter|Description|
|----|-----|
|Channel| The current channel of the instrument (1, 2, 3, or 4)|
| ACS mode | The mode of S4ACS (real=0 or simulated=1)
| Communication | The type of communication that should be used (ZeroMQ=0 or TCP-IP=1)|
| Image path | The path where the acquired images should be saved|


## Usage

The control of S4ACS can be done by using ethernet request...

## Contributing

- Do this
- Do that

## Authors and acknowledgment

- **Denis Bernardes (main developer)**
  - [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat&logo=github&logoColor=white)](https://github.com/DBernardes) 
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=flat&logo=linkedin&logoColor=white)](www.linkedin.com/in/denisbernardes) 
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:denis.bernardes099@gmail.com)
  - Affiliation: Instituto Nacional de Pesquisas Espaciais (INPE).
  - Address: 1758 Astronautas Avenue, Jardim da Granja, São José dos Campos, São Paulo, Brazil.

- **Claudia Vilega Rodrigues (supervisor)**
  - Affiliation: Instituto Nacional de Pesquisas Espaciais (INPE).
  - Address: 1758 Astronautas Avenue, Jardim da Granja, São José dos Campos, São Paulo, Brazil.

- **Eder Martioli (supervisor)**
  - Affiliation: Laboratório Nacional de Astrofísica (LNA).
  - Address: 154 Estados Unidos Street, Nações, Itajubá, Minas Gerais, Brazil.

- **Luciano Fraga (supervisor)**
  - Affiliation: Laboratório Nacional de Astrofísica (LNA).
  - Address: 154 Estados Unidos Street, Nações, Itajubá, Minas Gerais, Brazil.

- **Orlando Verducci Júnior (contributor)**
  - Affiliation: Laboratório Nacional de Astrofísica (LNA).
  - Address: 154 Estados Unidos Street, Nações, Itajubá, Minas Gerais, Brazil.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
