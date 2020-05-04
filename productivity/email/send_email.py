# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os.path

def send_email(addr, subject, body, attachments=[]):
	
	gmail_user = "yuxiaoli.bot@gmail.com"
	gmail_pwd = "automatic"
	FROM = gmail_user	# cheating recipient does not work
	TO = addr
	
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message['From'] = FROM
	COMMASPACE = ', '
	message['To'] = COMMASPACE.join(TO)
	
	message['Subject'] = subject
	message['Bcc'] = None
	
	# Add body to email
	message.attach(MIMEText(body, "plain", "utf-8"))
	
	for filepath in attachments:
		filename = os.path.basename(filepath)
		
		with open(filepath, 'rb') as attachment:
			# Add file as application/octet-stream
			# Email client can usually download this automatically as attachment
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())
			
		# Encode file in ASCII characters to send by email    
		encoders.encode_base64(part)

		# Add header as key/value pair to attachment part
		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {filename}",
		)
		
		# Add attachment to message and convert message to string
		message.attach(part)
		
	text = message.as_string()
	
	
	'''
	# SMTP_SSL Example
	server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	server_ssl.ehlo() # optional, called by login()
	server_ssl.login(gmail_user, gmail_pwd)  
	# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
	server_ssl.sendmail(FROM, TO, msg.as_string())
	#server_ssl.quit()
	server_ssl.close()
	'''
	
	# Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
	session.starttls() # enable security
	session.login(gmail_user, gmail_pwd) # login with mail_id and password
	#text = msg.as_string()
	session.sendmail(FROM, TO, text)
	session.quit()
	
	print('Mail sent')

def main():
	send_email(["yuxiaoli.qualcomm@gmail.com", "sean.li@cimoninc.com"], u"你好", "hello, world", ["attachment.txt"])
	
	
if __name__ == "__main__":
	main()
	