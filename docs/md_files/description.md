## Software description


S4CCS (see Figure 1) is a software being written using the graphical programming language Labview 2018 to control the four iXon Ultra EMCCD cameras, produced by the Andor Technology company. To communicate with the cameras, S4CCS uses the development package SDK version 2.104.30000.0 (02-24-2020), available for Linux and Windows operating systems. The data acquired by the cameras is saved in a fits file using a python (version 3.6) script running in Labview platform. For that, a python integration toolkit for labview, developed by the Enthought company, is used. S4CCS is kept in the code hosting platform Github and can be found in this link. This link presents a conference abstract about S4CCS. 

<div style="text-align: center">
  <figure>
    <img src="../images/S4ACSp.png" alt="Exemplo de Imagem" width="400">
    <figcaption>Figura 1: Camera Control System front panel.</figcaption>
  </figure>
</div>


With the current S4CCS version, it is possible to set the configuration of all parameters presented in Section 2.1. We can acquire a kinetic series of images with the maximum size of 1470 frames (1024 x 1024 pixels), with a delay of 1.7 ms between frames. Also, it is possible to acquire a series of images with a delay of 180 ms between each series. 
During the development, we noticed a limitation in the use of SDK. SDK can communicate with one camera at a time. The control of two or more cameras can be done only by switching the active camera at that moment. This reduces the performance of the instrument. So, to circumvent this problem, we decided to use four computers, one computer for each camera. In each computer, there will be one instance of S4CCS. We found that Pirola, V., et al., in their article, found the same solution for the polarimeter Dipol-UF. 

The control of all the S4CCS instances is done using S4GUI (see Figure 2). S4GUI communicates with each S4CCS instance using the TCP-IP protocol. S4GUI allows to set the operation mode of the cameras and start the acquisition of a series of images. To synchronize the image acquisition between each camera, S4GUI uses the sync box (see this link for the manual of the manufacturer). When the cameras are ready to start the next acquisition, S4GUI controls the sync box to send four digital pulses with a synchronization error of 12 ps between them. Thus, we can acquire a simultaneous and synchronized series of images for the four cameras.


Figure 2. Flowchart of the acquisition system of SPARC4.

## When S4CCS initializes
S4CCS does some tasks when it initializes. The main tasks are presented in this section.

The first task accomplished by S4CCS is to start the communication with the camera. For that, it verifies if the currently detected camera is an iXon Ultra. If it is, S4CCS continues with the initialization. If not, It will shut down the camera and pass to the next. This procedure was included because S4CCS was having problems in communicating with the camera when it runs in the same computer where the software AutoGuider of the OPD is running.

Another important task made by S4CCS during initialization is to find the index of the lastest acquired image. For that, S4CCS searches for the largest index found in the name of the images present in the current directory. The name of the next images will be created based on this index.


## Communication with S4CCS

S4CCS is able to control one camera at a time. Each camera is represented in Labview by a class named Channel. Each instance of the Channel class can be controlled by an external application (for example, S4GUI) using the TCP-IP protocol. For that, each channel has a Virtual Instrument (VI), a code block in the Labview language, which runs in parallel with S4CCS. This VI is responsible for the communication between the channel and the external application.  
First, this VI creates a listener, based on the IP of the external application and a pre-configured serial port. This process creates an ID of the connection. Then, the VI waits for a connection request on this ID from the external application. Once the connection is established, the message is read, processed by the channel, answered, and closed. After this, a new connection ID will be created, and the VI will wait for a new connection request. This process is used to avoid some problems related to communication. For example, even though the communication request fails, the external application can request another one some time later without reinitiating S4CCS.
It should be highlighted that the TCP-IP communication requires a series of steps that stop the execution of the code while the connection is not established. For this reason, the communication between S4CCS and this VI is done using the Labview package named Queue. The communication occurs between two queues with the same name, but the creation of one queue does not require the creation of the other one. For each channel, two queues are created: one to transmite and other to receive messages. Figure 2 presents a schematic structure of the S4CCS communication system. An advantage of using this system is that the communication with S4GUI could still work even though the communication with the camera fails.


## Set of commands implemented in S4CCS
Besides the use of a graphical interface to control the cameras, S4CCS provides the option to control the acquisition by command line. For that, there are a set of pre-configured commands in S4CCS. Below, a brief description of each one of these commands is presented. 
SET/GET: allows the user to set and get, respectively, the CCD parameters. For the SET command, the syntax should be `COMMAND PARAMETER VALUE` (separated by whitespaces), where `PARAMETER` should be a valid parameter of the operation mode of the CCD, and `VALUE` should be a valid value of this parameter. The syntax for the GET command is the same as the SET without the `VALUE`. The allowed values for the `PARAMETER` are presented in Section 2.1.

- EXPOSE: this command allows the user to start the acquisition of a series of images.  
- STATUS: this command returns the current status of the camera. The returned parameters are:
    - ERROR: this parameter indicates if any error was generated during the execution.
    - SERIAL_NUMBER: the serial number of the CCD.
    - ACQUIRING: the acquisition status (boolean).
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