Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 6*6
36
>>> a = 10
>>> b = 30
>>> print(a-b)
-20
>>> a/b
0.3333333333333333
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py =======
630
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py =======
6300
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py =======
6300
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py", line 4, in <module>
    print(c)
NameError: name 'c' is not defined
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py =======
6300
Traceback (most recent call last):
  File "E:/TN/SITP21/15thMay_B1_AI/Day 1/first_python_script.py", line 4, in <module>
    print(c)
NameError: name 'c' is not defined
>>> if = 10
SyntaxError: invalid syntax
>>> iff = 10
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36
>>> a=20
>>> a=b=20
>>> a,b=10,20
>>> a
10
>>> b
20
>>> a = 20,30
>>> a
(20, 30)
>>> 3**2
9
>>> 3**3
27
>>> 10%7
3
>>> 4>5
False
>>> 6==7
False
>>> b
20
>>> a
(20, 30)
>>> a = 10
>>> a
10
>>> b
20
>>> a += 3
>>> a
13
>>> a -= 2
>>> a
11
>>> 5>6
False
>>> 5>6 and 7>3
False
>>> 7>3
True
>>> False and True
False
>>> 5>6 or 7>3
True
>>> not 5>6 and 7>3
True
>>> 6>5 or 7>10
True
>>> 6>5
True
>>> 7>10
False
>>> 6>5 and 7>10
False
>>> 6>5 and 7>10 or 4>3
True
>>> not 6>5 and 7>10 or 4>3
True
>>> not (6>5 and 7>10 or 4>3)
False
>>> 6&7
6
>>> 2&3
2
>>> 11&7
3
>>> 7&11
3
>>> 7|11
15
>>> 7^11
12
>>> bin(7)
'0b111'
>>> bin(11)
'0b1011'
>>> a = 10
>>> b=20
>>> c=10
>>> id(a)
1652869524048
>>> id(c)
1652869524048
>>> a is c
True
>>> a is b
False
>>> "This is a string"
'This is a string'
>>> k = "This is a string"
>>> 'is' in k
True
>>> 'wow' in k
False
>>> 'z' not in k
True
>>> m = 30.5
>>> m
30.5
>>> type(m)
<class 'float'>
>>> a
10
>>> type(a)
<class 'int'>
>>> type(k)
<class 'str'>
>>> c = 3+3i
SyntaxError: invalid syntax
>>> c = 3+3j
>>> j = 4
>>> c = 45+3j
>>> j
4
>>> c
(45+3j)
>>> #### This is a comment line
>>> # STRING
>>> #################################
>>> s = 'this is a python string'
>>> s1 = "this is a python string"
>>> s2 = '''this is a python string'''
>>> s3 = """this is a python string"""
>>> type(s)
<class 'str'>
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'str'>
>>> type(s3)
<class 'str'>
>>> print(s)
this is a python string
>>> print(s1)
this is a python string
>>> print(s2)
this is a python string
>>> print(s3)
this is a python string
>>> s
'this is a python string'
>>> s4 = 'This is first line
SyntaxError: EOL while scanning string literal
>>> s4 = '''This is first line
now i can enter the second line
as well as the third line'''
>>> print(s4)
This is first line
now i can enter the second line
as well as the third line
>>> s4
'This is first line\nnow i can enter the second line\nas well as the third line'
>>> s5 = 'I\'ve been doing it'
>>> print(s5)
I've been doing it
>>> s = 'Hello World'
>>> # Access the elements inside
>>> len(s)
11
>>> s = 'Hello World!'
>>> s[0]
'H'
>>> s[-1]
'!'
>>> s[6]
'W'
>>> s[-5]
'o'
>>> s[-4]
'r'
>>> s[-7]
' '
>>> s[6]
'W'
>>> s[7]
'o'
>>> s[5]
' '
>>> s[0:5:1]
'Hello'
>>> s[6:11:1]
'World'
>>> s[6:-1:1]
'World'
>>> s[6:-1:2]
'Wrd'
>>> # Default Values in Slicing
>>> #1. Step size is by deafult +1
>>> s[6:-1]
'World'
>>> s[6:-1:]
'World'
>>> #2. Starting point is 0 by default
>>> s[:5]
'Hello'
>>> #3. Stopping point is end position by default
>>> s[6:12]
'World!'
>>> s[6:]
'World!'
>>> #2a. Starting point becomes end if the step is negative
>>> s[10:5:-1]
'dlroW'
>>> s[4::-1]
'olleH'
>>> s[:4:-1]
'!dlroW '
>>> s[::-1]
'!dlroW olleH'
>>> #3a. Stopping point becomes zero if the step is negative
>>> s[-6:]
'World!'
>>> s[-6::-1]
'W olleH'
>>> s[-6:-1:-1]
''
>>> s
'Hello World!'
>>> s * 2
'Hello World!Hello World!'
>>> s * 4
'Hello World!Hello World!Hello World!Hello World!'
>>> 'say' + 'something'
'saysomething'
>>> '*'*4
'****'
>>> '*'*3
'***'
>>> '*'*2
'**'
>>> s
'Hello World!'
>>> 'Hello in Python World!'
'Hello in Python World!'
>>> s = s[:6] + 'in Python ' + s[6:]
>>> s
'Hello in Python World!'
>>> s += ' Guys!!!!'
>>> s
'Hello in Python World! Guys!!!!'
>>> ###############################################
>>> # List - Collection of Heterogenous Elements
>>> ###############################################
>>> a = [4,6,3,8,9.4,'Hello',[5,7],'data']
>>> type(a)
<class 'list'>
>>> len(a)
8
>>> a[0]
4
>>> a[-1]
'data'
>>> a[:4]
[4, 6, 3, 8]
>>> a[-4:]
[9.4, 'Hello', [5, 7], 'data']
>>> a[-3::-1]
['Hello', 9.4, 8, 3, 6, 4]
>>> a[:-4:-1]
['data', [5, 7], 'Hello']
>>> a[-1]
'data'
>>> a[-1][-1]
'a'
>>> a[-2][0]
5
>>> b = [['good','bad',[4,'nice']]]
>>> len(b)
1
>>> b[-1][-1][-1]
'nice'
>>> b[-1]
['good', 'bad', [4, 'nice']]
>>> b[-1][-1]
[4, 'nice']
>>> b[-1][-1][-1][0]
'n'
>>> b
[['good', 'bad', [4, 'nice']]]
>>> a
[4, 6, 3, 8, 9.4, 'Hello', [5, 7], 'data']
>>> a[0]
4
>>> a[0] = 44
>>> a
[44, 6, 3, 8, 9.4, 'Hello', [5, 7], 'data']
>>> s
'Hello in Python World! Guys!!!!'
>>> s[0] = 'k'
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    s[0] = 'k'
TypeError: 'str' object does not support item assignment
>>> del a[3]
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data']
>>> del s[3]
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    del s[3]
TypeError: 'str' object doesn't support item deletion
>>> s += 'hello'
>>> s
'Hello in Python World! Guys!!!!hello'
>>> 
>>> 
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data']
>>> a += [10,20]
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data', 10, 20]
>>> a += [[8,9]]
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data', 10, 20, [8, 9]]
>>> a += 'hello'
>>> a += ['bye']
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data', 10, 20, [8, 9], 'h', 'e', 'l', 'l', 'o', 'bye']
>>> a += (4,78,98)
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7], 'data', 10, 20, [8, 9], 'h', 'e', 'l', 'l', 'o', 'bye', 4, 78, 98]
>>> a[5]
[5, 7]
>>> a[5] += ['inserted']
>>> a
[44, 6, 3, 9.4, 'Hello', [5, 7, 'inserted'], 'data', 10, 20, [8, 9], 'h', 'e', 'l', 'l', 'o', 'bye', 4, 78, 98]
>>> ord('A')
65
>>> chr(65)
'A'
>>> 