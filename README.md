# SPARC4 Acquisition Control System
This is the Labview software of the acquisition control system of the new astronomical instrument Simultaneous Polarimeter and Rapid Camera in Four Bands (SPARC4). This software is being developed to control two iXon Ultra EMCCD cameras of the Andor Technology company. It allows us to acquire image cubes for each camera, with the maximum cube size being 170 images full-frame (1024 x 1024 pixels). This software is able to write the acquired data in the machine hard disk, even during the cube acquisition. Also, it is possible to concatenate image cubes with a minimal delay between them. 

This readme presents a step-by-step tutorial to download the latest version of the code and run a simple test for image acquisition. Figure below presents an image of the interface that can be used to control the camera. However, this software is being developed only to control the cameras and its final version will not have an interface control. The presented interface is only for engineering purposes. 
 
![SPARC4_ACS_GUI](https://github.com/DBernardes/SPARC4_ACS/blob/master/GUI_LabView.png) 



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
