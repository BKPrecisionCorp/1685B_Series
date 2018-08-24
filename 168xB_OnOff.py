#   168xB.py
#
#   Copyright {2017} {B&K Precision Corporation}

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import serial
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM8'
ser.timeout = 5
print(ser)
ser.open()
print(ser.is_open)
ser.write("VOLT220\r".encode())
print("Wrote")
resp = ser.read(2)
print(resp)
print("read")
ser.write("GETS\r".encode())
print(ser.read(8))
ser.write("GETD\r".encode())
print(ser.read(9))
ser.close()
