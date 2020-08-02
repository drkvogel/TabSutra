```
20/05/20 8:56:37 kvogel-macbook-2018:~/Projects 
❯ mkdir TabSutra && cd $_ && git init
Initialized empty Git repository in /Users/kvogel/Projects/TabSutra/.git/
20/05/20 8:59:52 kvogel-macbook-2018:~/Projects/TabSutra ±(master) 
❯ code .
```


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
(venv) 20/05/20 10:41:50 kvogel-macbook-2018:~/Projects/TabSutra/src ±(master) ✗ 
❯ pip install selenium
❯ python dev.py
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

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

```
(venv) 20/05/20 10:41:54 kvogel-macbook-2018:~/Projects/TabSutra/src ±(master) ✗ 
❯ python dev.py 
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 83
```
catch this... `except SessionNotCreatedException as e:`

Updating Google Chrome      Version 81.0.4044.138 (Official Build) (64-bit)
Google Chrome is up to date Version 83.0.4103.61 (Official Build) (64-bit)

“RescueTime.app“ wants access to control “Visual Studio Code.app“. Allowing control will provide access to documents and data in “Visual Studio Code.app“, and to perform actions within that app.
RescueTime requires scripting access to some applications for window title tracking and supported web browsers for url tracking and FocusTime website blocking.

### name

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


