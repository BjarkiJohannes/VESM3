from bluedot import BlueDot
bd = BlueDot()
on=True
while on:
	bd.wait_for_press()
	print("Hello World!")
