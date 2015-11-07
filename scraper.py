from parser import *
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen

class UrlObj:
    def __init__(self, url, level):
        self.url=url
        self.level=level
def url_extractor(url, page, level):
        parser=HTMLUrlParser()
        parser.feed(page)
        out=[]
        for item in parser.url_list:
            temp=UrlObj(urljoin(url, item), level)
            out.append(temp)
        return out

def get_page(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = str(urlopen(req).read())
    return webpage

def content_extractor():
    pass

def scrape (url, levels, folder):
    parsed_uri = urlparse(url)
    file_name=folder+"/"+parsed_uri.netloc
    index=[]
    index.append(UrlObj(url,1))
    ticket=0
    while not index==[]:
        ticket+=1
        temp=index.pop()
        page=get_page(temp.url)
        if temp.level<levels:
            index=index+url_extractor(url, page, temp.level+1)

