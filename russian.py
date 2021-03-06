# Russian helper package

EN_TO_RU = {"A":"А",
            "B":"Б",
            "C":"К", # tricky letter
            "D":"Д",
            "E":"Е", # Ээ is just uncommon
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
            "e":"е",
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
            "z":"з",
            "'":"ь",
            "Ya":"Я",
            "Ye":"Е",
            "Yi":"И",
            "Yo":"Ё",
            "Yu":"Ю",
            "ya":"я",
            "ye":"е",
            "yi":"и",
            "yo":"ё",
            "yu":"ю"}

def cyrillicizeEnglish(instring):
    result = []
    c = 0
    while c < len(instring):
        chr = instring[c]
        #print(str(c) + "" + chr) # debug statement
        if not chr in EN_TO_RU:
            result.append(chr)
        elif chr == "'":
            prev = instring[c - 1].lower()
            if instring[c - 2:c].lower() == "ts":
                prev = "ц"
            next = chr
            if c < len(instring) - 1:
                next = instring[c + 1]
            result.append(hardsoft(prev, next))
        elif chr.lower() == "y":
            vowels = {"a", "e", "i", "o", "u"}
            if c == len(instring) - 1 or instring[c + 1].lower() not in vowels:
                if len(instring) > 1 and instring[c - 1].lower() in vowels:
                    result.append(EN_TO_RU[chr])
                else:
                    if chr.isupper():
                        result.append("И")
                    else:
                        result.append("и")
                c -= 1
            elif instring[c + 1].lower() == "a":
                result.append(EN_TO_RU[chr + "a"])
            elif instring[c + 1].lower() == "e":
                result.append(EN_TO_RU[chr + "e"])
            elif instring[c + 1].lower() == "i":
                result.append(EN_TO_RU[chr + "i"])
            elif instring[c + 1].lower() == "o":
                result.append(EN_TO_RU[chr + "o"])
            elif instring[c + 1].lower() == "u":
                result.append(EN_TO_RU[chr + "u"])
            c += 1
        elif chr.lower() == "h":
            if c == 0:
                result.append(EN_TO_RU[chr])
            elif instring[c - 1].lower() == "t":
                c += 1
                continue
            elif instring[c - 1] == "C":
                result.pop()
                result.append("Ч")
            elif instring[c - 1] == "c":
                result.pop()
                result.append("ч")
            elif instring[c - 1] == "I":
                result.pop()
                result.append("Ы")
            elif instring[c - 1] == "i":
                result.pop()
                result.append("ы")
            elif instring[c - 1] == "K":
                result.pop()
                result.append("Х")
            elif instring[c - 1] == "k":
                result.pop()
                result.append("х")
            elif instring[c - 1] == "P":
                result.pop()
                result.append("Ф")
            elif instring[c - 1] == "p":
                result.pop()
                result.append("ф")
            elif instring[c - 1] == "S":
                result.pop()
                result.append("Ш")
            elif instring[c - 1] == "s":
                result.pop()
                result.append("ш")
            elif instring[c - 1] == "Z":
                result.pop()
                result.append("Ж")
            elif instring[c - 1] == "z":
                result.pop()
                result.append("ж")
            else:
                result.append(EN_TO_RU[chr])
        elif chr.lower() == "c":
            softs = {"e", "i"}
            if c < len(instring) - 1 and instring[c + 1].lower() in softs:
                if chr.isupper():
                    result.append("С")
                else:
                    result.append("с")
            else:
                result.append(EN_TO_RU[chr])
        elif chr.lower() == "g":
            softs = {"e", "i"}
            if c < len(instring) - 1 and instring[c + 1].lower() in softs:
                if chr.isupper():
                    result.append("Ж")
                else:
                    result.append("ж")
            elif c > 0 and instring[c - 1].lower() == "d":
                if chr.isupper():
                    result.append("Ж")
                else:
                    result.append("ж")
            else:
                result.append(EN_TO_RU[chr])
        elif len(instring) - c > 3 and instring[c:c + 4].lower() == "shch":
            if chr.isupper():
                result.append("Щ")
            else:
                result.append("щ")
            c += 3
        elif len(instring) - c > 1 and instring[c:c + 2].lower() == "ee":
            if chr.isupper():
                result.append("И")
            else:
                result.append("и")
            c += 1
        elif len(instring) - c > 1 and instring[c:c + 2].lower() == "oo":
            if chr.isupper():
                result.append("У")
            else:
                result.append("у")
            c += 1
        elif len(instring) - c > 1 and instring[c:c + 2].lower() == "ts":
            if chr.isupper():
                result.append("Ц")
            else:
                result.append("ц")
            c += 1
        elif len(instring) - c > 1 and instring[c:c + 2].lower() == "qu":
            if chr.isupper():
                result.append("Кв")
            else:
                result.append("кв")
        else:
            result.append(EN_TO_RU[chr])
        c += 1
    return "".join(result)

def hardsoft(prev, thus):
    defineds = {"j", "h", "y", "ц"}
    hards = {"А", "Э", "Ы", "О", "У", "а", "э", "ы", "о", "у"}
    softs = {"Я", "Е", "И", "Ё", "Ю", "я", "е", "и", "ё", "ю"}
    result = "ь"
    if prev in defineds:
        result = "ь" #maybe not? idk
    elif thus in hards:
        result = "ь"
    elif thus in softs:
        result = "ъ"
    if prev.isupper():
        result = result.upper()
    return result


def cyrillicContent(instring):
    cyrset = set("ёъяшертыуиопющэасдфгчйкльжзхцвбнм")
    counter = 0.0;
    for chr in instring.lower():
        if chr in cyrset:
            counter += 1
    return counter / len(instring)

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
# Ъ ъ hard sign not implemented or '?
# Ь ь soft sign not implemented or '?
# th, ce/ci, ge/gi, ee
