filenames = ["colors"]

for filename in filenames:
    src = open(filename + ".tdesktop-theme", "r")
    thememap = open("theme.map", "r")
    themesrc = open(filename + ".atthemesrc", "w")

    rulelist = []
    srcrules = []
    bg = False
    bgColor = ""

    for line in thememap:
        rule = line.strip().split("=")
        rulelist.append([rule[1],rule[0]])

    for line in src:
        strippedline = line.strip()
        if strippedline.startswith("/") or strippedline.startswith("*") or len(strippedline) < 1:
            print("skip")
        else:
            rule = strippedline.split(":")
            rulename = rule[0].strip()
            if rulename == "convChatBackgroundColor":
                bg = True
            potcolor = rule[1].split("//")[0].strip()
            if potcolor.startswith("#"):
                if len(potcolor[1:-1]) == 8:
                    color = potcolor[1:-1]
                else:
                    color = potcolor[1:-1] + "ff"
            else :
                for srcrule in srcrules:
                    if srcrule[0] == potcolor[:-1]:
                        color = srcrule[1]
            if bg == False and rulename == "windowBgOver":
                bgColor = color
            srcrules.append([rulename,color])

    srcrules.append(["whatever", "ff00ffff"])
    srcrules.append(["findme", "00ffffff"])
    if bg == False:
        srcrules.append(["convChatBackgroundColor", bgColor])

    for themerule in srcrules:
        for maprule in rulelist:
            if maprule[0] == themerule[0]:
                themesrc.write(maprule[1]+"=#"+themerule[1]+"\n")
