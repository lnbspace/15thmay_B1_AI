Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> Abc()
<__main__.Abc object at 0x0000020C39C4BDC0>
>>> Abc
<class '__main__.Abc'>
>>> a = Abc()
>>> a
<__main__.Abc object at 0x0000020C39C4BDC0>
>>> type(a)
<class '__main__.Abc'>
>>> print(a)
<__main__.Abc object at 0x0000020C39C4BDC0>
>>> len(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    len(a)
TypeError: object of type 'Abc' has no len()
>>> b = Abc()
>>> b
<__main__.Abc object at 0x0000020C3BD82370>
>>> a+b
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'Abc' and 'Abc'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x
<__main__.Abc object at 0x0000018A651D0520>
>>> print(x)
<__main__.Abc object at 0x0000018A651D0520>
>>> x.a
10
>>> Abc.a
10
>>> x.a = 30
>>> Abc.a
10
>>> x.a
30
>>> y = Abc()
>>> y.a
10
>>> Abc.a = 20
>>> y.a
20
>>> x.a
30
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py ============
10
>>> x = Abc()
>>> Abc.a
10
>>> x.a
10
>>> x.a = 20
>>> Abc.a=40
>>> y = Abc()
>>> y.a
40
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
10
>>> x = Abc()
>>> x.a
10
>>> x.show()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x.show()
TypeError: show() takes 0 positional arguments but 1 was given
>>> show()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    show()
NameError: name 'show' is not defined
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
10
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
10
>>> x= Abc()
>>> x.show()
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.show()
Its showtime
>>> x.a
10
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x.values()
  File "E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py", line 23, in values
    print(a)
NameError: name 'a' is not defined
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
10
Its showtime
None
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
10
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
10
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
10
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> x = Abc()
>>> x.values()
10
Its showtime
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> obj = Xyz()
>>> obj.change(30,40)
>>> obj.show()
30 40.0
>>> obj2 = Xyz()
>>> obj.change(20,25)
>>> obj2.change(60,80)
>>> obj2.show()
60 80.0
>>> obj.show()
20 25.0
>>> Xyz.c = 3
>>> obj2.change(65,20)
>>> obj2.show()
195 6.666666666666667
>>> obj.show()
20 25.0
>>> obj.change(20,25)
>>> obj.show()
60 8.333333333333334
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> obj = Xyz()
Yes you are created
>>> obj2 = Xyz()
Yes you are created
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> obj = Xyz()
Yes you are created
>>> obj2 = Xyz()
Yes you are created
>>> del obj
You're gone
>>> obj2 = 45
You're gone
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> obj = Xyz()
>>> obj.show()
0 0
>>> obj2 = Xyz(40,50)
>>> obj2.show()
40 50
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> a = Register('Aman','DevOps')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a = Register('Aman','DevOps')
  File "E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py", line 69, in __init__
    for i in id_var.keys():
NameError: name 'id_var' is not defined
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> a = Register('Aman','DevOps')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a = Register('Aman','DevOps')
  File "E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py", line 69, in __init__
    for i in id_var.keys():
NameError: name 'id_var' is not defined
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 6/script_file.py =============
>>> a = Register('Aman','DevOps')
>>> b = Register('Rehan','IoT')
>>> c = Register('Thabasum','IoT')
>>> d = Register('Bhumi','DevOps')
>>> a.show()
ID:D1
NAME:Aman
COURSE:DevOps
>>> b.show()
ID:I1
NAME:Rehan
COURSE:IoT
>>> c.show()
ID:I2
NAME:Thabasum
COURSE:IoT
>>> d.show()
ID:D2
NAME:Bhumi
COURSE:DevOps
>>> 