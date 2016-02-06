import win32api, win32con
import time
import math

import ctypes

import sys

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
				("wScan", ctypes.c_ushort),
				("dwFlags", ctypes.c_ulong),
				("time", ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
				("wParamL", ctypes.c_short),
				("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
				("dy", ctypes.c_long),
				("mouseData", ctypes.c_ulong),
				("dwFlags", ctypes.c_ulong),
				("time",ctypes.c_ulong),
				("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
				 ("mi", MouseInput),
				 ("hi", HardwareInput)]

class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
				("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):

	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
	x = Input( ctypes.c_ulong(1), ii_ )
	SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def AltTab():
	'''
	Press Alt+Tab and hold Alt key for 2 seconds in order to see the overlay
	'''

	PressKey(0x012) #Alt
	PressKey(0x09) #Tab
	ReleaseKey(0x09) #~Tab

	time.sleep(2)	   
	ReleaseKey(0x012) #~Alt



def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def main():

	# print "running for {} min".format(total_min)

	passed_min = 0
	while True:

		print "{} min passed".format(passed_min)
		
		if (len(sys.argv) > 1):
			if (passed_min >= int(sys.argv[1])):
				break
		
		# AltTab()
		
		# click(1000, 500)
		
		# for i in range(1900):
		# 	x = i
		# 	y = int(1100/2 - math.sin(i/100.0)*500)
		# 	# y = int(1100/2)
		# 	win32api.SetCursorPos((x,y))
		# 	time.sleep(.01)
		# passed_min += 19/60
		
		# print "clicking"
		click(1000, 500)
		# win32api.SetCursorPos((passed_min,passed_min))
		time.sleep(4 * 60)
		passed_min += 4
	# x: 1900 - 2000
	# y: 1000 - 1100
if __name__ == "__main__":
	main()
