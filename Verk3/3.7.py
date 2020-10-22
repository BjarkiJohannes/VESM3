import serial
from bluedot import BlueDot

ser = serial.Serial('/dev/ttyACM0', 9600)
def bd1_pressed():
	ser.write('3')
def bd2_pressed():
	ser.write('5')
def bd3_pressed():
	ser.write('6')
def bd4_pressed():
	ser.write('9')

bd1 = BlueDot(port = 1)
bd2 = BlueDot(port = 2)
bd3 = BlueDot(port = 3)
bd4 = BlueDot(port = 4)


bd1.when_pressed = bd1_pressed
bd2.when_pressed = bd2_pressed
bd3.when_pressed = bd3_pressed
bd4.when_pressed = bd4_pressed

