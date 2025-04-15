 ![LabVIEW](https://a11ybadges.com/badge?logo=labview)
 ![Windows](https://img.shields.io/badge/Windows-0078D6?style=Flat&logo=windows&logoColor=white)
 [![GitHub license](https://badgen.net/github/license/Naereen/Strapdown.js)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
 [![DOI](https://zenodo.org/badge/295755182.svg)](https://zenodo.org/doi/10.5281/zenodo.12796063)
 [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

 # SPARC4 Acquisition Control System

The Simultaneous Polarimeter and Rapid Camera in Four Bands ([SPARC4](https://coast.lna.br/home/sparc4)) is a new astronomical instrument developed by *Instituto Nacional de Pesquisas Espaciais* (INPE), in collaboration with *Laboratório Nacional de Astrofísica* (LNA), that is currently installed on the Perkin-Elmer 1.6 m telescope of Picos dos Dias Observatory (in Portuguese, OPD). SPARC4 was developed to allow simultaneous photometric and polarimetric acquisitions in the g, r, i and, z bands of the Sloan Digital Sky Survey ([SDSS](https://www.sdss.org/)). The data acquisition is done using four Electron Multplying CCD cameras, one for each optical band of the instrument, produced by Oxford Instruments. The control of SPARC4 is done by a set of dedicated softwares. These softwares are the Acquisition Control System (S4ACS), the Instrument Control System, and the Graphical User Interface (S4GUI). S4ACS is responsible for controlling the scientific cameras of the instrument. S4ICS controls its moving mechanisms. S4GUI is an user interface the coordinates all the sub-systems of SPARC4.

For the development of S4ACS, the graphical programming language Laboratory Virtual Instrument Engineering Workbench (LabVIEW) 2018 was used together with the Software Development Kit (SDK) made available by the Oxford Instruments for the communication with the cameras. The data acquired by the cameras are saved in Flexible Image Transport System (FITS) files, created using python scripts. These scripts are run using an integrated library of LabVIEW for running Python interpreters. With the current version of S4ACS, it is possible to acquire a series of 1400 images of 1024 x 1024 pixels, with an overhead of 1.7 ms between images. Besides, it is possible to acquire several series of 1400 images, with an overhead of 120 ms between series. 
 
## Getting Started

These instructions will get you a copy of the .exe of S4ACS on your local. However, it should be highlighted that some dependencies are needed before running S4ACS, which are the Python interpreter, the Andor Software Development Kit (SDK) and the LabVIEW runtime engine. In this tutorial, we are considering that these dependencies were properly installed. 


### Installing S4ACS
1. Download and extract the S4ACS .zip file found in this [link](https://github.com/DBernardes/S4ACS/releases/latest). 
1. Inside the extracted folder, there is a file name `acs_config_TEMPLARE`.
This file has the configuration that S4ACS needs to run and it **must** be placed in the path `C:\Users\<user_name>\SPARC4\CCS\acs_config.cfg` (without the `_TEMPLATE` string).
1. Running the executable `S4ACS.exe`, an interface will show up. It should be similar to the image presented below. In this interface, set the `use config file` buttom in the most top panel to `NO`. This will set S4ACS to use the information presented in the `Init configuration` panel to initialize.
1. Configure the `Init configuration` panel according to your local environment. Table presented in this [link](https://github.com/DBernardes/S4ACS#description-of-the-inital-configuration-parameters) presents a description of the parameters cotained in this panel.
1. After this configuration, you should be able to run the software by pressing the white arrow at the top of the window.

<p align="center"><img src="docs/images/S4ACS_front_panel.png" alt="S4ACS front panel" width="500"/></p>


### Description of the inital configuration parameters

|Parameter|Description|
|----|-----|
|Remote IP| IP from where S4ACS will receive a query|
|Channel| The current channel of the instrument|
| CCS mode | The mode of S4ACS (real or simulated)
| Communication | The type of communication that should be used (TCP-IP or ZeroMQ)|
|Image path | The path where the acquired images should be saved|


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
