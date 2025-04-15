# Miscellaneous

This section presents a miscellaenous of topics related to the S4CCS development. These topics are not related to the documentation itself, but they contain information considered relevant to be used by the SPARC4 team.

## Defining standard acquisition mode: kinetics x single
To define the standard acquisition mode of SPARC4, we need first to characterize the overhead in the acquisition between two consecutive images in the Single Scan and the Kinetic modes for all the readout rates provided by the cameras. 
For that, the following experiment was developed. A EMCCD camera was connected to the S4CCS1 computer using the fiber optics set. Then, a series of 50 cycles of 1 full-frame each one was acquired for the Single Scan and the Kinetic modes. Also, a unique cube with 50 frames was acquired for the Kinetic mode. In all experiments, the used operation mode of the CCD was a readout rate of 30 MHz, a preamp gain 1, and an exposure time of 1e-5 s. For the first two experiments, the overhead between two consecutive cycles was calculated by the difference between the timestamp in the image header. This procedure was done for the entire series. For the last experiment, the overhead between frames was calculated by dividing the time interval needed to acquire the cycle, by the number of frames in the cube. The time interval of the cycle is the difference between the timestamp of the start of the acquisition and the time, in ns, for the start of the last frame. Table 2 presents the result obtained in the experiments.

Table 2. Overhead values between the acquisition of two consecutive images for the single scan and kinetic acquisition modes.

|Mode|Overhead (s)|Error (s)|
|----|-------------|---------|
|Single Scan|0.20|0.02|
|Kinetic (1 frame)|0.25|0.01|
|Kinetic (cube - 50 frames)|0.047||


## Ciclos Keep Clean
iXon Ultra cameras have a range of different Keep Clean Cycles that run depending on the actual model and the state the camera is in. The first Keep Clean Cycle runs while the camera is in an idle state, i.e. waiting for the PC to tell it to start an acquisition sequence. The next Keep Clean Cycle runs during an internal trigger kinetics series sequence. The final Keep Clean Cycle runs while the camera is waiting for an external trigger event to occur.

### Internal Keep clean
When the user configures a kinetics series acquisition, as well as defining the exposure time and the readout mode, they also define the number of scans to capture and the time between the scans. During the time between individual scans the sensor must be kept free of charge to ensure the data captured is a true reflection of the light that fell on it during the exposure period. The Keep Clean Cycle run during this time is very similar to that described in the Idle Keep Clean Cycle, in that the cycle is one vertical followed by a series of horizontals. In this mode, however, the number of times the cycle is repeated is determined by the cycle time set by the user. The Keep Clean Cycle is completed with a sufficient number of vertical shifts to ensure both the Image and Storage areas are charge free.

### External Keep Clean
The third Keep Clean Cycle is the External Keep Clean Cycle. This cycle uses a different sequence of horizontal and vertical clocking, as it must be able to respond to external events extremely rapidly, but at the same time keep the image area of the sensor charge free. The External Keep Clean Cycle consists of continuous cycles of one vertical shift, both Image and Storage, followed by reading out one full row, one horizontal shift (see Figure 14). When an external trigger is detected the current cycle completes before the exposure phase starts. It is worth noting that although the External Keep Clean Cycle will complete the current cycle, this will not result in the total loss of signal during this time period, as only one vertical shift will have occurred. For pulsed light of very short time duration, picoseconds (i.e. of the order of one vertical shift), the resultant image may appear to have shifted one row.

## Behavior of the readout noise with binning
Binning the pixels of the CCD is an option made available by the cameras where a number of NxN pixels can be binned before the readout, creating a super-pixel. This process has the advantage of reducing the image noise by a factor of 1/sqrt(NxN), since the readout noise is relative to each super-pixel instead of the individual pixels. Thus, in using a binning of 2x2, 4 pixels will be binned and the resulting noise will be 1/2 in comparison with these same pixels without binning. However, in our characterizations, we found a small increase of the read noise for larger values of binning (see this link). This is an unexpected behavior, since the readout process should be the same. For example, for a binning of 8x8, the read noise increased 47 % in comparison of the read noise for a binning of 1x1. Even so, the SNR of the superpixel counts is smaller than that if no binning is done. This happens because the signal is the same, but the total noise is smaller: 1.47 < 8.

Denis, voce acha que valeria a pena caracterizar isso por modo? Pensei em fazer um gráfico do número do valor do readout noise por superpixel em função do sqrt(do número de bins no super pixel)? Isso não precisaria ser feito no telescópio... pode ser feito um dia qualquer, deixando a aquisição rolar, enquanto vc faz outra coisa. 


## Fits creation
OPDAcquisition is the current software of the Picos dos Dias Observatory for the control of the scientific cameras. To save the acquired data, OPDAcquisition uses the Save_Image function of SDK. This function creates a FITS file with a unique extension. Both the header and the data are written in this extension. Also, it uses the GFITSIO library to write into the header the keywords related to TCS and other subsystems. However, to the best of our knowledge, this function does not allow us to write the data in parallel with the acquisition. For this reason, we use python 3.6 to save the FITS files. The data is a 2D array, and the header content is a json string.
(unused) However, we were having a problem related to the extensions of the fits file. In creating a new FITS, the GFITSIO also creates a predefined extension. In this extension, we can write new keywords, but no data can be written. To accomplish that, we should create a second extension with the same size of the acquired data. This creates a problem, once some tools that read and manipulate FITS files (like IRAF) require that both data and header should be in the first extension.
Using an issue on Github, the developer of the GFITSIO told us that we can write the data in the first fits extension if we resize its dimension. For this, the Resize_image function should be used. This procedure solved the problem and now we can create a fits file with the header and the data in the same extension.


## Image header keywords
The header content used in SPARC4 can be found in this link. A list of image header keywords needed for the pipeline is described in a specific section of the SPARC4 Pipeline Conceptual Design.
Reference links:
https://heasarc.gsfc.nasa.gov/docs/fcg/standard_dict.html
https://archive.eso.org/hdr?DpId=FORS2.2010-09-22T08:36:00.560

## Error log
Foi adicionada uma função de log de erro no S4CCS.
Todos os erros gerados durante a execução do programa são salvos em um arquivo txt chamado _error_log_file, criado dentro do diretório da noite
Quando um erro ocorrer no S4CCS, ele não impedirá a execução do programa, mas ficará registrado neste arquivo
No arquivo, os erros são separados naquilo que chamei de erros de execução e de segurança.
Um erro de execução está relacionado com a lógica ou bug de código. Se isto acontece, talvez eu precise corrigir alguma coisa no S4CCS
Um erro de segurança está relacionado as proteções que decidimos adicionar ao S4CCS sobre o modo de operação das câmeras


Quando um destes erros ocorrer, um led vermelho acenderá na região inferior do S4CCS (vejam a figura abaixo).
Além disso, um booleano com valor True será mandado na mensagem de status para o S4GUI.
Um erro de segurança impede que o S4CCS inicie uma nova exposição. Este erro pode ser corrigido reconfigurando o modo da câmera
Um erro de execução não necessariamente impede que o S4CCS realize uma aquisição, mas pode ter alguma outra consequência inesperada. Este erro ficará aceso no painel do S4CCS até que o usuário dê um CLEAN no botão que aparece ao lado da mensagem.


Por fim, é possível abrir o arquivo de log através do botão Open log que aparece na região inferior do S4CCS


## S4CCS Classes
Figure 4 presents the class diagram of S4CCS. Below, a brief description for each one of these classes is presented.
Channel: this class represents a channel of SPARC4 and it is responsible for all the tasks related to the control of the camera, such as the communication with the camera and S4GUI, start an exposure,  create a FITS file, etc. 
Simulated CCD camera: this class simulates the communication with a real camera. It has all the functions related to the data acquisition such as setting the operation parameters, starting an exposure, and reading the data. The CCD camera class inherits from this class.
CCD camera: this class uses the SDK package to communicate with the EMCCD cameras. Using this class, we can set the operation mode of the camera, start an exposure, verify the acquisition progress, and read the acquired data.
RxTx: this class uses a Labview package named queue to communicate with S4GUI. For that, the communication is done between two queues with the same name. The first one is on the S4CCS side. The second one is in a separate VI. This VI runs in parallel with S4CCS. Thus, even though the communication with the camera fails, the communication with S4GUI is still running. In a communication event, the message is sent by S4CCS to this VI using the transmitter queue. This VI, in its turn, sends the message to S4GUI using the TCP-IP protocol. Similarly, this VI receives the message sent by S4GUI and resends it to S4CCS using the receiver queue.
Save Image: this class is responsible for creating a FITS file and writing the header and the data into it. For that, it uses a python session running into the Labview platform. This session is controlled using the Python Toolkit class (see below). After an acquisition, the data and the header content is sent by S4CCS to another VI running in parallel. This VI is controlled by the Save Image class, which receives this information and uses it to create the FITS file using the Python Toolkit class.
State Machine: this is a class responsible to manage the tasks of the S4CCS over its execution. For example, the process of image acquisition is composed by the starting an exposure, verifying the acquisition progress, getting the acquired data, and writing it into the image. Each one of these steps there is a state of this class. So, over the iterations of the code, these states can be executed in the right order.
Header content: this class is responsible to manage the header data sent by S4GUI
Python Toolkit: this class wraps the Python Toolkit package developed by Enthought Company to control python the scripts used to save images
Stream: this class wraps the Stream package of Labview. It provides a structure to communicate with the control interface, similar to the RxTx class.

Figure 5. Class diagram of the Acquisition Control System.


## Flowchart of the image acquisition
Figure 5 presents the flowchart of the tasks executed by S4CCS when acquiring data. In this section a brief description of each one of these tasks is presented.
False: this is the standard state of S4CCS. In this state it does nothing.
Expose: in this state, S4CCS starts a new exposure. For that, the operation mode of the camera should be previously set.
Verify Acquisition: S4CCS verifies the progress of the acquisition. The information if the CCD is acquiring (boolean) and the current exposure time are obtained.
Are there acquired frames: if there is a new frame in the buffer of the camera, it will be saved in the next step. If not, S4CCS will pass to the abort acquisition state.
Abort Acquisition: if the camera is exposing and the user has pressed the abort acquisition button, the current exposure will be aborted. At this moment, the acquired data will be discarded and no FITS file is created
Get acquired data: S4CCS reads the data acquired by the camera
Send data/header message: the data and the image header are sent to another VI to be saved. This VI runs in parallel with S4CCS and it is responsible to write the header and data into the FITS file.
Still frames left: in a kinetic series, if there are still frames to be acquired, S4CCS will return to Verify Acquisition state. If not, S4CCS passes to the next step.
Still cycles left: if there are still existing cycles to be acquired, S4CCS passes to the Stop Acquisition state. If not, S4CCS ends the operation.
Pause Acquisition: in acquiring a series of images, if the user presses the Pause Acquisition button, S4CCS will pause the series after it finishes the acquisition of the current cycle. The series will be resumed when S4CCS receives the RESUME_ACQUISITION command. Otherwise, S4CCS goes to the next step.
Stop Acquisition: in acquiring a series of images, if the user presses the Stop Acquisition button, S4CCS will stop the series after it finishes the acquisition of the current cycle. Otherwise, S4CCS goes to the next cycle.


Figure 6. Flowchart of the states of a channel during an acquisition.


## Creating an installer in Labview
We can create an installer of our project to run it on a computer without needing to install Labview. Beyond the executable of our project, the installer contains all the drivers and third-party executables needed to run the code.
First, to create the installer, we need to add the executable of the project. The executable is created in a separated step, and it contains all the classes and libraries used by the code. Then, we should add the additional installers. Between these installers, the Labview run-time engine should be included. This engine is responsible for running the executable on a computer without Labview. Also, in this step, all the third-party drivers needed by the code should be included. For GEI, we have needed to add the drive to communicate with the serial port. Finally, pressing “build”, we can create the installer of the project.
Note: the creation of the S4CCS installer was done successfully. However, there were some problems in the creation of the GEI installer. These problems are described in the following. We did not have the installer of the driver for the communication with the serial-port. Apparently, this driver is included in a Labview package named Software Platform Bundle (in our case, the spring 2018 version, link). Unfortunately, the unique version of this software free for download is the last one. However, we downloaded this version and we installed it in our Labview 2018. Despite the difference in the software versions, we could create the GEI installer successfully. 