# rare-diseases-data-scraping

`data1.csv` is the currently incomplete detailed description about the diseases.

## File and their purpose
----
|File|Purpose|
|--|--|
`links.md` | linksof interest
`disease_links_scraper.py` | extracts the big list from https://rarediseases.info.nih.gov/diseases.
`disease_links.csv` | data extracted using the above script
`scrape_specific_page.ipynb` | Scrapes a given page for disease details
`reqmul.py` | Requests with multithreading - made to save all the 5910 pages offline as HTML for easy scraping later.

## Contents of `pages` folder

This directory contains all the files, the links for which were already scraped and are included in `disease_links.csv`. The naming convention is just the part after the last `/` in the corresponding url.
