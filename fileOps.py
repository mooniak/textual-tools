#
# fileOps.py
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
# Improvements: https://github.com/mooniak/textual-tools
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

import os


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


def folder_reader(name):
    if os.path.isdir(name):
        fileList = os.listdir(name)
        return fileList
    else:
        return None
