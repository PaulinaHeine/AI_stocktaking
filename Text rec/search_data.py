from Regex_name_transformation import regname_1, regname_2
import regex as re
from difflib import SequenceMatcher

data = {
    "SunfireV60x": "lalalalaal",
    "SunfireV65x": "blablablabla",
    "SparEnterpriseT200": "lililililili",
    "CiscoASR9000Series": "bliblablub"}

def search(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr'''
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        print(reObj)
        if reObj.search(name):
            print(key, data[key])


search("CiscoASR9000series", data)

def search(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr'''
    for key in data.keys():
        reObj = re.compile(regname_2(key))
        print(reObj)
        if reObj.search(name):
            print(key, data[key])


search("CiscoASR9000series", data)


'''
def similar(a,b):
    a = regname_1(a)
    print(a)
    b = regname_1(b)
    print(b)
    return SequenceMatcher(None,a,b).ratio()


def sim(text,key):
    a = re.compile(regname_1(text))
    b = re.compile(regname_1(key))
    re.search(pattern, string, flags=0)

def search(name, data):
    name = re.compile(regname_1(name))
    for key in data.keys():
        #reObj = re.compile(regname_1(key))
        if re.split(name, key):
            print(key, data[key])


'''