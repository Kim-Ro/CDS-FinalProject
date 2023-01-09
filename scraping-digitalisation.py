import re
import requests
import os
from bs4 import BeautifulSoup

# creating a list of links, where each item of the list represents a new page of the search results
linklist = [
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_search_result_summary_SearchResultSummaryPortlet_INSTANCE_Ja6zoyQuPn9a&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278273344&&facet.language=ENG&language=en&resultsPerPage=50',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278273964&&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=51&QUERY_ID=278273964',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278273988&&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=101&QUERY_ID=278273988',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278273999&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=151&QUERY_ID=278273999',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274105&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=201&QUERY_ID=278274105',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274115&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=251&QUERY_ID=278274115',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274125&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=301&QUERY_ID=278274125',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274136&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=351&QUERY_ID=278274136',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274145&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=401&QUERY_ID=278274145',
    'https://op.europa.eu/en/search-results?p_p_id=eu_europa_publications_portlet_pagination_PaginationPortlet_INSTANCE_gDBsAazqs5X2&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&queryText=digitalisation&keywordOptions=ALL&facet.documentFormat=PDF&facet.language=ENG&facet.collection=EUPub&facet.collection=EUDir&facet.collection=EULex&facet.collection=EUWebPage&facet.collection=EUSummariesOfLegislation&sortBy=RELEVANCE-DESC&SEARCH_TYPE=ADVANCED&QUERY_ID=278274156&&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&facet.language=ENG&language=en&resultsPerPage=50&startRow=451&QUERY_ID=278274156'
]

# scraping the PDF-download links from the search pages by looping over the list of links
ugly_links = []
for link in linklist:
    url = link
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, features="html.parser")
    get_pdf_links = soup.findAll("a",
                                 {"data-format": "PDF"})  # making sure it only downloads .pdf files and not .doc files
    ugly_links = ugly_links + get_pdf_links

# looping over the ugly_links list to extract the url that is hidden as an uri
document_links = []
for item in ugly_links:
    uri = item.get("data-uri")
    amp_url = "https://op.europa.eu" + uri
    url = re.sub('amp;', '', amp_url)  # removing 'amp;' from the link that is added in scraping
    document_links.append(url)

# downloading PDF files to data folder

def download_file(url, folder, count):
    name = str(count)
    local_filename = name
    path = os.path.join(folder + "/" + local_filename)
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            f.write(r.content)
    return local_filename


count = 1
for item in document_links:
    url = item
    folder = "/Users/kimrothe/CDS-FinalProject/data-digitalisation"
    download_file(url, folder, count)
    count +=1
