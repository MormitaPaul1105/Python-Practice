Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Dhaka_Rongpur= 355
>>> Rangpur_Bogra=444
>>> total=Dhaka_Rongpur+Rangpur_Bogra
>>> print(total)
799
>>> meter_per_hour=56
>>> Time=toyal/meter_per_hour
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Time=toyal/meter_per_hour
NameError: name 'toyal' is not defined. Did you mean: 'total'?
>>> Time=total/meter_per_hour
>>> print(Time)
14.267857142857142
>>> Round(Time,2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Round(Time,2)
NameError: name 'Round' is not defined. Did you mean: 'round'?
>>> round(Time,2)
14.27
>>> round(Time,3)
14.268
>>> Time_Remainder=total%meter_per_hour
>>> print(Time_Remainder)
15
>>> DRB_BRD_distance=total**2
>>> print(DRB_BRD_distance)
638401
