import subprocess
import os
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

d1 = pd.read_csv('../../data.csv')

base_url = "https://rarediseases.info.nih.gov/"
links = []

for i in range(5910):
    sub_url = d1.loc[i, "link"]
    url_link = base_url + sub_url
    links.append(url_link)

def download_page(link):
  # Get the file name from the end of the URL
  file_name = link.split('/')[-1]
  # Make sure the file name is not empty
  if file_name:
    file_path = os.path.join('pages', file_name)
  else:
    file_path = os.path.join('pages', 'index.html')
  # Check if the file already exists
  if os.path.exists(file_path):
    print('~', end="")
    return
  response = requests.get(link)
  if response.status_code == 200:
    # Save the web page to the specified directory
    with open(file_path, 'w') as f:
      f.write(response.text)
  elif response.status_code == 502:
      print("Uh oh! a server side restriction, perhaps an IP ban.")
  else:
    print(f'Error downloading {link}: {response.status_code}')

# Create a thread pool with 16 threads
with ThreadPoolExecutor(max_workers=16) as executor:
  # Submit a task to download each web page
  for link in links:
    executor.submit(download_page, link)