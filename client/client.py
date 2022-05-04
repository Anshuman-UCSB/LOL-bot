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
		

	def isLeader(self):
		return self.leader
	def getId(self):
		return self.id

if __name__ == "__main__":
	c = Client()
	c.login()