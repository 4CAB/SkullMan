import os
import time 

num = 0
if num == 0:
	os.system("pip3 install python3-xlib")
	time.sleep(10)
	os.system("sudo apt-get install scrot")
	time.sleep(10)
	os.system("sudo apt-get install python3-tk")
	time.sleep(10)
	os.system("sudo apt-get install python3-dev")
	time.sleep(10)
	os.system("pip3 install pyautogui")
	time.sleep(10)
	num += 1

while True:
	os.system("python3 BotCrack.py")
	print("Reconectando . . .")
