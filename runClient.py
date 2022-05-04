from subprocess import run
import traceback
run(['git','pull'])
try:
	import client.client as client
	client.main()
except Exception as ex:
    traceback.print_exc()
    input()