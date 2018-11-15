# Spotify Charts: Daily CSV Downloader
A script for quickly downloading a large amount of the **daily** CSV data files from the [Spotify Charts website](https://spotifycharts.com/regional/gb/daily/).

# Setup Instructions

This script was written and run in Python 3.6.2 so if there are any errors it is most likely due to running it on a different version of Python.

1) Install the Selenium package in Python with pip:

```pip install selenium```

2) [Download the Chrome web driver.](https://chromedriver.storage.googleapis.com/index.html?path=2.43/)

3) In the SpotifyCharts.py script, go to line 21 and find the line below:

```driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")```

Change the file path of the ChromeDrive.exe in the constructor to your ChromeDriver.exe file path.

# Usage

To use the script you need to pass it 3 parameters. The year, the month, and the day of the date you want to start downloading FROM in the format of YYYY/M/D. For example, "get_chart_data(2018, 6, 1)" to get all files from June 1st 2018 until now.

To download all the CSV files for November so far you call the function in the script file like so: 

```
# Download CSV files from November 1st up to the current day.
get_chart_data(2018, 11, 1)
```

Alternatively, you can open the command line in the folder that contains the script and enter the following command, changing the date parameters to your selection:

```
# This example command gets the CSV files from November 11th 2018 up to now
python -c "import SpotifyCharts; SpotifyCharts.get_chart_data(2018, 11, 11)"
```
