#!/usr/bin/python
import pyautogui

def main():
	response_time = 8;
	pyautogui.time.sleep(5)
	retry = False
	while True:
		
		if (retry):
			# skip current position and move on
			pyautogui.hotkey('ctrl', 'tab')
			pyautogui.time.sleep(response_time)
			retry = False
			continue
		# close current tab and startover
		pyautogui.hotkey('ctrl', 'w')
		pyautogui.time.sleep(response_time)
		# click blank
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('blank.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		retry = True
		continue

if __name__ == "__main__":
	main()
	