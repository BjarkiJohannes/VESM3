import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)
ser.write('3')
time.sleep(2)
ser.write('5')
time.sleep(2)
ser.write('6')
time.sleep(2)

