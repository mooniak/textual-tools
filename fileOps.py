def writer(name, txt):
    try:
        f = open(name, 'w', encoding='utf-8')
        f.write(txt)
    except IOError:
        print("File write error")
    except:
        print("File error")
    finally:
        try:
            f.close()
        except:
            pass