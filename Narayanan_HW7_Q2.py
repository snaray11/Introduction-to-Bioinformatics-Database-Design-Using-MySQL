#Name - Sithalechumi Narayanan
#Date - 10/28/2015
#BINF650 - Fall 2015 - Homework 7.

#Name of file - Narayanan_HW7_Q2.py

# Question 2

# Part 1 - To access database
import os,sys
import MySQLdb
import numpy as np

def Connect( host, db, user, passwd ):
	db = MySQLdb.connect (host=host,db=db,user=user,passwd=passwd)
	cur = db.cursor()
	return db, cur
	
	
# Part 2 - To get the ages of all the Pilots
def GetPilotAges(cur):
	cur.execute ("(select c50 from crash75 where c50 != '') union all (select c50 from crash80 where c50 != 'S' and c50 != '') union all (select c50 from crash85 where c50 != '');")
	age = cur.fetchall()
	type (age)
	return age
	
	
# Part 3 - To get the sum of all ages
def ConvertToVector(age):
	vectorAge = np.array(age,dtype=np.int) #converting the tuple age to numpy array/vector vectorAge
	return vectorAge
	

# Part 4 - To get the average age of all the Pilots
def SumAge(vectorAge):
	total = 0    #To find the total of all ages, I used a for loop
	for i in np.nditer(vectorAge,op_dtypes=['int32'], casting='same_kind'):
		total=total+i
	count=0         #To find the number of entries, I again used a for loop
	for j in vectorAge:
		count=count+1
	average=float(total/count)  
	return average
	