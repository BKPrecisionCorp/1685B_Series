#include "visa.h"
#include <iostream>
#include <Windows.h>
using namespace std;					

int main()
{
	ViStatus status;						
	ViSession defaultRM, device;		
	ViUInt32  retCount;			

	status = viOpenDefaultRM(&defaultRM); 
	if (status < VI_SUCCESS) { cout << "Error Opening Resource Manager"; cout << status << endl;}

	status = viOpen(defaultRM, "ASRL5::INSTR", VI_NULL, VI_NULL, &device);
	if (status < VI_SUCCESS) { cout << "Error Opening Communication: "; cout << status << endl; }

	short iIntfType;
	status = viGetAttribute(device, VI_ATTR_INTF_TYPE, &iIntfType);
	if (status < VI_SUCCESS) { cout << "Error Checking Interface"; cout << status << endl; }

	if (iIntfType == VI_INTF_ASRL) {													//Checking if interface is serial
		status = viSetAttribute(device, VI_ATTR_ASRL_BAUD, 9600);						// Sets BAUD rate to 9600
		if (status < VI_SUCCESS) { cout << "Error Editing Communication Attributes"; cout << status << endl; }
		status = viSetAttribute(device, VI_ATTR_ASRL_DATA_BITS, 8);						// Sets data bits to 8
		if (status < VI_SUCCESS) { cout << "Error Editing Communication Attributes"; cout << status << endl; }
		status = viSetAttribute(device, VI_ATTR_ASRL_PARITY, VI_ASRL_PAR_NONE);			// Sets parity to none
		if (status < VI_SUCCESS) { cout << "Error Editing Communication Attributes"; cout << status << endl; }
		status = viSetAttribute(device, VI_ATTR_ASRL_STOP_BITS, VI_ASRL_STOP_ONE);		// Sets stop bits to one
		if (status < VI_SUCCESS) { cout << "Error Editing Communication Attributes"; cout << status << endl; }
	}
	
	status = viSetAttribute(device, VI_ATTR_TMO_VALUE, 3000);									// Sets timeout to 3 seconds

	status = viWrite(device, (ViConstBuf)"VOLT010\r", 8, &retCount);							// Sends command to set voltage to 3 seconds
	if (status < VI_SUCCESS) { cout << "Error Setting Voltage"; cout << status << endl; }		// checks for errors.

	Sleep(100);
	viClose(device);
	viClose(defaultRM);
}

