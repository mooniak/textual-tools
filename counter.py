#
# counter.py v2.0.0
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
# Improvements: https://github.com/mooniak/Frequency-Counter
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.
import os


class Counter:
    punctuation = [' ', ',', '"', '\'', '.', '?', '!', '/', ':', '-', '%', '<', '>', '(', ')', '`']

    def __init__(self, unicodeRange=0):
        self.charCount = 0
        self.charCountNoWhiteSpace = 0
        self.ledgerSingle = {}
        self.ledgerDouble = {}
        self.ledgerTriple = {}
        self.unicodeRange = unicodeRange

    def count_characters(self, openfile):
        now = None
        before = None
        earlier = None
        for line in openfile:
            for char in line:
                earlier = before
                before = now
                now = char
                if char in self.ledgerSingle:
                    self.ledgerSingle[char] += 1
                else:
                    self.ledgerSingle[char] = 1
                    if now not in self.punctuation:
                        print(now)

                if not before == None:
                    if now not in self.punctuation and before not in self.punctuation:
                        if before + now in self.ledgerDouble:
                            self.ledgerDouble[before + now] += 1
                        else:
                            self.ledgerDouble[now + before] = 1

                if (not earlier == None) and (not before == None):
                    if now not in self.punctuation and before not in self.punctuation and earlier not in self.punctuation:
                        if earlier + before + now in self.ledgerTriple:
                            self.ledgerTriple[earlier + before + now] += 1
                        else:
                            self.ledgerTriple[earlier + before + now] = 1

                self.charCount += 1
                if not char.isspace():
                    self.charCountNoWhiteSpace += 1

    def count(self, name):
        try:
            if os.path.isdir(name):
                fileList = os.listdir(name)
                for file in fileList:
                    # print(file)
                    try:
                        f = open(name + "/" + file, encoding='utf-8')
                        self.count_characters(f)
                    except UnicodeDecodeError:
                        f = open(name + "/" + file, encoding='utf-16')
                        self.count_characters(f)
                    finally:
                        f.close()
            else:
                try:
                    f = open(name, encoding='utf-8')
                    self.count_characters(f)
                except UnicodeDecodeError:
                    f = open(name, encoding='utf-16')
                    self.count_characters(f)
                finally:
                    f.close()
        except IOError:
            print("File read error")

