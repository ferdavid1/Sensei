from gpiozero import LED
import sys
import time
state=1
red=LED(14)



if state:
	red.on()
	time.sleep(.2)

else:
	red.off()
