Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> stack=[10,89,67,45,89,34]
>>> def push(value):
	stack.append(value)


>>> print("current contents of stack",stack)
current contents of stack [10, 89, 67, 45, 89, 34]
>>> push(23)
>>> push(56)
>>> stack
[10, 89, 67, 45, 89, 34, 23, 56]
>>> stack.pop()
56
>>> stack.pop()
23
>>> stack.pop()
34
>>> stack
[10, 89, 67, 45, 89]
>>> 
