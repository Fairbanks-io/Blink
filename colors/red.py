from blinkstick import blinkstick

b = blinkstick.find_first()

if b is None:
    print("No BlinkSticks found...")
else:
    print ("Red")
    b.set_color(name='red')
