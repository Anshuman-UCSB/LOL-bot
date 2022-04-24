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

while True:
	req = requests.get(f"{host}/instr/{id}")
	instr = req.json()
	if instr['instr'] == 'wait':
		sleep(1)
	elif instr['instr'] == 'login':
		run("TASKKILL /F /IM LeagueClient.exe")
		run('"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
		pyautogui.displayMousePosition()
		while pyautogui.pixel(345,142) != (235,0,41):
			print(pyautogui.pixel(345,142))
		pyautogui.click(285,317)
		pyautogui.typewrite(instr['user'])
		pyautogui.press("tab")
		pyautogui.typewrite(instr['pass'])
		pyautogui.press("enter")
		