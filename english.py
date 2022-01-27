# English helper package

def latinContent(instring):
    latset = set("abcdefghijklmnopqrstuvwxyz'")
    counter = 0.0;
    for chr in instring.lower():
        if chr in latset:
            counter += 1
    return counter / len(instring)
