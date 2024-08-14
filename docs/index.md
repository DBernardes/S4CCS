# SPARC4 Camera Control System (S4S4CCS)

# Table of contents

* [Introduction](index.md)
* [Hardware](md_files/hardware.md)
* [Software description](md_files/description.md)
* [Miscellaneous](md_files/misc.md)


The Simultaneous Polarimeter and Rapid Camera in Four Bands ([SPARC4](https://coast.lna.br/home/sparc4)) is a new astronomical instrument developed by *Instituto Nacional de Pesquisas Espaciais* (INPE), in collaboration with *Laboratório Nacional de Astrofísica* (LNA), that is currently installed on the Perkin-Elmer 1.6 m telescope of Picos dos Dias Observatory (in Portuguese, OPD). SPARC4 was developed to allow simultaneous photometric and polarimetric acquisitions in the g, r, i and, z bands of the Sloan Digital Sky Survey ([SDSS](https://www.sdss.org/)). The data acquisition is done using four Electron Multplying CCD cameras, one for each optical band of the instrument, produced by Oxford Instruments. 

The Camera Control System (S4CCS) is a software developed using the graphical programming language Laboratory Virtual Instrument Engineering Workbench (LabVIEW) 2018 together with the Software Development Kit (SDK) package provided by Oxford Instruments to control the four EMCCD cameras of SPARC4. Using S4CCS, we can configure the operation mode of the cameras and trigger the acquisition of a series of images. To control all the scientific cameras, one instance of S4CCS is run in a dedicated computer. The coordination of these instances, as well as other instrument sub-systems, is done by the Graphical User Interface of SPARC4 (S4GUI). 

This documentation presents the main aspected related to the S4CCS development and it is organized as follows. The [Hardware](md_files/hardware.md) presents the hardware components used by S4CCS. The [Software description](md_files/description.md) section presents a detailed description of S4CCS. The [Miscellaneous](md_files/misc.md) section presents a miscellanous of topics considered relevant by the development team.


## References

* [SPARC4 Pipeline Conceptual Design](https://docs.google.com/document/d/1XMjYvKL8cMeHNLGMJ8LkWZRggZ6GBdIkDbU32HSNDus/edit?usp=sharing)