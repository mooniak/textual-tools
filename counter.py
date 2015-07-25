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
                f = open(name+"/"+file, encoding='utf-8')
                reader(f)
        else:
            f = open(name, encoding='utf-8')
            reader(f)
    except IOError:
        print ("File read error")
    except:
        print ("File error")

    return sorted(collections.Counter(list).items())


def writer(name, txt):
    try:
        f = open(name, 'w')
        f.write(txt)
    except IOError:
        print ("File write error")
    except:
        print ("File error")
    finally:
        f.close()


def cruncher(list):
    out = ""
    for item in list:
        try:
            char = item[0].split()
            if len(char) != 0:
                s = char[0]
                codep = s.encode("unicode_escape")
                out += str(codep) + " " + unicodedata.name(item[0]) + " " + str(item[1]) + " " + str(
                    round(item[1] / charCountNoWhiteSpace * 100, 3)) + "%\n"
        except:
            out += item[0] + " " + str(item[1]) + "\n"
    return out


names = sys.argv
if not len(names) > 1:
    print ("No input given. format: $python3 counter <input file or folder> <log file (optional)>")
else:
    txtOut = cruncher(counter(names[1])) + "\nchar count : " + str(charCount) + "\nchar count with no spacers : " + str(
        charCountNoWhiteSpace)
    print(txtOut)
    if len(names) > 2:
        writer(names[2], txtOut)
