#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, StaleElementReferenceException
# from selenium.common import SessionNotCreatedException, StaleElementReferenceException
import time

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

# TODO ptprompt?

    def go(self):
        try:
            # page = get_page()
            # self.browser = self.get_browser()
            # self.parse_page()
                # AttributeError: 'NoneType' object has no attribute 'get'
            self.parse_page_with_sleep()
            # self.parse_page_with_find()

        except SessionNotCreatedException as e:
            print(e.message)
            return

def main():
    tabsutra = TabSutra()
    tabsutra.go()

if __name__ == "__main__":
    main()
