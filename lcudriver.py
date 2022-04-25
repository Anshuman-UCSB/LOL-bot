from lcu_driver import Connector
from time import time, sleep

connector = Connector()

async def getIdName(connection):
	req = await connection.request('get', '/lol-summoner/v1/current-summoner')
	json = await req.json()
	return (json['accountId'],json['displayName'])

@connector.ready
async def connect(connection):

	print(await getIdName(connection))
	# await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
	
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