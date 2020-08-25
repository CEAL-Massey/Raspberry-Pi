import signal
import socket
import structure_pb2
from datetime import datetime
import pytz
import i2cexample
import time

HOST = '192.168.20.7'
PORT = 8886

temp_sensor = 0x04
humid_sensor = 0x05


temp = structure_pb2.sens_dat()
temp.type = "temp"
temp.unit = "Celsius"
#temp.data = (5*float(i2cexample.readNumber(temp_sensor))/512)

humid = structure_pb2.sens_dat()
humid.type = "hum"
humid.unit = "percent"
#humid.data = i2cexample.readNumber(humid_sensor)

incrementer = 0

while  incrementer <= 10:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT)) #Connect to foriegn host (TCP server on laptop)

	now = datetime.now(pytz.timezone('Pacific/Auckland'))
	now = now.strftime('%Y:%d:%m:%H:%M:%S')

	temp.timestamp = now
	temp.data = 1.2222
	to_send = [temp.SerializeToString()]
	#,humid.SerializeToString()]

	s.sendall(to_send[0]) #Send serialized reading
	data = s.recv(1024)
	print('Received', repr(data))
	s.shutdown(1)
	incrementer = incrementer+1
	time.sleep(5)
