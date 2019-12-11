from blinkstick import blinkstick

b = blinkstick.find_first()

if b is None:
    print("No BlinkSticks found...")
else:
    print ("Blue")
    b.set_color(name="blue")
