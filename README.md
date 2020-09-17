# SPARC4-Acquisition-Control
 This is the Labview software of the acquisition control system of the new astronomical instrument Simultaneous Polarimeter and Rapid Camera in Four Bands (SPARC4). This software is designed to control two iXon Ultra EMCCD cameras of the Andor Technology company. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
![Software Development Kit (SDK)](https://andor.oxinst.com/products/software-development-kit/)

![GFITSIO](https://github.com/USNavalResearchLaboratory/GFITSIO)


### Installing
Clone this repo using ``` git clone https://github.com/DBernardes/SPARC4_ACS.git ```

## Running the tests
1. To perform this test, you need EMCCD to be connected to your PC.
2. Open the project SPARC4_AC.lvproj
3. Run the VI SPARC4_GUI.vi
4. Set the night directory where the acquired images should be saved.
5. Press Acquire button to start an acquisition. This would allows you to obtain a FITS files in your directory with data acquired by the camera.


## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Denis Bernardes**

See also the list of [contributors]() who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
