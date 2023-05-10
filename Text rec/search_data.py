from Regex_name_transformation import regname_1
import regex as re
from difflib import SequenceMatcher

data = {
    "SunfireV60x": "lalalalaal",
    "SunfireV65x": "blablablabla",
    "SparEnterpriseT200": "lililililili",
    "CiscoASR9000Series": "bliblablub"}

def search(name, data):
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        if reObj.match(name):
            print(key, data[key])


search("CiscoASR9000series", data)
'''
def similar(a,b):
    a = regname_1(a)
    print(a)
    b = regname_1(b)
    return SequenceMatcher(None,a,b).ratio()
'''


