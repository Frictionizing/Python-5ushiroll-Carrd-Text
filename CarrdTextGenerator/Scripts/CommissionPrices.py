import pathlib
#Find the path to file, x is path to split, y is replacement text

base = [0] * 15
char = [0] * 15
bg   = [0] * 15

#Money related Dictionaries
comm = ["Daily Dragon Feature",             #0
        "YCH",                              #1
        "Colored Sketch",                   #2
        "Mawshot",                          #3
        "Cell-Shaded Headshot",             #4  
        "Simple Reference Sheet",           #5
        "Flat Colored Fullbody",            #6
        "Cell-Shaded Halfbody",             #7
        "Banner",                           #8
        "Cell-Shaded Fullbody",             #9
        "Demonify Me",                      #10
        "Rendered Headshot",                #11
        "Sketch Page",                      #12
        "Complex Reference Sheet",          #13
        "Full Render"                       #14
        ]                      

#Prices of base commission
priceDict = {
    comm[0]  : base[0],
    comm[1]  : base[1],
    comm[2]  : base[2],
    comm[3]  : base[3],
    comm[4]  : base[4],
    comm[5]  : base[5],
    comm[6]  : base[6],
    comm[7]  : base[7],
    comm[8]  : base[8],
    comm[9]  : base[9],
    comm[10] : base[10],
    comm[11] : base[11],
    comm[12] : base[12],
    comm[13] : base[13],
    comm[14] : base[14]
}

#Extra Character count prices
charDict = {
    comm[0]  : char[0],
    comm[1]  : char[1],
    comm[2]  : char[2],
    comm[3]  : char[3],
    comm[4]  : char[4],
    comm[5]  : char[5],
    comm[6]  : char[6],
    comm[7]  : char[7],
    comm[8]  : char[8],
    comm[9]  : char[9],
    comm[10] : char[10],
    comm[11] : char[11],
    comm[12] : char[12],
    comm[13] : char[13],
    comm[14] : char[14]
}

#Complex Background upgrade prices
bgDict = {
    comm[0]  : bg[0],
    comm[1]  : bg[1],
    comm[2]  : bg[2],
    comm[3]  : bg[3],
    comm[4]  : bg[4],
    comm[5]  : bg[5],
    comm[6]  : bg[6],
    comm[7]  : bg[7],
    comm[8]  : bg[8],
    comm[9]  : bg[9],
    comm[10] : bg[10],
    comm[11] : bg[11],
    comm[12] : bg[12],
    comm[13] : bg[13],
    comm[14] : bg[14]
}

###MAIN

def findPath(x,y):
    p = str(pathlib.Path(__file__))
    return p.split(x)[0] + y

def readSheet():
    with open(findPath("\Scripts","\\Texts\MoneySheet.txt")) as f:
        r = f.readlines()
    f.close()

    base.clear()
    char.clear()
    bg.clear()

    le = 15
    c = 0
    prices = []

    for i in range (0,len(r),le+1):
        for j in range(0,le):
            prices.append(int(r[i+j][:-1]))

        for i in prices:
            if c == 0:
                base.append(i)
            elif c == 1:
                char.append(i)
            elif c==2:
                bg.append(i)
        prices.clear()
        c += 1

    for i in range(0,15):
        priceDict.update({comm[i] : base[i]})
        charDict.update({comm[i] : char[i]})
        bgDict.update({comm[i] : bg[i]})

readSheet()

###

#Conversion rate to CAD if payment type is Square (set to 1.3 means 1.00 USD = 1.30 CAD)
cashConvert = {
    "PAYPAL" : 1,
    "SQUARE" : 1.37
}

#Type of currency
cashConvert2 = {
    "PAYPAL" : "USD",
    "SQUARE" : "CAD"
}

###

#Commission Type Dictionaries
#Shortened Google Sheet format
shortDict = {
    comm[0]  : "DD",
    comm[1]  : "YCH",
    comm[2]  : "COS",
    comm[3]  : "MAW",
    comm[4]  : "CS-H",
    comm[5]  : "SRS",
    comm[6]  : "FC-FB",
    comm[7]  : "CS-HB",
    comm[8]  : "BAN",
    comm[9] : "CS-FB",
    comm[10] : "DM",
    comm[11] : "RH",
    comm[12] : "SP",
    comm[13] : "CRS",
    comm[14] : "Full-Ren"
}

#Gramatically correct plural form for commissions with 2 or more characters
pluralDict = {
    comm[0]  : "Daily Dragon Feature",
    comm[1]  : "YCH",
    comm[2]  : "Colored Sketch w/ Extra Character",
    comm[3]  : "Mawshot w/ Extra Character",
    comm[4]  : "Cell-Shaded Headshots",
    comm[5]  : "Simple Reference Sheet",
    comm[6]  : "Flat Colored Fullbodies",
    comm[7]  : "Cell-Shaded Halfbodies",
    comm[8]  : "Banner w/ Extra Character",
    comm[9] : "Cell-Shaded Fullbodies",
    comm[10] : "Demonify Me",
    comm[11] : "Rendered Headshots",
    comm[12] : "Sketch Page",
    comm[13] : "Complex Reference Sheet",
    comm[14] : "Full Render w/ Extra Character"
}
