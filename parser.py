from html.parser import HTMLParser

class HTMLDataParser(HTMLParser):
    pass

class HTMLUrlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url_list=[]
    def handle_starttag(self, tag, attrs):
        if tag=="a":
            self.url_list.append(attrs[0][1])
