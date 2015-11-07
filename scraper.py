from hparser import HTMLUrlParser
from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen

class UrlObj:
    def __init__(self, url, level):
        self.url=url
        self.level=level

url_keeper=[]

def url_extractor(url, page, level):
    p= HTMLUrlParser()
    p.feed(page)
    out=[]
    for item in p.url_list:
        if "#" in item:
            turl=item[0:item.index('#')]
        else:
            turl=item
        turl=urljoin(url, turl)
        parsed_turl = urlparse(turl)
        parsed_base=urlparse(url_keeper[0])
        print(turl)
        if turl not in url_keeper and parsed_turl.netloc==parsed_base.netloc:
            url_keeper.append(turl)
            temp=UrlObj(turl, level)
            out.append(temp)
    return out

def get_page(url):
    print(url)
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = str(urlopen(req).read())
        return webpage
    except:
        print("Could not get "+url)
        return ""

def content_extractor():
    pass

def scrape (url, levels, folder):
    global url_keeper
    parsed_uri = urlparse(url)
    file_name=folder+"/"+parsed_uri.netloc
    url_keeper=[]
    index=[]
    url_keeper.append(url)
    index.append(UrlObj(url,1))
    ticket=0
    while not index==[]:
        ticket+=1
        temp=index.pop()
        page=get_page(temp.url)
        if not page=="":
            if temp.level<levels:
                index=index+url_extractor(url, page, temp.level+1)


