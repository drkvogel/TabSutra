

tabsutra/tabgrabber:
`chrome://inspect/#devices`
check "Discover USB devices"
phone has to be connected via USB
have to allow data access
and have to run `adb devices` (or `adb start-server`?)
then, in chrome, click `cmd+s` to save, navigate to `~/gdrive/backup/android-tabs-backup/s7/`, `enter`
and then it's a webpage with titles and URLs, but not linked
it would have to:
prompt you to
  connect phone via USB
  allow data access
  check "Discover USB devices"
run adb devices or prompt you to
  trap errors
grab the page
parse the html
turn it into links
save somewhere


followed this: [How can I export the list of open Chrome tabs? ](https://android.stackexchange.com/questions/56635/how-can-i-export-the-list-of-open-chrome-tabs?utm_campaign=google_rich_qa)

[general/dev/mobile/android/adb.md](file:///Users/kvogel/Projects/general/dev/mobile/android/adb.md)
```
❯ adb devices
List of devices attached
* daemon not running; starting now at tcp:5037
* daemon started successfully
```

Dev Tools, Remote Devices (panel at bottom)
>This panel has been deprecated in favor of the `chrome://inspect/#devices interface`, which has equivalent functionality
[chrome://inspect/#devices](chrome://inspect/#devices)

saved to [2020-05-12-android-chrome-tabs.html](file:///Users/kvogel/gdrive/backup/android-chrome-tabs/s7/2020-05-12-android-chrome-tabs.html)
3437 tabs?!
2020-05-19-android-chrome-tabs.html

e.g.
```
Object Relational Tutorial — SQLAlchemy 1.3 Documentation
https://docs.sqlalchemy.org/en/13/orm/tutorial.html#building-a-relationship
inspect  pause  focus tab  reload  close
```
how to get it out of html? beautifulsoup, I guess... or Scrapy?

[notes/row.html](/notes/row.html)
```html
<div class="row">
  <div class="properties-box"><img>
    <div class="subrow-box">
      <div class="subrow">
        <div class="name">SQLAlchemy in Flask — Flask Documentation (1.1.x)</div>
        <div class="url">https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/</div>
      </div>
      <div class="actions"><span class="action" tabindex="1">inspect</span><span class="action"
          tabindex="1">pause</span><span class="action" tabindex="1">focus tab</span><span class="action"
          tabindex="1">reload</span><span class="action" tabindex="1">close</span></div>
    </div>
  </div>
</div>
```
selector: `#\39 886674432514d5231\:chrome_devtools_remote > div.list.pages > div:nth-child(9)`
js path: `document.querySelector("#\\39 886674432514d5231\\:chrome_devtools_remote > div.list.pages > div:nth-child(9)")`
XPath: `//*[@id="9886674432514d5231:chrome_devtools_remote"]/div[2]/div[9]`
full XPath: `/html/body/div[2]/div[2]/div[1]/div[5]/div[2]/div[2]/div/div[2]/div[9]`

but we want just the `subrow`:
```html
      <div class="subrow">
        <div class="name">SQLAlchemy in Flask — Flask Documentation (1.1.x)</div>
        <div class="url">https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/</div>
      </div>
```
selector: `#\39 886674432514d5231\:chrome_devtools_remote > div.list.pages > div:nth-child(9) > div > div > div.subrow`
js path: `document.querySelector("#\\39 886674432514d5231\\:chrome_devtools_remote > div.list.pages > div:nth-child(9) > div > div > div.subrow")`
XPath: `//*[@id="9886674432514d5231:chrome_devtools_remote"]/div[2]/div[9]/div/div/div[1]/div[1]`
full XPath: `/html/body/div[2]/div[2]/div[1]/div[5]/div[2]/div[2]/div/div[2]/div[9]/div/div/div[1]`

[Beautiful Soup Documentation — Beautiful Soup 4.9.0 documentation ](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```py
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
```

[chrome://inspect/#devices](chrome://inspect/#devices) is a Chrome-specific URL
use selenium?

```py
from selenium import webdriver
chrome = webdriver.Chrome()
chrome.get("chrome://inspect/#devices")

for elem in chrome.find_elements_by_class_name("subrow"):
    print(elem.text) # or just use elem
```
?
2020-05-20 11:22:16
whaaat, no pages on chrome://inspect/#devices ?
ah, you have to connect with `adb devices`:
```
20/05/20 11:20:42 kvogel-macbook-2018:~/Projects/TabSutra ±(master) ✗ 
❯ adb devices 
List of devices attached
* daemon not running; starting now at tcp:5037
* daemon started successfully
9886674432514d5231      device
```

### setup

```
20/05/20 9:04:51 kvogel-macbook-2018:~/Projects/TabSutra ±(master) 
❯ python -m venv venv
20/05/20 10:38:43 kvogel-macbook-2018:~/Projects/TabSutra ±(master) ✗ 
❯ . ./venv/bin/activate
```

```
(venv) 20/05/20 10:41:54 kvogel-macbook-2018:~/Projects/TabSutra/src ±(master) ✗ 
❯ python dev.py 
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 83
```
catch this... `except SessionNotCreatedException as e:`

Updating Google Chrome      Version 81.0.4044.138 (Official Build) (64-bit)
Google Chrome is up to date Version 83.0.4103.61 (Official Build) (64-bit)

2020-10-09 14:34:51 doesn't work
worked with `sleep()`

```
(venv) 20/10/9 14:32:04 kvogel-macbook-2018:~/Projects/TabSutra/src ±(master) 
❯ python dev.py
```
```py
Traceback (most recent call last):
  File "dev.py", line 86, in go
    self.parse_page()
  File "dev.py", line 25, in parse_page
    self.browser = webdriver.Chrome()
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py", line 81, in __init__
    desired_capabilities=desired_capabilities)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py", line 157, in __init__
    self.start_session(capabilities, browser_profile)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py", line 252, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/Users/kvogel/Projects/TabSutra/venv/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 83
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "dev.py", line 97, in <module>
    main()
  File "dev.py", line 94, in main
    tabsutra.go()
  File "dev.py", line 89, in go
    print(e.message)
AttributeError: 'SessionNotCreatedException' object has no attribute 'message'
```


2020-11-08 20:04:36

`selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 83`

`Google Chrome is up to date Version 86.0.4240.183 (Official Build) (x86_64)`

[Downloads - ChromeDriver - WebDriver for Chrome ](https://chromedriver.chromium.org/downloads)
[https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.20/ ](https://chromedriver.storage.googleapis.com/index.html?path=87.0.4280.20/)
`https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_mac64.zip`

```
(venv) 20/11/8 19:59:09 kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ which chromedriver
/usr/local/bin/chromedriver
❯ chromedriver --version
ChromeDriver 83.0.4103.39 (ccbf011cb2d2b19b506d844400483861342c20cd-refs/branch-heads/4103@{#416})

20/11/8 20:07:42 kvogel-macbook:/usr/local/bin 
❯ mv ~/Downloads/chromedriver ./chromedriver.87 
❯ ./chromedriver.87 --version
ChromeDriver 87.0.4280.20 (c99e81631faa0b2a448e658c0dbd8311fb04ddbd-refs/branch-heads/4280@{#355})

(venv) 20/11/8 20:08:15 kvogel-macbook:/usr/local/bin 
❯ ln -s chromedriver.87 chromedriver  
❯ ll chromedriver
-rwxr-xr-x  1 kvogel  staff    15M 14 Oct 03:01 chromedriver*
❯ \ls -l chromedriver
lrwxr-xr-x  1 kvogel  admin  15  8 Nov 20:09 chromedriver -> chromedriver.87
❯ chromedriver --version
ChromeDriver 87.0.4280.20 (c99e81631faa0b2a448e658c0dbd8311fb04ddbd-refs/branch-heads/4280@{#355})
```

[Downloads - ChromeDriver - WebDriver for Chrome ](https://chromedriver.chromium.org/downloads)
[https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/ ](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/)

```
(venv) 20/11/8 20:10:54 kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ~/Downloads/chromedriver --version
ChromeDriver 86.0.4240.22 (398b0743353ff36fb1b82468f63a3a93b4e2e89e-refs/branch-heads/4240@{#378})
❯ mv ~/Downloads/chromedriver /usr/local/bin/chromedriver.86
❯ cd -
/usr/local/bin
(venv) 20/11/8 20:17:20 kvogel-macbook:/usr/local/bin 
❯ rm chromedriver
remove chromedriver? y
❯ ln -s chromedriver.86 chromedriver
❯ cd -
~/Projects/TabSutra
(venv) 20/11/8 20:18:07 kvogel-macbook:~/Projects/TabSutra ±(master) ✗ 
❯ ./run.sh

❯ cd src 
❯ ls
dev.py*
❯ head dev.py 
#!/usr/bin/env python

❯ ./dev.py
self.browser = webdriver.Chrome()...
self.browser.get("chrome://inspect/#devices")...
time.sleep(5)...
for elem in self.browser.find_elements_by_class_name("subrow"):...
self.browser: <selenium.webdriv
```

Android Device (s7) shows in 

```
(venv) 20/11/8 22:12:02 kvogel-macbook:~/Projects/TabSutra/src ±(master) ✗ 
❯ rl ~/gdrive/backup/android-chrome-tabs/s7/2020-11-08-Chrome-DevTools-Inspect\#Devices.html 
/Users/kvogel/gdrive/backup/android-chrome-tabs/s7/2020-11-08-Chrome-DevTools-Inspect#Devices.html
```

### Profile error occurred

error from Chrome:
>Profile error occurred. Something went wrong when opening your profile. Some features may be unavailable.

## defer

### get the current file's modified time

`os.path.getmtime(file_name)` gives epoch time
```
21/02/8 20:08:22 kvogel-elitebook:~/cbird/Downloads
❯ bpython
bpython version 0.18 on top of Python 3.8.5 /usr/bin/python3
```
```py
>>> import os
>>> os.path.getmtime('1.txt')
1612537918.8621852
>>>
```
works on Windows proper (and gives the same time):
```
08/02/2021 20:06:21.21 KVOGEL-ELITEBOO:C:\Users\cbird\Downloads
> python
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
```
```py
>>> import os
>>> os.path.getmtime('1.txt')
1612537918.8621852
```

/home/kvogel/pl/python/blog/210208-import-from-other-dir.md
/home/kvogel/pl/python/blog/210208-reimport-module.md


```
21/02/8 19:40:14 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ touch src/__init__.py
❯ bpython
bpython version 0.18 on top of Python 3.8.5 /usr/bin/python3
```
```py
>>> from src.dev import TabSutra
>>> ts = TabSutra()
>>> ts.get_platform()
platform.system(): Linux
'wsl'
```

TODO: detect OS and set up accordingly
TODO ptprompt?

[localhost:9515](http://localhost:9515/)
```json
{"value":{"error":"unknown command","message":"unknown command: unknown command: ","stacktrace":"#0 0x5653d0219199 \u003Cunknown>\n"}}
```

### errors in selenium logs

logs in `chrome.exe` running in `cmd.exe`:
```
[22108:1952:0208/123145.158:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: PRAGMA auto_vacuum
[22108:1952:0208/123145.243:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: PRAGMA journal_mode=TRUNCATE
[22108:1952:0208/123145.292:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:1952:0208/123145.488:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:1952:0208/123145.525:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY, value LONGVARCHAR)
[22108:1952:0208/123145.631:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: PRAGMA auto_vacuum
[22108:1952:0208/123145.664:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: PRAGMA journal_mode=TRUNCATE
[22108:1952:0208/123145.694:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:1952:0208/123145.743:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:1952:0208/123145.774:ERROR:database.cc(1707)] Cookie sqlite error 5, errno 1: database is locked, sql: CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY, value LONGVARCHAR)
[22108:24472:0208/123148.325:ERROR:database.cc(1707)] ReportingAndNEL sqlite error 5, errno 1: database is locked, sql: PRAGMA auto_vacuum
[22108:24472:0208/123148.357:ERROR:database.cc(1707)] ReportingAndNEL sqlite error 5, errno 1: database is locked, sql: PRAGMA journal_mode=TRUNCATE
[22108:24472:0208/123148.388:ERROR:database.cc(1707)] ReportingAndNEL sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:24472:0208/123148.420:ERROR:database.cc(1707)] ReportingAndNEL sqlite error 5, errno 1: database is locked, sql: SELECT 1 FROM sqlite_master WHERE type=? AND name=?
[22108:24472:0208/123148.452:ERROR:database.cc(1707)] ReportingAndNEL sqlite error 5, errno 1: database is locked, sql: CREATE TABLE meta(key LONGVARCHAR NOT NULL UNIQUE PRIMARY KEY, value LONGVARCHAR)
```

### name

2020-10-09 14:33:38 not really right.
droidtab? 

sutra /ˈsuːtrə/ noun
1. a rule or aphorism in Sanskrit literature, or a set of these on grammar or Hindu law or philosophy.
2. a Buddhist or Jainist scripture.
Kama means "desire, wish or longing". In contemporary literature, kama refers usually to sexual desire.

In [Google Translate ](https://translate.google.com/#view=home&op=translate&sl=bn&tl=en&text=%E0%A6%B8%E0%A7%82%E0%A6%A4%E0%A7%8D%E0%A6%B0)
Sutra == Formula, origin, fountain head, primary source
Translations of सूत्र
formula सूत्र, गुन, नुसख़ा
thread धागा, सूत्र, सूत, तंतु, तागा
Sutra सूत्र
clue संकेत, सूत्र, भनक, सुराग़, जुर्म की गवाही, अपराध का प्रमाण
filament रेशा, सूत्र, तन्तु, बिजली के लम्प का न जलनेवाला तार
provenance उत्पत्ति, उत्पत्तिस्थान, सूत्र
provenience उत्पत्ति, सूत्र, उत्पत्तिस्थान
origin उत्पत्ति, स्रोत, व्युत्पत्ति, मूल देश, सूत्र, बीज
fountain head सूत्र, मूललेख
fiber रेशा, तन्तु, रेशम, सूत्र, तंत्रिका, बनावट
primary source सूत्र, मूललेख
quarry शिकार, स्रोत, मारा हुआ पशु, सूत्र
7 more translations

TODO: canonical way to make sure Python3 is used rather than py2? Error if not installed?

TODO: canonical way to make sure python dependencies are installed e.g. selenium?

### auto-install correct `chromedriver`?

[selenium - SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 81](https://stackoverflow.com/questions/60296873/sessionnotcreatedexception-message-session-not-created-this-version-of-chrome)
[python - Error message: "'chromedriver' executable needs to be available in the path"](https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path/52878725#52878725)
[webdriver-manager · PyPI ](https://pypi.org/project/webdriver-manager/)
>I solved these kinds of problems using the webdrive manager.
>You can automatically use the correct chromedriver by using the webdrive-manager. 
>Install the webdrive-manager: `pip install webdriver-manager`
>Then use the driver in python as follows:
```py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```


## done

```
20/05/20 8:56:37 kvogel-macbook-2018:~/Projects 
❯ mkdir TabSutra && cd $_ && git init
Initialized empty Git repository in /Users/kvogel/Projects/TabSutra/.git/
20/05/20 8:59:52 kvogel-macbook-2018:~/Projects/TabSutra ±(master) 
❯ code .
```

### WSL install selenium

```
(venv) 20/05/20 10:41:50 kvogel-macbook-2018:~/Projects/TabSutra/src ±(master) ✗ 
❯ pip install selenium
❯ python dev.py
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

2021-02-08 10:46:07
```
21/02/8 10:44:51 kvogel-elitebook:~/projects/tabsutra ±(master) 
❯ ./run.sh
Traceback (most recent call last):
  File "src/dev.py", line 3, in <module>
    from selenium import webdriver
ModuleNotFoundError: No module named 'selenium'
21/02/8 10:45:08 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ pip3 install selenium
...
Requirement already satisfied: urllib3 in /usr/lib/python3/dist-packages (from selenium) (1.25.8)
Installing collected packages: selenium
Successfully installed selenium-3.141.0
```
### MacOS download chromedriver and put in PATH

[ChromeDriver - WebDriver for Chrome ](https://sites.google.com/a/chromium.org/chromedriver/home)
https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/
https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_mac64.zip

```
20/05/20 10:44:29 kvogel-macbook-2018:~/Downloads
❯ unzip chromedriver_mac64.zip
Archive:  chromedriver_mac64.zip
  inflating: chromedriver
❯ mv chromedriver /usr/local/bin
20/05/20 10:45:15 kvogel-macbook-2018:~/Downloads
❯ which chromedriver
/usr/local/bin/chromedriver
```

### WSL download chromedriver and put in PATH

```
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```
```
❯ mv chromedriver ~/.local/bin
```


### Use python3

```
21/02/8 10:41:47 kvogel-elitebook:~/projects/tabsutra ±(master) 
❯ ./run.sh 
  File "src/dev.py", line 33
    print(f"self.browser: {self.browser}")
                                        ^
SyntaxError: invalid syntax
```
`src/dev.py`:
```diff
-#!/usr/bin/env python
+#!/usr/bin/env python3
```


### DeprecationWarning: use options instead of chrome_options
```
21/02/8 13:14:10 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ ./run.sh  
src/dev.py:98: DeprecationWarning: use options instead of chrome_options
  driver = webdriver.Chrome(chrome_options=options, executable_path="/home/kvogel/.local/bin/chromedriver", )
```
```diff
-            driver = webdriver.Chrome(options=chrome_options, executable_path="/home/kvogel/.local/bin/chromedriver", )
+            driver = webdriver.Chrome(options=options, executable_path="/home/kvogel/.local/bin/chromedriver", )
```
fixed

### chromedriver mismatch?

```
21/02/8 11:59:15 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ chromedriver
Starting ChromeDriver 88.0.4324.96 (68dba2d8a0b149a1d3afac56fa74648032bcf46b-refs/branch-heads/4324@{#1784}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```

[About Version](chrome://version/)
>Google Chrome is up to date Version 88.0.4324.150 (Official Build) (64-bit)

doesn't look like it

### Add chrome.exe to PATH in WSL

```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary
```

Process Hacker, find Chrome process, right-click, properties: `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
i.e. `/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe`

```
21/02/8 13:12:02 kvogel-elitebook:~/projects/tabsutra ±(master) ✗ 
❯ vi ~/.zshrc
```
```diff
+# for selenium webdriver (chromedriver):
+export PATH=$PATH:/mnt/c/Program\ Files\ \(x86\)/Google/Chrome/Application/
```
```
❯ . $_       
This is /home/kvogel/.zshrc
❯ which chrome.exe 
/mnt/c/Program Files (x86)/Google/Chrome/Application//chrome.exe
```
but still need to do
```py
options = Options()
options.binary_location = "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="/home/kvogel/.local/bin/chromedriver", )
```
or get
```
selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary
```

