import pyautogui
import os
import time
import random

codigos = ["Srlf6d9BF-0", "L7AmWbQMSi4", "0GadFaEJ8Lg","pOnjlmUafgg",]
countries = ["Venezuela", "Mexico", "Argentina", "Chile", "Colombia", "Cuba", "Guatemala", "Honduras", "El Salvador", "Panama",]
tiempos = [170, 190, 55, 100]

while True:
	############################
	#ingresar a youtube
	pyautogui.moveTo(350, 80)
	pyautogui.click()
	pyautogui.typewrite("youtube.com")
	pyautogui.press("enter")
	time.sleep(5)
	#Conecta Hola VPN
	pyautogui.moveTo(1100, 80)
	pyautogui.click()
	time.sleep(2)
	pyautogui.moveTo(900, 350)
	pyautogui.click()
	time.sleep(2)
	country = random.randint(0,8)
	pyautogui.typewrite(countries[country])
	time.sleep(2)
	pyautogui.moveTo(1000, 300)
	pyautogui.click()
	time.sleep(10)
	#ingresa a la barra de busqueda de youtube
	pyautogui.moveTo(350, 118)
	pyautogui.click()
	num = random.randint(0,3)
	pyautogui.typewrite(codigos[num])
	pyautogui.press("enter")
	time.sleep(5)
	#ingresa al video
	pyautogui.moveTo(350, 300)
	pyautogui.click()
	time.sleep(tiempos[num])
