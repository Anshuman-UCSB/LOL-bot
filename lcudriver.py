from lcu_driver import Connector
from time import time, sleep

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

	# await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
	# print(await getIdName(connection))
	# sleep(5)
	# await invite(connection,*(91622819, 'Hevraz'))
	await connection.request('post', '/lol-lobby/v2/party/2f5efd75-e75b-42d0-9260-8020090ae1d8/join')
	print(await(await connection.request('get', '/lol-lobby/v2/lobby')).json())
	
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