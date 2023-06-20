
'''Suchalgorithmen & Vergleichsalgorithmen. Alles was ausgelesen wurde, muss mit der Datenbank verglichen werden,
dafür gibt es mehrere Algorihtmen:
-search(name, data) = Es müssen genau die Buchstaben in genau der Rheinfolge erhalten werden, dann MAtch keine fehlenden Buchstaben erlaubt
-search_more_loop(names, data)= Es müssen die Buchstaben oder ähnliche (Z.B.: o wie e) in genau der Rheinfolge erhalten werden, dann MAtch keine fehlenden Buchstaben erlaubt
-proof_avb(data, p,  res_set ) = Passen die Buchstaben, Rheinfolge egal, überein?  Fehlenden Buchstaben erlaubt je nachdem wieviele fehlen
 '''

from Text.Regex_name_transformation import regname_1, regname_2
import regex as re
from difflib import SequenceMatcher
from Text.Datenbank import read_data

from Text.image_read import text_rec
'''
data = {
XXX
}
'''


def search(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr'''
    # reobj = []
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        # print(reObj)
        if reObj.search(name):
            print("Match found in run1")
            print(key, data[key])
            break
        else:
            for key in data.keys():
                # reObj = re.compile(regname_2(key))
                # print(reObj)
                if reObj.search(name):
                    print("Match found in run2")
                    print(key, data[key])




def search_more(name, data):
    '''Funktion gibt Matches aus wenn rex alle characters enthalten
    oder mehr und missclassified okay'''
    for key in data.keys():
        reObj = re.compile(regname_1(key))
        # print(reObj)
        if reObj.search(name):
            print("Match found in run1")
            return key, data[key]
            break
    for key in data.keys():
        print("No match found in run1, trying run2 (missclassificatins okay)")
        reObj = re.compile(regname_2(key))
        # print(reObj)
        if reObj.search(name):
            return key, data[key]
            break



data = read_data
def search_more_loop(names, data):
    '''
    Funktion geht alle geesenen strings durch und sucht nach einem match in der datei auch mis misclassifieds
    :param names: list of returned strings from mage read
    :param data: datenbank
    :return: match
    '''
    y = []
    for i in range(len(names)):
        name = "".join(names[i])
        for key in data.keys():
            reObj = re.compile(regname_1(key))
            if reObj.search(name):
                y.append([names[i], key, data[key]])
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



def similarity(name):
    '''
    Gibt eine Liste aller chararcter in einer sequenz einzeln aus
    '''
    sequence = []
    #so viele buchstaben müssen übereinstimmen
    for c in range(len(name)):
        sequence.append(name[c])
    return sequence



def proof_avb(data, p, res_set ):
    '''

    :param data: Datenbank in der die devices hinterlegt werden
    :param p: % die übereinstimmen sollen
    :param  res_set: Die ausgelesenen sequenzen welche noch transformiert werden um ausgelesen werden zukönnen
            (Die rückgabe von text_rec =  res_set)
    :return:
    '''
    result = []
    for i in range(len(res_set)):
       seq = similarity(res_set[i].lower())
       for d in data.keys():
            perc = len(d) * p  # p muss in 0.xx angegeben werden
            ref_d = similarity(d.lower())
            counter = 0
            for c in seq:
                if c in ref_d:
                    counter += 1
                    del ref_d[ref_d.index(c)]
                #print(ref_d)
            if counter > perc:
                #xxx% aud d sind in seq enthalten
                print(f" {d} in {seq} passen zu {(counter/len(d))*100}% {counter}übereinstimmungen, {perc} =perc")
                result.append(seq)
    #result = [set(result)]
    return result
            #else:
                #print(f"Die Wörter {d} und {seq} passen zu {(counter/len(d))*100}% {counter}übereinstimmungen")
                #return False

