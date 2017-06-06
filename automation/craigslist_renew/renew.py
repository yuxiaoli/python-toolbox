#!/usr/bin/python
import pyautogui
import argparse

def renew(num_attempts):
	renew_counter = 0;	# posts renewed
	response_time = 1;
	attempt = 0;
	has_next = True;

	while True:
		try:
			# print("inside try")
			
			# find and click the renew button
			renewButtonLocationX,renewButtonLocationY  = pyautogui.locateCenterOnScreen('renew_button.PNG')
			pyautogui.moveTo(renewButtonLocationX, renewButtonLocationY)
			pyautogui.click()
			pyautogui.time.sleep(response_time)
			
			# go back to account postings page
			# for other browsers
			# pyautogui.press('backspace')
			
			# for chrome
			pyautogui.keyDown('alt')
			pyautogui.press('left')
			pyautogui.keyUp('alt')
			pyautogui.time.sleep(response_time)
			
			# update result and reset vars
			renew_counter += 1
			attempt = 0
			has_next = True

		# Exception handle when pyautogui can't locate the renew button on the screen
		except Exception:
			# print("inside exception")
			if (attempt < num_attempts):
				attempt += 1
				continue
			
			if (has_next):
				pyautogui.press('pgdn')
				has_next = False
				attempt = 0
				continue
			
			break
		   
	return renew_counter

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--num_attempts', type=int, default=6)
	args = parser.parse_args()
	
	num_renewed = renew(args.num_attempts)
	
	print("renew completed. {0} posts renewed".format(num_renewed))

if __name__ == "__main__":
	main()
	