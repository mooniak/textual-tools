#
# hparser.py
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
# Improvements: https://github.com/mooniak/textual-tools
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

from html.parser import HTMLParser


class HTMLDataParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.page = ""

    def handle_data(self, data):
        if not self.lasttag == "script" and not self.lasttag == "style":
            data = str(data).strip()
            if not data == '\n' and not data == "b'":
                self.page += data + "\n"


class HTMLUrlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url_list = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.url_list.append(attrs[0][1])