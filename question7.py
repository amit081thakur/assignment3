Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,9,2,8,3,7,4,6,5]
>>> total_evens=0
>>> total_odds=0
>>> for x in list:
	if not x%2:
		total_evens=total_evens + 1
	else:
		total_odds=total_odds + 1

		
>>> print(" no. of evens:",total_evens)
 no. of evens: 4
>>> print(" no. of odds:",total_odds)
 no. of odds: 5
>>> 
