# Function library for 1685B, 1686B, 1687B and 1688B power supplies
#

currMult = 10
voltMult = 10

def spdWrite(ser, cmd):
    ser.write(cmd.encode())
    return ser.read_until(terminator=b'\r')

def spdQuery(ser, cmd):
    resp = []
    notDone = True
    ser.write(cmd.encode())
    while(notDone):
        r = ser.read_until(terminator=b'\r')
        print(r.decode())
        if(not(len(r) > 0)):
           notDone = False
        else:
            resp.append(r)
    return resp

def setCurrent(ser, value):
    """Set the current. Val is a number in normal format. i.e. 1.0 = 1.0 A"""
    val = int(value*currMult)
    print(spdWrite(ser, "CURR%03d\r"%val))

def setVoltage(ser, value):
    """Set the voltage. Val is a number in normal format. i.e. 1.0 = 1.0 V"""
    val = int(value*voltMult)
    print(spdWrite(ser, "VOLT%03d\r"%val))

def setComm(port, addr):
    """Port is 0 for USB/RS-232 and 1 for RS-485. Address 0-255"""
    print(spdWrite(ser, "CCOM"+address+str(port)+"%03d\r" % addr))

def getComm(ser):
    """Get the RS-485 address number. No parameters. Returns an array, first value is the comm type (0-USB/RS232, 1-RS485), and the address number 0-255 """
    resp = spdQuery(ser, "GCOM\r")
    return [int(chr(resp[0][0])), int(resp[0][1:3])]

def getMaxVoltCurr(ser):
    """Get the maximum voltage and current from the supply. The response is an array: [0] = voltage, [1] = current"""
    resp = spdQuery(ser, "GMAX\r")
    print(resp)
    return [int(resp[0][0:3])/10., int(resp[0][3:5])/10.]  

def getOVP(ser):
    """Get the Over Voltage Protection set point. Response is the value in volts."""
    resp = spdQuery(ser, "GOVP\r")
    print(resp)
    return int(resp[0])/10.  

def getData(ser):
    """Get the current, voltage and state. Response is an array: [0] - Current, [1] - Voltage, [2] - state (0-cv, 1-cc)"""
    resp = spdQuery(ser, "GETD\r")
    print(resp)
    return [int(resp[0][0:3])/10., int(resp[0][4:7])/10., int(chr(resp[0][8]))]

def getSettings(ser):
    """Get the current, voltage and state. Response is an array: [0] - Current, [1] - Voltage"""
    resp = spdQuery(ser, "GETS\r")
    print(resp)
    return [int(resp[0][0:3])/10., int(resp[0][3:6])/10.]
    
