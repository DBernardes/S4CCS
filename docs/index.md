# SPARC4 Camera Control System (S4CCS)

The Simultaneous Polarimeter and Rapid Camera in Four Bands ([SPARC4](https://coast.lna.br/home/sparc4)) is a new astronomical instrument developed by *Instituto Nacional de Pesquisas Espaciais* (INPE), in collaboration with *Laboratório Nacional de Astrofísica* (LNA), that is currently installed on the Perkin-Elmer 1.6 m telescope of Picos dos Dias Observatory (in Portuguese, OPD). SPARC4 was developed to allow simultaneous photometric and polarimetric acquisitions in the g, r, i and, z bands of the Sloan Digital Sky Survey ([SDSS](https://www.sdss.org/)). The data acquisition is done using four Electron Multplying CCD cameras, one for each optical band of the instrument, produced by Oxford Instruments. The control of SPARC4 is done by a set of dedicated softwares. These softwares are the Camera Control System (S4CCS), the Instrument Control System, and the Graphical User Interface (S4GUI). S4CCS is responsible for controlling the scientific cameras of the instrument. S4ICS controls its moving mechanisms. S4GUI is an user interface the coordinates all the sub-systems of SPARC4.

Camera Control System (CCS) is a software developed using the graphical programming language Labview 2018 to control the four EMCCD cameras of the SPARC4 instrument. The communication with these cameras is done using the Software Development Kit (SDK) package provided by Andor Technology Company. Using CCS, we can configure the operation mode of the cameras. Based on the provided configuration, CCS allows the acquisition of a series of images, writing all the information related to the acquisition, like the instrument and its subsystems configuration, into the image  header.
During the development of this project, we have noticed that the control of two or more cameras by the same instance of CCS reduces the performance of the instrument. So, we decided to use four CCS instances, installed in four different computers to control the EMCCD cameras. The control of these four CCS instances is done using another application named Graphical User Interface (S4GUI). With the S4GUI, we were able to use the CCS instances to control the cameras. Also, the synchronization of the acquisition of each instance (channel) is done by using a digital pulse generator, or sync box. When the cameras are ready to start a new acquisition, the sync box sends a digital pulse for each one. 
To help with the development of CCS, Graphical Engineering Interface (GEI) was developed. GEI is a smaller version of S4GUI, and it allows you to execute some simple tasks related to image acquisition. Using GEI, we are able to pass to CCS the operation mode of CCDs and to acquire a series of images.
This document presents an overview of CCS development. Section 2 presents the hardware components used by CCS. Section 3 presents a detailed software description. Section 4 presents the definition of the standard acquisition mode of the CCDs.  Section 5 presents some results of the read noise of the cameras as a function of the binning of the pixels. Section 6 presents our solution for the creation of a FITS file. Section 7 presents the image header keywords written by the software. Section 8 presents the class diagram used in the development, and Section 9 presents the flowchart of the state machine of CCS during an acquisition.	

# Table of contents

* [Introduction](index.md)
* [Hardware](md_files/hardware.md)
* [Software description](md_files/description.md)




## References

* [SPARC4 Pipeline Conceptual Design](https://docs.google.com/document/d/1XMjYvKL8cMeHNLGMJ8LkWZRggZ6GBdIkDbU32HSNDus/edit?usp=sharing)