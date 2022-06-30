from distutils.util import execute
from lib2to3.pgen2 import driver
from traceback import print_tb
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pickle
import time


########################################################################################################

# for headless chrome
options = webdriver.ChromeOptions()
options.headless = False
# options.add_argument('--start-maximized')

# to use my own main chrome profile.(can't use multiple session at once)
# options.add_argument("user-data-dir=C:\\Users\\Arjun\\AppData\\Local\\Google\\Chrome\\User Data");

# for that shit log error message
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(
    executable_path='C:\\chromedriver\\chromedriver.exe', options=options)
browser.set_window_size(1366, 768)
wait = WebDriverWait(browser, 10)

########################################################################################################


def element_catch(xpath):
    return wait.until(ec.presence_of_element_located((By.XPATH, xpath)))


# to handle the login and cookies
def save_localstorage():
    browser.execute_script(
        "localStorage.token = '5909325ce3820585405f3c46c5bc13a17089394770335c464b58c065b8dbc01c'")


cookies_path = 'F:\\Manab World Backup\\Manab Workspace\\GITHUB\\physicswallah-site-scraper\\cookies.pkl'
try:
    # load cookies
    coockies = pickle.load(open(
        cookies_path, 'rb'))
    browser.get(
        "https://study.physicswallah.live/")
    for cookie in coockies:
        browser.add_cookie(cookie)
        print("adding cookies")
        save_localstorage()
except Exception as e:
    # it'll fail for the first time, when cookie file is not present
    print(str(e))
    print("Error loading cookies")


def save_cookies():
    cookies = browser.get_cookies()
    pickle.dump(cookies, open(cookies_path, 'wb'))


def close_all():
    # close all open tabs
    if len(browser.window_handles) < 1:
        return
    for window_handle in browser.window_handles[:]:
        browser.switch_to.window(window_handle)
        browser.close()


def quit():
    save_cookies()
    close_all()
    browser.quit()


# ........................................................................................................ #
chapter_link = input("Paste the chapter link: ")
# chapter_link = 'https://study.physicswallah.live/tabs/tabs/batch-tab/613f3f0b09fa3d001891a954/new-overview'

# Getting chapter's page
browser.get(chapter_link)
# r = browser.execute_script("return window.performance.getEntries();")
# .......................................................................................................................
