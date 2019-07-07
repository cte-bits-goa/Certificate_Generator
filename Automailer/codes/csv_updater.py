import pandas as pd
import yagmail
import os
import shutil
"""
Return three lists names, the directory of certificates and email addresses
read from a file specified by filename.
"""
LIMIT=45
def get_update_contacts():
    input_df = pd.read_csv("inputfile.csv")
    flag=False
    shutil.copy("inputfile.csv","Copies/Last_copy.csv")
    if len(input_df) > LIMIT :
        rem_df=input_df[LIMIT:]
        input_df=input_df[:LIMIT]
        rem_df.to_csv("inputfile.csv",index=False)
        Progress="Mailing List updated till {}".format(input_df['Name'].tolist()[-1])
    else :
        Progress="Mailing List Completed"
        flag=True
    names = input_df['Name'].tolist()
    emails = input_df['Email'].tolist()
    certs = input_df['Cert'].tolist()
    if flag:
    	os.remove("inputfile.csv")
    	os.mkdir("complete")
    return names, certs, emails