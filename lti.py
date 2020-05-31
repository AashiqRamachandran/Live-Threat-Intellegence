import pyshark
from greynoise import GreyNoise
import time
api_client = GreyNoise(api_key="UW3D9zMw61AxTsy9ydprpLz6WGwZLFIJNJR1ra0bPVaKE37zsl3kOoPiiXfqfQUG")
cap =pyshark.LiveCapture(interface='eth0')
cap.sniff(timeout=1)
for packet in cap.sniff_continuously():
	#print('Just arrived:', packet.ip.src)
	data_of_ip=api_client.quick(packet.ip.src)
	print(data_of_ip)
	time.sleep(2)
