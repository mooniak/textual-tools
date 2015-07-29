import collections, sys, unicodedata, os

charCount = 0
charCountNoWhiteSpace = 0
list = []


def reader(openfile):
    global charCount, charCountNoWhiteSpace
    for line in openfile:
        for char in line:
            list.append(char)
            charCount += 1
            if not char.isspace():
                charCountNoWhiteSpace += 1


def counter(name):
    try:
        if os.path.isdir(name):
            fileList = os.listdir(name)
            for file in fileList:
                f = open(name + "/" + file, encoding='utf-8')
                reader(f)
        else:
            f = open(name, encoding='utf-8')
            reader(f)
    except IOError:
        print("File read error")
    except:
        print("File error")

    return sorted(collections.Counter(list).items(), key=lambda tup: tup[1], reverse=True)


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


def cruncher(list1):
    out = ""
    for item in list1:
        try:
            char = item[0].split()
            if len(char) != 0:
                s = char[0]
                codep = s.encode("unicode_escape")
                codep=str(codep)[1:].replace('\\','').strip("'")
                print(str(codep) + " " + str(item[1]) + " " + str(
                    round(item[1] / charCountNoWhiteSpace * 100, 3)) + "%")
                out += "<tr><td class='c'>"+s + "</td><td class='u'>" + str(codep) + "</td><td class='u'>" + str(item[1]) + "</td><td class='u'>" + str(
                    round(item[1] / charCountNoWhiteSpace * 100, 3)) + "%</td></tr>"
        except:
            out += item[0] + " " + str(item[1]) + "\n"
    return out


def printHTML(outFilename, fileName, outNumbers ):
    global  charCount, charCountNoWhiteSpace
    fileLoc=os.path.abspath(fileName)
    outStr = "<!DOCTYPE html><html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/><title>Text Frequency Report</title><style>body{{font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important;}}h2{{font-size: 48px;}}th{{font-size: large;background: #eee; padding: 10px; border-left: 1px #D8D8D8 solid; font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important;}}td.c{{font-size: 24px; padding: 16px 0px; text-align: center; vertical-align: center;}}td.u{{font-size: large; font-family: 'Inconsolata', Lucida Console, Monaco, monospace !important; text-align: left; background: #F7F7F7; padding-left: 20px; vertical-align: center;}}.report{{text-align: center; float: left; width: 100%; border-collapse: collapse; border: 1px solid #e0e0e0;}}.meta{{text-align: center; float: left; width: 50%; border-collapse: collapse; border: 1px solid #e0e0e0; margin-bottom: 50px;text-align: left;}}</style></head><body><h2>Text Frequency Report</h2><div><table border='1' class='meta'><tr><th> Source </th><th> <a href='{}'>{}</a> </th><tr><tr><th> spec </th><th> <a href='/'>spec</a> </th><tr><tr><th> Char Count </th><th> {} </th><tr><tr><th> Char Count with spaces </th><th>{} </th><tr></table></div><div><table border='1' class='report'><tr><th> සන් / Glyph </th><th> යුනිකේත / Unicode Sequence </th><th> වාර ගණන / Number of occurences </th><th> ප්‍රතිශතය / Percentage </th></tr>{}</table></div></body></html>".format(fileName, fileLoc, charCount, charCountNoWhiteSpace, outNumbers)
    return outStr


names = sys.argv
if not len(names) > 1:
    print("No input given. format: $python3 counter <input file or folder> <log file (optional)>")
else:
    txtOut = cruncher(counter(names[1]))
    print("\nchar count : " + str(charCount) + "\nchar count with no spacers : " + str(
        charCountNoWhiteSpace))
    if len(names) > 2:
        writer(names[2], printHTML(names[2], names[1], txtOut))
