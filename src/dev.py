#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException, StaleElementReferenceException
import time
import os, platform, sys, time


# TODO check if adb installed
# TODO run adb devices, check if device
# TODO make sure phone is attached
# TODO make sure phone data is allowed

class TabSutra():
    CHROME_INSPECT_URL = 'chrome://inspect/#devices'
    SLEEP_SECONDS = 3

    # jls_extract_var = 'chrome://inspect/#devices'
    # CHROME_INSPECT_URL = jls_extract_var
    # ??? Java linting my Python file?? : vscode (https://www.reddit.com/r/vscode/comments/n05vl9/java_linting_my_python_file/)

    def __init__(self):
        pass

    def get_browser(self):
        self.driver = webdriver.Chrome()

    def parse_page_with_sleep(self):
        # this works:
        # print("self.browser = webdriver.Chrome()...")
        options = Options()
        # options.add_argument("--headless") # len(subrows): 0 No rows fetched. Quitting.
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--lang=en_GB')
        self.driver = webdriver.Chrome(options=options)
        print(f'self.browser.get({self.CHROME_INSPECT_URL})...')
        self.driver.get(self.CHROME_INSPECT_URL)
        print(f'sleeping for {self.SLEEP_SECONDS} seconds...')
        print(f'TODO should poll to see if browser ready, not sleep')
        time.sleep(self.SLEEP_SECONDS) #
        # print('for elem in self.browser.find_elements_by_class_name(\"subrow\"):...')
        # print(f'self.browser: {self.browser}')
        # subrows = self.driver.find_elements_by_class_name('subrow') # DeprecationWarning: find_elements_by_* commands are deprecated. Please use find_elements() instead
        subrows = self.driver.find_elements(By.CLASS_NAME, 'subrow')
        print(f'len(subrows): {len(subrows)}')
        if len(subrows) <= 1:
            print('No rows fetched. Quitting.')
            sys.exit(0)

        # for elem in self.browser.find_elements_by_class_name('subrow'):
        try:
            with open('tabs.md', 'w') as out_file:
                for elem in subrows:
                    print(elem.text)
                    lines = elem.text.split('\n')
                    if len(lines) > 1:
                        title = lines[0]
                        url = lines[1]
                        out_line = f'[{title}]({url})\n'
                    else:
                        out_line = f'{elem.text}\n'
                    out_file.write(out_line)
        except StaleElementReferenceException:
            # always get: "selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document"
            # at the end, even though the list of tabs is complete
            print('Got StaleElementReferenceException')


    def parse_page_with_find(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.CHROME_INSPECT_URL)

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
                rows = self.driver.find_elements_by_class_name("subrow")
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

        self.driver.close()

        # selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
        #   (Session info: chrome=83.0.4103.61)

    # def get_page():
    #     chrome = webdriver.Chrome()
    #     chrome.get("chrome://inspect/#devices")


    def go(self):
        try:
            this_file_path = os.path.abspath(__file__) # os.path.dirname(os.path.abspath(__file__))
            this_file_mtime = os.path.getmtime(this_file_path)
            this_file_mtime_hr = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(this_file_mtime))
            print(f'This is {this_file_path}, modified at {this_file_mtime_hr}')
            print(f'Platform: {self.get_platform()}')
            print()

            options = Options()
            options.add_argument("--headless")
            #, executable_path="/home/kvogel/.local/bin/chromedriver", )
            # otherwise on WSL get: `selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary`
            # even if `chrome.exe` is in PATH
            # options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            # driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Utility/BrowserDrivers/chromedriver.exe", )
            # driver.get('http://google.com/')
            driver = webdriver.Chrome(options=options)

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
        # print(f'platform.system(): {platform.system()}, os.uname().release: {os.uname().release}')
        if platform.system() == 'Linux':
            # Linux or WSL
            if 'microsoft-standard' in os.uname().release:
                return 'wsl'
            else:
                return 'linux'
        elif platform.system() == 'Darwin':
            return 'macos'
        elif platform.system() == 'Windows':
            return 'windows'


def main():
    tabsutra = TabSutra()
    tabsutra.go()

if __name__ == "__main__":
    main()
