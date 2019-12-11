from blinkstick import blinkstick
import psutil

b = blinkstick.find_first()

if b is None:
    print("No BlinkSticks found...")
else:
    print ("Displaying CPU usage (Green = 0%, Amber = 50%, Red = 100%)")
    print ("Press Ctrl+C to exit")
    
    #go into a forever loop
    while True:
        cpu = psutil.cpu_percent(interval=1)
        intensity = int(255 * cpu / 100)

        b.set_color(red=intensity, green=255 - intensity, blue=0)
