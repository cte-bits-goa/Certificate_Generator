import json
import requests
import pandas as pd
sem=input("Enter semester(eg:Semester 2 2019-20):")
fname=input("Enter CSV name:")
csv = pd.read_csv(fname)
file=open('certid.txt',"w")
names=csv['Name']
courses=csv['Course']
positions=csv['Position']
key=input("Enter authorization key")
url = "http://legacy-cert.bpgc-cte.org/api/certgen"
headers = {
  'authorization': key,
  'Content-Type': 'application/json'
}
for name,position,course in zip(names,positions,courses):
    payload = "{\r\n\t\"name\": \""+name+"\",\r\n\t\"course\": \""+course+"\",\r\n\t\"type\": \""+position+"\",\r\n\t\"time\": \""+sem+"\"\r\n}\r\n\r\n"

    response = requests.post(url, headers=headers, data = payload)
    print(response.content)
    certid=(response.content.decode())
    file.write(certid+"\n")
