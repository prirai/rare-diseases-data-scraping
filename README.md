# rare-diseases-data-scraping

Data scraped from - https://rarediseases.info.nih.gov

`data1.csv` is the currently incomplete detailed description about the diseases.

## File and their purpose
----
|File|Purpose|
|--|--|
`links.md` | links of interest
`disease_links_scraper.py` | extracts the big list from https://rarediseases.info.nih.gov/diseases.
`disease_links.csv` | data extracted using the above script
`scrape_specific_page.ipynb` | Scrapes a given page for disease details (names, symptoms and causes).
`reqmul.py` | Requests with multithreading - made to save all the 5910 pages offline as HTML for easy scraping later.

## Contents of `pages` folder

This directory contains all the files, the links for which were already scraped and are included in `disease_links.csv`. The naming convention is just the part after the last `/` in the corresponding url.
`reqmul.py` checks from previously downloaded files and doesn't overwrite. Current script allows somewhere around 700 pages after which it gets a server restriction. The previous versions were even worse and could only get 100 to max 200 at a time and that too in a long time. wget, axel, aria2, selenium have been already tried.

Scraped Disease at a glance section, people affected,  symptoms, categories, ages and causes for all diseases using the offline HTML pages (code in `page_details_extractor-offline.ipynb`). They are saved in the `disease_details.csv` file.
