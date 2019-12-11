from blinkstick import blinkstick

for b in blinkstick.find_all():
    b.set_random_color()
    print b.get_info_block1() + " was set to Hex: " + b.get_color(color_format="hex")
