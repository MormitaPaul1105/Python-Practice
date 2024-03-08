Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text='''I love Apple
... but I love Mango more than Apple'''
>>> print(text)
I love Apple
but I love Mango more than Apple
>>> text[0:]
'I love Apple\nbut I love Mango more than Apple'
>>> print(text[0:])
I love Apple
but I love Mango more than Apple
>>> print(text[12:])

but I love Mango more than Apple
>>> print(text[15:])
t I love Mango more than Apple
>>> print(text[16:])
 I love Mango more than Apple
>>> print(text[:12])
I love Apple
>>> print(text[0:44])
I love Apple
but I love Mango more than Appl
>>> print(text[0:45])
I love Apple
but I love Mango more than Apple
>>> print(text[0])
I
>>> print[1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
text[1]TypeError: 'builtin_function_or_method' object is not subscriptable
SyntaxError: invalid syntax
text[2]
'l'
v1="and there have only"
v2=3
v3='''Mangoes into the basket
because I ate almost everything'''
str(v2)
'3'
Add=v1+""+v2+""+v3
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Add=v1+""+v2+""+v3
TypeError: can only concatenate str (not "int") to str
Add=v1+""+str(v2)+""+v3
print(add)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(add)
NameError: name 'add' is not defined. Did you mean: 'Add'?
print(Add)
and there have only3Mangoes into the basket
because I ate almost everything
Add=text+""+v1+""+str(v2)+""+v3
print(Add)
I love Apple
but I love Mango more than Appleand there have only3Mangoes into the basket
because I ate almost everything
Add=text+' '+v1+" "+str(v2)+" "+v3
print(Add)
I love Apple
but I love Mango more than Apple and there have only 3 Mangoes into the basket
because I ate almost everything
v4="Let's talk about my other favourite fruits"
v5='They are "Lychee","Jam", "Watermelon" etc.'
Add=text+" "+v1+" "+str(v2)+" "+v3+' '+v4+' '+v5
print(Add)
I love Apple
but I love Mango more than Apple and there have only 3 Mangoes into the basket
because I ate almost everything Let's talk about my other favourite fruits They are "Lychee","Jam", "Watermelon" etc.
