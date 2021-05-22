import pandas as pd

data = pd.read_csv("Records.csv", header=0)
typemap = {"Instructor": "Appreciation",
           "Mentor": "Appreciation",
           "Merit": "Merit", "Participation": "Participation"}  # this dictionary is used to create the type column for the type of certificate to be generated for the awardee

data["Type"] = data["Position"].map(typemap)


data["CertID"] = data["CertID"].apply(
    lambda x: "http://legacy-cert.bpgc-cte.org/certs/{}.html".format(x))  # to convert the certID into a link to be clickable in the certificate for authentication

data["Position"] = data["Position"].replace(
    regex=r'Instructor', value='an instructor')  # replacing the positions to make it grammatically correct in the certificate
data["Position"] = data["Position"].replace(
    regex=r'Mentor', value='a Mentor')

# making the new csv file to be used in the latex file
data.to_csv('FinalRecords.csv')

print(data)
