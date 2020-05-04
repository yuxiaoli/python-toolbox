# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

def send_text_email(addr, subject, content):
	
	gmail_user = "yuxiaoli.bot@gmail.com"
	gmail_pwd = "automatic"
	FROM = gmail_user	# cheating recipient does not work
	TO = addr
	
	
	msg = MIMEText(content)
	msg['Subject'] = subject
	msg['From'] = FROM
	
	COMMASPACE = ', '
	msg['To'] = COMMASPACE.join(TO)
	
	
	# SMTP_SSL Example
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(gmail_user, gmail_pwd)  
	# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
	server_ssl.sendmail(FROM, TO, msg.as_string())
	#server_ssl.quit()
	server_ssl.close()
	print('successfully sent the mail')

def main():
	send_text_email(["yuxiaoli.qualcomm@gmail.com", "c_yuxiao@quicinc.com"], "test", "hello, world")
	
	
if __name__ == "__main__":
	main()
	