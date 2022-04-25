from lcu_driver import Connector
from time import time, sleep

connector = Connector()


@connector.ready
async def connect(connection):

	summoner = await connection.request('post', '/lol-lobby/v2/lobby', data={"queueId":400})
	print(await summoner.json())
	rolePref={
		"firstPreference": "SUPPORT",
		"secondPreference": "JUNGLE"
	}
	roleChoose = await connection.request('put', '/lol-lobby/v2/lobby/members/localMember/position-preferences', data=rolePref)
	print(await roleChoose.json())

	queueUp = await connection.request('post','/lol-lobby/v2/lobby/matchmaking/search')
	print(await queueUp.json())

	queueResponse = "initialized"
	while(queueResponse != "InProgress"):
		queuePop = await connection.request('get','/lol-matchmaking/v1/ready-check')
		resp = await queuePop.json()
		queueResponse = (dict(resp)['state'])
		print(queueResponse)
		sleep(2)
	

	accept = await connection.request('post','/lol-matchmaking/v1/ready-check/decline')
	print(await accept.json())

connector.start()