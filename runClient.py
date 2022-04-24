from subprocess import run
run(['git','pull'])
try:
	import client
except Exception as ex:
    traceback.print_exc()
    input()