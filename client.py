import requests
import os
from time import sleep
from capture import *
import pickle
from subprocess import run
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
		run('"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
		waitPixel(345,142,(235,0,41))
		pyautogui.click(285,317)
		pyautogui.typewrite(instr['user'])
		sleep(.1)
		pyautogui.press("tab")
		sleep(.1)
		pyautogui.typewrite(instr['pass'])
		sleep(.1)
		pyautogui.press("enter")
		waitPixel(894,135,(201,170,104))
		pyautogui.displayMousePosition()
