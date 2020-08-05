'''
pip install boto3
'''
import boto3
from botocore.exceptions import ClientError

from python_toolbox.productivity.email.send_email import create_message

def send_text_email(address, subject, body, region="us-west-2"):
	# Replace sender@example.com with your "From" address.
	# This address must be verified with Amazon SES.
	SENDER = "Sean Li <sean.li@cimoninc.com>"
	#SENDER = "Sean Li <yuxiaoli.bot@gmail.com>"

	# Replace recipient@example.com with a "To" address. If your account is still in the sandbox, this address must be verified.
	#COMMASPACE = ', '
	#RECIPIENT = COMMASPACE.join(address)

	# Specify a configuration set. If you do not want to use a configuration set, comment the following variable, and the ConfigurationSetName=CONFIGURATION_SET argument below.
	#CONFIGURATION_SET = "ConfigSet"

	# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
	#AWS_REGION = region

	# The subject line for the email.
	SUBJECT = subject

	# The email body for recipients with non-HTML email clients.
	BODY_TEXT = (body)
				
	# The HTML body of the email.
	BODY_HTML = """<html>
	<head></head>
	<body>
	  <h1>Amazon SES Test (SDK for Python)</h1>
	  <p>This email was sent with
		<a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
		<a href='https://aws.amazon.com/sdk-for-python/'>
		  AWS SDK for Python (Boto)</a>.</p>
	</body>
	</html>
				"""            

	# The character encoding for the email.
	CHARSET = "UTF-8"

	# Create a new SES resource and specify a region.
	client = boto3.client('ses',region_name=region)
	
	# Try to send the email.
	try:
		#Provide the contents of the email.
		response = client.send_email(
			Destination={
				'ToAddresses': address,
			},
			Message={
				'Body': {
					# 'Html': {
						# 'Charset': CHARSET,
						# 'Data': BODY_HTML,
					# },
					'Text': {
						'Charset': CHARSET,
						'Data': BODY_TEXT,
					},
				},
				'Subject': {
					'Charset': CHARSET,
					'Data': SUBJECT,
				},
			},
			Source=SENDER,
			# If you are not using a configuration set, comment or delete the following line
			#ConfigurationSetName=CONFIGURATION_SET,
		)
		
	# Display an error if something goes wrong.	
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email sent! Message ID:"),
		print(response['MessageId'])

def send_email(address, subject, body, attachments=[], region="us-west-2"):
	# Replace sender@example.com with your "From" address.
	# This address must be verified with Amazon SES.
	SENDER = "Sean Li <sean.li@cimoninc.com>"
	#SENDER = "Sean Li <yuxiaoli.bot@gmail.com>"

	# Replace recipient@example.com with a "To" address. If your account is still in the sandbox, this address must be verified.
	#COMMASPACE = ', '
	#RECIPIENT = COMMASPACE.join(address)

	# Specify a configuration set. If you do not want to use a configuration set, comment the following variable, and the ConfigurationSetName=CONFIGURATION_SET argument below.
	#CONFIGURATION_SET = "ConfigSet"

	# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
	#AWS_REGION = region
	
	FROM = SENDER
	TO = address
	message = create_message(FROM, TO, subject, body, attachments)
	text = message.as_string()

	# Create a new SES resource and specify a region.
	client = boto3.client('ses',region_name=region)
	
	try:
		response = client.send_raw_email(
			RawMessage={
				'Data': text
			}
		)
		
	# Display an error if something goes wrong.	
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email sent! Message ID:"),
		print(response['MessageId'])

if __name__ == "__main__":
	receivers = ["yuxiaoli.qualcomm@gmail.com", "sean.li@cimoninc.com"]
	subject = u"你好"
	body = "hello, world"
	attachments = ["attachment.txt"]
	
	send_email(receivers, subject, body, attachments)