# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
# Here are the email package modules we'll need
from email.mime.multipart import MIMEMultipart

def send_text_email(from_addr, to_addr, subject, content):
	
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr

	# Send the message via our own SMTP server.
	s = smtplib.SMTP('localhost')
	s.send_message(msg)
	s.quit()

def main():
	send_text_email("c_yuxiao@quicinc.com", "yuxiaoli.qualcomm@gmail.com", "hi from c-yuxiao", "hello, world")
	send_text_email("test@test.com", "c_yuxiao@quicinc.com, yuxiaoli.qualcomm@gmail.com", "hi from c-yuxiao", "hello, world")
	
	
if __name__ == "__main__":
	main()
	