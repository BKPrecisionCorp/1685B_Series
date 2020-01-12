from tkinter import *
import serial
import lib1685b

ser = serial.Serial("/dev/ttyUSB0")
ser.timeout = 0.1

win = Tk()



def setVoltage():
    val = voltscale.get()
    print(val)
    lib1685b.setVoltage(ser, val)

def setCurrent():
    val = currscale.get()
    print(val)
    lib1685b.setCurrent(ser, val)


    
currscale = Scale(win, from_=0, to=10, resolution=0.1, orient=HORIZONTAL, length=300)
currscale.pack()
Button(win, text="Set Current", command=setCurrent).pack()

voltscale = Scale(win, from_=0, to=36, resolution=0.1, orient=HORIZONTAL, length=300)
voltscale.pack()
Button(win, text="Set Voltage", command=setVoltage).pack()

vlab = StringVar()
vlab.set("voltage")
Label(win, textvariable = vlab, width=15, relief=RAISED).pack()
clab = StringVar()
clab.set("current")
Label(win, textvariable = clab, width=15).pack()

def getD():
    vals = lib1685b.getData(ser)
    vlab.set("Volt="+str(vals[0]))
    clab.set("Curr="+str(vals[1]))
    
Button(win, text="Get V/C", command=getD).pack()


win.mainloop()
