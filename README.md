# CDS-FinalProject
The repository for the final project (exam) of the Cultural Data Science at Aarhus University in the winter semester 2022/23

**Project title:** The recognition of digitalization as a driver for climate change in EU politics

**Project description:** In this project the recognition of digitalization as a driver for climate change in EU politics is analyzed by comparing how much it is mentioned in recent Eu publications to it's calculated impact of 4.2%. To achieve a representation of the current recognition, the 100 most recent Eu publications on the topic of the environment will be scraped from the website of the EU publications office. Text mining for a digitalization related vocabulary combined with a sentiment analysis will determine how much recognition of digitalization there is in the current climate debate.

## Scraping.py
This file contains the python code used for the scraping of the publications on the topic of environment by the [EU publications office](https://op.europa.eu/en/home).

**current problem:** my code is scraping the download url's to all papers, however, copied and pasted in the address line of a browser, they don't work. If i copied the uri from the html-code of the website, manually type "https//:op.europe.eu" in the address lline and paste the uri, it results in a download of the paper. The output url of the code matches exactly the result of the manual way, except for the fact that one url works and the other doesnt.

**general question:** is it possible to scrape pdf documents from their download links, or does it have to be an online access url of the document ending in ":pdf"?
