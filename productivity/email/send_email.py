'''
https://myaccount.google.com/lesssecureapps
https://accounts.google.com/b/0/DisplayUnlockCaptcha

https://stackoverflow.com/questions/33233694/gmail-api-can-i-send-email-using-the-service-account
You cannot use a service account to impersonate a free gmail account. I spent a lot of time confirming this after reading a reply that was here before. Maybe it worked at some point, but it doesn't anymore.
'''
# Import smtplib for the actual sending function
import smtplib
#import ssl
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os.path
'''
import sys
sys.path.append('..')
from gdrive.gdrive import GMail
import mimetypes
import base64
'''
#import yagmail

def setup_server(port = 465):
	smtp_server = "smtp.gmail.com"
	# Create a secure SSL context
	#context = ssl.create_default_context()
	
	server = None
	try:
		if (port == 465):	# For SSL
			#server = smtplib.SMTP_SSL(smtp_server, port, context=context)
			server = smtplib.SMTP_SSL(smtp_server, port)
			
		elif (port == 587):	# For starttls
			server = smtplib.SMTP(smtp_server, port)
			#server.ehlo() # Can be omitted
			#server.starttls(context=context) # Secure the connection
			server.starttls()
			#server.ehlo() # Can be omitted
			
	except Exception as e:
		# Print any error messages to stdout
		print(e)
	
	return server

def create_message(sender, to, subject, body, attachments=[]):
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message['From'] = sender
	COMMASPACE = ', '
	message['To'] = COMMASPACE.join(to)
	
	message['Subject'] = subject
	message['Bcc'] = None
	
	# Add body to email
	message.attach(MIMEText(body, "plain", "utf-8"))
	
	# Add attachments
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
		
	return message

def send_email(address, subject, body, attachments=[]):
	gmail_user = "yuxiaoli.bot@gmail.com"
	gmail_pwd = "automatic"
	FROM = gmail_user	# cheating recipient does not work
	TO = address
	message = create_message(FROM, TO, subject, body, attachments)
	
	text = message.as_string()
	
	server = setup_server()
	server.login(gmail_user, gmail_pwd) # login with mail_id and password
	server.sendmail(FROM, TO, text)
	server.quit()
	
	print('Mail sent')
'''
def create_message_with_attachment(sender, to, subject, message_text, file):
	"""Create a message for an email.

	Args:
	sender: Email address of the sender.
	to: Email address of the receiver.
	subject: The subject of the email message.
	message_text: The text of the email message.
	file: The path to the file to be attached.

	Returns:
	An object containing a base64url encoded email object.
	"""
	message = MIMEMultipart()
	message['to'] = to
	message['from'] = sender
	message['subject'] = subject

	msg = MIMEText(message_text)
	message.attach(msg)
	
	content_type, encoding = mimetypes.guess_type(file)

	if content_type is None or encoding is not None:
		content_type = 'application/octet-stream'
	main_type, sub_type = content_type.split('/', 1)
	if main_type == 'text':
		fp = open(file, 'rb')
		msg = MIMEText(fp.read(), _subtype=sub_type)
		fp.close()
	elif main_type == 'image':
		fp = open(file, 'rb')
		msg = MIMEImage(fp.read(), _subtype=sub_type)
		fp.close()
	elif main_type == 'audio':
		fp = open(file, 'rb')
		msg = MIMEAudio(fp.read(), _subtype=sub_type)
		fp.close()
	else:
		fp = open(file, 'rb')
		msg = MIMEBase(main_type, sub_type)
		msg.set_payload(fp.read())
		fp.close()
		filename = os.path.basename(file)
		msg.add_header('Content-Disposition', 'attachment', filename=filename)
		message.attach(msg)
	
	return {'raw': base64.urlsafe_b64encode(message.as_string().encode("utf-8")).decode()}
	
def send_gmail(sender, to, subject, message_text, file, private_key_file):
	gmail_server = GMail(private_key_file)
	message = create_message_with_attachment(sender, to, subject, message_text, file)
	gmail_server.send(message)
'''
def main():
	receivers = ["yuxiaoli.qualcomm@gmail.com", "sean.li@cimoninc.com"]
	subject = u"你好"
	body = "hello, world"
	attachments = ["attachment.txt"]
	
	send_email(receivers, subject, body)#, attachments)
	
	'''
	yag_server = yagmail.SMTP("yuxiaoli.bot@gmail.com", "automatic")
	yag_server.send(
		to=receivers,
		subject=subject,
		contents=body,
		attachments=attachments
	)
	'''
	
	#send_gmail("yuxiaoli.bot@gmail.com", receivers[0], subject, body, attachments[0], "b007.json")
	
	
if __name__ == "__main__":
	main()
	