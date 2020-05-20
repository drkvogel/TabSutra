#!/usr/bin/env python

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
import time

# def get_page():
#     chrome = webdriver.Chrome()
#     chrome.get("chrome://inspect/#devices")

# TODO make sure phone is attached
# TODO make sure phone data is allowed

class TabSutra():
    def __init__(self):
        pass

    def get_browser(self):
        self.browser = webdriver.Chrome()

    def parse_page(self):
        self.browser = webdriver.Chrome()
        self.browser.get("chrome://inspect/#devices")
        # if not 
        time.sleep(5) # booyah!
        # better way to wait until page ready?
        # poll, with timeout?
        for elem in self.browser.find_elements_by_class_name("subrow"):
        # for elem in self.browser.fin
            print(elem.text) # or just use elem

# selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
#   (Session info: chrome=83.0.4103.61)

    def go(self):
        try:
            # page = get_page()
            # self.browser = self.get_browser()
            # self.parse_page()
                # AttributeError: 'NoneType' object has no attribute 'get'
            self.parse_page()

        except SessionNotCreatedException as e:
            print(e.message)
            return

def main():
    tabsutra = TabSutra()
    tabsutra.go()

if __name__ == "__main__":
    main()
