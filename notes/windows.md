


```
Microsoft Windows [Version 10.0.19042.789]
(c) 2020 Microsoft Corporation. All rights reserved.

08/02/2021 19:09:39.95 KVOGEL-ELITEBOO:C:\WINDOWS\system32
> python
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
```py
>>> import os
>>> os.uname()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'uname'
```
[Error: No module named os.uname under python 2.7](https://stackoverflow.com/questions/36250558/error-no-module-named-os-uname-under-python-2-7)
>A portable way to get some informations about the system is `sys.platform`, and the [platform package](https://docs.python.org/3/library/platform.html).

```
>>> import sys
>>> sys.platform
'win32'
```

```py
>>> import platform
>>> platform.platform()
'Windows-10-10.0.19041-SP0'
>>> platform.system()
'Windows'
```
