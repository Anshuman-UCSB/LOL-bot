from subprocess import run
import sys
import traceback
run(['git','pull'])
try:
	import client
	client.main()
except Exception as ex:
    traceback.print_exc()
    input()