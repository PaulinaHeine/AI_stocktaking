'''
Funktion die aus Namen Rexgex slices macht. Z.B.: Sun -> (?i).*s.*u.*n.*
'''

import regex as re

digits = {0: ["O","o"], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
characters = {"a": ["a","o","r"], #A
              "b": ["b","L","R"], #B
              "c": ["c","L"],
              "d": ["d","l","B","R"],
              "e": ["e","a","r"],
              "f": ["f","R","r","I"],
              "g": ["g"],
              "h": ["h"],
              "i": ["i"],
              "j": ["j"],
              "k": ["k"],
              "l": ["l"],
              "m": ["m"],
              "n": ["n"],
              "o": ["o"],
              "p": ["p"],
              "q": ["q"],
              "r": ["r","F"],
              "s": ["s"],
              "t": ["t"],
              "u": ["u"],
              "v": ["v"],
              "w": ["w"],
              "x": ["x"],
              "y": ["y"],
              "z": ["z"],}

def regname_1(name):
    '''
    Function that returns the devicename in Regex form
    :param name: Input device name
    :return: device name in regex form as a rexex type
    '''
    rex = ["(?i).*"]
    splitted = re.findall(".", name)
    for c in range(len(splitted)):
        rex.append(splitted[c])
        rex.append(".*")
    rex = "".join(rex)
    return rex

def regname_2(name):
    '''
    Function that returns the devicename in Regex form with multiple possibilities for missclassified caracters
    :param name: Input device name
    :return: device name in regex form as a rexex type
    '''
    rex = ["(?i).*"]
    splitted = re.findall(".", name)
    for c in range(len(splitted)):
        for i in characters.keys():
            if str(i).upper() == splitted[c].upper():
                rex.extend(f"{characters[i]}")
        rex.append(".*")

    #for x in range(len(rex)):
    #    rex[x] = "".join(rex[x])
    rex = "".join(rex)
    rex = re.compile(rex)
    return rex


