import pyautogui
import os
import time
import random

enlace = "yoube"
codigos = ["Srlf6d9BF-0", "L7AmWbQMSi4", "0GadFaEJ8Lg","pOnjlmUafgg",]
countries = ["Argentina","Chile","Costa_Rica","Mexico","Spain",]
tiempos = [170, 190, 55, 100]

while True:
	#conectar a nordvpn latinoamerica
	country = random.randint(0,4)
	os.system(f"nordvpn connect {countries[country]}")
	time.sleep(5)
	#ingresar a youtube
	pyautogui.moveTo(350, 80)
	pyautogui.click()
	pyautogui.typewrite("www.youtube.com")
	pyautogui.press("enter")
	time.sleep(4)
	#evitar anuncio que ocupa pantalla
	pyautogui.moveTo(700,600)
	pyautogui.click()
	time.sleep(10)
	#dentra al link de youtbe
	pyautogui.moveTo(240,380)
	pyautogui.click()
	time.sleep(10)
	#ingresa a la barra de busqueda de youtube
	pyautogui.moveTo(350, 118)
	pyautogui.click()
	num = random.randint(0,3)
	pyautogui.typewrite(codigos[num])
	pyautogui.press("enter")
	time.sleep(8)
	#ingresa al video
	pyautogui.moveTo(350, 300)
	pyautogui.click()
	time.sleep(tiempos[num])
	#cerrar navegador
	break

