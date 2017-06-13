#!/usr/bin/python
import pyautogui

def main():
	response_time = 8;
	pyautogui.time.sleep(5)
	while True:
		
		# click "Continue" sml
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('continue_sml.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		pyautogui.time.sleep(100)

if __name__ == "__main__":
	main()
	