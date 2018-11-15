# Need to download Chrome web driver for Selenium at:
# https://chromedriver.storage.googleapis.com/index.html?path=2.43/

# Selenium docs: https://selenium-python.readthedocs.io
from selenium import webdriver
import time
import datetime
from datetime import timedelta

def fix_format(x):
    if len(x) == 1:
        result = "0" + x
        return result
    else:
        return x

# Gets data from specified date up to current date
def get_chart_data(year, month, day):
    # Pass the file path of your Chrome webdriver to the Chrome() constructor
    # Change the constructor to your ChromeDriver location
    driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
    has_finished = False
    date = datetime.datetime(year, month, day)
    while not has_finished:
        date_formatted = str(date.year) + "-" + fix_format(str(date.month)) + "-" + fix_format(str(date.day))
        print("Current date: " + date_formatted)
        driver.get("https://spotifycharts.com/regional/gb/daily/" + date_formatted)
        try:
            element = driver.find_element_by_link_text("DOWNLOAD TO CSV")
            element.click()
            date = date + timedelta(days=1)
            time.sleep(5)
        except:
            print("Attempted download of Spotify Chart data from specified date up to current date.")
            print("If no data was downloaded, ensure that the provided date was correctly formatted:")
            print("For Example: get_chart_data(2018, 08, 03)")
            has_finished = True
