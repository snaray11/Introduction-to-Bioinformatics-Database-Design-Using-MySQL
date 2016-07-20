Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os, sys
>>> os.chdir ('C:\BINF650\pysrc' )
>>> sys.path.append( 'pysrc' )
>>> import Narayanan_HW7_Q2 as hw7
>>> db, cur = hw7.Connect( 'binf.gmu.edu', 'snaray11', 'snaray11', 'snaray112624' )
>>> age=hw7.GetPilotAges(cur)
>>> vectorAge = hw7.ConvertToVector(age)
>>> Average1 = hw7.SumAge(vectorAge)
>>> print Average1
40.0
>>> 
