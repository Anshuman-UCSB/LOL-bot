from lcu_driver import Connector
from time import time, sleep

connector = Connector()


@connector.ready
async def connect(connection):

	await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":430})
	
	queueUp = await connection.request('post','/lol-lobby/v2/lobby/matchmaking/search')

	# queueResponse = "initialized"
	# while(queueResponse != "InProgress"):
	# 	queuePop = await connection.request('get','/lol-matchmaking/v1/ready-check')
	# 	resp = await queuePop.json()
	# 	print(dict(resp))
	# 	queueResponse = (dict(resp)['state'])
	# 	print(queueResponse)
	# 	sleep(2)
	

	# accept = await connection.request('post','/lol-matchmaking/v1/ready-check/decline')
	# print(await accept.json())

if __name__ == "__main__":
	connector.start()