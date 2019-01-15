import smtplib
import pandas as pd
from string import Template
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

MY_ADDRESS = 'cte.bitsgoa@gmail.com'
PASSWORD = 'passwd goes here'



def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    input_df = pd.read_csv(filename)
    names = input_df['Name'].tolist()
    emails = input_df['Email'].tolist()

    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
"""
Write another such function to get certificate pdf name and call it in main,
depending how certs are named maybe using ID nos. etc.
"""

def main():
    names, emails = get_contacts('inputfile.csv') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(name)
        print(email)
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is a TEST, or is it? mass fuckin mail bitches"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        path = "cert.pdf"
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(op.basename(path)))
        msg.attach(part)
     
        # send the message via the server set up earlier.
        s.sendmail(MY_ADDRESS,email,msg.as_string())
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
	main()
