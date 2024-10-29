import requests
from bs4 import BeautifulSoup


class WikiReq:
    def __init__(self, link):
        self.req = requests.get(url=link)

    def print_page(self):
        print(self.req.text)


wiki = WikiReq('https://ru.wikipedia.org/wiki/')
wiki.print_page()
