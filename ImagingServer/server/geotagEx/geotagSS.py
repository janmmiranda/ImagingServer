from decimal import *
import math

def routine(target, picture):
	#latitude = DecimalField(max_digits=9, decimal_places=6, default=0)
	#longitude = DecimalField(max_digits=9, decimal_places=6, default=0)


	aperP = 0.06245406936;
	#angle per pixel dependent on camera
	latAD = float(math.tan(math.radians(1))*20903520)
	#TAN(RADIANS(1))*20903520
	#Constant derived from earth's diameter
	
	#calculate angle offset from altitude to the pixels offset from center
	#total angle x
	taX = float(-picture.roll + target.x*aperP)
	#total angle y
	taY = float(picture.pitch + target.y*aperP)

	#convert angle offset to distances(feet)
	rollDie = float(math.tan(math.radians(taX))*picture.alt)
	pitchDie = float(math.tan(math.radians(taY))*picture.alt)

	#calculate offsets
	latOff = float(math.fabs(pitchDie)/latAD)
	lonOff = float(math.fabs(rollDie)/latAD)

	#final coords
	latitude = float(latOff + picture.lat)
	longitude = float(lonOff + picture.lon)
	print("lat: ", latitude, "\nLon: ", longitude)
	return latitude, longitude


class target():
	def __init__(self, x, y, length, width):
		self.x = x
		# x position on picture
		self.y = y 
		# y position on picture
		self.length = length 
		# length of picture
		self.width = width 
		# width of picture

class picture():
	def __init__(self, yaw, pitch, roll, lat, lon, alt):
		self.yaw = yaw
		self.pitch = pitch
		self.roll = roll
		self.lat = lat
		self.lon = lon
		self.alt = alt

targetOne = target(25, 30, 300, 400)
picOne = picture(0, 0, 5, 40, 99, 1000)

def main():
	routine(targetOne, picOne)
	

main()	
input("\n\nPress the enter key to quit.")