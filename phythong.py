<<

# Built in functions available:
#   Read() - get line of text from user
#   ReadKey() - get a single keypress from user
#
# If an optional function called Exit() is defined then it is called when script terminates # # Type in 'App.' to explore the available modules using the popup help system

# Example to demonstrate getting user input then performing SDO and NMT operations # Start a simulation node with id 0x01

# show menu
print "Button Indicators"
# print "Type button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit."

# called during SDO transfers
def Progress(percentage, param):
	print str(percentage) + " done"


# loop until exit
while True:
	# key = Read()
	key = input("Type button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit.")
	print ""


	# exit script  
	if key == 'x':
		break

	size = 4
	buffer = App.CreateBuffer(size)
	buffer[1] = 0
	buffer[2] = 0
	buffer[3] = 0
	
  # read device type
	if key == 'all':
		try:
			print "type '0' for Off, '1' for On"
			key = Read()
			
			if key == '0':
				buffer[0] = 0
				ret_message = 'All Button Indicators Off'
			else:
				buffer[0] = 1
				ret_message = 'All Button Indicators On'
			
			for x in range (1, 22):
				App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
			print ret_message
			print "\nType button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit."
		except App.CANopenException as exc:
			print exc.Message
			print "\nType button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit."
	elif key == 'ta':
		try:
			print "type 'l' for left, 'r' for right, 's' for split, 'o' for off"
			key = Read()
			
			if key == 'l':
				buffer[0] = 9
				for x in range (25, 33):
					App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
					buffer[0] = buffer[0] - 1
				ret_message = 'TA Left'
			elif key == 'r':
				buffer[0] = 2
				for x in range (25, 33):
				#for x in range (1, 9):
					App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
					buffer[0] = buffer[0] + 1
				ret_message = 'TA Right'
			elif key == 's':
				buffer[0] = 10
				for x in range (25, 33):
					App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
					buffer[0] = buffer[0] + 1
				ret_message = 'TA Split'
			else:
				buffer[0] = 0
				for x in range (25, 33):
					App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
				ret_message = 'TA Off'
			print ret_message
			print "\nType button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit."
		except App.CANopenException as exc:
			print exc.Message
			print "\nType button number, 'ta' for traffic advsor, 'all' for all, 'x' to exit."
	else:
		try:
			x = int(key)
			if x > 21:
				raise KeyError('InvalidKey')
			
			print "0 is off, 1 is on"
			k_press = Read()
			ret_message = "Indicator for Button " + key
			if k_press == '0':
				buffer[0] = 0
				ret_message = ret_message + " is Off."
			else:
				buffer[0] = 1
				ret_message = ret_message + " is On."
			App.Instances.CANopen.SDODownload(0x01, 0x2080, x, buffer, size, Progress)
			print ret_message
			print "\nType button number, 'all' for all, 'x' to exit."
		except KeyError:
			print "Not a valid key."
			print "\nType button number, 'all' for all, 'x' to exit."
		except App.CANopenException as exc:
			print exc.Message
			print "\nType button number, 'all' for all, 'x' to exit."

print "Finished"



>>
