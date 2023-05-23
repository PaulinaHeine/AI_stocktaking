from Regex_name_transformation import regname_1, regname_2
import regex as re
from difflib import SequenceMatcher

from Text.image_read import text_rec, images, configs

data = {
    "SunfireV60x": "lalalalaal",
    "SunfireV65x": "blablablabla",
    "SparcEnterpriseT200": "lililililili",
    "CiscoASR9000Series": "bliblablub",
    "SunFireX4100":"nananananan"}



def search(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr'''
    #reobj = []
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        #print(reObj)
        if reObj.search(name):
            print("Match found in run1")
            print(key, data[key])
            break
        else:
            for key in data.keys():
                #reObj = re.compile(regname_2(key))
                #print(reObj)
                if reObj.search(name):
                    print("Match found in run2")
                    print(key, data[key])


#search("CiscoASR9000series", data)


def search_more(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr und missclassified okay'''
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        #print(reObj)
        if reObj.search(name):
            print("Match found in run1")
            return key, data[key]
            break
    for key in data.keys():
        print("No match found in run1, trying run2 (missclassificatins okay)")
        reObj = re.compile(regname_2(key))
        #print(reObj)
        if reObj.search(name):
            return key, data[key]
            break


search_more("CiseoASR9000Series", data)


def search_more_loop(names,data):
    '''
    Funktion geht alle geesenen strings durch und sucht nach einem match in der datei
    :param names: list of returned strings from mage read
    :param data: datenbank
    :return: match
    '''
    y = []
    for i in range(len(names)):
        name = names[i]
        for key in data.keys():
            reObj = re.compile(regname_1(key))
            if reObj.search(name):
                y.append([names[i],key, data[key]])
                print(f"MATCH FOUND FOR {name}")
                break
            pass
            if not reObj.search(name):
                for key in data.keys():
                    reObj = re.compile(regname_2(key))
                    if reObj.search(name):
                        y.append([names[i], key, data[key]])
                        print(f"MATCH FOUND FOR {name}")
                        break
                    break
                pass

    return y

y=search_more_loop(x,data)


y=search_more_loop(names=text_rec(images, configs),data=data)

