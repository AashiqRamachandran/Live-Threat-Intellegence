import pyshark
import time
import argparse
import get_malicious
import hashlib
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from greynoise import GreyNoise

otx = OTXv2("2e8bf67d611de674bd70308e0c48371a36b9ebf5847aa33f670efd0b2f2b9bf3")
#greynoise API initialization
#api_client = GreyNoise(api_key="UW3D9zMw61AxTsy9ydprpLz6WGwZLFIJNJR1ra0bPVaKE37zsl3kOoPiiXfqfQUG")
cap =pyshark.LiveCapture(interface='eth0')
cap.sniff(timeout=1)
for packet in cap.sniff_continuously():
	print('Just arrived:', packet.ip.src)
	#Geynoise query
	#data_of_ip_gn=api_client.quick(packet.ip.src)
	#print(data_of_ip_gn)
	alerts = get_malicious.ip(otx, args['ip'])
    	if len(alerts) > 0:
        	print('Identified as potentially malicious from AlienVault OTX')
        	print(str(alerts))
    	else:
        	print('Unknown or not identified as malicious from AlienVault OTX')
		time.sleep(2)
