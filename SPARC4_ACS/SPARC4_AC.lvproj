<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="GEI Classes" Type="Folder">
			<Item Name="TCS.lvclass" Type="LVClass" URL="../TCS/TCS.lvclass"/>
			<Item Name="Channel GEI.lvclass" Type="LVClass" URL="../Channel GUI/Channel GEI.lvclass"/>
			<Item Name="SPARC4_GEI.lvclass" Type="LVClass" URL="../SPARC4_GUI/SPARC4_GEI.lvclass"/>
			<Item Name="Serial Communication.lvclass" Type="LVClass" URL="../Serial Communication/Serial Communication.lvclass"/>
			<Item Name="Filter_Wheel.lvclass" Type="LVClass" URL="../Filter_Wheel/Filter_Wheel.lvclass"/>
			<Item Name="FWCS_ACS_Iterator.lvclass" Type="LVClass" URL="../FWCS_ACS_Iterator/FWCS_ACS_Iterator.lvclass"/>
		</Item>
		<Item Name="GEI RxTx" Type="Folder">
			<Item Name="GUI_CH1_Comm_Stream.vi" Type="VI" URL="../GUI_CH1_Comm_Stream.vi"/>
			<Item Name="FWCS_Stream.vi" Type="VI" URL="../FWCS_Stream.vi"/>
			<Item Name="FWCS_TCPIP.vi" Type="VI" URL="../FWCS_TCPIP.vi"/>
			<Item Name="GUI_CH1_Comm_TCPIP_NEW.vi" Type="VI" URL="../GUI_CH1_Comm_TCPIP_NEW.vi"/>
			<Item Name="GUI_CH1_Comm_TCPIP.vi" Type="VI" URL="../GUI_CH1_Comm_TCPIP.vi"/>
		</Item>
		<Item Name="ACS RxTx" Type="Folder">
			<Item Name="CH1_Comm_Stream.vi" Type="VI" URL="../CH1_Comm_Stream.vi"/>
			<Item Name="CH1_Comm_TCPIP_NEW.vi" Type="VI" URL="../CH1_Comm_TCPIP_NEW.vi"/>
			<Item Name="CH2_Comm_TCPIP_NEW.vi" Type="VI" URL="../CH2_Comm_TCPIP_NEW.vi"/>
			<Item Name="CH3_Comm_TCPIP_NEW.vi" Type="VI" URL="../CH3_Comm_TCPIP_NEW.vi"/>
			<Item Name="CH4_Comm_TCPIP_NEW.vi" Type="VI" URL="../CH4_Comm_TCPIP_NEW.vi"/>
			<Item Name="CH1_Comm_TCPIP.vi" Type="VI" URL="../CH1_Comm_TCPIP.vi"/>
		</Item>
		<Item Name="TCS Comm" Type="Folder">
			<Item Name="TCS_Rx.vi" Type="VI" URL="../TCS_Rx.vi"/>
			<Item Name="TCS_Tx.vi" Type="VI" URL="../TCS_Tx.vi"/>
			<Item Name="TCS_VISA.vi" Type="VI" URL="../TCS_VISA.vi"/>
			<Item Name="TCS_Stream.vi" Type="VI" URL="../TCS_Stream.vi"/>
			<Item Name="TCS_Rx_VISA.vi" Type="VI" URL="../TCS_Rx_VISA.vi"/>
			<Item Name="TCS_Tx_VISA.vi" Type="VI" URL="../TCS_Tx_VISA.vi"/>
		</Item>
		<Item Name="Save Header" Type="Folder">
			<Item Name="CH1_Save_Header.vi" Type="VI" URL="../CH1_Save_Header.vi"/>
			<Item Name="CH3_Save_Header.vi" Type="VI" URL="../CH3_Save_Header.vi"/>
			<Item Name="CH4_Save_Header.vi" Type="VI" URL="../CH4_Save_Header.vi"/>
			<Item Name="CH2_Save_Header.vi" Type="VI" URL="../CH2_Save_Header.vi"/>
			<Item Name="CH1_Save_Header_Python.vi" Type="VI" URL="../CH1_Save_Header_Python.vi"/>
		</Item>
		<Item Name="Spreadsheets" Type="Folder" URL="../Spreadsheets">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="python scripts" Type="Folder" URL="../python scripts">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="ACS_version.txt" Type="Document" URL="../ACS_version.txt"/>
		<Item Name="ATMCD32D.dll" Type="Document" URL="../../../../../../Program Files (x86)/National Instruments/LabVIEW 2018/ATMCD32D.dll"/>
		<Item Name="SPARC4_GEI.vi" Type="VI" URL="../SPARC4_GEI.vi"/>
		<Item Name="S4ACS.vi" Type="VI" URL="../S4ACS.vi"/>
		<Item Name="TESTE.vi" Type="VI" URL="../TESTE.vi"/>
		<Item Name="old tests.vi" Type="VI" URL="../old tests.vi"/>
		<Item Name="Simulated_CCD_Camera.lvclass" Type="LVClass" URL="../Simulated_CCD_Camera/Simulated_CCD_Camera.lvclass"/>
		<Item Name="Simulated_Header.lvclass" Type="LVClass" URL="../Simulated_Header/Simulated_Header.lvclass"/>
		<Item Name="CCDCamera.lvclass" Type="LVClass" URL="../CCDCamera/CCDCamera.lvclass"/>
		<Item Name="State Machine.lvclass" Type="LVClass" URL="../State Machine/State Machine.lvclass"/>
		<Item Name="Channel.lvclass" Type="LVClass" URL="../Channel/Channel.lvclass"/>
		<Item Name="Header.lvclass" Type="LVClass" URL="../Header/Header.lvclass"/>
		<Item Name="Interface.lvclass" Type="LVClass" URL="../Interface/Interface.lvclass"/>
		<Item Name="Stream.lvclass" Type="LVClass" URL="../Stream/Stream.lvclass"/>
		<Item Name="Save Image.lvclass" Type="LVClass" URL="../Save Image/Save Image.lvclass"/>
		<Item Name="TCS_ACS.lvclass" Type="LVClass" URL="../TCS_ACS/TCS_ACS.lvclass"/>
		<Item Name="RxTx.lvclass" Type="LVClass" URL="../RxTx/RxTx.lvclass"/>
		<Item Name="TCPIP.lvclass" Type="LVClass" URL="../TCPIP/TCPIP.lvclass"/>
		<Item Name="Configuration File.lvclass" Type="LVClass" URL="../Configuration File/Configuration File.lvclass"/>
		<Item Name="Python Toolkit.lvclass" Type="LVClass" URL="../Python Toolkit/Python Toolkit.lvclass"/>
		<Item Name="SetDDGTriggerMode.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetDDGTriggerMode.vi"/>
		<Item Name="GetVSSpeed.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetVSSpeed.vi"/>
		<Item Name="SetVerticalSpeed.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetVerticalSpeed.vi"/>
		<Item Name="GetSizeOfCircularBuffer.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetSizeOfCircularBuffer.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="Shutter_mode typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/Shutter_mode typedef.ctl"/>
				<Item Name="Shutter_type typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/Shutter_type typedef.ctl"/>
				<Item Name="SetShutter.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetShutter.vi"/>
				<Item Name="HSSpeed_type typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/HSSpeed_type typedef.ctl"/>
				<Item Name="AcquisitionMode_mode typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/AcquisitionMode_mode typedef.ctl"/>
				<Item Name="ReadMode_mode typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/ReadMode_mode typedef.ctl"/>
				<Item Name="TriggerMode_mode typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/TriggerMode_mode typedef.ctl"/>
				<Item Name="CoolerOFF.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/CoolerOFF.vi"/>
				<Item Name="CoolerON.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/CoolerON.vi"/>
				<Item Name="ShutDown.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/ShutDown.vi"/>
				<Item Name="StartAcquisition.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/StartAcquisition.vi"/>
				<Item Name="GetStatus.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetStatus.vi"/>
				<Item Name="AbortAcquisition.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/AbortAcquisition.vi"/>
				<Item Name="GetCameraSerialNumber.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetCameraSerialNumber.vi"/>
				<Item Name="Add ECO For DLL.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Add ECO For DLL.vi"/>
				<Item Name="Error Code Offset global.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Error Code Offset global.vi"/>
				<Item Name="Get Error Source.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Get Error Source.vi"/>
				<Item Name="Join Strings.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Join Strings.vi"/>
				<Item Name="Subtract ECO For DLL.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Subtract ECO For DLL.vi"/>
				<Item Name="Add ECO For LabVIEW.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Add ECO For LabVIEW.vi"/>
				<Item Name="gfitsio.lvlib" Type="Library" URL="/&lt;userlib&gt;/gfitsio/gfitsio.lvlib"/>
				<Item Name="SetAcquisitionMode.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetAcquisitionMode.vi"/>
				<Item Name="SetReadMode.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetReadMode.vi"/>
				<Item Name="SetVSSpeed.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetVSSpeed.vi"/>
				<Item Name="SetImage.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetImage.vi"/>
				<Item Name="SetExposureTime.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetExposureTime.vi"/>
				<Item Name="SetADChannel.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetADChannel.vi"/>
				<Item Name="SetTriggerMode.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetTriggerMode.vi"/>
				<Item Name="SetHSSpeed.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetHSSpeed.vi"/>
				<Item Name="SetPreAmpGain.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetPreAmpGain.vi"/>
				<Item Name="SetEMCCDGain.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetEMCCDGain.vi"/>
				<Item Name="SetNumberKinetics.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetNumberKinetics.vi"/>
				<Item Name="SetFrameTransferMode.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetFrameTransferMode.vi"/>
				<Item Name="GetCameraHandle.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetCameraHandle.vi"/>
				<Item Name="GetImages16.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetImages16.vi"/>
				<Item Name="GetNumberNewImages.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetNumberNewImages.vi"/>
				<Item Name="Error Code Enum typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/Error Code Enum typedef.ctl"/>
				<Item Name="U32 To Error Code Enum.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/U32 To Error Code Enum.vi"/>
				<Item Name="GetTemperature.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetTemperature.vi"/>
				<Item Name="DDGTriggerMode_mode typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/DDGTriggerMode_mode typedef.ctl"/>
				<Item Name="GetRelativeImageTimes.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetRelativeImageTimes.vi"/>
				<Item Name="SetCurrentCamera.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetCurrentCamera.vi"/>
				<Item Name="Initialize.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/Initialize.vi"/>
				<Item Name="Error Code Handler.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/Error Code Handler.vi"/>
				<Item Name="SetVSAmplitude.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetVSAmplitude.vi"/>
				<Item Name="GetMetaDataInfo.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/GetMetaDataInfo.vi"/>
				<Item Name="SYSTEMTIME structure typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SYSTEMTIME structure typedef.ctl"/>
				<Item Name="U16 Array To SYSTEMTIME.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d_internal.llb/U16 Array To SYSTEMTIME.vi"/>
				<Item Name="SetTemperature.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SetTemperature.vi"/>
				<Item Name="SaveAsFITS.vi" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/SaveAsFITS.vi"/>
				<Item Name="FITS_type typedef.ctl" Type="VI" URL="/&lt;userlib&gt;/atmcd32d.llb/FITS_type typedef.ctl"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="VariantType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/VariantDataType/VariantType.lvlib"/>
				<Item Name="NI_Data Type.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/Data Type/NI_Data Type.lvlib"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="TCP Listen List Operations.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen List Operations.ctl"/>
				<Item Name="TCP Listen Internal List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen Internal List.vi"/>
				<Item Name="Internecine Avoider.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/Internecine Avoider.vi"/>
				<Item Name="TCP Listen.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen.vi"/>
				<Item Name="Python Integration Toolkit.lvlib" Type="Library" URL="/&lt;vilib&gt;/Enthought/Python Integration Toolkit/Python Integration Toolkit.lvlib"/>
				<Item Name="Is Path and Not Empty.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Is Path and Not Empty.vi"/>
				<Item Name="Registry refnum.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry refnum.ctl"/>
				<Item Name="Registry Handle Master.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Handle Master.vi"/>
				<Item Name="Close Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Close Registry Key.vi"/>
				<Item Name="Registry Simplify Data Type.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry Simplify Data Type.vi"/>
				<Item Name="Registry WinErr-LVErr.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry WinErr-LVErr.vi"/>
				<Item Name="Read Registry Value STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value STR.vi"/>
				<Item Name="Read Registry Value DWORD.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value DWORD.vi"/>
				<Item Name="Read Registry Value.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value.vi"/>
				<Item Name="Read Registry Value Simple STR.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple STR.vi"/>
				<Item Name="Read Registry Value Simple U32.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple U32.vi"/>
				<Item Name="Read Registry Value Simple.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Read Registry Value Simple.vi"/>
				<Item Name="STR_ASCII-Unicode.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/STR_ASCII-Unicode.vi"/>
				<Item Name="Registry View.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry View.ctl"/>
				<Item Name="Registry RtKey.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry RtKey.ctl"/>
				<Item Name="Registry SAM.ctl" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Registry SAM.ctl"/>
				<Item Name="Open Registry Key.vi" Type="VI" URL="/&lt;vilib&gt;/registry/registry.llb/Open Registry Key.vi"/>
				<Item Name="LVDateTimeRec.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVDateTimeRec.ctl"/>
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
			</Item>
			<Item Name="User32.dll" Type="Document" URL="User32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Atmcd32d.dll" Type="Document" URL="Atmcd32d.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Advapi32.dll" Type="Document" URL="Advapi32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="ACS" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{E412B969-F517-40EA-94F9-3D673C4A56B7}</Property>
				<Property Name="App_INI_GUID" Type="Str">{1CAAB5A8-8AC9-4B83-A2A4-75D1276E0708}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{EBD3E9D1-87EC-4D07-9D0E-E12F7D672B36}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">ACS</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/ACS</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{77B8811B-88C5-4D06-B0B4-2511D9D9BCC5}</Property>
				<Property Name="Bld_version.build" Type="Int">33</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">ACS.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/ACS/ACS.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/ACS/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{55B0EC18-08BE-4765-B542-8BB1A821C5D3}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/S4ACS.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/Save Header/CH4_Save_Header.vi</Property>
				<Property Name="Source[10].type" Type="Str">VI</Property>
				<Property Name="Source[11].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[11].itemID" Type="Ref">/My Computer/Save Header/CH2_Save_Header.vi</Property>
				<Property Name="Source[11].type" Type="Str">VI</Property>
				<Property Name="Source[12].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[12].itemID" Type="Ref">/My Computer/ACS_version.txt</Property>
				<Property Name="Source[13].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[13].itemID" Type="Ref">/My Computer/ATMCD32D.dll</Property>
				<Property Name="Source[14].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[14].itemID" Type="Ref">/My Computer/Save Header/CH1_Save_Header_Python.vi</Property>
				<Property Name="Source[14].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[14].type" Type="Str">VI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/Save Header/CH1_Save_Header.vi</Property>
				<Property Name="Source[2].type" Type="Str">VI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/ACS RxTx/CH1_Comm_TCPIP_NEW.vi</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">VI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/ACS RxTx/CH1_Comm_Stream.vi</Property>
				<Property Name="Source[4].type" Type="Str">VI</Property>
				<Property Name="Source[5].Container.applyProperties" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/GEI Classes</Property>
				<Property Name="Source[5].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[5].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[5].properties[1].type" Type="Str">Allow debugging</Property>
				<Property Name="Source[5].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[5].propertiesCount" Type="Int">2</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/ACS RxTx/CH2_Comm_TCPIP_NEW.vi</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[6].type" Type="Str">VI</Property>
				<Property Name="Source[7].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/ACS RxTx/CH3_Comm_TCPIP_NEW.vi</Property>
				<Property Name="Source[7].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[7].type" Type="Str">VI</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/ACS RxTx/CH4_Comm_TCPIP_NEW.vi</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[8].type" Type="Str">VI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/Save Header/CH3_Save_Header.vi</Property>
				<Property Name="Source[9].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">15</Property>
				<Property Name="TgtF_companyName" Type="Str">INPE</Property>
				<Property Name="TgtF_fileDescription" Type="Str">ACS</Property>
				<Property Name="TgtF_internalName" Type="Str">ACS</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 </Property>
				<Property Name="TgtF_productName" Type="Str">ACS</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{A2BA6095-6D2D-49C8-9CF6-24A881229297}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">ACS.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="GEI" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{FEA7FC95-23EB-458D-B83A-01364B665D2D}</Property>
				<Property Name="App_INI_GUID" Type="Str">{E2C59289-4EA0-472F-BA9C-CDDA5AE98BD3}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{4315F096-A985-40E7-8CBA-B2619F1F05A5}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">GEI</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/GEI</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{BC4F78AE-1AD6-4DF8-84A1-957EAE627C2D}</Property>
				<Property Name="Bld_version.build" Type="Int">20</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">GEI.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/GEI/GEI.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/GEI/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{291B3988-8B3D-4C51-9ACD-AB53E9432E47}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/SPARC4_GEI.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[10].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[10].itemID" Type="Ref">/My Computer/GEI RxTx/FWCS_TCPIP.vi</Property>
				<Property Name="Source[10].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[10].type" Type="Str">VI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/TCS Comm/TCS_Rx_VISA.vi</Property>
				<Property Name="Source[2].type" Type="Str">VI</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/TCS Comm/TCS_Tx_VISA.vi</Property>
				<Property Name="Source[3].type" Type="Str">VI</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/GEI RxTx/FWCS_Stream.vi</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].type" Type="Str">VI</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/GEI RxTx/GUI_CH1_Comm_TCPIP_NEW.vi</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">VI</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/GEI RxTx/GUI_CH1_Comm_Stream.vi</Property>
				<Property Name="Source[6].type" Type="Str">VI</Property>
				<Property Name="Source[7].Container.applyProperties" Type="Bool">true</Property>
				<Property Name="Source[7].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[7].itemID" Type="Ref">/My Computer/GEI Classes</Property>
				<Property Name="Source[7].properties[0].type" Type="Str">Run when opened</Property>
				<Property Name="Source[7].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[7].properties[1].type" Type="Str">Allow debugging</Property>
				<Property Name="Source[7].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[7].propertiesCount" Type="Int">2</Property>
				<Property Name="Source[7].type" Type="Str">Container</Property>
				<Property Name="Source[8].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[8].itemID" Type="Ref">/My Computer/TCS Comm/TCS_VISA.vi</Property>
				<Property Name="Source[8].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[8].type" Type="Str">VI</Property>
				<Property Name="Source[9].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[9].itemID" Type="Ref">/My Computer/TCS Comm/TCS_Stream.vi</Property>
				<Property Name="Source[9].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[9].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">11</Property>
				<Property Name="TgtF_enableDebugging" Type="Bool">true</Property>
				<Property Name="TgtF_fileDescription" Type="Str">GEI</Property>
				<Property Name="TgtF_internalName" Type="Str">GEI</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 </Property>
				<Property Name="TgtF_productName" Type="Str">GEI</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{2C2C9409-DE18-40E4-A7A8-E1DAFA54F994}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">GEI.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="GEI Installer" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">SPARC4_AC</Property>
				<Property Name="Destination[0].parent" Type="Str">{3912416A-D2E5-411B-AFEE-B63654D690C0}</Property>
				<Property Name="Destination[0].tag" Type="Str">{FBC3ECE0-9F33-4FE2-8847-30A8F44E38CB}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="DestinationCount" Type="Int">1</Property>
				<Property Name="DistPart[0].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[0].productID" Type="Str">{F19060DD-AA3B-4C3D-8E47-5792E36DFF3A}</Property>
				<Property Name="DistPart[0].productName" Type="Str">NI-488.2 Runtime 21.5</Property>
				<Property Name="DistPart[0].upgradeCode" Type="Str">{357F6618-C660-41A2-A185-5578CC876D1D}</Property>
				<Property Name="DistPart[1].flavorID" Type="Str">_deployment_</Property>
				<Property Name="DistPart[1].productID" Type="Str">{31B755F6-2A76-49DE-A454-4D6BD9D59470}</Property>
				<Property Name="DistPart[1].productName" Type="Str">NI-VISA Runtime 21.5</Property>
				<Property Name="DistPart[1].upgradeCode" Type="Str">{8627993A-3F66-483C-A562-0D3BA3F267B1}</Property>
				<Property Name="DistPart[10].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[10].productID" Type="Str">{3E3DA894-1DB5-472B-9EE1-9F0B16203718}</Property>
				<Property Name="DistPart[10].productName" Type="Str">NI 1588-2008 Network Management Runtime 21.3.0</Property>
				<Property Name="DistPart[10].upgradeCode" Type="Str">{AA333F93-319C-4ECC-8388-D40D5F7582F4}</Property>
				<Property Name="DistPart[2].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[2].productID" Type="Str">{FEB8324C-1913-4673-9B2E-89F3D074E0BD}</Property>
				<Property Name="DistPart[2].productName" Type="Str">NI LabVIEW Runtime 2018</Property>
				<Property Name="DistPart[2].SoftDep[0].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[0].productName" Type="Str">NI LabVIEW Runtime 2018 Non-English Support.</Property>
				<Property Name="DistPart[2].SoftDep[0].upgradeCode" Type="Str">{3C68D03D-EF38-41B5-9977-E27520759DD6}</Property>
				<Property Name="DistPart[2].SoftDep[1].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[1].productName" Type="Str">NI ActiveX Container</Property>
				<Property Name="DistPart[2].SoftDep[1].upgradeCode" Type="Str">{1038A887-23E1-4289-B0BD-0C4B83C6BA21}</Property>
				<Property Name="DistPart[2].SoftDep[10].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[10].productName" Type="Str">NI mDNS Responder 17.0</Property>
				<Property Name="DistPart[2].SoftDep[10].upgradeCode" Type="Str">{9607874B-4BB3-42CB-B450-A2F5EF60BA3B}</Property>
				<Property Name="DistPart[2].SoftDep[11].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[11].productName" Type="Str">NI Deployment Framework 2018</Property>
				<Property Name="DistPart[2].SoftDep[11].upgradeCode" Type="Str">{838942E4-B73C-492E-81A3-AA1E291FD0DC}</Property>
				<Property Name="DistPart[2].SoftDep[12].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[12].productName" Type="Str">NI Error Reporting 2018</Property>
				<Property Name="DistPart[2].SoftDep[12].upgradeCode" Type="Str">{42E818C6-2B08-4DE7-BD91-B0FD704C119A}</Property>
				<Property Name="DistPart[2].SoftDep[2].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[2].productName" Type="Str">Math Kernel Libraries 2017</Property>
				<Property Name="DistPart[2].SoftDep[2].upgradeCode" Type="Str">{699C1AC5-2CF2-4745-9674-B19536EBA8A3}</Property>
				<Property Name="DistPart[2].SoftDep[3].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[3].productName" Type="Str">Math Kernel Libraries 2018</Property>
				<Property Name="DistPart[2].SoftDep[3].upgradeCode" Type="Str">{33A780B9-8BDE-4A3A-9672-24778EFBEFC4}</Property>
				<Property Name="DistPart[2].SoftDep[4].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[4].productName" Type="Str">NI Logos 18.0</Property>
				<Property Name="DistPart[2].SoftDep[4].upgradeCode" Type="Str">{5E4A4CE3-4D06-11D4-8B22-006008C16337}</Property>
				<Property Name="DistPart[2].SoftDep[5].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[5].productName" Type="Str">NI TDM Streaming 18.0</Property>
				<Property Name="DistPart[2].SoftDep[5].upgradeCode" Type="Str">{4CD11BE6-6BB7-4082-8A27-C13771BC309B}</Property>
				<Property Name="DistPart[2].SoftDep[6].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[6].productName" Type="Str">NI LabVIEW Web Server 2018</Property>
				<Property Name="DistPart[2].SoftDep[6].upgradeCode" Type="Str">{0960380B-EA86-4E0C-8B57-14CD8CCF2C15}</Property>
				<Property Name="DistPart[2].SoftDep[7].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[7].productName" Type="Str">NI LabVIEW Real-Time NBFifo 2018</Property>
				<Property Name="DistPart[2].SoftDep[7].upgradeCode" Type="Str">{EF4708F6-5A34-4DBA-B12B-79CC2004E20B}</Property>
				<Property Name="DistPart[2].SoftDep[8].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[8].productName" Type="Str">NI VC2010MSMs</Property>
				<Property Name="DistPart[2].SoftDep[8].upgradeCode" Type="Str">{EFBA6F9E-F934-4BD7-AC51-60CCA480489C}</Property>
				<Property Name="DistPart[2].SoftDep[9].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[2].SoftDep[9].productName" Type="Str">NI VC2015 Runtime</Property>
				<Property Name="DistPart[2].SoftDep[9].upgradeCode" Type="Str">{D42E7BAE-6589-4570-B6A3-3E28889392E7}</Property>
				<Property Name="DistPart[2].SoftDepCount" Type="Int">13</Property>
				<Property Name="DistPart[2].upgradeCode" Type="Str">{3B195EBF-4A09-46E6-8EAD-931568C1344C}</Property>
				<Property Name="DistPart[3].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[3].productID" Type="Str">{64949A3D-2F4C-48A7-8834-93935C89AF2C}</Property>
				<Property Name="DistPart[3].productName" Type="Str">NI-VISA .NET Runtime 21.5</Property>
				<Property Name="DistPart[3].upgradeCode" Type="Str">{33687859-DC67-437F-A652-689B14A1C74C}</Property>
				<Property Name="DistPart[4].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[4].productID" Type="Str">{4CABF148-0D5C-4508-9965-E22FD0550FCA}</Property>
				<Property Name="DistPart[4].productName" Type="Str">NI-VISA .NET Runtime 17.5</Property>
				<Property Name="DistPart[4].upgradeCode" Type="Str">{33687859-DC67-437F-A652-689B14A1C74C}</Property>
				<Property Name="DistPart[5].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[5].productID" Type="Str">{009E3668-C399-4959-8AC1-A9421C0F9E6A}</Property>
				<Property Name="DistPart[5].productName" Type="Str">NI System Web Server 2018</Property>
				<Property Name="DistPart[5].upgradeCode" Type="Str">{FCF64B73-B7D4-4971-8F11-24BAF7CC3E6C}</Property>
				<Property Name="DistPart[6].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[6].productID" Type="Str">{FB8B8893-3059-4F1C-A549-437F0642394A}</Property>
				<Property Name="DistPart[6].productName" Type="Str">NI LabWindows/CVI Shared Runtime 2020 f1</Property>
				<Property Name="DistPart[6].SoftDep[0].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[0].productName" Type="Str">Analysis Support</Property>
				<Property Name="DistPart[6].SoftDep[0].upgradeCode" Type="Str">{86208B51-159E-4F6F-9C62-0D5EFC9324D8}</Property>
				<Property Name="DistPart[6].SoftDep[1].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[1].productName" Type="Str">.NET Support</Property>
				<Property Name="DistPart[6].SoftDep[1].upgradeCode" Type="Str">{0DDB211A-941B-4125-9518-E81E10409F2E}</Property>
				<Property Name="DistPart[6].SoftDep[2].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[2].productName" Type="Str">Network Variable Support</Property>
				<Property Name="DistPart[6].SoftDep[2].upgradeCode" Type="Str">{15CE39FE-1354-484D-B8CA-459077449FB3}</Property>
				<Property Name="DistPart[6].SoftDep[3].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[3].productName" Type="Str">Network Streams Support</Property>
				<Property Name="DistPart[6].SoftDep[3].upgradeCode" Type="Str">{40A5AD7F-4BAF-4A5C-8B56-426B84F75C05}</Property>
				<Property Name="DistPart[6].SoftDep[4].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[4].productName" Type="Str">TDMS Support</Property>
				<Property Name="DistPart[6].SoftDep[4].upgradeCode" Type="Str">{5A8AF88D-486D-4E30-A7A5-8D8A039BBEBF}</Property>
				<Property Name="DistPart[6].SoftDepCount" Type="Int">5</Property>
				<Property Name="DistPart[6].upgradeCode" Type="Str">{80D3D303-75B9-4607-9312-E5FC68E5BFD2}</Property>
				<Property Name="DistPart[7].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[7].productID" Type="Str">{F2301F6E-7BFE-4E8A-B824-DB312F771EDE}</Property>
				<Property Name="DistPart[7].productName" Type="Str">NI-488.2 Configuration Support 21.5</Property>
				<Property Name="DistPart[7].upgradeCode" Type="Str">{123307D2-8A89-48BC-A4E7-18C51BDCCED4}</Property>
				<Property Name="DistPart[8].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[8].productID" Type="Str">{2BB15880-EA12-40AA-B577-27419E77E2F9}</Property>
				<Property Name="DistPart[8].productName" Type="Str">NI LabVIEW Runtime 2019 SP1 f5</Property>
				<Property Name="DistPart[8].SoftDep[0].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[0].productName" Type="Str">NI ActiveX Container</Property>
				<Property Name="DistPart[8].SoftDep[0].upgradeCode" Type="Str">{1038A887-23E1-4289-B0BD-0C4B83C6BA21}</Property>
				<Property Name="DistPart[8].SoftDep[1].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[1].productName" Type="Str">NI Deployment Framework 2019</Property>
				<Property Name="DistPart[8].SoftDep[1].upgradeCode" Type="Str">{838942E4-B73C-492E-81A3-AA1E291FD0DC}</Property>
				<Property Name="DistPart[8].SoftDep[10].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[10].productName" Type="Str">NI VC2015 Runtime</Property>
				<Property Name="DistPart[8].SoftDep[10].upgradeCode" Type="Str">{D42E7BAE-6589-4570-B6A3-3E28889392E7}</Property>
				<Property Name="DistPart[8].SoftDep[11].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[11].productName" Type="Str">NI TDM Streaming 19.0</Property>
				<Property Name="DistPart[8].SoftDep[11].upgradeCode" Type="Str">{4CD11BE6-6BB7-4082-8A27-C13771BC309B}</Property>
				<Property Name="DistPart[8].SoftDep[2].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[2].productName" Type="Str">NI Error Reporting 2019</Property>
				<Property Name="DistPart[8].SoftDep[2].upgradeCode" Type="Str">{42E818C6-2B08-4DE7-BD91-B0FD704C119A}</Property>
				<Property Name="DistPart[8].SoftDep[3].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[3].productName" Type="Str">NI LabVIEW Real-Time NBFifo 2019</Property>
				<Property Name="DistPart[8].SoftDep[3].upgradeCode" Type="Str">{8386B074-C90C-43A8-99F2-203BAAB4111C}</Property>
				<Property Name="DistPart[8].SoftDep[4].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[4].productName" Type="Str">NI LabVIEW Runtime 2019 SP1 Non-English Support.</Property>
				<Property Name="DistPart[8].SoftDep[4].upgradeCode" Type="Str">{446D49A5-F830-4ADF-8C78-F03284D6882D}</Property>
				<Property Name="DistPart[8].SoftDep[5].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[5].productName" Type="Str">NI Logos 19.0</Property>
				<Property Name="DistPart[8].SoftDep[5].upgradeCode" Type="Str">{5E4A4CE3-4D06-11D4-8B22-006008C16337}</Property>
				<Property Name="DistPart[8].SoftDep[6].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[6].productName" Type="Str">NI LabVIEW Web Server 2019</Property>
				<Property Name="DistPart[8].SoftDep[6].upgradeCode" Type="Str">{0960380B-EA86-4E0C-8B57-14CD8CCF2C15}</Property>
				<Property Name="DistPart[8].SoftDep[7].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[7].productName" Type="Str">NI mDNS Responder 19.0</Property>
				<Property Name="DistPart[8].SoftDep[7].upgradeCode" Type="Str">{9607874B-4BB3-42CB-B450-A2F5EF60BA3B}</Property>
				<Property Name="DistPart[8].SoftDep[8].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[8].productName" Type="Str">Math Kernel Libraries 2017</Property>
				<Property Name="DistPart[8].SoftDep[8].upgradeCode" Type="Str">{699C1AC5-2CF2-4745-9674-B19536EBA8A3}</Property>
				<Property Name="DistPart[8].SoftDep[9].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[8].SoftDep[9].productName" Type="Str">Math Kernel Libraries 2018</Property>
				<Property Name="DistPart[8].SoftDep[9].upgradeCode" Type="Str">{33A780B9-8BDE-4A3A-9672-24778EFBEFC4}</Property>
				<Property Name="DistPart[8].SoftDepCount" Type="Int">12</Property>
				<Property Name="DistPart[8].upgradeCode" Type="Str">{7D6295E5-8FB8-4BCE-B1CD-B5B396FA1D3F}</Property>
				<Property Name="DistPart[9].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[9].productID" Type="Str">{BD8C6E18-4165-4F92-9010-60D2E8A50F9A}</Property>
				<Property Name="DistPart[9].productName" Type="Str">NI DataSocket 19.0</Property>
				<Property Name="DistPart[9].upgradeCode" Type="Str">{81A7E53E-9524-41CE-90D3-7DD3D90B6C58}</Property>
				<Property Name="DistPartCount" Type="Int">11</Property>
				<Property Name="INST_autoIncrement" Type="Bool">true</Property>
				<Property Name="INST_buildLocation" Type="Path">../builds/GEI Installer</Property>
				<Property Name="INST_buildLocation.type" Type="Str">relativeToCommon</Property>
				<Property Name="INST_buildSpecName" Type="Str">GEI Installer</Property>
				<Property Name="INST_defaultDir" Type="Str">{FBC3ECE0-9F33-4FE2-8847-30A8F44E38CB}</Property>
				<Property Name="INST_productName" Type="Str">GEI Installer</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.3</Property>
				<Property Name="InstSpecBitness" Type="Str">32-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">18008007</Property>
				<Property Name="MSI_distID" Type="Str">{DEE7EF4A-CBDC-42E3-BF70-42F786686AB5}</Property>
				<Property Name="MSI_osCheck" Type="Int">0</Property>
				<Property Name="MSI_upgradeCode" Type="Str">{17373605-A9C9-44E0-936C-6FE1E8FDF4BD}</Property>
				<Property Name="RegDest[0].dirName" Type="Str">Software</Property>
				<Property Name="RegDest[0].dirTag" Type="Str">{DDFAFC8B-E728-4AC8-96DE-B920EBB97A86}</Property>
				<Property Name="RegDest[0].parentTag" Type="Str">2</Property>
				<Property Name="RegDestCount" Type="Int">1</Property>
				<Property Name="Source[0].dest" Type="Str">{FBC3ECE0-9F33-4FE2-8847-30A8F44E38CB}</Property>
				<Property Name="Source[0].File[0].dest" Type="Str">{FBC3ECE0-9F33-4FE2-8847-30A8F44E38CB}</Property>
				<Property Name="Source[0].File[0].name" Type="Str">GEI.exe</Property>
				<Property Name="Source[0].File[0].Shortcut[0].destIndex" Type="Int">0</Property>
				<Property Name="Source[0].File[0].Shortcut[0].name" Type="Str">GEI</Property>
				<Property Name="Source[0].File[0].Shortcut[0].subDir" Type="Str">GEI Installer</Property>
				<Property Name="Source[0].File[0].ShortcutCount" Type="Int">1</Property>
				<Property Name="Source[0].File[0].tag" Type="Str">{2C2C9409-DE18-40E4-A7A8-E1DAFA54F994}</Property>
				<Property Name="Source[0].FileCount" Type="Int">1</Property>
				<Property Name="Source[0].name" Type="Str">GEI</Property>
				<Property Name="Source[0].tag" Type="Ref">/My Computer/Build Specifications/GEI</Property>
				<Property Name="Source[0].type" Type="Str">EXE</Property>
				<Property Name="SourceCount" Type="Int">1</Property>
			</Item>
		</Item>
	</Item>
</Project>
