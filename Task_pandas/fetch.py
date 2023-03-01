#converting csv to json file

import pandas as pd

csv_file = r'C:\Users\SAMARTH GUPTA\Documents\employee.csv'
emp_df = pd.read_csv(csv_file)

print("data from csv : \n",emp_df)


json_output = r'C:\Users\SAMARTH GUPTA\Documents\employee.json'
output = emp_df.to_json(json_output,indent = 1,orient = "records")

df = pd.read_json(json_output)
print("\ndata from json : ")
print(df)

print("\n data type of mobile is : " , df['mobile'].dtype)
print(df.shape)

print("\ndisplaying max 4 columns : ")
pd.set_option('display.max_columns',4)

print("\n top 7 records : ")
print(df.head(7))