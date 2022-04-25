import requests
import os
from time import sleep
from capture import *
import pickle
from subprocess import run,, Popen
import pyautogui

host = "http://72.205.82.44:8008"
req = requests.get(host+"/register")
id = req.json()['id']

print("Client initialized, connecting to",host)

def waitPixel(x, y, color):
	while pyautogui.pixel(x,y) != color:
		print(f"waiting for ({x},{y}) to turn to {color}")
		sleep(.1)

while True:
	req = requests.get(f"{host}/instr/{id}")
	instr = req.json()
	if instr['instr'] == 'wait':
		sleep(1)
	elif instr['instr'] == 'login':
		run("TASKKILL /F /IM LeagueClient.exe")
		pyautogui.press('win')
		pyautogui.typewrite("League of legends")
		pyautogui.press('enter')
		waitPixel(345,142,(235,0,41))
		pyautogui.click(285,317)			# login screen
		print("Client is opened")
		sleep(10)
		pyautogui.typewrite(instr['user'])
		sleep(.1)
		pyautogui.press("tab")
		sleep(.1)
		pyautogui.typewrite(instr['pass'])
		sleep(.1)
		pyautogui.press("enter")
		waitPixel(894,135,(201,170,104)) 	# click play screen
		waitPixel(1290, 137,(227,186,61))	# home screen
		pyautogui.click(894,135)			# click play button
		pyautogui.displayMousePosition()

