# Russian helper package

EN_TO_RU = {"A":"А",
            "B":"Б",
            "C":"К", # tricky letter
            "D":"Д",
            "E":"Э", # two options
            "F":"Ф",
            "G":"Г",
            "H":"Х",
            "I":"И",
            "J":"Ж", # ?
            "K":"К",
            "L":"Л",
            "M":"М",
            "N":"Н",
            "O":"О",
            "P":"П",
            "Q":"К", # ?
            "R":"Р",
            "S":"С",
            "T":"Т",
            "U":"У",
            "V":"В",
            "W":"В", # closest
            "X":"КС", # should be fine
            "Y":"Й",
            "Z":"З",
            "a":"а",
            "b":"б",
            "c":"к",
            "d":"д",
            "e":"э",
            "f":"ф",
            "g":"г",
            "h":"х",
            "i":"и",
            "j":"ж",
            "k":"к",
            "l":"л",
            "m":"м",
            "n":"н",
            "o":"о",
            "p":"п",
            "q":"к",
            "r":"р",
            "s":"с",
            "t":"т",
            "u":"у",
            "v":"в",
            "w":"в",
            "x":"кс",
            "y":"й",
            "z":"з",}

def cyrillicizeEnglish(instring):
    result = ""
    for chr in instring:
        if chr in EN_TO_RU:
            result += EN_TO_RU[chr]
        else:
            result += chr
    return result

# Ё ё Yo yo
# Ю ю Yu yu
# Я я Ya ya
# Ф ф Ph ph
# Х х Kh kh
# Ж ж Zh zh
# Ц ц Ts ts
# Ч ч Ch ch
# Ш ш Sh sh
# Щ щ Shch shch
# Ы ы Ih ih
# Ъ ъ hard sign not implemented
# Ь ь soft sign not implemented
# th, ce/ci, ge/gi
