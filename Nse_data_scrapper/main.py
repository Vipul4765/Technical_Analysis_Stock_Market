from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from next_date import increment_date

start_date = "01012020"
end_date = "13082024"
flag = False


def data_of_date(curr_date):
    # Set up Chrome options
    chrome_options = Options()
    download_dir = "D:\\stock_data_csv"
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Set up WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Open the URL
    driver.get(f'https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{curr_date}.csv')

    # Wait for download to complete
    time.sleep(10)


while not flag:
    if start_date == end_date:
        flag = True
    data_of_date(start_date)
    start_date = increment_date(start_date)
