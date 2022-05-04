import pyautogui
from time import sleep

def checkPixel(x, y, color):
	return pyautogui.pixel(x,y) == color

def waitPixel(x, y, color):
	while checkPixel(x,y,color) == False:
		sleep(.1)

def clickImage(image, confidence = .9):
	x,y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
	pyautogui.click(x,y)