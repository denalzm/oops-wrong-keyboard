# English helper package

RU_TO_EN = {"А":"A",
            "Б":"B",
            "В":"V",
            "Г":"G",
            "Д":"D",
            "Е":"E",
            "Ё":"YO",
            "Ж":"ZH",
            "З":"Z",
            "И":"I",
            "Й":"Y",
            "К":"K",
            "Л":"L",
            "М":"M",
            "Н":"N",
            "О":"O",
            "П":"P",
            "Р":"R",
            "С":"S",
            "Т":"T",
            "У":"U",
            "Ф":"PH",
            "Х":"H",
            "Ц":"TS",
            "Ч":"CH",
            "Ш":"SH",
            "Щ":"SHCH",
            "Ъ":"'",
            "Ы":"IH",
            "Ь":"'",
            "Э":"E",
            "Ю":"YU",
            "Я":"YA",
            "а":"a",
            "б":"b",
            "в":"v",
            "г":"g",
            "д":"d",
            "е":"e",
            "ё":"yo",
            "ж":"zh",
            "з":"z",
            "и":"i",
            "й":"y",
            "к":"k",
            "л":"l",
            "м":"m",
            "н":"n",
            "о":"o",
            "п":"p",
            "р":"r",
            "с":"s",
            "т":"t",
            "у":"u",
            "ф":"ph",
            "х":"h",
            "ц":"ts",
            "ч":"ch",
            "ш":"sh",
            "щ":"shch",
            "ъ":"'",
            "ы":"ih",
            "ь":"'",
            "э":"e",
            "ю":"yu",
            "я":"ya", }

def latinContent(instring):
    latset = set("abcdefghijklmnopqrstuvwxyz'")
    counter = 0.0;
    for chr in instring.lower():
        if chr in latset:
            counter += 1
    return counter / len(instring)

def latinizeRussian(instring):
    result = []
    c = 0
    while c < len(instring):
        chr = instring[c]
        #print(str(c) + "" + chr) # debug statement
        if not chr in RU_TO_EN:
            result.append(chr)
        else:
            result.append(RU_TO_EN[chr])
        c += 1
    return "".join(result)
