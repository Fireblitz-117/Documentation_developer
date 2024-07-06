#https://docs.python.org/2/library/p.html
from cdifflib import CSequenceMatcher
from Webscraper import web_scraper_multiple

def plagiarism_checker(content):
    file1= open("/Users/aaron.v/Documents/DocumentationDeveloper/Plagiarism/text.txt", "r")
    file1data=file1.read()
    websitedata = web_scraper_multiple()
    comparingsample = file1data+str(websitedata)
    similarity=CSequenceMatcher(None, content, comparingsample).ratio()
    return(similarity*100)