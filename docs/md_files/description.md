## Software description


S4CCS is a software developed using the LabVIEW 2018 programming language and the Software Development Kit (SDK) package, version 2.104.30000.0 (02-24-2020), made available by Oxford Instruments, to control the SPARC4 EMCCDs (see Figure 1). The operational system used for the development of S4CCS was the Windows Server 2016 Standard, version 1607. Using S4CCS, it is possible to configure all the parameters of the SPARC4 scientific detectors and acquire a series of images. The acquired data is saved in a Flexible Image Transport System (FITS) file. All the information related to the acquisition, as the instrument configuration and the telescope and weather information, are written into the FITS file header in parallel with the acquisition. Both the creation of the files and the edition of the headers are made using scripts in Python language. These scripts are run using a Python interpreter 3.6, running in the LabVIEW platform, using a native library for creating Python sessions. With the current S4CCS version, it is possible to acquire a series with up to 1400 images of 1024 x  1024 pixels, with an overhead of 4.5 ms between images. Besides, it is possible to acquire several series of images with an overhead of 120 ms between series, using the asynchronous mode of the instrument. 

<div style="text-align: center">
  <figure>
    <img src="../images/S4ACSp.png" alt="Exemplo de Imagem" width="400">
    <figcaption>Figura 1: Camera Control System front panel.</figcaption>
  </figure>
</div>


During the development of S4CCS, we verified that SDK is able to communicate with only one camera at a time. For the control of several cameras, the current active device should be set. This procedure could reduce the performance of the instrument if more than one camera is controlled by the same computer. This occurs because the reading of the acquired data by two different cameras can not be done simultaneously. To circumvent this problem, we decided to use one camera per computer and, for each computer, one instance of S4CCS.

S4CCS provides a series of security procedures to prevent a misuse of the EMCCD cameras. One of them is related to the configuration of these cameras' parameters. The SPARC4 cameras present several parameters for controlling their operation. The proper use of these parameters can be a little complex without some technical knowledge. For this reason, S4CCS performs a sequence of verification steps over the parameter values provided by S4GUI, raising a warning in the case of any inconsistency. 



## Communication 

Each S4CCS instance communicates with the SPARC4 and observatory sub-systems using the ZeroMQ protocol. This is an open-source standard capable of communicating with several different languages using the Ethernet. S4CCS uses two communication patterns. In the first one, it periodically publishes its status using the publish-subscribe pattern. S4GUI, in turn, uses these publications to access the status of the 4 channels at any time. Moreover, S4CCS uses this communication pattern to access the status of the instrument and the observatory sub-systems and get the information to be written into the image headers. The second pattern used by S4CCS is the request-reply. This pattern is used in receiving the requests sent by S4GUI, like a command to set the cameras configuration or even the trigger of the acquisition of an image series.

Figure 2. Flowchart of the acquisition system of SPARC4.


## Log files

In other to help diagnose the behavior of S4CCS during its use to control the SPARC4 cameras, its creates three files for each observation night. These files are used to log relevant information related to the operation of S4CCS. In the first file, unexpected errors that might happen while S4CCS is running are logged. The second file is used to log any inconsistency found between the information received from the sub-systems of the observatory and the formatting expected for the image header. For the last file, events considered important during the execution of S4CCS, as requests received from S4GUI or problems detected for an incoming configuration of the camera are logged.

## S4CCS operating modes

S4CCS presents two operation modes: real and simulated. In the real mode, S4CCS communicates with a real camera. Therefore, all the tasks performed by the software, as writing the operation mode, or reading the acquired image, occur using SDK to control this device. In the simulated mode, on the other hand, S4CCS simulates all the functions that require the use of SDK. In image acquisitions, for example, S4CCS creates an image filled with zeros with the same size request by the user. This mode was useful when performing engineering tests of the system, dispensing the use of a real camera.



## When S4CCS initializes
S4CCS does some tasks when it initializes. The main tasks are presented in this section.

The first task accomplished by S4CCS is to start the communication with the camera. For that, it verifies if the currently detected camera is an iXon Ultra. If it is, S4CCS continues with the initialization. If not, It will shut down the camera and pass to the next. This procedure was included because S4CCS was having problems in communicating with the camera when it runs in the same computer where the software AutoGuider of the OPD is running.


## Commands accepted by S4CCS

S4CCS provides a set of pre-configured commands that allow the control of the EMCCD cameras. Following, a brief description these commands is presented. 

- SET: allow the user to set a parameter of the cameras. The syntax should be `COMMAND <PARAMETER> <VALUE>`, where `PARAMETER` should be a valid parameter of the operation mode of the CCD, and `VALUE` should be a valid value of this parameter. The allowed parameter and their allowed values are presented in Section ??

- EXPOSE: start the acquisition of a series of images.  
- STATUS: return the current status of the camera. The returned parameters are:
    - ERROR: this parameter indicates if any error was generated during the execution.
    - SERIAL_NUMBER: the serial number of CCD.
    - ACQUIRING: the acquisition status.
    - CUBES_DONE: the number of cubes already acquired in the series.
    - FRAMES_DONE: the number of frames already acquired in the cube.
    - FRAME_EXPOSURE_TIME: the exposure time of the current frame.
    - FRAMES_DONE: the number of acquired frames.
    - LAST_IMAGE_NAME: the name of the last image saved.
    - CURRENT_TEMPERATURE: the current CCD temperature.
    - TEMPERATURE_STATUS: the current status of the temperature. The possible values for this parameter are:
        - TEMPERATURE_OFF: the cooler of the CCD is off.
        - TEMPERATURE_NOT_REACHED: when the CCD is reducing its internal temperature to reach the target.
        - TEMPERATURE_NOT_STABILIZED: when the CCD has reached the target temperature, but it still not stabilized.
        - TEMPERATURE_STABILIZED: the CCD reached the target temperature and this temperature is stabilized.
    - CCD_STATUS: the current status of the CCD. The possible values are:
        - IDLE: when the CCD is doing nothing.
        - ACTIVE: the CCD is exposing.


Besides this set of commands, there is another one that should only be used by S4GUI. These commands are related to the internal operation of S4GUI and S4CCS.

- WRITE_SETUP: with this command, S4GUI should send to S4CCS all the parameters related to the CCD operation mode presented in Section 2.1 as a JSON string
- ABORT_ACQUISITION: aborts the current acquisition and stops the current series. When the acquisition of the exposure is aborted, the acquired data is discarded and no file is created.
- STOP_ACQUISITION: when this command is sent, S4CCS will finish the current exposure, save the FITS file, and stop the series. 
- PAUSE_ACQUISITION: with this command, S4CCS will finish the current exposure, save the FITS file, and pause the current series. The series will be resumed only after receiving the RESUME_ACQUISITION command

### Treat command
Each Channel class has its own state machine class. This class is responsible for the control of the tasks performed by the channel. During an acquisition, this state machine executes some tasks like verify if the CCD is exposed, read the acquired data and save this data in a FITS file. However, it would be a problem if S4CCS receives a new command from S4GUI while it is executing these steps.
For this reason, all the commands received by S4CCS pass through a verification stage. In this stage, S4CCS will check if the command can be written into the state machine of the channel. Otherwise, it is ignored. This procedure is done to prevent a command being sent in some way that could harm the operation of S4CCS and the cameras. Following, a brief explanation of how these commands work is presented.
The ``SET``, ``GET``, and WRITE_SETUP commands will work when CCD is IDLE. The ``EXPOSE`` command works when the CCD is in the IDLE state and when it was not found any error during the execution of S4CCS. The ABORT_ACQUISITION will work when the CCD is exposing. The ``STOP_ACQUISITION``, `PAUSE_ACQUISITION`, and ``RESUME_ACQUISITION`` will work during the acquisition of a series of images. Finally, the WRITE_HEADER_DATA, STATUS, and STOP_APP commands work anytime. 

## Graphical Engineering Interface
For development purposes, GEI (see Figure 3) is being developed to communicate with S4CCS. GEI is a smaller version of S4GUI and it is used to execute tasks related to image acquisition, like configuring the operation mode of the cameras, starting the acquisition of a series of images, and stopping or aborting an acquisition. During the acquisition, GEI presents some of the parameters of the CCD status presented in Section 3.2, that are: the CCD on/off status, exposure time of the current acquisition, serial number, current temperature, last image name, temperature status, and the CCD status. Beyond these functionalities, using GEI we can set the observation type (ZERO, FLAT, OBJECT, FOCUS, DARK, or TEST), set the suffix of the image name, and write a comment for the image header. All these tasks can also be done by using the command line option.


<div style="text-align: center">
  <figure>
    <img src="../images/GEI_Front_Panel.png" alt="Exemplo de Imagem" width="400">
    <figcaption>Figura 2: Graphical Engineering Interface front panel.</figcaption>
  </figure>
</div>



## Verification of the parameters provided to S4CCS
S4CCS uses SDK to write the operation mode into the camera, and each parameter presented in Section 2.1 has its own SDK function. When S4CCS receives a new parameter, it calls the corresponding function of SDK. However, we have noticed that the camera only sets the new parameters when executing the StartAcquisition function. This process takes longer as larger is the number of parameters to be set. So, we have implemented a verification step every time S4CCS receives a new parameter. Only if the new parameter is different from the older one, it is written into the camera. This reduces the amount of time needed to execute the StartAcquisition function, at the same time that it works as a security procedure for the camera, avoiding executing SDK unnecessarily. Also, we have included the SDK function PrepareAcquisition as an additional step when configuring the cameras to mitigate the delay when starting an acquisition. Besides, if S4CCS receives a parameter that is not allowed to change, it returns an error message and does not allow to start an exposure.
In this step, we have included a verification of the minimum allowed exposure time as a function of the operation mode of the camera. This was done because we notice that, in frame transfer mode, there is a problem where the user can set an exposure time smaller than the readout time. When it happens, the real time in which the CCD is exposing is greater than the exposure time set by the user. This could lead to errors in measurements and for this reason, S4CCS limits the minimum exposure time of the camera. The used values for this process can be found in Table 3 of this article.


## Tasks management in image acquisition
As presented previously, S4CCS allows the user to acquire a series of images with a small overhead between them. To accomplish this, we performed a management of the tasks related to the image acquisition, optimizing this overhead. Between the main tasks that were managed, we could cite:
The writing data/header process is done in parallel with the acquisition.This process takes a significant amount of time. So, we planned to place it in an independent VI.  At the end of one acquisition, S4CCS sends the data and the header information to this VI. The VI appends in a queue each data/header received from S4CCS and starts to write them into the FITS files. As said before, S4CCS uses a python script to save and manipulate data.


## Simulated mode and real mode of S4CCS
S4CCS can operate in two different ways: the real mode and the simulated mode. In real mode, S4CCS communicates with a real camera. All the tasks, from the writing of the operation mode, until the reading the acquired image, occur with the use of this device. However, in the simulated mode, S4CCS simulates the communication with a CCD camera. All functions that use SDK are replaced by others that simulate the behavior of this device. For example, when GEI sends the STATUS command to get the acquiring on/off parameter, S4CCS calculates the elapsed time since the start of the exposure and returns if the CCD is acquiring or not. However, the data created by the simulated S4CCS is an array of zeros with the same size provided for the operation mode of the camera. There is a keyword in the image header to indicate whether the image was acquired in the simulated or real mode.
The simulated mode was implemented to help with S4CCS and S4GUI development. With this mode, we could test the communication between S4GUI and four S4CCS instances without needing four cameras. Also, the simulated mode will help with the commissioning of SPARC4. First, the operation of the instrument and all its sub-systems could be tested without depending on the cameras. Also, the acquisition of simulated images will allow testing the pipeline of data reduction with a configuration very close to the real one. 


## The image viewer
An image viewer (see Figure x) was developed to facilitate observations. The use of this viewer is recommended in doing the focus of the telescope and in recognizing the field. This viewer is composed of a graph window to visualize the last acquired image. With this graph, there are slides to control the image LUT, options for zooming in and zooming out the image, and a cursor to inspect the image pixel by pixel. Also, this viewer presents a button to disable image saving if the user wants to.

## When the communication with the camera fails (in development)
A management was implemented for the time when the communication with the CCD fails. If any kind of error occurs during the execution of S4CCS, it starts a procedure to restore the communication. In this procedure, S4CCS tries to reinitiate the camera for every time interval of 10 seconds. During this time, it is possible to restart the power supply of the CCDs or reconnect the USB cables. While this procedure is running, the communication with the S4GUI is still working, and the CCD status “COMMUNICATION_FAILED” is sent. If S4CCS is successful in restoring the communication, the software execution continues with the CCD in the IDLE state. If the communication is not restored in 5 minutes, S4CCS will stop.