from subprocess import run
import traceback
run(['git','pull'])
try:
	from client import client
	client.main()
except Exception as ex:
    traceback.print_exc()
    input()