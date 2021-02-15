#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException, StaleElementReferenceException
# from selenium.common import SessionNotCreatedException, StaleElementReferenceException
import time
import os, platform, sys, time

# def get_page():
#     chrome = webdriver.Chrome()
#     chrome.get("chrome://inspect/#devices")

# TODO check if adb installed
# TODO run adb devices, check if device
# TODO make sure phone is attached
# TODO make sure phone data is allowed

class TabSutra():
    def __init__(self):
        pass

    def get_browser(self):
        self.browser = webdriver.Chrome()

    def parse_page_with_sleep(self):
        # this works:
        print("self.browser = webdriver.Chrome()...")
        self.browser = webdriver.Chrome()
        print("self.browser.get(\"chrome://inspect/#devices\")...")
        self.browser.get("chrome://inspect/#devices")
        print("time.sleep(5)...")
        time.sleep(15) #
        print("for elem in self.browser.find_elements_by_class_name(\"subrow\"):...")
        print(f"self.browser: {self.browser}")
        for elem in self.browser.find_elements_by_class_name("subrow"):
            print(elem.text)

    def parse_page_with_find(self):
        self.browser = webdriver.Chrome()
        self.browser.get("chrome://inspect/#devices")

        # e.g. row:
        # BBC Learning English - How do I compare two things? Thai - BBC Sounds
        # https://www.bbc.co.uk/sounds/play/p06r930z

        # better way to wait until page ready?
        # poll, with timeout?
        for x in range(10):
            print("Looking for tabs...")
            time.sleep(1)
            # TODO test for parent element instead?
            # if rows is None:
            #     print('Not yet...')
            #     time.sleep(1)
            # else:
            #     break
            try:
                rows = self.browser.find_elements_by_class_name("subrow")
                print('Got rows')
                print('Waiting...', end='')
                time.sleep(2) # wait a bit...
                print('done')
                HEAD_ROWS = 15
                print(f'First {HEAD_ROWS} rows:')
                for n in range(HEAD_ROWS):
                    print(f'{n}: {rows[0].text}')
                break
            except StaleElementReferenceException as e:
                print(f'e: {e.message}')
                print('Not yet...')
            

        print('outside loop')
        # for row in rows:
        #     print(row.text)
        # HEAD_ROWS = 15
        # print(f'First {HEAD_ROWS} rows:')
        # for n in range(HEAD_ROWS):
        #     print(f'{n}: {rows[0].text}')

        self.browser.close()

        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
        #   (Session info: chrome=83.0.4103.61)

    def go(self):
        try:
            # C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
            # chrome.exe current path:
            # '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe'
            # chromedriver current path:
            # /home/kvogel/.local/bin/chromedriver

            this_file_path = os.path.abspath(__file__) # os.path.dirname(os.path.abspath(__file__))
            this_file_mtime = os.path.getmtime(this_file_path)

            # print(f'this_file_mtime: {this_file_mtime}') #  1612816979.1176763
            # time_now = time.time()
            # print(f'time_now {time_now}') # 1612816983.5057838
            # time_now = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
            # print(f'time_now {time_now}') # 2021-02-08
            # print('boo asfasdfasdfasd xxx!')

            this_file_mtime_hr = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(this_file_mtime))
            print(f'this is {this_file_path}, modified at {this_file_mtime_hr}')
                # this is /home/kvogel/projects/tabsutra/src/dev.py, modified at 2021-02-08 20:44:07

            print(f'go(): Platform: {self.get_platform()}')
            print()
            sys.exit(0)

            options = Options()

            # if self.get_platform() == 
            options.binary_location = "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            driver = webdriver.Chrome(options=options, executable_path="/home/kvogel/.local/bin/chromedriver", )
            # otherwise on WSL get: `selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary`
            # even if `chrome.exe` is in PATH

            # options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            # driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe", )
            # driver.get('http://google.com/')

            # page = get_page()
            # self.browser = self.get_browser()
            # self.parse_page()
                # AttributeError: 'NoneType' object has no attribute 'get'
            self.parse_page_with_sleep()
            # self.parse_page_with_find()

        except SessionNotCreatedException as e:
            print(e.message)
            return

    def get_platform(self):
        # print(f'platform.system(): {platform.system()}')
        if platform.system() == 'Linux':
        # if sys.platform == 'linux':
            # Linux or WSL
            # uname = os.uname()
            # if uname.sysname == 'Linux':
            if 'microsoft-standard' in os.uname().release:
                return 'wsl'
            else:
                return 'linux'
        # elif uname.sysname == 'Darwin':
        # elif sys.platform == 'darwin':
        elif platform.system() == 'Darwin':
            return 'macos'
        # elif uname.sysname
        elif platform.system() == 'Windows':
            return 'windows'
            # print(f'uname: {uname.')


def main():
    tabsutra = TabSutra()
    print(f'main(): Platform: {tabsutra.get_platform()}')
    # sys.exit(0)
    tabsutra.go()

if __name__ == "__main__":
    main()
