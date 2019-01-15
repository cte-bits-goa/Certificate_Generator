import pandas as pd
import numpy as np 
for_split = pd.read_csv('Student_Certs_sem1_19.csv')
swd_names = np.load('swd_names.npy')
for_split['Name'] = swd_names
merit_df = pd.DataFrame(columns = for_split.columns)
complete_df = pd.DataFrame(columns = for_split.columns)

for row in for_split.iterrows():
	if(row[1]['Certificate'] == 'Merit'):
		merit_df = merit_df.append(row[1], ignore_index = True)
	elif(row[1]['Certificate'] == 'Completion'):
		complete_df = complete_df.append(row[1], ignore_index = True)

merit_df.to_csv('Merit_Students.csv', index= False)
complete_df.to_csv('Completed_Students.csv', index= False)

