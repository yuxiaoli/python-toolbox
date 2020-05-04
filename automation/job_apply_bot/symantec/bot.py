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
			pyautogui.keyDown('ctrl')
			pyautogui.click()
			pyautogui.keyUp('ctrl')
			pyautogui.time.sleep(response_time)
			
			# click "Select files"
			btnLocX,btnLocY = pyautogui.locateCenterOnScreen('select_files.PNG')
			pyautogui.moveTo(btnLocX, btnLocY)
			pyautogui.click()
			pyautogui.time.sleep(1)
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
			
			pyautogui.keyDown('shift')
			for x in range(5):
				pyautogui.press('tab')
			pyautogui.keyUp('shift')
			pyautogui.press('enter')
			for x in range(14):
				pyautogui.press('up')
			pyautogui.press('enter')
			# click "Next"
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			for x in range(15):
				pyautogui.press('tab')
			pyautogui.typewrite('052014')
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.typewrite('082014')
			for x in range(6):
				pyautogui.press('tab')
			pyautogui.typewrite('052012')
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.typewrite('082012')
			for x in range(8):
				pyautogui.press('tab')
			pyautogui.typewrite('2010')
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.typewrite('2014')
			for x in range(3):
				pyautogui.press('tab')
			pyautogui.typewrite('C/C++, Python, Java, HTML, Perl, Verilog, Assembly, Git')
			# click "Next"
			for x in range(6):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			for x in range(4):
				pyautogui.press('tab')
			pyautogui.press('enter')
			for x in range(2):
				pyautogui.press('down')
			pyautogui.press('enter')
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('space')
			for x in range(8):
				pyautogui.press('tab')
			pyautogui.press('enter')
			for x in range(3):
				pyautogui.press('down')
			pyautogui.press('enter')
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('space')
			# click "Next"
			for x in range(2):
				pyautogui.press('tab')
			pyautogui.press('enter')
			pyautogui.time.sleep(response_time)
			
			for x in range(6):
				pyautogui.press('tab')
			pyautogui.press('space')
			pyautogui.press('tab')
			pyautogui.typewrite('Yuxiao Li')
			pyautogui.press('tab')
			pyautogui.typewrite('06152017')
			# click "Next"
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
			# go back
			pyautogui.hotkey('alt', 'left')
			pyautogui.time.sleep(response_time)
			retry = True
			continue

if __name__ == "__main__":
	main()
	