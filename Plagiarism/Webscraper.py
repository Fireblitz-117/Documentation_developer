from bs4 import BeautifulSoup
import urllib3

def web_scraper(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data.decode('utf-8'))
    body = soup.find_all("body")
    return body

def web_scraper_multiple():
    body1 = web_scraper('http://olympus.realpython.org/profiles/poseidon')
    body2 = web_scraper('http://info.cern.ch/')
    body3 = web_scraper('http://relaxedfreshbeautifulsecret.neverssl.com/online')
    body4 = web_scraper('http://olympus.realpython.org/profiles/poseidon')
    return body1+body2+body3+body4
    

web_scraper_multiple()