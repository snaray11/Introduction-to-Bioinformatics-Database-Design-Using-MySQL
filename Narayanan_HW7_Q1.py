#Name - Sithalechumi Narayanan
#Date - 10/28/2015
#BINF650 - Fall 2015 - Homework 7.

#Name of file - Narayanan_HW7_Q1.py

# Question 1

# Part 1 - To access database
import os,sys
import MySQLdb

def Connect( host, db, user, passwd ):
	db = MySQLdb.connect (host=host,db=db,user=user,passwd=passwd)
	cur = db.cursor()
	return db, cur


# Part 2 - To fetch all data in column c14
def GetData( cur ):
	cur.execute("select c14 from crash85")
	data=cur.fetchall()
	return data

	
# Part 3 - To count the total number of entries (number of incidents) for every city
def CityCount( data ):
		data2=set(data)       
		dct = { }
		for x in data2:
			dct[x]=0            
		for y in data:
			dct[y]+=1	   
		return dct
		
		
# Part 4 - To find out which city/cities fall under the category of having more than 200 entries
# Or more than 200 incidents
def City200( dct ):
    for key in dct:
	 if dct[key] > 200:
	    print key ,dct[key]
		


