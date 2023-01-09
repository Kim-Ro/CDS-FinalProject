# CDS-FinalProject
The repository for the final project (exam) of the Cultural Data Science at Aarhus University in the winter semester 2022/23

**Project title:** Exploring the sentiment of digitalisation in the EU climate debate

**Project description:** In this project the sentiment of digitalisation in the EU climate debate is explored. First, a digitalisation vocabulary is generated half automatically by scraping EU publications on digitalisation and looking for the most used words and half manually by choosing the digitalisation related words from the results. This vocabulary is then used to identify the relevant pages of the 1000 most recent publications of the EU publications office on the topic of environment. These pages are then analysed in sentiment to test the hypothesis that digitalisation is seen as a solution rather than a risk for the climate crisis in the EU climate debate. The output of the code and the result of this project may differ as the scraping is programmed to use the most recent publications. For reproducability the code of "Scraping-digitalisation.py" and "Scraping-environment.py" has to be altered by replaing the scraping links with links from a search limiting the results shown to the date mentioned in this file under the corresponding filename.

## Scraping-digitalisation.py
This file contains the python code used for the scraping of the publications that are a result of a search on digitalisation, filtered by results in English and with a PDF as a format.
Executed on 05/01/2023 for the project.

## Scraping-environment.py
This file contains the python code used for the scraping of the publications on the topic of environment by the [EU publications office](https://op.europa.eu/en/home). The results of the EU publications database were filtered by English as a language and PDF as the format.
Executed on 20/12/2022 for the project.

## data-digitalisation
This folder contains the scraped PDF's from the 05/01/2023.

## data-environment
This folder contains the scraped PDF's from the 20/12/2022.

