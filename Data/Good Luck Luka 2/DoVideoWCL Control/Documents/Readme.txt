 
***************************************************
* ** DoVideoWCL Control SP1 **  
*
* Duma Optronics, Ltd.
* P.O.B. 3370, Nesher 20306, Israel.
*
* SERVICE:
*    Phone (972)-4-8200577
*    FAX   (972)-4-8204190
*
*    Please be ready to give the part,  
*    model and serial numbers from the 
*    BeamOn measurement system label.
* 
***************************************************
 
Version: 3.00
October 2013


Introduction: 
	How to use the DoVideoWCL.DLL for the Beam Profiler system
	in user-defined applications.
*********************************************************************

The DoVideoWCL.DLL  is a software package needed in order to write an application
program for the Beam Profiler system.

The Control contains easy to operate functions that enable measuring 
and creating your own applications under Windows XP / 7 environment.

The DoVideoWCL.DLL written in Microsoft C#.


Description of files
********************
The DoVideoWCL control consists of a set of files for operation under Windows.
The interface with the ActiveX is done by calls to its functions.
For proper operation – the corresponding header file should be included.

   -- DoVideoWCL.DLL		– 32 bit Control DLL for Windows.
   
   Additional DLL for hardware operation, which should be in working directory:

   -- DOVideoControl.dll
   -- DOVideoCapture.dll
   -- Interop.DOPROFILERCCDLib.dll
   -- Interop.PICTUREPROCESSORLib.dll
   -- AxInterop.DOPROFILERCCDLib.dll
   -- AxInterop.PICTUREPROCESSORLib.dll

			  should be in working directory.
   -- C# 		- Example program for using DoVideoWCL
   -- LabView 		- Example program for using DoVideoWCL
  
Please refer to the simple example program demonstrating how to use this
library.



