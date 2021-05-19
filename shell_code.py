Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLE - Collection of Hete. Elements - Immutable
>>> ######################################################
>>> a = (4,5,7,8,4,8,'45',[5,7,'hello'])
>>> type(a)
<class 'tuple'>
>>> len(a)
8
>>> print(a)
(4, 5, 7, 8, 4, 8, '45', [5, 7, 'hello'])
>>> a1 = 4,5,7,8,4,8,'45',[5,7,'hello']
>>> a1
(4, 5, 7, 8, 4, 8, '45', [5, 7, 'hello'])
>>> type(a1)
<class 'tuple'>
>>> a[0]
4
>>> a[-4]
4
>>> a[0] = 56
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[0] = 56
TypeError: 'tuple' object does not support item assignment
>>> del a[-1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del a[-1]
TypeError: 'tuple' object doesn't support item deletion
>>> a[4:]
(4, 8, '45', [5, 7, 'hello'])
>>> b = 4,5
>>> len(b)
2
>>> c = ('hello')
>>> type(c)
<class 'str'>
>>> d = (45)
>>> type(d)
<class 'int'>
>>> c = ('hello',None)
>>> type(c)
<class 'tuple'>
>>> c
('hello', None)
>>> d = tuple('Hello')
>>> d
('H', 'e', 'l', 'l', 'o')
>>> (4*5)+8
28
>>> d = (45,)
>>> type(d)
<class 'tuple'>
>>> c = 'Hello',
>>> e = ('Hello'),
>>> type(c)
<class 'tuple'>
>>> type(e)
<class 'tuple'>
>>> 
>>> c + e
('Hello', 'Hello')
>>> c * 4
('Hello', 'Hello', 'Hello', 'Hello')
>>> 
>>> c
('Hello',)
>>> c += (45,)
>>> c
('Hello', 45)
>>> c += [45]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c += [45]
TypeError: can only concatenate tuple (not "list") to tuple
>>> f = [']
     
SyntaxError: EOL while scanning string literal
>>> f = ['Hello']
>>> f += (45,)
>>> f
['Hello', 45]
>>> 
>>> #####################################################
>>> # Dictionary - key:value pair, hete. - mutable
>>> #####################################################
>>> d = {'Name':['Orange','Banana','Apple'], 'Color':['Orange', 'Yellow','Red']}
>>> type(d)
<class 'dict'>
>>> len(d)
2
>>> print(d)
{'Name': ['Orange', 'Banana', 'Apple'], 'Color': ['Orange', 'Yellow', 'Red']}
>>> e = {45:60, 6.5:(56,'go'),(4,5):'anything'}
>>> type(e)
<class 'dict'>
>>> len(e)
3
>>> print(e)
{45: 60, 6.5: (56, 'go'), (4, 5): 'anything'}
>>> 
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['Name']
['Orange', 'Banana', 'Apple']
>>> d[''Color]
SyntaxError: invalid syntax
>>> d['Color']
['Orange', 'Yellow', 'Red']
>>> e[45]
60
>>> e[6.5]
(56, 'go')
>>> e[(4,5)]
'anything'
>>> e[6.5][-1]
'go'
>>> 
>>> d
{'Name': ['Orange', 'Banana', 'Apple'], 'Color': ['Orange', 'Yellow', 'Red']}
>>> d['price'] = [60,30,120]
>>> d
{'Name': ['Orange', 'Banana', 'Apple'], 'Color': ['Orange', 'Yellow', 'Red'], 'price': [60, 30, 120]}
>>> d['Name'] = ['Oranges','Bananas','Apples']
>>> d
{'Name': ['Oranges', 'Bananas', 'Apples'], 'Color': ['Orange', 'Yellow', 'Red'], 'price': [60, 30, 120]}
>>> d['Color'] = 'color'
>>> d
{'Name': ['Oranges', 'Bananas', 'Apples'], 'Color': 'color', 'price': [60, 30, 120]}
>>> d['Price'] += [35]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    d['Price'] += [35]
KeyError: 'Price'
>>> d['price'] += [35]
>>> d
{'Name': ['Oranges', 'Bananas', 'Apples'], 'Color': 'color', 'price': [60, 30, 120, 35]}
>>> del d['Color']
>>> d
{'Name': ['Oranges', 'Bananas', 'Apples'], 'price': [60, 30, 120, 35]}
>>> del d['price'][1]
>>> d
{'Name': ['Oranges', 'Bananas', 'Apples'], 'price': [60, 120, 35]}
>>> {'fruit':['Oranges', 'Bananas', 'Apples'], 'price': [60, 120, 35]}
{'fruit': ['Oranges', 'Bananas', 'Apples'], 'price': [60, 120, 35]}
>>> d['fruit'] = d['Name']
>>> del d['Name']
>>> d
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples']}
>>> d['fruit']
['Oranges', 'Bananas', 'Apples']
>>> d['price']
[60, 120, 35]
>>> d
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples']}
>>> d + {'a':45}
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d + {'a':45}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d * 3
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d * 3
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> 
>>> 
>>> 
>>> a
(4, 5, 7, 8, 4, 8, '45', [5, 7, 'hello'])
>>> 4 in a
True
>>> 'fruit' in d
True
>>> d
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples']}
>>> 60 in d
False
>>> d
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples']}
>>> e = {'color':['orange','yellow','red']}
>>> d
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples']}
>>> e
{'color': ['orange', 'yellow', 'red']}
>>> {d,e}
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    {d,e}
TypeError: unhashable type: 'dict'
>>> {**d, **e}
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples'], 'color': ['orange', 'yellow', 'red']}
>>> m = {**d, **e}
>>> m
{'price': [60, 120, 35], 'fruit': ['Oranges', 'Bananas', 'Apples'], 'color': ['orange', 'yellow', 'red']}
>>> 

>>> ###################################
>>> ## Sets - holds unique data, unordered
>>> #######################################
>>> k = {4,5,6,87,'hedllo',4,5,6,87,4}
>>> k
{'hedllo', 4, 5, 6, 87}
>>> type(k)
<class 'set'>
>>> len(k)
5
>>> print(k)
{'hedllo', 4, 5, 6, 87}
>>> k[0]
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    k[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> #####################################
>>> ## Boolean ---- True, False
>>> #####################################
>>> bool(45)
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(-1)
True
>>> bool('')
False
>>> bool(' ')
True
>>> bool([])
False
>>> bool([()])
True
>>> bool(([]))
False
>>> bool(([],))
True
>>> 
>>> 
>>> #####################################
>>> int(4.5)
4
>>> float(3)
3.0
>>> int('45')
45
>>> float('45.5')
45.5
>>> str(45)
'45'
>>> int('45.5')
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    int('45.5')
ValueError: invalid literal for int() with base 10: '45.5'
>>> float('45')
45.0
>>> eval('45.5')
45.5
>>> eval('455')
455
>>> int(eval('45.5'))
45
>>> a
(4, 5, 7, 8, 4, 8, '45', [5, 7, 'hello'])
>>> list(a)
[4, 5, 7, 8, 4, 8, '45', [5, 7, 'hello']]
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    set(a)
TypeError: unhashable type: 'list'
>>> b
(4, 5)
>>> set(b)
{4, 5}
>>> #######################################################
>>> #### Data-class Functions
>>> #######################################################
>>> len(a)
8
>>> s = 'i have a string'
>>> s.capitalize()
'I have a string'
>>> s1 = s.capitalize()
>>> s1
'I have a string'
>>> s.index('have')
2
>>> a = [5,6,87,9]
>>> a.append(45)
>>> a
[5, 6, 87, 9, 45]
>>> a.sort()
>>> a
[5, 6, 9, 45, 87]
>>> help(s.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> s.count('a')
2
>>> ###################### Common Functions- used  mostly
>>> # String
>>> ### count
>>> ### index
>>> ### split
>>> ### upper
>>> ### lower
>>> ### join
>>> ### format
>>> ### isnumeric
>>> ### isalpha
>>> 
>>> # List
>>> ### append
>>> ### sort
>>> ### pop
>>> ### remove
>>> ### insert
>>> ### index
>>> ### count
>>> 
>>> # Tuple
>>> ### index
>>> ### count
>>> 
>>> ### Dictionary
>>> # Dictionary
>>> ### keys
>>> ### values
>>> ### get
>>> 
>>> # Set
>>> ### add
>>> ### uinion
>>> ### union
>>> ### intersection
>>> 
================ RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ===============
4
>>> s
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
================ RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ===============
4
>>> 
================ RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ===============
Enter your name: Peeyush Sanam
Your name is Peeyush Sanam
>>> print(4,5,6,7,8,'hello')
4 5 6 7 8 hello
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter your name: Sanam Peeyush
Your name is Sanam Peeyush
Welcome
>>> print(4,5,6,7,8,'hello',sep='%%%')
4%%%5%%%6%%%7%%%8%%%hello
>>> k = 0
>>> print(4,5,6,7,8,'hello', sep=k)
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    print(4,5,6,7,8,'hello', sep=k)
TypeError: sep must be None or a string, not int
>>> k = '0'
>>> print(4,5,6,7,8,'hello', sep=k)
4050607080hello
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter your name: Peeyush
Your name is-Peeyush

Welcome
>>> a
'Peeyush'
>>> type(a)
<class 'str'>
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the value: 45
45
>>> type(a)
<class 'str'>
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the value: 4
Enter the other value: 3
The Calculated value is:  64
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the value: 4
Enter the other value: 4
The Calculated value is:  256
<class 'int'>
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 44
Its an Even Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 37
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 37
Its an Odd Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 46
Its an Even Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 33
Its an Odd Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 34
Its an Even Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 35
Its an Odd Number
>>> 
======= RESTART: E:/TN/SITP21/15thMay_B1_AI/Day 2/python_scripting_file.py ======
Enter the number: 34
Its an Even Number
>>> 