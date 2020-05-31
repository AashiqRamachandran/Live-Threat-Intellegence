import pyshark
cap =pyshark.LiveCapture(interface='eth0')
cap.sniff(timeout=1)
for packet in cap.sniff_continuously():
	print('Just arrived:', packet.ip.src)
