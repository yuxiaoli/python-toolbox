#!/usr/bin/python
import pyautogui

def main():
	response_time = 6;
	retry = False

	while True:
		try:
			# click "Apply Now"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('apply.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(response_time)
			
			# click "Next"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			# pyautogui.keyDown('shift')
			# for x in range(3):
				# pyautogui.press('tab')
			# pyautogui.keyUp('shift')
			# pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "Next"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			# pyautogui.keyDown('shift')
			# for x in range(3):
				# pyautogui.press('tab')
			# pyautogui.keyUp('shift')
			# pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			pyautogui.press('end')
			pyautogui.time.sleep(1)
			# click "Select files"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_files.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(1)
			# double click "Yuxiao Li"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('yuxiaoli.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click(clicks=2)
			# pyautogui.time.sleep(2)
			# pyautogui.typewrite('C:\Users\yuxiaoli\Downloads\Yuxiao Li.pdf')
			pyautogui.typewrite('Yuxiao Li.pdf')
			pyautogui.press('enter')
			pyautogui.time.sleep(1)	# must to wait here
			# click "Next"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			for x in range(3):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "select one"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_one.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			for x in range(5):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.press('down')
			pyautogui.press('enter')
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
			pyautogui.press('tab')
			pyautogui.typewrite('06122017')
			pyautogui.press('tab')
			pyautogui.typewrite('Google')
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
			# click "Next"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "select one"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_one.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			for x in range(5):
				pyautogui.press('tab')
			pyautogui.press('enter')
			# select "Asian"
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
			# select "Male"
			pyautogui.press('tab')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('down')
			pyautogui.press('enter')
			# click on read_confirmation_checkbox
			# pyautogui.press('end')
			# pyautogui.time.sleep(1)
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('read_confirmation_checkbox.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			pyautogui.press('tab')
			pyautogui.press('space')
			# click "Next"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('next.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# click "Submit"
			# btnLocX,btnLocY = pyautogui.locateCenterOnScreen('submit.PNG')
			# pyautogui.moveTo(btnLocX, btnLocY)
			# pyautogui.click()
			# for x in range(6):
				# pyautogui.press('tab')
			# pyautogui.press('enter')
			pyautogui.keyDown('shift')
			for x in range(3):
				pyautogui.press('tab')
			pyautogui.keyUp('shift')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			# close current tabs twice
			pyautogui.keyDown('ctrl')
			pyautogui.press('w')
			pyautogui.press('w')
			pyautogui.keyUp('ctrl')
			pyautogui.time.sleep(2)
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
			pyautogui.time.sleep(1)
			retry = True
			continue	

if __name__ == "__main__":
	main()
	