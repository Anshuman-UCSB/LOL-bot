import pygetwindow as gw
import requests
import os
from time import sleep
from lcu_driver import Connector
from subprocess import run
import pyautogui
from utils import *

HOST = "http://72.205.82.44:42069"

class Client:
	def __init__(self):
		print(HOST+"/register")
		try:
			r = requests.get(HOST+"/register")
			self.id = r.json()['id']
			print("Registered client with id",self.id)
			self.creds = tuple(r.json()['account'].values())
			print(self.creds)
		except KeyError:
			print("ERROR: all client ID's are registered already")
			exit(-2)
		except:
			print("ERROR: No response from server, is server running?")
			exit(-1)
		self.leader = (self.id == 0)
	
	def login(self):
		run("TASKKILL /F /IM LeagueClient.exe")
		pyautogui.press('win')
		pyautogui.typewrite("League of legends")
		pyautogui.press('enter')
		waitPixel(346, 143, (235,0,41))
		sleep(.5)
		pyautogui.click(282,316)
		pyautogui.typewrite(self.creds[0])
		pyautogui.press("tab")
		pyautogui.typewrite(self.creds[1])
		pyautogui.press("enter")
		assert (gw.getWindowsWithTitle('League')[0].topleft) == (110,320)
		
	def clickOk(self):
		clickImage("images/ok.png")

	def enterLobby(self):
		if self.isLeader:
			connector = Connector()

			@connector.ready
			async def connect(connection):
				summoner = await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
				partyId = (await summoner.json())['partyId']
				print("Created lobby with id:",partyId)
				r = requests.post(HOST+"/lobby/"+partyId)

			connector.start()
		else:
			connector = Connector()

			@connector.ready
			async def connect(connection):
				r = requests.get(HOST+"/lobby/")
				partyId = r.json()['id']
				print("Recieved party id:",partyId)
				await connection.request('post', f'/lol-lobby/v2/party/{partyId}/join')
			
			connector.start()

	def isLeader(self):
		return self.leader
	def getId(self):
		return self.id


def main():
	c = Client()
	# c.enterLobby()
	import debug
	
if __name__ == "__main__":
	main()