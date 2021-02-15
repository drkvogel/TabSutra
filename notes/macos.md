```
21/02/8 16:25:15 kvogel@kvogel-macbook:~/Projects/dotfiles-private ±(master) 
❯ python -V
Python 3.7.3
❯ bpython
bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
```
```py
>>> import os
>>> os
<module 'os' from '/usr/local/anaconda3/lib/python3.7/os.py'>
>>> list(os)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    list(os)
TypeError: 'module' object is not iterable
>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_
NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 
'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O
_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_
TRUNC', 'O_WRONLY', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_GL
OBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR', 'SEEK_
END', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGN
ALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__'
, '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_expo
rts_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot'
, 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'e
nviron', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fcho
wn', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'get_blocking', 'get_
exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'ge
tgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill',
 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkd
ir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'pread', '
putenv', 'pwrite', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', '
sched_get_priority_max', 'sched_get_priority_min', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'se
tgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 
'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supp
orts_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system'
, 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unseten
v', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write', 'writev']
```


```py
>>> os.__doc__
```
```
"OS routines for NT or Posix depending on what system we're on.\n\nThis exports:\n  - all functions from posix or nt, e.g. unlink, stat, etc.\n  
- os.path is either posixpath or ntpath\n  - os.name is either 'posix' or 'nt'\n  - os.curdir is a string representing the current directory (alw
ays '.')\n  - os.pardir is a string representing the parent directory (always '..')\n  - os.sep is the (or a most common) pathname separator ('/'
 or '\\\\')\n  - os.extsep is the extension separator (always '.')\n  - os.altsep is the alternate pathname separator (None or '/')\n  - os.paths
ep is the component separator used in $PATH etc\n  - os.linesep is the line separator in text files ('\\r' or '\\n' or '\\r\\n')\n  - os.defpath 
is the default search path for executables\n  - os.devnull is the file path of the null device ('/dev/null', etc.)\n\nPrograms that import and us
e 'os' stand a better chance of being\nportable between different platforms.  Of course, they must then\nonly use functions that are defined by a
ll platforms (e.g., unlink\nand opendir), and leave all pathname manipulation to os.path\n(e.g., split and join).\n"
```
```py
>>> os.name
'posix'
>>> os.uname()
posix.uname_result(sysname='Darwin', nodename='kvogel-macbook.local', release='18.7.0', version='Darwin Kernel Version 18.7.0: Mon Feb 10 21:08:4
5 PST 2020; root:xnu-4903.278.28~1/RELEASE_X86_64', machine='x86_64')
```

```py
# bpython version 0.18 on top of Python 3.7.3 /usr/local/anaconda3/bin/python
>>> import platform
>>> platform.system()
'Darwin'
>>> import sys
>>> sys.platform
'darwin'
```

2021-02-13 11:39:09
```
21/02/13 11:38:47 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ./run.sh 
Traceback (most recent call last):
  File "src/dev.py", line 3, in <module>
    from selenium import webdriver
ModuleNotFoundError: No module named 'selenium'
❯ . ./venv/bin/activate
(venv) 21/02/13 11:39:53 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ./run.sh             
self.browser = webdriver.Chrome()...
```
OK... but:
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 86
Current browser version is 88.0.4324.150 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
```
[python - Find which version of package is installed with pip](https://stackoverflow.com/questions/10214827/find-which-version-of-package-is-installed-with-pip)
>As of pip 1.3, there is a `pip show` command.
```
$ pip show Jinja2
Name: Jinja2
Version: 2.7.3
Location: /path/to/virtualenv/lib/python2.7/site-packages
Requires: markupsafe
```
>In older versions, `pip freeze` and `grep` should do the job nicely.
```
$ pip freeze | grep Jinja2
Jinja2==2.7.3
```

```
(venv) 21/02/13 11:40:00 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ pip show selenium
Name: selenium
Version: 3.141.0
Summary: Python bindings for Selenium
Home-page: https://github.com/SeleniumHQ/selenium/
Author: UNKNOWN
Author-email: UNKNOWN
License: Apache 2.0
Location: /Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages
Requires: urllib3
Required-by: 

❯ pip -V           
pip 19.0.3 from /Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/pip (python 3.7)

❯ pip install selenium
Requirement already satisfied: selenium in ./venv/lib/python3.7/site-packages (3.141.0)
Requirement already satisfied: urllib3 in ./venv/lib/python3.7/site-packages (from selenium) (1.25.9)
You are using pip version 19.0.3, however version 21.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

❯ pip install --upgrade selenium
Requirement already up-to-date: selenium in ./venv/lib/python3.7/site-packages (3.141.0)
Requirement already satisfied, skipping upgrade: urllib3 in ./venv/lib/python3.7/site-packages (from selenium) (1.25.9)
```

selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 

```
❯ which chromedriver
/usr/local/bin/chromedriver
```
[Settings – About Chrome](chrome://settings/help)
>Google Chrome is up to date Version 88.0.4324.150 (Official Build) (x86_64)

[Downloads - ChromeDriver - WebDriver for Chrome ](https://chromedriver.chromium.org/downloads)
>Current Releases
>If you are using Chrome version 89, please download ChromeDriver 89.0.4389.23
>If you are using Chrome version 88, please download ChromeDriver 88.0.4324.96
>If you are using Chrome version 87, please download ChromeDriver 87.0.4280.88

Chrome version will keep changing, so will have to make sure `chromedriver` version matches, and download/prompt to download if not, or...
use a fixed version of chromium (headless?)


### check existence of url

```
21/02/13 12:04:53 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ wget --spider https://chromedriver.storage.googleapis.com/index.html\?path\=88.0.4324.96/
dyld: Library not loaded: /usr/local/opt/openssl/lib/libssl.1.0.0.dylib
  Referenced from: /usr/local/bin/wget
  Reason: image not found
[1]    24582 abort      wget --spider
```

```
21/02/13 12:04:59 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ brew install wget
==> Downloading https://homebrew.bintray.com/bottles/wget-1.20.3_2.mojave.bottle.tar.gz
Already downloaded: /Users/kvogel/Library/Caches/Homebrew/downloads/08c4734a2d875d0205367bd2f0330c91aa7a3d92b33f9add04f39250149419ef--wget-1.20.3_2.mojave.bottle.tar.gz
Error: wget 1.19.5 is already installed
To upgrade to 1.20.3_2, run `brew upgrade wget`.
==> `brew cleanup` has not been run in 30 days, running now...
Removing: /Users/kvogel/Library/Caches/Homebrew/adns--1.6.0.mojave.bottle.tar.gz... (272.6KB)
...
```

```
21/02/13 12:07:58 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ brew upgrade wget
==> Upgrading 1 outdated package:
wget 1.19.5 -> 1.20.3_2
==> Upgrading wget 1.19.5 -> 1.20.3_2
...
❯ wget
wget: missing URL
```
OK...
```
21/02/13 12:10:54 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ wget --spider https://chromedriver.storage.googleapis.com/index.html\?path\=88.0.4324.96/
Spider mode enabled. Check if remote file exists.
--2021-02-13 12:11:16--  https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/
Resolving chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)... 2a00:1450:4009:819::2010, 172.217.169.80
Connecting to chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)|2a00:1450:4009:819::2010|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10574 (10K) [text/html]
Remote file exists and could contain further links,
but recursion is disabled -- not retrieving.
```

### curl

```
21/02/13 12:14:06 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ curl -o /dev/null --silent --head --write-out '%{http_code}\n' asdfas
000
❯ curl -o /dev/null --silent --head --write-out '%{http_code}\n' https://google.com
301
❯ curl -o /dev/null --silent --head --write-out '%{http_code}\n' https://www.google.com
200
❯ curl -o /dev/null --silent --head --write-out '%{http_code}\n' https://chromedriver.storage.googleapis.com/index.html\?path\=88.0.4324.96/
200
❯ curl -o /dev/null --silent --head --write-out '%{http_code}\n' https://chromedriver.storage.googleapis.com/index.html\?path\=88.0.4324.96xxx/
200
```
?? 

[https://chromedriver.storage.googleapis.com/index.html/?path%5C=88.0.4324.96xxx/ ](https://chromedriver.storage.googleapis.com/index.html/?path%5C=88.0.4324.96xxx/)
```xml
<Error>
<Code>NoSuchKey</Code>
<Message>The specified key does not exist.</Message>
<Details>No such object: chromedriver/index.html/</Details>
</Error>
```
It is a directory listing. The real path is `https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_mac64.zip`
```
(venv) 21/02/13 12:19:52 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_mac64.zip
--2021-02-13 13:10:28--  https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_mac64.zip
Resolving chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)... 2a00:1450:4009:819::2010, 142.250.178.16
Connecting to chromedriver.storage.googleapis.com (chromedriver.storage.googleapis.com)|2a00:1450:4009:819::2010|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8137203 (7.8M) [application/zip]
Saving to: ‘chromedriver_mac64.zip’
chromedriver_mac64.zip               100%[===================================================================>]   7.76M  8.48MB/s    in 0.2021-02-13 13:10:29 (8.48 MB/s) - ‘chromedriver_mac64.zip’ saved [8137203/8137203]

❯ unzip chromedriver_mac64.zip 
  inflating: chromedriver    

(venv) 21/02/13 13:11:43 kvogel@kvogel-macbook:/usr/local/bin 
❯ chromedriver -v
ChromeDriver 86.0.4240.22 (398b0743353ff36fb1b82468f63a3a93b4e2e89e-refs/branch-heads/4240@{#378})
❯ sudo mv chromedriver chromedriver-86
❯ sudo mv ~/p/TabSutra/chromedriver .
```

[selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version](https://www.google.com/search?q=selenium.common.exceptions.SessionNotCreatedException%3A+Message%3A+session+not+created%3A+This+version+of+ChromeDriver+only+supports+Chrome+version&ie=UTF-8)

[how to keep chromedriver in sync with chrome version](https://www.google.com/search?q=how+to+keep+chromedriver+in+sync+with+chrome+version&ie=UTF-8)
[Keep Chrome WebDriver version in sync with Chrome? : selenium ](https://www.reddit.com/r/selenium/comments/bolseh/keep_chrome_webdriver_version_in_sync_with_chrome/)
[How to work with a specific version of ChromeDriver while Chrome Browser gets updated automatically through Python selenium](https://stackoverflow.com/questions/50692358/how-to-work-with-a-specific-version-of-chromedriver-while-chrome-browser-gets-up)
[webdriver - ChromeDriver and Chrome Browser out of sync](https://stackoverflow.com/questions/59337189/chromedriver-and-chrome-browser-out-of-sync)


s7 always allow
how to check if not allowed? prompt to allow

two cables weren't working for data transfer, put knot in them

ok, `./run.sh`, connects, sleep(5), then prints to stdout...
should save to file?
and is not in TabsOutliner format, or better, markdown link format
ends with:
```py
Traceback (most recent call last):
  File "src/dev.py", line 106, in <module>
    main()
  File "src/dev.py", line 103, in main
    tabsutra.go()
  File "src/dev.py", line 94, in go
    self.parse_page_with_sleep()
  File "src/dev.py", line 35, in parse_page_with_sleep
    print(elem.text)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py", line 76, in text
    return self._execute(Command.GET_ELEMENT_TEXT)['value']
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=88.0.4324.150)
```

```
(venv) 21/02/13 13:22:15 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ./run.sh > s7-tabs-210213T1322.txt
...
(venv) 21/02/13 13:24:59 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ll s7-tabs-210213T1322.txt 
-rw-r--r--  1 kvogel  staff   602K 13 Feb 13:24 s7-tabs-210213T1322.txt
```

uploaded to gdrive via web
[s7-tabs-210213T1322.txt](https://drive.google.com/file/d/13RG6zgZR0R5_tlcaAC1OgyOVlLy9jpMk/view?usp=sharing)

new chrome instance doesn't quit afterwards

### google drive cli

[upload to google drive via command line](https://www.google.com/search?q=upload+to+google+drive+via+command+line&ie=UTF-8)
[How to upload a file to Google Drive from the command line -OliverMarshall.net ](https://olivermarshall.net/how-to-upload-a-file-to-google-drive-from-the-command-line/)
[Uploading files to Google Drive directly from the Terminal (using Curl)  by Daniel Ellis  Towards Data Science ](https://towardsdatascience.com/uploading-files-to-google-drive-directly-from-the-terminal-using-curl-2b89db28bb06)
[How to Upload a File to Google Drive from the Terminal/Command Line ~ ServerKaKa ](https://www.serverkaka.com/2018/05/upload-file-to-google-drive-from-the-command-line-terminal.html)
[windows - Is there a command line utility to script uploads to Google Drive and share items? - Super User ](https://superuser.com/questions/730774/is-there-a-command-line-utility-to-script-uploads-to-google-drive-and-share-item)
[drive-cli · PyPI ](https://pypi.org/project/drive-cli/)
[Upload to Google Drive without any UI?](https://stackoverflow.com/questions/12446535/upload-to-google-drive-without-any-ui)
[Google Drive API    Google Developers ](https://developers.google.com/drive/)
[How to upload a file to Google Drive from the command line -OliverMarshall.net ](http://olivermarshall.net/how-to-upload-a-file-to-google-drive-from-the-command-line/)

[prasmussen/gdrive: Google Drive CLI Client ](https://github.com/prasmussen/gdrive)
```
21/02/13 12:21:40 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ which gdrive
gdrive not found
21/02/13 13:31:18 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ brew install gdrive
==> Downloading https://homebrew.bintray.com/bottles/gdrive-2.1.0.mojave.bottle.3.tar.gz
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/e26ef4bec660913f42aa735c28f58393912d2d0293bf98a351fa2b27a1baee01?response-content-disposition=attachment%3Bfilename%3D%22gdrive-2.1.0.mojave.bott
######################################################################## 100.0%
==> Pouring gdrive-2.1.0.mojave.bottle.3.tar.gz
🍺  /usr/local/Cellar/gdrive/2.1.0: 4 files, 8.5MB
==> `brew cleanup` has not been run in 30 days, running now...
Error: Permission denied @ apply2files - /usr/local/lib/prey/versions/1.9.9/.DS_Store

21/02/13 13:32:37 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ gdrive list
Authentication needed
Go to the following url in your browser:
https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=36...oe99eg.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&state=state

Enter verification code:
```
[Sign in – Google accounts ](https://accounts.google.com/signin/oauth/danger?authuser=0&part=AJi8...qMo&as=S-603...75&rapt=AEj...#)
>This app is blocked
>This app tried to access sensitive info in your Google Account. To keep your account safe, Google blocked this access.


```
21/02/13 13:35:31 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ pip install drive-cli
```
```
21/02/13 13:35:52 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) ✗
❯ drive ls
/usr/local/anaconda3/lib/python3.7/site-packages/oauth2client/_helpers.py:255: UserWarning: Cannot access /usr/local/anaconda3/lib/python3.7/site-packages/drive_cli/token.json: No such file or directory
  warnings.warn(_MISSING_FILE_MESSAGE.format(filename))

Your browser has been opened to visit:

    https://accounts.google.com/o/oauth2/auth?client_id=94718881080-76dmod3u5a3ot1vufq29u04kdr5igmuc.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&access_type=offline&response_type=code

If your browser is on a different machine then exit and re-run this
application with the command-line parameter

  --noauth_local_webserver

^C
Aborted!
```

>This app is blocked
>This app tried to access sensitive info in your Google Account. To keep your account safe, Google blocked this access.

[gdrive This app is blocked This app tried to access sensitive info in your Google Account. To keep your account safe, Google blocked this access.](https://www.google.com/search?q=gdrive+This+app+is+blocked+This+app+tried+to+access+sensitive+info+in+your+Google+Account.+To+keep+your+account+safe%2C+Google+blocked+this+access)
[Allow less secure apps to access your Gmail account  DevAnswers.co ](https://devanswers.co/allow-less-secure-apps-access-gmail-account/)
[Less secure apps & your Google Account - Google Account Help ](https://support.google.com/accounts/answer/6010255?hl=en)
[Sign in with App Passwords - Google Account Help ](https://support.google.com/accounts/answer/185833)


[node.js - How to use Selenium chromedriver without being forced to update?](https://stackoverflow.com/questions/40288651/how-to-use-selenium-chromedriver-without-being-forced-to-update)
>The Selenium Documentation has information on how to customize the chromedriver options. I have downloaded a version of Chromium and used this logic to hook it up [for node/javascript]:
```js
var chrome = require("selenium-webdriver/chrome");
var service = new chrome.ServiceBuilder().build();

var options = new chrome.Options();
options.setChromeBinaryPath("PATH/TO/MY/CHROMIUM");

var driver = new chrome.Driver(options, service);
```
redo in node/js?
  make chrome extn? or vscode extn?
  use specific version of chromium rather than current version of chrome which keeps changing?


[Bash get exit code of command on a Linux / Unix - nixCraft ](https://www.cyberciti.biz/faq/bash-get-exit-code-of-command/)
`status=$?`

[get exit code of wget spider](https://www.google.com/search?q=get+exit+code+of+wget+spider&ie=UTF-8)
[get http status of wget spider](https://www.google.com/search?q=get+http+status+of+wget+spider&ie=UTF-8)
[bash - Script to get the HTTP status code of a list of urls?](https://stackoverflow.com/questions/6136022/script-to-get-the-http-status-code-of-a-list-of-urls)

```
(venv) 21/02/13 15:24:07 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) 
❯ git config --global pull.ff true 
```

```
(venv) 21/02/13 16:33:15 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) 
❯ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless google.com
[0213/163325.153874:ERROR:xattr.cc(63)] setxattr org.chromium.crashpad.database.initialized on file /var/folders/jt/0c4t1hnn613c8_7q19pgmrhw0000gn/T/: Operation not permitted (1)
[0213/163325.157029:ERROR:file_io.cc(90)] ReadExactly: expected 8, observed 0
[0213/163325.159692:ERROR:xattr.cc(63)] setxattr org.chromium.crashpad.database.initialized on file /var/folders/jt/0c4t1hnn613c8_7q19pgmrhw0000gn/T/: Operation not permitted (1)
[0213/163325.572173:WARNING:ipc_message_attachment_set.cc(49)] MessageAttachmentSet destroyed with unconsumed attachments: 0/1
[0213/163325.572298:WARNING:ipc_message_attachment_set.cc(49)] MessageAttachmentSet destroyed with unconsumed attachments: 0/1
```

Chrome "--headless" ERROR:xattr  setxattr org.chromium.crashpad.database.initialized on file Operation not permitted 
[Chrome "--headless" ERROR:xattr setxattr org.chromium.crashpad.database.initialized on file Operation not permitted](https://www.google.com/search?q=Chrome+%22--headless%22+ERROR%3Axattr+setxattr+org.chromium.crashpad.database.initialized+on+file+Operation+not+permitted&ie=UTF-8)
[Chrome --headless crashes : MacOS ](https://www.reddit.com/r/MacOS/comments/8zxoxs/chrome_headless_crashes/)
[permissions - Chrome crashpad crashes on xattr - Super User ](https://superuser.com/questions/1292863/chrome-crashpad-crashes-on-xattr)

add ` --crash-dumps-dir=/tmp`
```
(venv) 21/02/13 16:33:25 kvogel@kvogel-macbook:~/Projects/TabSutra ±(master) 
❯ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --crash-dumps-dir=/tmp google.com 
[0213/163519.681147:ERROR:command_buffer_proxy_impl.cc(122)] ContextResult::kTransientFailure: Failed to send GpuChannelMsg_CreateCommandBuffer.
```

ERROR:command_buffer_proxy_impl.cc ContextResult::kTransientFailure: Failed to send GpuChannelMsg_CreateCommandBuffer

[running Chrome in headless mode](https://stackoverflow.com/questions/49103799/running-chrome-in-headless-mode)

[ERROR:command_buffer_proxy_impl.cc ContextResult::kTransientFailure: Failed to send GpuChannelMsg_CreateCommandBuffer](https://www.google.com/search?q=ERROR%3Acommand_buffer_proxy_impl.cc+ContextResult%3A%3AkTransientFailure%3A+Failed+to+send+GpuChannelMsg_CreateCommandBuffer&ie=UTF-8)
[Headless Chrome Terminates](https://stackoverflow.com/questions/55992970/headless-chrome-terminates)
[List of Chromium Command Line Switches « Peter Beverloo ](https://peter.sh/experiments/chromium-command-line-switches/)


[nodejs selenium vs](https://www.google.com/search?q=nodejs+selenium+vs)
[node.js - What is the difference between mocha and Selenium?](https://stackoverflow.com/questions/22894253/what-is-the-difference-between-mocha-and-selenium)
[javascript - Alternatives to Selenium Webdriver](https://stackoverflow.com/questions/29671060/alternatives-to-selenium-webdriver)

[PhantomJS Is Dead, Use Chrome Headless in Continuous Integration - Semaphore ](https://semaphoreci.com/blog/2018/03/27/phantomjs-is-dead-use-chrome-headless-in-continuous-integration.html)
[Replacing PhantomJS with headless Chrome  BigBinary Blog ](https://bigbinary.com/blog/replacing-phantomjs-with-headless-chrome)
[Replacing PhantomJS with Chrome — headless  by Polo Ornelas  Medium ](https://medium.com/@polographer/replacing-phantomjs-with-chrome-headless-88ae3d0657bf)
[Getting Started with Headless Chrome    Web    Google Developers ](https://developers.google.com/web/updates/2017/04/headless-chrome)
[Web-scraping JavaScript page with Python](https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python)
[Seleniumworks: Headless Browser Testing using PhantomJS - GhostDriver  WebDriver ](http://seleniumworks.blogspot.com/2013/03/headless-browser-testing-using.html)
    [Inspect with Chrome Developer Tools](chrome://inspect/#pages)
[chrome command location mac](https://www.google.com/search?q=chrome+command+location+mac&ie=UTF-8)
[chrome headless](https://www.google.com/search?q=chrome+headless&ie=UTF-8)
[How to run a headless Chrome browser in Selenium WebDriver.  by Anton Smirnov  ITNEXT ](https://itnext.io/how-to-run-a-headless-chrome-browser-in-selenium-webdriver-c5521bc12bf0)
[python - Running Selenium with Headless Chrome Webdriver](https://stackoverflow.com/questions/53657215/running-selenium-with-headless-chrome-webdriver)
[chrome headless nodejs](https://www.google.com/search?q=chrome+headless+nodejs&ie=UTF-8)
[Getting started with Puppeteer & Headless chrome in NodeJs  by Aditya Joshi  Medium ](https://adityaajoshi.medium.com/getting-started-with-puppeteer-headless-chrome-in-nodejs-4826595e3366)
[Headless Browser Examples with Puppeteer  Toptal ](https://www.toptal.com/puppeteer/headless-browser-puppeteer-tutorial)
[Don't Fear the Repo: Enhanced Git Flow Explained  Toptal ](https://www.toptal.com/gitflow/enhanced-git-flow-explained)
[node.js - Headless automation with Nodejs Selenium Webdriver](https://stackoverflow.com/questions/44197253/headless-automation-with-nodejs-selenium-webdriver)
[Install Chrome Headless using NPM](https://stackoverflow.com/questions/44516816/install-chrome-headless-using-npm)

