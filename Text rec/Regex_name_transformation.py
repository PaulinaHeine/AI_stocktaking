'''
Funktion die aus Namen Rexgex slices macht. Z.B.: Sun -> (?i).*s.*u.*n.*
'''

import regex as re

digits = {0: ["O","o"], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

def regname_1(name):
    '''
    Function that returns the devicename in Regex form
    :param name: Input device name
    :return: device name in regex form
    '''
    rex = ["(?i).*"]
    splitted = re.findall(".", name)
    for c in range(len(splitted)):
        rex.append(splitted[c])
        rex.append(".*")
    rex = "".join(rex)

    return rex
