import requests
import os
from time import sleep
import lculeader,lcudriver
from capture import *
from subprocess import run
import pyautogui

host = "http://72.205.82.44:8008"
req = requests.get(host+"/register")
id = req.json()['id']

print("Client initialized, connecting to",host)

def waitPixel(x, y, color):
	print(f"waiting for ({x},{y}) to turn to {color}")
	while pyautogui.pixel(x,y) != color:
		sleep(.5)
def whilePixel(x, y, color, xp, yp):
	waitPixel(x,y,color)
	print(f"clicking while ({x},{y}) is {color}")
	while pyautogui.pixel(x,y) == color:
		pyautogui.click(xp,yp,clicks=2,interval=.25)
		sleep(1)

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
		pyautogui.typewrite(instr['user'])
		sleep(.1)
		pyautogui.press("tab")
		sleep(.1)
		pyautogui.typewrite(instr['pass'])
		sleep(.1)
		pyautogui.press("enter")
		waitPixel(894,135,(201,170,104)) 	# play screen
		# whilePixel(1290, 137,(227,186,61),443,151)	# home screen
		waitPixel(1290, 137,(227,186,61))	# home screen
		requests.post(host+'/tasks/'+str(id), data=instr['instr'])
		sleep(5)
		# pyautogui.displayMousePosition()
	elif instr['instr']=="createLobby":
		lculeader.connector.start()
	elif instr['instr']=="joinLobby":
		lcudriver.connector.start()

