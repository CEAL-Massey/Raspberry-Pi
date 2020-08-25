#Holds functions necessary for i2c communication#
#Also where the addresses are stored for each arduino#

import smbus
import time

temp_sensor = 0x04
humid_sensor = 0x05
bus = smbus.SMBus(1)


def writeNumber(address, value):
	bus.write_byte(address, value)
	return -1
def readNumber(address):
	number = bus.read_byte_data(address, 5)
	return number

#while True:
	#data = raw_input("Enter something > ")
	#data_list = list(data)
	#for i in data_list:
	#	writeNumber(int(ord(i)))
	#	time.sleep(0.1)

	#writeNumber(int(0x0A))

###Unblock bottom for testing###
	#result = readNumber(temp_sensor)
	#result = (float(result)/255)*5
	#print("Number from uno:", result)
	#time.sleep(1)
	#result = readNumber(humid_sensor)
	#print("Number from due:", result)
	#time.sleep(1)
