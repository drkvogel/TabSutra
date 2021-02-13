
# WSL

```PY
>>> os.name
'posix'
>>> os.uname()
posix.uname_result(sysname='Linux', nodename='kvogel-elitebook', release='4.19.104-microsoft-standard', version='#1 SMP Wed Feb 19 
06:37:35 UTC 2020', machine='x86_64')

>>> uname = os.uname()
>>> uname.release
'4.19.104-microsoft-standard'
```


```py
>>> import platform
>>> platform.system()
'Linux'
>>> 
```

