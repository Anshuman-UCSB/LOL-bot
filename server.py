import socket, threading
from threading import Thread
import cPickle

class Listener(Thread):
	def __init__(self, HOST, PORT):
		Thread.__init__(self, daemon = True)
		self.hp = (HOST, PORT)

	def run(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((HOST, PORT))
			s.listen()
			conn, addr = s.accept()
			with conn:
				print(f"Connected by {addr}")
				while True:
					recv = conn.recv(1024)
					data = recv
					n = 0
					while len(recv) == 1024:
						data+=recv
						print(n)
						recv = conn.recv(1024)
						n+=1
					if not data:
						break
					
					conn.sendall(b'recv')
		print("Done")
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

th = Listener(HOST, PORT)
th.start()


if __name__ == "__main__":
	from time import sleep
	while th.is_alive():
		sleep(.1)