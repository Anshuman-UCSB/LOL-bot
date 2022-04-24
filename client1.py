import socket
from time import sleep
from capture import *
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(captureScreen())
	# s.sendall(b'Hi')
	data = s.recv(1024)
print(f"Received {data!r}")