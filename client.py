import requests
import os
from time import sleep
from capture import *
import pickle

host = "http://72.205.82.44:8008"
req = requests.get(host+"/register")
id = req.json()['id']

while True:
	req = requests.get(f"{host}/instr/{id}")
	instr = req.json()
	if instr['instr'] == 'wait':
		sleep(1)
	elif instr['instr'] == 'login':
		os.system("TASKKILL /F /IM LeagueClient.exe")
		os.system('"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')