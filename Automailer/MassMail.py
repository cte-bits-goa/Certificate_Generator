import pandas as pd
import yagmail
import os
import shutil
from codes.Validation import *
from codes.csv_updater import *
from codes.Mailer import *

#Parameters
prompt_msg=open("Text_files/prompt.txt","r").read()

def main():
	if not validate():
		return

	prompt=int(input(prompt_msg.format(MY_ADDRESS,Message,course,LIMIT)))
	if prompt != 0 :
		return

	names, certs, emails = get_update_contacts()
	
	for name, cert, email in zip(names, certs, emails):
	    mail_cert(name,cert,email)

if __name__ == '__main__':
	main()