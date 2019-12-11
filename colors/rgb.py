from blinkstick import blinkstick

b = blinkstick.find_first()

if b is None:
    print("No BlinkSticks found...")
else:
    print ("Party Time!")
    
    #go into a forever loop
    while True:
        b.morph(name='red')
	b.morph(name='green')
	b.morph(name='blue')
