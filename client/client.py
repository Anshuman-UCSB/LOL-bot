import requests
import os
from time import sleep
import lcu_driver
from subprocess import run
import pyautogui
from utils import *

class Client:
	def __init__(self):
		self.id = 0 # TODO: make request to server to ask for id
		self.leader = (self.id == 1)
		self.creds = ("username","password") # TODO: get from server
	
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

	def isLeader(self):
		return self.leader
	def getId(self):
		return self.id


def main():
	c = Client()
	c.login()
	import debug
	
if __name__ == "__main__":
	main()