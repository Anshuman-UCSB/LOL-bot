import requests
import os
from time import sleep
from lcu_driver import Connector
from subprocess import run
import pyautogui
from utils import *

class Client:
	def __init__(self):
		self.id = 1 # TODO: make request to server to ask for id
		self.leader = (self.id == 1)
		self.creds = ("expertdope3","expertdope3") # TODO: get from server
	
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

	def clickOk(self):
		clickImage("images/ok.png")

	def enterLobby(self):
		if self.isLeader:
			connector = Connector()
			async def getLobbyId(connection):
				req = await connection.request('get', '/lol-lobby/v2/lobby')
				json = await req.json()
				return json['chatRoomId']
			@connector.ready
			async def connect(connection):
				summoner = await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
				partyId = (await summoner.json())['partyId']
				print(partyId)

			connector.start()

	def isLeader(self):
		return self.leader
	def getId(self):
		return self.id


def main():
	c = Client()
	c.enterLobby()
	import debug
	
if __name__ == "__main__":
	main()