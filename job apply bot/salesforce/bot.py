#!/usr/bin/python
import pyautogui

def main():
	response_time = 12
	retry = False
	
	while True:
		try:
			pyautogui.press('end')
			pyautogui.time.sleep(1)
			# click "Apply Now"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('apply.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(response_time)
			
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('email.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('pmc.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.press('left')
			pyautogui.press('left')
			'''
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('hear_about_us.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			for x in range(27):
				pyautogui.press('down')
			'''
			# click "Continue"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('continue0.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "Choose File"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('choose_file.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(1)
			# double click "Yuxiao Li"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('yuxiaoli.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click(clicks=2)
			pyautogui.typewrite('Yuxiao Li.pdf')
			# pyautogui.time.sleep(10)
			pyautogui.press('enter')
			pyautogui.time.sleep(1)	# must to wait here
			# click "Continue"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('continue.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "Continue" sml
			loading_time = 0
			loading_time_limit = 60
			while (pyautogui.locateCenterOnScreen('continue_sml.PNG') == None):
				pyautogui.time.sleep(response_time)
				loading_time += response_time
				if (loading_time > loading_time_limit):
					break
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('continue_sml.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(response_time)
			
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('checkbox.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.press('end')
			pyautogui.time.sleep(1)
			# click "Gender"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('gender.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			# select "Male
			pyautogui.press('up')
			pyautogui.press('tab')
			for x in range(6):
				pyautogui.press('up')
			pyautogui.press('tab')
			pyautogui.press('up')
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			# click "Submit"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('submit.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# close current tabs twice
			pyautogui.keyDown('ctrl')
			pyautogui.press('w')
			pyautogui.press('w')
			pyautogui.keyUp('ctrl')
			pyautogui.time.sleep(1)
			retry = False
			
		except Exception:
			if (retry):
				# skip current position and move on
				pyautogui.hotkey('ctrl', 'tab')
				pyautogui.time.sleep(1)
				retry = False
				continue
			# close current tab and startover
			pyautogui.hotkey('ctrl', 'w')
			pyautogui.time.sleep(1)
			# click blank
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('blank.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(1)
			retry = True
			continue
			

if __name__ == "__main__":
	main()
	