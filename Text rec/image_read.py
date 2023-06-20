from Text.Pic_edit import canny, get_grayscale
import pytesseract
import cv2
import matplotlib as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Paulina.Heine\AppData\Local\Tesseract-OCR\tesseract.exe"
X
X
X
X
X
def read_picture(pfad):
    img = cv2.imread(pfad)
    img_grey = get_grayscale(img)
    img_canny = canny(img_grey)
    images = [img_grey, img_canny]
    configs = [r'--oem 3 --psm 6', r'--psm 4', r"--psm 11 --oem 3"]

    return images, configs



def text_rec(images, configs):
    '''
    Bilder mit versch. Bearbeitungen werden mit versch. configurationen ausgelesen
    ,anschließendwird gefiltert, so dass keine Sonderzeichen und zu kurze Fragmente ausgegeben werden.
    '''
    res_set = set()

    for con in configs:
        print("loading")
        for i in images:
            print("...loading...")
            # Alle sinnvollen Einstellungen werden durchprobiert
            # print("read")
            res_list = pytesseract.image_to_string(i, config=con)
            # Alle Einträge werden in einzelne snippets unterteilt
            # print("split")
            res_list_2 = res_list.split("\n")
            # Alle leeren Einträge werden entfernt
            # print("blanks")
            while '' in res_list_2:
                res_list_2.remove('')
            # print("isalnum")
            # Sonderzeichen entfernen
            for x in range(len(res_list_2)):
                res_set.add(''.join(filter(str.isalnum, res_list_2[x])))

    # Alle Einträge mit weniger als 3 Einträgen werden entferht
    # print("charlimit")
    res_set = list(filter(lambda el: len(el) > 3, res_set))
    res_set = list(filter(lambda el: len(el) < 30, res_set))
    print("done")
    res_set = sorted(res_set)
    print(f"We have {len(res_set)}entries")
    return res_set

#res_set = text_rec(images, configs)

