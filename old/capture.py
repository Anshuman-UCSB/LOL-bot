import mss
import numpy as np

def captureScreen():
	with mss.mss() as sct:
		monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
		img_array = np.array(sct.grab(monitor))
		return img_array