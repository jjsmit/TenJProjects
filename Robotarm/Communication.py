import re
import serial
import serial.tools.list_ports as port_list

for port in port_list.comports():
    i = 0
    print(i," ", port)
    i += 1

# comIndex = input("select comport number:")
port = port_list.comports()[0]

portString = re.search("\S+", str(port)).group()
print(portString)
ser = serial.Serial(portString)

while(True):
    angle = input("angle:")
    ser.write(int(angle).to_bytes(1,byteorder='big'))

