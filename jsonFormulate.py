#
# jsonFormulate.py
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
# Improvements: https://github.com/mooniak/textual-tools
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

import json


class CharObj:
    def __init__(self, character, count):
        self.character = character
        self.count = count


def json_formulate(counter):
    ledgerSingle = []
    ledgerDouble = []
    ledgerTriple = []
    for key, val in counter.ledgerSingle.items():
        ledgerSingle.append(CharObj(key, val).__dict__)
    for key, val in counter.ledgerDouble.items():
        ledgerDouble.append(CharObj(key, val).__dict__)
    for key, val in counter.ledgerTriple.items():
        ledgerTriple.append(CharObj(key, val).__dict__)

    ledgerSingle = sorted(ledgerSingle, key=lambda x: x['count'], reverse=True)
    ledgerDouble = sorted(ledgerDouble, key=lambda x: x['count'], reverse=True)
    ledgerTriple = sorted(ledgerTriple, key=lambda x: x['count'], reverse=True)

    out = {}
    out['ledgerSingle'] = ledgerSingle
    out['ledgerDouble'] = ledgerDouble
    out['ledgerTriple'] = ledgerTriple
    out['charCount'] = counter.charCount
    out['charCountNoWhiteSpace'] = counter.charCountNoWhiteSpace
    out['wordCount'] = counter.wordCount
    out['unicodeRange'] = counter.unicodeRange
    out['name'] = counter.name
    out['source'] = counter.source

    return "textReport(" + json.dumps(out, ensure_ascii=False) + ")"
