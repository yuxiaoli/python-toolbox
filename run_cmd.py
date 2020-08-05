import subprocess
#import shlex
import sys
import datetime
from python_toolbox.aws.ses_send_email import send_email
import socket

def create_email(ret, cmd, stdout, stderr, start, end):
	subject = ""
	hostname = socket.gethostname()
	body = cmd + '\n' + \
			'@' + hostname + '\n' + \
			'\n' + \
			"Start: " + str(start) + '\n' + \
			"End: " + str(end) + '\n' + \
			"Duration: "
			
	delta = end - start
	minutes, seconds = divmod(delta.seconds, 60)
	hours, minutes = divmod(minutes, 60)
	
	duration = ""
	if (hours):
		duration += str(hours) + "h "
	if (minutes):
		duration += str(minutes) + "m "
	duration += str(seconds) + "s"
	
	body += duration + '\n' + \
			'\n'
	
	attachment = None
	
	if (ret == 0):	# Success
		subject = "Success"
		attachment = "output.txt"
		
		# Create "output.txt"
		f = open(attachment, 'w')
		f.write(stdout)
		f.close()
		
	else:	# Fail
		subject = "Fail"
		body += stderr
	
	return subject, body, attachment
	
def process_result(result, start, end):
	ret = result.returncode
	args = result.args
	separator = ' '
	cmd = separator.join(args)
	
	stdout = ""
	if (result.stdout):
		stdout = result.stdout.decode('utf-8')
	stderr = ""
	if (result.stderr):
		stderr = result.stderr.decode('utf-8')
		
	subject, body, attachment = create_email(ret, cmd, stdout, stderr, start, end)
	
	if (attachment):
		attachment = [attachment]
	else:
		attachment = []
		
	to = ["seanli.cimon@gmail.com"]
	send_email(to, subject, body, attachment)

def run_cmd(args):
	#print(args)
	start = datetime.datetime.now()
	result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	end = datetime.datetime.now()
	
	process_result(result, start, end)

def execute(cmd):
	args = cmd.split()
	result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
	
if __name__ == "__main__":
	args = sys.argv
	args.pop(0)
	run_cmd(args)