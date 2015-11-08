from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen
import os

from hparser import HTMLUrlParser, HTMLDataParser
from fileOps import writer


class UrlObj:
    def __init__(self, url, level):
        self.url = url
        self.level = level


url_keeper = []


def url_extractor(url, page, level):
    p = HTMLUrlParser()
    p.feed(page)
    out = []
    for item in p.url_list:
        if "#" in item:
            turl = item[0:item.index('#')]
        else:
            turl = item
        turl = urljoin(url, turl)
        parsed_turl = urlparse(turl)
        parsed_base = urlparse(url_keeper[0])
        if turl not in url_keeper and parsed_turl.netloc == parsed_base.netloc:
            url_keeper.append(turl)
            temp = UrlObj(turl, level)
            out.append(temp)
    return out


def get_page(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req)
        encoding = response.headers.get_content_charset()
        return response.read().decode(encoding)
    except:
        print("Could not get " + url)
        return ""


def content_extractor():
    pass


def scrape(url, levels, folder=None):
    global url_keeper
    parsed_uri = urlparse(url)

    if folder == None:
        folder = os.getcwd() + "/" + parsed_uri.netloc
        os.mkdir(folder)

    file_name = folder + "/" + parsed_uri.netloc
    url_keeper = []
    index = []
    url_keeper.append(url)
    index.append(UrlObj(url, 1))
    ticket = 0
    while not index == []:
        ticket += 1
        temp = index.pop()
        page = get_page(temp.url)
        if not page == "":
            p = HTMLDataParser()
            p.feed(page)
            writer(file_name + "_" + str(temp.level) + "_" + str(ticket) + ".txt", p.page)
            if temp.level < levels:
                index = index + url_extractor(url, page, temp.level + 1)


scrape("http://mooniak.com/ayanna-font/tests/", 2)