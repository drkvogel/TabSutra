
### chromedriver out of date

```
23/09/21 6:58:17 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ ./run.sh

This is /Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py on Python 3.11.4 (main, Jul 25 2023, 17:36:13) [Clang 14.0.3 (clang-1403.0.22.14.1)]

adb found at /Users/kvogel/.local/bin/platform-tools/adb
Traceback (most recent call last):
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 168, in go
    driver = webdriver.Chrome(options=options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/chrome/webdriver.py", line 80, in __init__
    super().__init__(
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/chromium/webdriver.py", line 104, in __init__
    super().__init__(
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 286, in __init__
    self.start_session(capabilities, browser_profile)
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 378, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 440, in execute
    self.error_handler.check_response(response)
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/errorhandler.py", line 245, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114
Current browser version is 116.0.5845.187 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
Stacktrace:
0   chromedriver                        0x00000001010e3f48 chromedriver + 4226888
1   chromedriver                        0x00000001010dc4f4 chromedriver + 4195572
2   chromedriver                        0x0000000100d20d68 chromedriver + 281960
3   chromedriver                        0x0000000100d4cbac chromedriver + 461740
4   chromedriver                        0x0000000100d48fd8 chromedriver + 446424
5   chromedriver                        0x0000000100d46150 chromedriver + 434512
6   chromedriver                        0x0000000100d8393c chromedriver + 686396
7   chromedriver                        0x0000000100d83164 chromedriver + 684388
8   chromedriver                        0x0000000100d4ff1c chromedriver + 474908
9   chromedriver                        0x0000000100d50ef4 chromedriver + 478964
10  chromedriver                        0x00000001010a559c chromedriver + 3970460
11  chromedriver                        0x00000001010a96f0 chromedriver + 3987184
12  chromedriver                        0x00000001010af5b4 chromedriver + 4011444
13  chromedriver                        0x00000001010aa2fc chromedriver + 3990268
14  chromedriver                        0x00000001010821c0 chromedriver + 3826112
15  chromedriver                        0x00000001010c6088 chromedriver + 4104328
16  chromedriver                        0x00000001010c61e0 chromedriver + 4104672
17  chromedriver                        0x00000001010d5f28 chromedriver + 4169512
18  libsystem_pthread.dylib             0x00000001a9b3ffa8 _pthread_start + 148
19  libsystem_pthread.dylib             0x00000001a9b3ada0 thread_start + 8


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 206, in <module>
    main()
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 203, in main
    tabsutra.go()
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 178, in go
    print(e.message)
          ^^^^^^^^^
AttributeError: 'SessionNotCreatedException' object has no attribute 'message'
```

[chromedriver](https://www.google.com/search?q=chromedriver&ie=UTF-8)
[ChromeDriver - WebDriver for Chrome - Version Selection ](https://chromedriver.chromium.org/downloads/version-selection)
[GitHub - GoogleChromeLabs/chrome-for-testing ](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints)
[GitHub - GoogleChromeLabs/chrome-for-testing ](https://github.com/GoogleChromeLabs/chrome-for-testing#other-api-endpoints)
[@puppeteer/browsers  Puppeteer ](https://pptr.dev/browsers-api)

[how to download latest chromedriver](https://www.google.com/search?q=how+to+download+latest+chromedriver&ie=UTF-8)
[How to download Chrome Driver for Selenium - AutomationTestingHub AutomationTestingHub ](https://www.automationtestinghub.com/download-chrome-driver/)
[linux - How to always download the latest version of chromedriver and geckodriver?](https://stackoverflow.com/questions/69641344/how-to-always-download-the-latest-version-of-chromedriver-and-geckodriver)

[Chromedriver Download Scripts · GitHub ](https://gist.github.com/ddavison/936d843ad17140021fad)
```bash
#!/bin/sh
####
# Author: ddavison
# Description: Download the Mac chromedriver into the current directory
####
function downloadchrome {
  #latest=`curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE`
  version="2.9"
  download_location="http://chromedriver.storage.googleapis.com/$version/chromedriver_mac32.zip"
  rm /tmp/chromedriver_mac32.zip
  wget -P /tmp $download_location
  unzip /tmp/chromedriver_mac32.zip -d .
  mv ./chromedriver ./chromedriver.mac
  chmod u+x ./chromedriver.mac
}
downloadchrome
```

```
23/09/21 6:59:05 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE
114.0.5735.90%
❯ which jq
jq not found
❯ brew install jq

23/09/21 7:56:35 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ brew install wget
```

```
23/09/21 7:42:14 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ man curl
       -s, --silent
              Silent or quiet mode.
```

```json
  "timestamp": "2023-09-20T19:08:13.905Z",
  "channels": {
    "Stable": {
      "channel": "Stable",
      "version": "117.0.5938.88",
      "revision": "1181205",
      "downloads": {
        "chromedriver": [
          {
            "platform": "mac-arm64",
            "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/mac-arm64/chromedriver-mac-arm64.zip"
          },
```
  "channels", "Stable" "downloads" "chromedriver": [
          {
            "platform": "mac-arm64",
            "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/mac-arm64/chromedriver-mac-arm64.zip"
          },


[jq Manual (development version) ](https://jqlang.github.io/jq/manual/#invoking-jq)

>`--raw-output` / `-r`:
>With this option, if the filter's result is a string then it will be written directly to standard output rather than being formatted as a JSON string with quotes. This can be useful for making jq filters talk to non-JSON-based systems.

```
23/09/21 8:12:06 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ curl -s https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq '.channels.Stable.downloads.chromedriver'
[
  {
    "platform": "linux64",
    "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/linux64/chromedriver-linux64.zip"
  },
  {
    "platform": "mac-arm64",
    "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/mac-arm64/chromedriver-mac-arm64.zip"
  },

23/09/21 8:12:19 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ curl -s https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json | jq '.channels.Stable.downloads.chromedriver | .[]'
{
  "platform": "linux64",
  "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/linux64/chromedriver-linux64.zip"
}
{
  "platform": "mac-arm64",
  "url": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.88/mac-arm64/chromedriver-mac-arm64.zip"
}
```


[ChromeDriver - WebDriver for Chrome - Version Selection ](https://chromedriver.chromium.org/downloads/version-selection)

[GitHub - GoogleChromeLabs/chrome-for-testing ](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints)
[GitHub - GoogleChromeLabs/chrome-for-testing ](https://github.com/GoogleChromeLabs/chrome-for-testing#other-api-endpoints)
[@puppeteer/browsers  Puppeteer ](https://pptr.dev/browsers-api)
[how to download latest chromedriver](https://www.google.com/search?q=how+to+download+latest+chromedriver&ie=UTF-8#ip=1)
[selenium webdriver - How can we download chromedriver 117?](https://stackoverflow.com/questions/77111127/how-can-we-download-chromedriver-117)
[How to Install Chrome Driver on Mac ](https://www.swtestacademy.com/install-chrome-driver-on-mac/)

[ChromeDriver - WebDriver for Chrome ](https://sites.google.com/chromium.org/driver/home) looks same as
[ChromeDriver - WebDriver for Chrome ](https://chromedriver.chromium.org/home)

[googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json ](https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json)
[How to download Chrome Driver for Selenium - AutomationTestingHub AutomationTestingHub ](https://www.automationtestinghub.com/download-chrome-driver/)
[linux - How to always download the latest version of chromedriver and geckodriver?](https://stackoverflow.com/questions/69641344/how-to-always-download-the-latest-version-of-chromedriver-and-geckodriver)
[Chromedriver Download Scripts · GitHub ](https://gist.github.com/ddavison/936d843ad17140021fad)

[Linux Commands Comparison curl vs wget ](https://www.tutorialspoint.com/linux-commands-comparison-curl-vs-wget)
[utilities - What is the difference between curl and wget? - Unix & Linux Stack Exchange ](https://unix.stackexchange.com/questions/47434/what-is-the-difference-between-curl-and-wget)

### jq

[Tutorial ](https://jqlang.github.io/jq/tutorial/)
[jq Manual (development version) ](https://jqlang.github.io/jq/manual/#conditionals-and-comparisons)

[selenium webdriver - Unable to download chrome driver for version 115](https://stackoverflow.com/questions/76746946/unable-to-download-chrome-driver-for-version-115)
[Simplifying ChromeDriver Downloads for Automation Testers  LinkedIn ](https://www.linkedin.com/pulse/simplifying-chromedriver-downloads-automation-testers-fayez-alibrahim/)
[jq find value match in array](https://www.google.com/search?q=jq+find+value+match+in+array&ie=UTF-8)
[json - How to filter an array of objects based on values in an inner array with jq?](https://stackoverflow.com/questions/26701538/how-to-filter-an-array-of-objects-based-on-values-in-an-inner-array-with-jq)


[Guide to Linux jq Command for JSON Processing  Baeldung on Linux ](https://www.baeldung.com/linux/jq-command-json)



```
23/11/23 19:13:42 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ ./run.sh
This is /Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py on Python 3.11.6 (main, Oct  2 2023, 13:45:54) [Clang 15.0.0 (clang-1500.0.40.1)]

adb found at /Users/kvogel/.local/bin/platform-tools/adb
Traceback (most recent call last):
...
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 114
```


>Chrome is up to date Version 119.0.6045.159 (Official Build) (arm64)


[ChromeDriver - WebDriver for Chrome - Downloads ](https://chromedriver.chromium.org/downloads)
>If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. This page provides convenient JSON endpoints for specific ChromeDriver version downloading.
[Chrome for Testing availability ](https://googlechromelabs.github.io/chrome-for-testing/)



https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/mac-arm64/chromedriver-mac-arm64.zip

or via brew:
```
# 23/11/23 19:19:24 kvogel@kvogel-macbook-2021:~/Downloads/chromedriver-mac-arm64
$ which chromedriver
/opt/homebrew/bin/chromedriver
# 23/11/23 19:19:31 kvogel@kvogel-macbook-2021:~/Downloads/chromedriver-mac-arm64
$ brew install chromedriver
...
==> Upgrading 1 outdated package:
chromedriver 114.0.5735.90 -> 119.0.6045.105
==> Upgrading chromedriver
==> Downloading https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/mac-arm64/chromedriver-mac-arm64.zip
==> Unlinking Binary '/opt/homebrew/bin/chromedriver'
==> Linking Binary 'chromedriver' to '/opt/homebrew/bin/chromedriver'
==> Purging files for version 114.0.5735.90 of Cask chromedriver
🍺  chromedriver was successfully upgraded!
```

then need to approve it... can do with xattr?


```
23/11/23 19:21:12 kvogel@kvogel-macbook-2021:~/projects/general/projects/repos/tabsutra ±(master) ✗
❯ ./run.sh

This is /Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py on Python 3.11.6 (main, Oct  2 2023, 13:45:54) [Clang 15.0.0 (clang-1500.0.40.1)]

adb found at /Users/kvogel/.local/bin/platform-tools/adb
filename: backups/tabs-2023-11-23T192159.md
self.browser.get(chrome://inspect/#devices)...
sleeping for 3 seconds...
TODO should poll to see if browser ready, not sleep. Or at least prompt.
Make sure access permissions are granted on, then press a key to continue
len(subrows): 366
.............................................................................................................................................................................................................................................................................................................................................................................Traceback (most recent call last):
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 206, in <module>
    main()
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 203, in main
    tabsutra.go()
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 174, in go
    self.parse_page_with_sleep()
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/src/dev.py", line 78, in parse_page_with_sleep
    lines = elem.text.split('\n')
            ^^^^^^^^^
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webelement.py", line 89, in text
    return self._execute(Command.GET_ELEMENT_TEXT)["value"]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webelement.py", line 403, in _execute
    return self._parent.execute(command, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 440, in execute
    self.error_handler.check_response(response)
  File "/Users/kvogel/projects/general/projects/repos/tabsutra/venv/lib/python3.11/site-packages/selenium/webdriver/remote/errorhandler.py", line 245, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: No node with given id found
  (Session info: chrome=119.0.6045.159)
Stacktrace:
0   chromedriver                        0x0000000105322004 chromedriver + 4169732
1   chromedriver                        0x0000000105319ff8 chromedriver + 4136952
2   chromedriver                        0x0000000104f6f500 chromedriver + 292096
3   chromedriver                        0x0000000104f57f6c chromedriver + 196460
4   chromedriver                        0x0000000104f55f30 chromedriver + 188208
5   chromedriver                        0x0000000104f56b14 chromedriver + 191252
6   chromedriver                        0x0000000104f7d8f8 chromedriver + 350456
7   chromedriver                        0x0000000104f751f8 chromedriver + 315896
8   chromedriver                        0x0000000104f739dc chromedriver + 309724
9   chromedriver                        0x0000000104f76780 chromedriver + 321408
10  chromedriver                        0x0000000104f768ac chromedriver + 321708
11  chromedriver                        0x0000000104faeee4 chromedriver + 552676
12  chromedriver                        0x0000000104fa9db4 chromedriver + 531892
13  chromedriver                        0x0000000104fef818 chromedriver + 817176
14  chromedriver                        0x0000000104fa85e8 chromedriver + 525800
15  chromedriver                        0x0000000104fa94b8 chromedriver + 529592
16  chromedriver                        0x00000001052e8334 chromedriver + 3932980
17  chromedriver                        0x00000001052ec970 chromedriver + 3950960
18  chromedriver                        0x00000001052d0774 chromedriver + 3835764
19  chromedriver                        0x00000001052ed478 chromedriver + 3953784
20  chromedriver                        0x00000001052c2ab4 chromedriver + 3779252
21  chromedriver                        0x0000000105309914 chromedriver + 4069652
22  chromedriver                        0x0000000105309a90 chromedriver + 4070032
23  chromedriver                        0x0000000105319c70 chromedriver + 4136048
24  libsystem_pthread.dylib             0x000000018b363034 _pthread_start + 136
25  libsystem_pthread.dylib             0x000000018b35de3c thread_start + 8
```

but:
/Users/kvogel/projects/general/projects/repos/tabsutra/backups/tabs-2023-11-23T192159.md

