# SPARC4 Acquisition Control System

## Introduction

The Astrophysics Division of the *Instituto Nacional de Pesquisas Espaciais* (INPE) in collaboration with the *Laboratório Nacional de Astrofísica* (LNA) is developing a new astronomical instrument, the Simultaneous Polarimeter and Rapid Camera in Four Bands ([SPARC4](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/8446/844626/Concept-of-SPARC4--a-simultaneous-polarimeter-and-rapid-camera/10.1117/12.924976.full?casa_token=7b-hbhyqIMoAAAAA%3a99lzc7LW-gGeFuEs1N_7ZGdcFS1EiapC3jbzEYyrWT3PDiUP4RXPDEiR9IdfuRvDY7pPetsPx88&SSO=1)). SPARC4 will be installed on the 1.6 m Perkin-Elmer telescope at Observatório Pico dos Dias (OPD), Brazil, and it will allow image acquisition in the four Sloan Digital Sky Survey (SDSS) photometric bands: g, r, i and z. For the acquisition in each band (channel), there is a dedicated iXon Ultra EMCCD, produced by Andor Technology. These devices have an optical window and coating optimized for the spectral range in which they were designed to operate. These cameras also have frame transfer and electron-multiplying capabilities, allowing acquisition rates (AR) of up to 26 fps full-frame (1024 x 1024 pixels) even on faint astronomical objects, which requires high sensitivity for short exposure times.   

For the control of the SPARC4 cameras, it is being developed the SPARC4 acquisition control system (ACS). The ACS is in version 1.7 and its development is being done through the graphical programming language Labview with the Software Development Kit (SDK) package, made availabel by Andor, to comunicate with the cameras. This software will allow simultaneous and synchronized acquisition for the four SPARC4 channels. The synchronization will be made by a digital pulse generator developed by the Highlands Technology with a resolution of 10 ps between pulses. For each channel it is possible to acquire cubes with up to 170 full-frame images (1024 x x1024 pixels) with a delay of approximately 1.7 ms between exposures. It is also possible to concatenate cubes with 170 images with a delay of 950 ms between cubes. Thus, this system will allow the acquisition of synchronized image cubes for the four channels, a feature that is not available on the control software delivered by the manufacturer, the Andor Solis.

This README presents a step-by-step tutorial to download the latest version of the code and run a simple test for image acquisition. Figure below presents an image of the Graphical Engineering Interface (GEI) developed to control the ACS for engineering purposes. However, the ACS is being developed only to control the cameras and its final version will not have a graphical interface. 

<p align="center">
  <img src="https://github.com/DBernardes/SPARC4_ACS/blob/master/SPARC4_ACS_GEI.png" />
</p>

 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
There are some packages that need to be installed before running the software. The first one is the Software Development Kit (SDK) developed by Andor Technology to control the CCDs. The second one is the GFITSIO package, used to save the data acquired by the camera in FITS format. 

[Software Development Kit (SDK)](https://andor.oxinst.com/products/software-development-kit/)

[GFITSIO](https://github.com/USNavalResearchLaboratory/GFITSIO)


### Installing
Clone this repo using ``` git clone https://github.com/DBernardes/SPARC4_ACS.git ```

## Running the tests
1. Before running the software, you need to connect an Andor iXon Ultra EMCCD camera to your computer. If you do not have this camera, the ACS will run in the simulated mode. In this mode, the ACS uses a class that simulates the communication with the camera to create the FITS images.
2. Open the project SPARC4_AC.lvproj.
3. Run the VI SPARC4_GUI.vi.
4. Wait until the camera starts.
5. Set the night directory where the acquired images should be saved.
6. Press the Acquire button to start an acquisition. This would allow you to obtain a FITS files in your directory with the data acquired by the camera.

## Authors and Contact

* **Denis Bernardes**: 

email: denis.bernardes099@gmail.com 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
