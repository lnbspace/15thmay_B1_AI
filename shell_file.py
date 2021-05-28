Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py =============
>>> x = Abc('python')
Created
>>> del x
Deleted
>>> x = Abc('python')
Created
>>> print(x)
python
>>> x
<__main__.Abc object at 0x0000023A086300A0>
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py =============
>>> x = Abc('python')
Created
>>> print(x)
My Data
python
>>> x
python
>>> type(x)
<class '__main__.Abc'>
>>> y = x
>>> y
python
>>> type(y)
<class '__main__.Abc'>
>>> str(y)
'My Data\npython'
>>> d = str(y)
>>> d
'My Data\npython'
>>> e = repr(y)
>>> e
'python'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py =============
>>> x = Abc('python')
Created
>>> print(x)
python
>>> x
My Data
python
>>> y = x
>>> str(y)
'python'
>>> e = repr(y)
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> x[2]
't'
>>> x
My Data
python
>>> print(x)
python
>>> x[2:]
'thon'
>>> x[::-1]
'nohtyp'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> len(x)
6
>>> x()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x()
TypeError: 'Abc' object is not callable
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> x()
'python'
>>> x(3)
'pythonpythonpython'
>>> d = x(3)
>>> d
'pythonpythonpython'
>>> type(d)
<class 'str'>
>>> e = x(3,' String')
>>> e
'pythonpythonpython String'
>>> y = Abc('Java')
Created
>>> x > y
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x > y
TypeError: '>' not supported between instances of 'Abc' and 'Abc'
>>> True
True
>>> y>x
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    y>x
TypeError: '>' not supported between instances of 'Abc' and 'Abc'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> y = Abc('Java')
Created
>>> x > y
True
>>> y > x
False
>>> x < y
False
>>> y < x
True
>>> x >= y
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x >= y
TypeError: '>=' not supported between instances of 'Abc' and 'Abc'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> y = Abc('Java')
Created
>>> x >= y
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x >= y
TypeError: '>=' not supported between instances of 'Abc' and 'Abc'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> y = Abc('Java')
Created
>>> x >= y
True
>>> x>y
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x>y
TypeError: '>' not supported between instances of 'Abc' and 'Abc'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> y = Abc('Java')
Created
>>> x >= y
True
>>> x>y
True
>>> x<y
False
>>> x<=y
False
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc('python')
Created
>>> y = Abc('Java')
Created
>>> x==y
False
>>> s = 'aaaab'
>>> s2 = 'ac'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 37, in <module>
    class Abc(Xyz):
NameError: name 'Xyz' is not defined
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Abc(4)
>>> x.show()
4
>>> x.something()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    x.something()
AttributeError: 'Abc' object has no attribute 'something'
>>> p = Pqr()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    p = Pqr()
TypeError: __init__() missing 1 required positional argument: 'data'
>>> p = Pqr('hi')
>>> p.show()
hi
>>> p.something()
Yeah it is something
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Xyz('hi')
>>> y = Pqr(5)
>>> x.some()
its from Xyz
>>> y.somethin()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    y.somethin()
AttributeError: 'Pqr' object has no attribute 'somethin'
>>> y.something()
Yeah it is something
>>> y.show()
5
>>> x.show()
hi
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Mno()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    x = Mno()
TypeError: __init__() missing 1 required positional argument: 'data'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Mno()
>>> x.my()
My is MNO
>>> x.something()
Yeah it is something
>>> x.show()

>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Rqp()
>>> x.rrr()
Raaraaraa
>>> x.show()

>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Rqp()
>>> x.do()
I will do nothing
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Name()
>>> x.show()
wow
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Name()
>>> x.show()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    x.show()
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 68, in show
    super.show()
AttributeError: type object 'super' has no attribute 'show'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Name()
>>> x.show()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    x.show()
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 68, in show
    Abc.show()
TypeError: show() missing 1 required positional argument: 'self'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Name()
>>> x.show()

wow
>>> x = Name('Python')
>>> x.show()
Python
wow
>>> x = Zyx()
>>> x.val
45
>>> x.val = 56
>>> Zyx.val = 8888
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
>>> x = Zyx()
>>> x.val
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    x.val
AttributeError: 'Zyx' object has no attribute 'val'
>>> x.__val
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    x.__val
AttributeError: 'Zyx' object has no attribute '__val'
>>> x._Zyx__val
45
>>> Zyx.val
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    Zyx.val
AttributeError: type object 'Zyx' has no attribute 'val'
>>> Zyx.__val
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    Zyx.__val
AttributeError: type object 'Zyx' has no attribute '__val'
>>> Zyx._Zyx__val
45
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:3
Enter the second value:2
1.5
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:30
Enter the second value:0
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 74, in <module>
    print(a/b)
ZeroDivisionError: division by zero
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:4.5
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 72, in <module>
    a = int(input('Enter the first value:'))
ValueError: invalid literal for int() with base 10: '4.5'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:4
Enter the second value:2.1
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 73, in <module>
    b = int(input('Enter the second value:'))
ValueError: invalid literal for int() with base 10: '2.1'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py", line 72, in <module>
    a = int(input('Enter the first value:'))
ValueError: invalid literal for int() with base 10: ''
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:4
Enter the second value:0
You tried dividing by zero
4
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:4
Enter the second value:1.1
It didn't work well
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:4
Enter the second value:-3
-1.3333333333333333
Its going on well
Its done
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:0
Enter the second value:0
It didn't work well
Its going on well
Its done
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 7/script_file.py ============
Enter the first value:3.5
It didn't work well
Its going on well
Its done
>>> 