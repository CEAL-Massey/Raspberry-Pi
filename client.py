import socket
import structure_pb2
import datetime
import i2cexample


HOST = '192.168.20.10'
PORT = 65432

temp_sensor = 0x04
humid_sensor = 0x05

time = datetime.datetime.today()
time = time.strftime('%Y%m%d%H%M%S')

temp = structure_pb2.sens_dat()
temp.type = "temp"
temp.unit = "Celsius"
temp.timestamp = time
temp.data = (5*float(i2cexample.readNumber(temp_sensor))/512)

humid = structure_pb2.sens_dat()
humid.type = "hum"
humid.unit = "percent"
humid.timestamp = time
humid.data = i2cexample.readNumber(humid_sensor)

to_send = [temp.SerializeToString(),humid.SerializeToString()]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for x in range(len(to_send)):
	s.sendall(to_send[x])
	data = s.recv(1024)

print('Received', repr(data))
