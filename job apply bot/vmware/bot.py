#!/usr/bin/python
import pyautogui

def main():
	response_time = 5;

	while True:
		# click "Apply Now"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('apply.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		pyautogui.press('end')
		pyautogui.time.sleep(1)
		# click "Select files"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_files.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(1)
		# double click "Yuxiao Li"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('yuxiaoli.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click(clicks=2)
		pyautogui.time.sleep(2)
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# click "select one"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_one.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.press('enter')
		for x in range(3):
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# click "select one"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_one.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.press('down')
		pyautogui.press('down')
		pyautogui.press('down')
		pyautogui.press('enter')
		for x in range(2):
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
		pyautogui.press('end')
		pyautogui.time.sleep(1)
		# click on read_confirmation_checkbox
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('read_confirmation_checkbox.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		pyautogui.press('end')
		pyautogui.time.sleep(1)
		# click on no_disability_checkbox
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('no_disability_checkbox.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		# sign (type in name)
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('name.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.typewrite('Yuxiao Li')
		# date
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('date.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.typewrite('06102017')
		# click "Next"
		btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
		pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# click "Submit"
		# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('submit.PNG')
		# pyautogui.moveTo(btnLocX, btnLocY)
		pyautogui.click()
		pyautogui.time.sleep(response_time)
		
		# close current tabs twice
		pyautogui.keyDown('ctrl')
		pyautogui.press('w')
		pyautogui.press('w')
		pyautogui.keyUp('ctrl')
		pyautogui.time.sleep(1)

if __name__ == "__main__":
	main()
	