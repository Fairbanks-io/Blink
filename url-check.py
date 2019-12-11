from blinkstick import blinkstick
import urllib
from sys import argv
import time

b = blinkstick.find_first()
script, url = argv

if b is None:
    print("No BlinkSticks found...")
else:
	status = urllib.urlopen(url).getcode()
    	print(status)
	if(status == 200):
		b.set_color(name='green')
		time.sleep(5)
		b.turn_off()
	else:
		b.pulse(name='red', repeats=10, duration=300)
		b.morph(name='red')
		time.sleep(5)
		b.turn_off()
