import pandas as pd
import yagmail
import os
import shutil
'''
This is the mailer and progress tracker that works on yagmail
'''
Message=open("Text_files/message.txt","r").read()
course=open("Text_files/course.txt","r").read()
Credentials=open("Credentials.txt","r").read()
MY_ADDRESS,PASSWORD = Credentials.split('\n')[0],Credentials.split('\n')[1]
path="Certs/{}"

def mail_cert(name,cert,email):
    contents = [Message.format(NAME=name,COURSE=course),path.format(cert)]
    yagmail.SMTP(MY_ADDRESS,PASSWORD).send(email,'CTE {} Certificate'.format(course),contents)
    print("Mail Sent to {}".format(name))