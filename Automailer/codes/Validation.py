import pandas as pd
import yagmail
import os
import shutil
#Checks if files are present and correctly formatted
def validate():
	
	#Checks inputfile.csv
	if not os.path.exists("inputfile.csv"):
		if os.path.exists("complete") :
			print("Mails are completed for this course")
		else :
			print("inputfile.csv not found")
		return False
	else :
		print("inputfile.csv Present")
	
	#Checks Certs folder
	if not os.path.exists("Certs"):
		print("Certs directory not found")
		return False
	else :
		print("Certs folder Present")

	#checks for Text files
	condition=0
	if not os.path.exists("Text_files/message.txt"):
		print("message.txt not found")
		return False
	else :
		condition=1
	if not os.path.exists("Text_files/prompt.txt"):
		print("prompt.txt not found")
		return False
	else :
		condition=1
	if not os.path.exists("Text_files/course.txt"):
		print("course.txt not found")
		return False
	else :
		condition=1
	if condition == 1:
		print("Text files present")

	#checks for copy of file
	if not os.path.exists("inputfile_copy.csv"):
		shutil.copy("inputfile.csv","Copies/inputfile_copy.csv")
		print("inputfile copy created")
	else :
		print("inputfile copy present")
	return True