import pyautogui
import os
import time
import random

codigos = ["Srlf6d9BF-0", "L7AmWbQMSi4", "0GadFaEJ8Lg","pOnjlmUafgg",]
countries = ["Venezuela", "Mexico", "Argentina", "Chile", "Colombia", "Cuba", "Guatemala", "Honduras", "El Salvador", "Panama",]
tiempos = [170, 190, 55, 100]

while False:
	############################
	pyautogui.moveTo(1200, 290)
	pyautogui.click()
	#ingresar a youtube
	pyautogui.moveTo(350, 80)
	pyautogui.click()
	pyautogui.typewrite("youtube.com")
	pyautogui.press("enter")
	time.sleep(10)
	#Conecta Hola VPN
	pyautogui.moveTo(1250, 80)
	pyautogui.click()
	time.sleep(2)
	pyautogui.moveTo(1100, 350)
	pyautogui.click()
	time.sleep(2)
	country = random.randint(0,8)
	pyautogui.typewrite(countries[country])
	time.sleep(2)
	pyautogui.moveTo(1100, 300)
	pyautogui.click()
	time.sleep(40)
	#ingresa a la barra de busqueda de youtube
	pyautogui.moveTo(350, 118)
	pyautogui.click()
	num = random.randint(0,3)
	pyautogui.typewrite(codigos[num])
	pyautogui.press("enter")
	time.sleep(15)
	#ingresa al video
	pyautogui.moveTo(350, 300)
	pyautogui.click()
	time.sleep(tiempos[num])
	break

pyautogui.moveTo(400,80)
pyautogui.click()
time.sleep(1)
pyautogui.click()
a = chr(47)
pyautogui.hotkey("alt", "47")
#pyautogui.typewrite(f"{a}watch?v=L7AmWbQMSi4")
#pyautogui.press("enter")
