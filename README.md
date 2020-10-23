# SPARC4 Acquisition Control System
The acquisition control system (ACS) of the SPARC4 is written/developed using the graphical programming language Labview. The ACS is in version 1.5, and it is being developed to control two iXon Ultra EMCCD cameras of the Andor Technology company. The communication with the software is done through the TCP-IP protocol. The communication with the cameras is done using the Software Development Kit (SDK) package developed by Andor, available for Linux and Windows OS. With the current software versions, it is possible to acquire image cubes for each camera, with the maximum cube size of 170 images full-frame (1024 x 1024 pixels). It is possible to concatenate image cubes with full-frame images with a delay varying from 195 ms up to 950 ms between them, depending on the cube size. Also, there are a set of pre-configured commands to control the cameras: SET, GET, EXPOSE, and STATUS. The SET command allows the user to set a specific parameter. The GET command allows you to get the current value of a parameter. The EXPOSE command starts the exposure. The STATUS command gets the status of the CCD.

This README presents a step-by-step tutorial to download the latest version of the code and run a simple test for image acquisition. Figure below presents an image of the interface that can be used to control the camera. However, this software is being developed only to control the cameras and its final version will not have a control interface. The presented interface is only for engineering purposes. 

<p align="center">
  <img src="https://github.com/DBernardes/SPARC4_ACS/blob/master/SPARC4_ACS_GEI.png" />
</p>

 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
There are some packages that need to be installed before running the software. The first one is the Software Development Kit (SDK) developed by Andor Technology to control the CCDs. The second one is the GFITSIO package, used to save the data acquired by the camera in FITS format. 

![Software Development Kit (SDK)](https://andor.oxinst.com/products/software-development-kit/)

![GFITSIO](https://github.com/USNavalResearchLaboratory/GFITSIO)


### Installing
Clone this repo using ``` git clone https://github.com/DBernardes/SPARC4_ACS.git ```

## Running the tests
1. Before running the software, you need EMCCD to be connected to your PC.
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
