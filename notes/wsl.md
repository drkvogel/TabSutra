
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
2021-02-08 21:25:36
maybe it won't work in WSL!
  because of networking stuff not working properly?
  because we're trying to use Chrome in native Windows from WSL?

[selenium wsl](https://www.google.com/search?q=selenium+wsl&ie=UTF-8)
[How to Run Selenium on WSL 2 ](https://magenic.com/thinking/how-to-run-selenium-on-wsl-2)
[ubuntu - Running Selenium on WSL using Chrome - Super User ](https://superuser.com/questions/1475553/running-selenium-on-wsl-using-chrome)
[selenium - Chromedriver fails inside WSL after updating Windows to 1903 - Super User ](https://superuser.com/questions/1446085/chromedriver-fails-inside-wsl-after-updating-windows-to-1903)

[ChromeDriver in WSL2  Greg Brisebois ](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)
