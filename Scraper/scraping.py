import json
import requests

from bs4 import BeautifulSoup


class Scraper:

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    def scrape(self, url):
        s = requests.session()
        page = s.get(url, headers=Scraper.headers)
        soup = BeautifulSoup(page.text, "lxml")
        if 'www.myntra.com' in url:
            price = json.loads(soup.find_all('script')[1].string)[
                'offers']['price']
            return int(price)
        elif 'www.ajio.com' in url:
            price = json.loads(soup.find_all('script')[6].string)[
                'offers']['price']
            return int(price)
        else:
            raise Exception('URL is invalid')
