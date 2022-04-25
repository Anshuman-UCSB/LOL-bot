from lcu_driver import Connector
import requests
from time import time, sleep

host = "http://72.205.82.44:8008"

connector = Connector()

async def getIdName(connection):
	req = await connection.request('get', '/lol-summoner/v1/current-summoner')
	json = await req.json()
	return (json['accountId'],json['displayName'])

async def invite(connection, id, name):
	myId, myName = await getIdName(connection)
	body = {
			# "fromSummonerId": myId,
			# "fromSummonerName": myName,
			# "state": "Requested",
			"toSummonerId": id,
			# "toSummonerName": name,
		}
	req = await connection.request('post', '/lol-lobby/v1/lobby/invitations', json=body)
	pass

async def getLobbyId(connection):
	req = await connection.request('get', '/lol-lobby/v2/lobby')
	json = await req.json()
	return json['chatRoomId']


@connector.ready
async def connect(connection):
	req = requests.get(host+"/lobby")
	print(req)
	partyId = req.text
	print(partyId)
	await connection.request('post', f'/lol-lobby/v2/party/{partyId}/join')
	
	# await connection.request('post','/lol-lobby/v2/lobby/matchmaking/search')
	# sleep(3)
	# queueResponse = "initialized"
	# while(queueResponse != "InProgress"):
	# 	queuePop = await connection.request('get','/lol-matchmaking/v1/ready-check')
	# 	resp = await queuePop.json()
	# 	print(resp)
	# 	queueResponse = (resp['state'])
	# 	print(queueResponse)
	# 	sleep(2)
	
	
	# accept = await connection.request('post','/lol-matchmaking/v1/ready-check/decline')
	# print(await accept.json())

if __name__ == "__main__":
	connector.start()