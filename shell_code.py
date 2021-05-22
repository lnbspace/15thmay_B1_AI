Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
Wow this is my function
>>> xyz()
Wow this is my function
>>> s = xyz()
Wow this is my function
>>> s
>>> print(s)
None
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
I got, Hiii
>>> xyz2(45)
I got, 45
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
wow
wow
>>> k
'nice'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
It does something...
Value of m=4.5
It does something...
Value of n=30
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
(68, 39304, 21.0)
>>> a,b,c=xyz5(34)
>>> a
68
>>> b
39304
>>> c
>>> c
21.0
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py =============
66
>>> xyz6(a=34,c=10,b=5)
29
>>> xyz6(34,10,5)
39
>>> xyz6(4,5)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    xyz6(4,5)
TypeError: xyz6() missing 1 required positional argument: 'c'
>>> xyz6(a=34,c=10)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    xyz6(a=34,c=10)
TypeError: xyz6() missing 1 required positional argument: 'b'
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz7(3,4)
-3
>>> xyz7(3,4,5)
2
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz8(b=10)
0
>>> xyz8(c=50)
-30
>>> xyz8()
10
>>> xyz8(3,4,5,8)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    xyz8(3,4,5,8)
TypeError: xyz8() takes from 0 to 3 positional arguments but 4 were given
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz9(2)
()
2
>>> xyz9(2,45)
(45,)
2
>>> xyz9(2,45,67)
(45, 67)
2
>>> xyz9(2,45,67,89)
(45, 67, 89)
2
>>> xyz9(2,45,67,89,'hello')
(45, 67, 89, 'hello')
2
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz10()
>>> xyz10(435)
435
>>> xyz10(435,4)
435
4
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz11(3,4,6,7,5,3,7,0)
0
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz11(3,4,6,7,5,3,7,0)
-28
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz12(name='Sanam', data='Dont know', more=[45,5,6], orEk = 45)
name Sanam
data Dont know
more [45, 5, 6]
orEk 45
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz12(name='Sanam', data='Dont know', more=[45,5,6], orEk = 45)
name Sanam
data Dont know
more [45, 5, 6]
orEk 45
{'name': 'Sanam', 'data': 'Dont know', 'more': [45, 5, 6], 'orEk': 45}
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> xyz13(3,5,7,8,name=78)
(3, 5, 7, 8)
{'name': 78}
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
go
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc()
Hello
>>> help(abc)
Help on function abc in module __main__:

abc()
    This is my function document
    and I have created inside the function only

>>> print(abc.__doc__)

    This is my function document
    and I have created inside the function only
    
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> z
'\na = 10\nb = 30\nprint(a+b)\n'
>>> exec(z)
40
>>> a
10
>>> b
30
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> z
'\na = 10\nb = 30\nprint(a+b)\n'
>>> a
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> exec(z)
40
>>> a
10
>>> b
30
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> k = abc
>>> k()
Hello
>>> abc()
Hello
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc2(5)
5
>>> abc2(13)
9
None
None
None
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc2(13)
9
9
10
11
12
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc3(45)
45
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc4(34)
good 34
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    abc4(34)
  File "E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py", line 130, in abc4
    return ab(x,x*2)
TypeError: ab() takes 1 positional argument but 2 were given
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc4(34)
good 34
102
>>> m = abc4(34)
good 34
102
>>> m
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc4(34)
good 34
102
>>> m = abc4(34)
good 34
102
>>> m
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc5(34)
good 34
102
>>> m = abc5(34)
good 34
>>> m
102
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> m = abc6(34)
good 34
>>> m
<function abc6.<locals>.ab at 0x0000021D2FF9DAF0>
>>> m(4,99)
103
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc('go')
'gogo'
>>> abc(4)
8
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> abc('go')
'gogo'
>>> abc2('go')
'gogo'
>>> lambda x:x+3
<function <lambda> at 0x0000022CFDAEDB80>
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> operate([4,6,890,4])
8
12
1780
8
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
6
108
12
16
68
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
6
108
12
16
68
--------------------
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
6
108
12
16
68
--------------------
27
157464
216
512
39304
--------------------
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
6
108
12
16
68
--------------------
27
157464
216
512
39304
--------------------
>>> print(map(lambda n:n+4, a))
<map object at 0x000001896E510CA0>
>>> list(map(lambda n:n+4, a))
[7, 58, 10, 12, 38]
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
[3, 7, 11]
>>> a = [3,54,6,8,34,7,11,44]
>>> b = map(lambda n:n+4, a)
>>> b
<map object at 0x000001D518280C40>
>>> next(b)
7
>>> next(b)
58
>>> next(b)
10
>>> next(b)
12
>>> next(b)
38
>>> next(b)
11
>>> next(b)
15
>>> next(b)
48
>>> next(b)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    next(b)
StopIteration
>>> list(b)
[]
>>> b = map(lambda n:n+4, a)
>>> list(b)
[7, 58, 10, 12, 38, 11, 15, 48]
>>> next(b)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    next(b)
StopIteration
>>> list(b)
[]
>>> b = map(lambda n:n+4, a)
>>> next(b)
7
>>> next(b)
58
>>> list(b)
[10, 12, 38, 11, 15, 48]
>>> list(b)
[]
>>> b = map(lambda n:n+4, a)
>>> for i in b:
	print(i)

	
7
58
10
12
38
11
15
48
>>> for i in b:
	print(i)

	
>>> 
============= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 4/scirpt_file.py ============
>>> k = xyz(34)
>>> k
<generator object xyz at 0x000001C613471740>
>>> list(k)
[35, 36, 34, 68]
>>> list(k)
[]
>>> k = xyz(34)
>>> m = map(lambda p:p*2, k)
>>> list(m)
[70, 72, 68, 136]
>>> 