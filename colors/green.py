from blinkstick import blinkstick
import psutil

bstick = blinkstick.find_first()

if bstick is None:
    print("No BlinkSticks found...")
else:
    print ("Green")
    bstick.set_color(name="green")
