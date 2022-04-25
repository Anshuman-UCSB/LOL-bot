from fastapi import FastAPI, Request
import cv2
import pickle
from states import States

app = FastAPI()

DEBUG = True

class Client():
	def __init__(self, id):
		self.id = id
		self.state = States.WAITING
		self.instr = {"instr":"wait"}
	
	def getScreen(self):
		return self.screen
	def __str__(self):
		return f"Client {self.id} at {self.state}"
	def __repr__(self):
		return self.__str__()

clients = []
clientNum = 2 if DEBUG else 5
id = 0
lobbyId = ""

@app.get("/register")
async def root():
	global id
	if id == clientNum:
		return {"msg":"err"}
	clients.append(Client(id))
	print(f"Client {id} registered, waiting for 5 Clients to start")
	if id == clientNum-1:
		await setup()
	id+=1
	return {"id":id-1}

async def setup():
	with open("accounts.txt",'r') as f:
		acc = map(lambda x: x.split(":"), f.read().splitlines())
		for client, (user,pw) in zip(clients,acc):
			client.instr = {"instr":"login", "user":user, "pass":pw}

@app.get("/instr/{id}")
async def getinstr(id:int):
	try:
		return clients[id].instr
	except IndexError:
		return {"msg":"Invalid id"}

nextState = {
	b"login": "createLobby",
}

@app.post("/tasks/{id}")
async def getTask(id: int, data: Request):
	dat = await data.body()
	clients[id].state = dat
	clients[id].instr = {"instr":nextState[dat]}
	print("saving screen")
	return {"msg":"recv"}

@app.post("/lobby")
async def getTask(id: int, data: Request):
	global lobbyId
	dat = await data.body()
	lobbyId = dat
	print("Recieved lobby code",lobbyId)
	return {"msg":"recv"}