from blinkstick import blinkstick

for b in blinkstick.find_all():
    b.turn_off()
    print b.get_info_block1() + " turned off"
