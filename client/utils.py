import pyautogui
from time import sleep

def checkPixel(x, y, color):
	return pyautogui.pixel(x,y) == color

def waitPixel(x, y, color):
	while checkPixel(x,y,color) == False:
		sleep(.1)