import sys, argparse
# from subprocess import check_call
if sys.hexversion > 0x03000000:
	import winreg
else:
	import _winreg as winreg
'''
pip install pywin32
'''
import win32gui, win32con, os



def cleanup_path(path, separator):
	item_list = path.split(separator)

	# remove items from a list while iterating
	for index in reversed(xrange(len(item_list))):
		# print(index)
		# print(item_list[index])
		if not item_list[index]:
			del item_list[index]
		elif item_list[index][-1] == '\\':
			item_list[index] = item_list[index][:-1]
			# print(item_list[index])

	item_set = set(item_list)	# removes any duplicate
	item_list[:] = []	# it's assigning to a list slice that just happens to be the entire list, thereby replacing the list contents within the same Python list object, rather than just reseating one reference
	# if your list is accessed via multiple references the fact that you're just reseating one of the references and NOT altering the list object itself can lead to subtle, disastrous bugs
	for item in item_set:
		# print(item)
		# print(os.path.exists(item))
		if os.path.exists(item):	# check existence
			item_list.append(item)

	path = separator.join(item_list)
	# string is immutable in python
	return path



class Win32Environment:
	def __init__(self, scope):
		if scope not in ('user', 'system'):
			print("error: unknown scope")
			sys.exit(1)

		self.scope = scope
		if scope == 'user':
			self.root = winreg.HKEY_CURRENT_USER
			self.path = 'Environment'
		else: # scope = 'system'
			self.root = winreg.HKEY_LOCAL_MACHINE
			self.path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

	def getenv(self, name):
		try:
			key = winreg.OpenKey(self.root, self.path, 0, winreg.KEY_READ)
			try:
				value, type_id = winreg.QueryValueEx(key, name)
			except WindowsError:
				print("error: key not found")
				value = ''
			winreg.CloseKey(key)
		except Exception as e:
			print("error: winreg can't open")
			print(e)

		return value

	def setenv(self, name, value):
		try:
			# note: for 'system' scope, you must run this as Administrator
			key = winreg.OpenKey(self.root, self.path, 0, winreg.KEY_ALL_ACCESS)
			if not value:
				print("warning: setting value to be null")
			# to do - write the old value to a system log with time before set for safety reasons
			try:
				winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
			except WindowsError:
				print("error: set failed")
				
			winreg.CloseKey(key)
			# broadcast all the gui processes, most currently opening processes would ignore the broadcast without handling
			win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
		except Exception as e:
			print(e)


	def delenv(self, name):
		try:
			key = winreg.OpenKey(self.root, self.path, 0, winreg.KEY_ALL_ACCESS)
			# to do - write the old value to a system log with time before delete for safety reasons
			try:
				winreg.DeleteValue(key, name)
			except WindowsError:
				print("error: delete failed")
			winreg.CloseKey(key)
			win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
		except Exception as e:
			print(e)



def main():
	parser = argparse.ArgumentParser(
		prog='edit_sys_environ.py',
		usage='python edit_sys_environ.py var_name --scope user/system [-s var_value --append] [-d]',
		description = "utility script to get/set/delete windows environment variable",
		epilog="the old value will be written to a system log file () before set for safety purposes",
		fromfile_prefix_chars='@'
		)

	parser.add_argument('var_name', metavar='environ_var_name', help='the name of the environment variable')
	parser.add_argument('--scope', metavar='user/system', default = 'system', help='must be user/system')   # dest = scope
	parser.add_argument('-s', '--set', dest = 'var_value', metavar='environ_var_value', help='the value of the environment variable to be set')
	parser.add_argument('--append', action='store_true')  # dest = append
	parser.add_argument('-d', '--delete', action='store_true')  # dest = delete
	parser.add_argument('--cleanup', action='store_true')  # dest = cleanup
	args = parser.parse_args()

	env_reg = Win32Environment(args.scope)
	if args.var_value:
		if args.append:
			var_value = env_reg.getenv(args.var_name) + ";" + args.var_value
			env_reg.setenv(args.var_name, var_value)
		else:
			env_reg.setenv(args.var_name, args.var_value)

	elif args.delete:
		env_reg.delenv(args.var_name)
		
	else:
		var_value = env_reg.getenv(args.var_name)
		print('{0} = {1}'.format(args.var_name, var_value))
		if args.cleanup:
			if args.var_name.upper() == "PATH":
				var_value = cleanup_path(var_value, os.pathsep)
				# print(var_value)
				env_reg.setenv(args.var_name, var_value)
			else:
				print("can only cleanup path")
				# sys.exit(0)

if __name__ == "__main__":
	main()