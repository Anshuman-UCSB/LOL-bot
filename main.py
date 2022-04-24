from fastapi import FastAPI, Request
import cv2
import pickle
from states import States

app = FastAPI()

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
id = 0

@app.get("/register")
async def root():
	global id
	if id == 5:
		return {"msg":"err"}
	clients.append(Client(id))
	print(f"Client {id} registered, waiting for 5 Clients to start")
	if id == 4:
		await setup()
	id+=1
	return {"id":id-1}

async def setup():
	with open("accounts.txt",'r') as f:
		acc = map(lambda x: x.split(":"), f.read().splitlines())
		for client, (user,pw) in zip(clients,acc):
			client.instr = {"instr":"login", "user":user, "pw":pw}

@app.get("/instr/{id}")
async def getinstr(id:int):
	try:
		return clients[id].instr
	except IndexError:
		return {"msg":"Invalid id"}

@app.post("/screen/{id}")
async def getScreen(id: int, data: Request):
	dat = await data.body()
	clients[id].screen = pickle.loads(dat)
	print("saving screen")
	return {"msg":"recv"}
