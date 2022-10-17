"""
TO-DO
-----
Data:
-Incrementalization of spreadsheet
-spreadsheet updating
--getting current date

Frontend
-Showing
-Dot Darkening based on productivity progress
-Grid display

Very Frontend
-Make this a usable app somehow. (web app, android, idk)
"""
from datetime import date
import pandas

date_today = date.today()
#We're gonna use this^ to check if there's an activity
#entry for today or not

#print("Today's date:", date_today)


df = pandas.read_excel("data.xlsx")

#print(df)
#print(df.index)


#print(df.loc[0]) #important for later
#print("Len: " , len(df)) #important for later [number of rows]

for i in range(len(df)):
    print(df.loc[i])
    print("--")
