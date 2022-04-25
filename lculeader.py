import requests
from lcu_driver import Connector
from time import time, sleep

connector = Connector()
host = "http://72.205.82.44:8008"

async def getIdName(connection):
	req = await connection.request('get', '/lol-summoner/v1/current-summoner')
	json = await req.json()
	return (json['accountId'],json['displayName'])

async def getLobbyId(connection):
	req = await connection.request('get', '/lol-lobby/v2/lobby')
	json = await req.json()
	return json['chatRoomId']


@connector.ready
async def connect(connection):
	await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
	lobbyId = await getLobbyId(connection)
	requests.post(host+'/lobby', data = {"id":lobbyId})
	print("Posted", lobbyId)
	
if __name__ == "__main__":
	connector.start()