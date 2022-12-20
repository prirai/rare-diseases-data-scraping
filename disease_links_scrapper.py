from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver_path = '/usr/bin/geckodriver'
service = Service(driver_path)
ff_options = Options()
# ff_options.add_argument('--headless')
ff_options.add_argument('--window-size=1920,1080')
driver = Firefox(service=service, options=ff_options)

from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://rarediseases.info.nih.gov/diseases"

data = []
df = pd.DataFrame(data)

driver.get(base_url)

timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "results")))
except TimeoutException:
    driver.quit()

SAVE_INTERVAL = 50
SAVE_FILE_PATH = 'disease_links.csv'

i = 0
while True:
    i += 1
    if i % 50 == 0:
        df.to_csv(SAVE_FILE_PATH, index=False)

    url_link = driver.current_url
    print(url_link)
    s1 = BeautifulSoup(driver.page_source, 'html.parser')
    results_div = s1.find('div', {'class': 'results pt-lg-2'})

    for a_tag in results_div.find_all('a'):
        d = {}
        title = a_tag.find('h5').string
        details = a_tag.find('p')
        if details is None:
            details = ""
        else:
            details = details.string
        link = a_tag['href']
        d['title'] = title
        d['details'] = details
        d['link'] = link
        dict = pd.DataFrame(d, index=[0])
        df = pd.concat([df, dict], ignore_index=True)

    try:
        driver.find_element(By.XPATH, '/html/body/app-root/ng-component/div[2]/div/div/div/div/div[2]/div[3]/div/a[2]').click()
    except:
        break

df.to_csv(SAVE_FILE_PATH, index=False)

driver.close()