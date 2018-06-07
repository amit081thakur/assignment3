Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import deque
>>> queue = deque()
>>> queue.append(34)
>>> queue.append(45)
>>> queue.append(78)
>>> queue.append(90)
>>> queue.append(2)
>>> queue
deque([34, 45, 78, 90, 2])
>>> queue.popleft()
34
>>> queue.popleft()
45
>>> queue.popleft()
78
>>> queue
deque([90, 2])
>>> 
