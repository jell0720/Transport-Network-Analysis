import csv
#Row wise
def write_to_file(filename,content):
	f=open(filename,'a')
	f.writelines(content)
	f.close()

#file_name='2014-03-02.csv'
#header='Data/Day2/'
def seperate_bus_day():
	for i in range(1,8):# for 7 days
		file_name='2014-03-0'+str(i)+'.csv'# File name of the day
		header='Data/Day'+str(i)+'/'# To differentiate between days
		print header
	
		with open(header+file_name,'r') as csvfile:
			readers=csv.reader(csvfile,delimiter=' ',quotechar='|')
			for row in readers:
   				a=row[0].split(',')
   				write_to_file(header+'Buses/'+a[5]+'.csv',row[0]+'\n')#bus unique id is file name

seperate_bus_day()
#Column wise
#import pandas as pd
#df=pd.read_csv('Data/2014-03-01.csv')
#saved_column=df['long']
#print saved_column[1]
