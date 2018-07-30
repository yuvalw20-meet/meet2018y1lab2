Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> my_name='student'
>>> print("hi,"+myname')
	  
SyntaxError: EOL while scanning string literal
>>> Print (“hi, ”+ my_name)
	  
SyntaxError: invalid character in identifier
>>> Print (“Hi, ”+ my_name)
	  
SyntaxError: invalid character in identifier
>>> Print (“Hi, ”+ my_name)
	  
SyntaxError: invalid character in identifier
>>> print (“Hi, ”+ my_name)
	  
SyntaxError: invalid character in identifier
>>> print ("hi, "+my_name)
	  
hi, student
>>> print('I am ‘ + my_age + ‘years old’)
	  
SyntaxError: EOL while scanning string literal
>>> print('I am ' + my_age + 'years old')
	  
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print('I am ' + my_age + 'years old')
NameError: name 'my_age' is not defined
>>> 
