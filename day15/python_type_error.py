#written in terminal............
'''C:\Users\panka>python
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<python-input-0>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello world')
hello world
>>> #fdsddsdsd
>>> print(age)
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    print(age)
          ^^^
NameError: name 'age' is not defined
>>> age = 19
>>> print(age)
19
>>> num = [1,2,3,4,5]
>>> num[5]
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    num[5]
    ~~~^^^
IndexError: list index out of range
>>> import maths
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    import maths
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> pow(2,4)
16
>>> sq(2,2)
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    sq(2,2)
    ^^
NameError: name 'sq' is not defined
>>> math.PI
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    math.PI
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>> math.sq(2,2)
Traceback (most recent call last):
  File "<python-input-14>", line 1, in <module>
    math.sq(2,2)
    ^^^^^^^
AttributeError: module 'math' has no attribute 'sq'
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    users['county']
    ~~~~~^^^^^^^^^^
KeyError: 'county'
>>> user['country']
Traceback (most recent call last):
  File "<python-input-18>", line 1, in <module>
    user['country']
    ^^^^
NameError: name 'user' is not defined. Did you mean: 'users'?
>>> users['country']
'Finland'
>>> 4 + '3'
Traceback (most recent call last):
  File "<python-input-20>", line 1, in <module>
    4 + '3'
    ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> from math import power
Traceback (most recent call last):
  File "<python-input-22>", line 1, in <module>
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,5)
32.0
>>> int('12a')
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    int('12a')
    ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '12a'
>>> 1/0
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    1/0
    ~^~
ZeroDivisionError: division by zero
>>>'''