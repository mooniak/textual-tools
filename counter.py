#
# counter.py v0.1.0
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
# Improvements: https://github.com/mooniak/Frequency-Counter
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.
#
# This is a simple Python script to count unicode character frequencies and percentages of a text file. 
# This will genrate a simple html file with the report.
# 
# HOWTO $python3 counter <input file or folder> <log file (optional)>


import collections, sys, unicodedata, os

charCount = 0
charCountNoWhiteSpace = 0
ledgerSingle={}
ledgerDouble={}
ledgerTriple={}
punctuation=[' ',',','"','\'','.','?','!','/',':','-','%','<','>','(',')','`']

def counter(openfile):
    global charCount, charCountNoWhiteSpace
    now=None
    before=None
    earlier=None
    for line in openfile:
        for char in line:
            earlier=before
            before=now
            now=char
            if char in ledgerSingle:
                ledgerSingle[char]+=1
            else:
                ledgerSingle[char]=1
                if now not in punctuation:
                    print(now)

            if not before==None:
                if now not in punctuation and before not in punctuation:
                    if before+now in ledgerDouble:
                        ledgerDouble[before+now]+=1
                    else:
                        ledgerDouble[now+before]=1

            if (not earlier==None) and (not before==None):
                if now not in punctuation and before not in punctuation and earlier not in punctuation:
                    if earlier+before+now in ledgerTriple:
                        ledgerTriple[earlier+before+now]+=1
                    else:
                        ledgerTriple[earlier+before+now]=1

            charCount += 1
            if not char.isspace():
                charCountNoWhiteSpace += 1


def reader(name):
    try:
        if os.path.isdir(name):
            fileList = os.listdir(name)
            for file in fileList:
                # print(file)
                try:
                    f = open(name + "/" + file, encoding='utf-8')
                    counter(f)
                except UnicodeDecodeError:
                    f = open(name + "/" + file, encoding='utf-16')
                    counter(f)
                finally:
                    f.close()
        else:
            try:
                f = open(name, encoding='utf-8')
                counter(f)
            except UnicodeDecodeError:
                f = open(name, encoding='utf-16')
                counter(f)
            finally:
                f.close()
    except IOError:
        print("File read error")


def writer(name, txt):
    try:
        f = open(name, 'w', encoding='utf-8')
        f.write(txt)
    except IOError:
        print("File write error")
    except:
        print("File error")
    finally:
        f.close()


def cruncher(list):
    out = ""
    for item in list:
        char = item[0].split()
        if len(char) != 0:
            s = char[0]
            codep = s.encode("unicode_escape")
            codep=str(codep)[1:].replace('\\','').strip("'")
            out += "<tr><td class='c'>"+s + "</td><td class='u'>" + str(codep) + "</td><td class='u'>" + str(item[1]) + "</td><td class='u'>" + str(
                round(item[1] / charCountNoWhiteSpace * 100, 3)) + "%</td></tr>"
    return out


def printHTML(fileName, outNumbers ):
    global  charCount, charCountNoWhiteSpace
    fileLoc=os.path.abspath(fileName)
    outStr = "<!DOCTYPE html><html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/><title>Text Frequency Report</title><style>body{{font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important;}}h2{{font-size: 48px;}}th{{font-size: large;background: #eee; padding: 10px; border-left: 1px #D8D8D8 solid; font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important;}}td.c{{font-size: 24px; padding: 16px 0px; text-align: center; vertical-align: center;}}td.u{{font-size: large; font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important; text-align: left; background: #F7F7F7; padding-left: 20px; vertical-align: center;}}.report{{text-align: center; float: left; width: 100%; border-collapse: collapse; border: 1px solid #e0e0e0;}}.meta{{text-align: center; float: left; width: 50%; border-collapse: collapse; border: 1px solid #e0e0e0; margin-bottom: 50px;text-align: left;}}</style></head><body><h2>Text Frequency Report</h2><div style='overflow:hidden'><table border='1' class='meta'><tr><th> Source </th><th> <a href='{}'>{}</a> </th><tr><tr><th> spec </th><th> <a href='/'>spec</a> </th><tr><tr><th> Char Count </th><th> {} </th><tr><tr><th> Char Count with spaces </th><th>{} </th><tr></table></div>{}</body></html>".format(fileName, fileLoc, charCount, charCountNoWhiteSpace, outNumbers)
    return outStr


names = sys.argv
if not len(names) > 1:
    print("No input given. format: $python3 counter <input file or folder> <log file (optional)>")
else:
    reader(names[1])
    txtOut="<h3>Singles</h3><div style='margin-bottom: 10px;overflow: hidden;'><table border='1' class='report'><tr><th> සන් / Glyph </th><th> යුනිකේත / Unicode Sequence </th><th> වාර ගණන / Number of occurences </th><th> ප්‍රතිශතය / Percentage </th></tr>"
    txtOut += cruncher(sorted(collections.Counter(ledgerSingle).items(), key=lambda tup: tup[1], reverse=True))
    txtOut +="</table></div><h3>Doubles</h3><div style='margin-bottom: 10px;overflow: hidden;'><table border='1' class='report'><tr><th> සන් / Glyph </th><th> යුනිකේත / Unicode Sequence </th><th> වාර ගණන / Number of occurences </th><th> ප්‍රතිශතය / Percentage </th></tr>"
    txtOut += cruncher(sorted(collections.Counter(ledgerDouble).items(), key=lambda tup: tup[1], reverse=True))
    txtOut +="</table></div><h3>Triples</h3><div style='margin-bottom: 10px;overflow: hidden;'><table border='1' class='report'><tr><th> සන් / Glyph </th><th> යුනිකේත / Unicode Sequence </th><th> වාර ගණන / Number of occurences </th><th> ප්‍රතිශතය / Percentage </th></tr>"
    txtOut += cruncher(sorted(collections.Counter(ledgerTriple).items(), key=lambda tup: tup[1], reverse=True))
    txtOut +="</table></div>"

    print("\nchar count : " + str(charCount) + "\nchar count with no spacers : " + str(
        charCountNoWhiteSpace))
    if len(names) > 2:
        writer(names[2], printHTML(names[1], txtOut))
    else:
        writer("report.html", printHTML(names[1], txtOut))
