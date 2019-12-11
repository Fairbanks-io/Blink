from blinkstick import blinkstick
from kubernetes import client, config
import time
import sys

config.load_kube_config()
b = blinkstick.find_first()

if b is None:
	#print("No BlinkSticks found...")
	sys.exit()
else:
	v1 = client.CoreV1Api()
	while True:
		res = v1.list_node()
		err = None
		for i in res.items:
			if(i.status.conditions[3].status != 'True'):
				err = True
			else:
				err = False

		if(err == True):
			#print("Unhealthy Node(s):"); print("%s\t%s\t%s=%s" % ( i.status.addresses[0].address, i.metadata.name, i.status.conditions[3].type, i.status.conditions[3].status ))
			b.pulse(name='red', repeats=5, duration=200)
			b.morph(name='red')
		else:
			b.blink(name="green", delay=25)
			
		time.sleep(10)
