Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os, sys
>>> os.chdir ('C:\BINF650\pysrc' )
>>> sys.path.append( 'pysrc' )
>>> import Narayanan_HW7_Q1 as hw7
>>> db, cur = hw7.Connect( 'binf.gmu.edu', 'snaray11', 'snaray11', 'snaray112624' )
>>> data=hw7.GetData(cur)
>>> data2=hw7.CityCount(data)
>>> hw7.City200(data2)
('KANSAS CITY',) 231
('ST LOUIS',) 486
('CHICAGO',) 315
('ANCHORAGE',) 234
>>> 
