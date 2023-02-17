import pathlib
#Find the path to file, x is path to split, y is replacement text

base = [0] * 20
char = [0] * 20
bg   = [0] * 20

#Money related Dictionaries
comm = ["Daily Dragon Feature",             #0
        "YCH",                              #1
        "Colored Sketch",                   #2
        "Mawshot",                          #3
        "Cell-Shaded Headshot",             #4  
        "Simple Reference Sheet",           #5
        "Flat Colored Fullbody",            #6
        "Headshot Page",                    #7
        "Cell-Shaded Halfbody",             #8
        "Banner",                           #9
        "Cell-Shaded Fullbody",             #10
        "Demonify Me",                      #11
        "Rendered Headshot",                #12
        "Sketch Page",                      #13
        "Complex Reference Sheet",          #14
        "Full Render",                      #15
        "Gacha Splash Art 3 Star",          #16
        "Gacha Splash Art 4 Star",          #17
        "Gacha Splash Art 5 Star",          #18
        "Gacha Splash Art 6 Star"           #19
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
    comm[14] : base[14],
    comm[15] : base[15],
    comm[16] : base[16],
    comm[17] : base[17],
    comm[18] : base[18],
    comm[19] : base[19]
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
    comm[14] : char[14],
    comm[15] : char[15],
    comm[16] : char[16],
    comm[17] : char[17],
    comm[18] : char[18],
    comm[19] : char[19]
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
    comm[14] : bg[14],
    comm[15] : bg[15],
    comm[16] : bg[16],
    comm[17] : bg[17],
    comm[18] : bg[18],
    comm[19] : bg[19]
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

    le = 20
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

    for i in range(0,20):
        priceDict.update({comm[i] : base[i]})
        charDict.update({comm[i] : char[i]})
        bgDict.update({comm[i] : bg[i]})

readSheet()

###

#Conversion rate to CAD if payment type is Square (set to 1.3 means 1.00 USD = 1.30 CAD)
cashConvert = {
    "PAYPAL" : 1,
    "SQUARE" : 1.3
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
    comm[7]  : "HSP",
    comm[8]  : "CS-HB",
    comm[9]  : "BAN",
    comm[10] : "CS-FB",
    comm[11] : "DM",
    comm[12] : "RH",
    comm[13] : "SP",
    comm[14] : "CRS",
    comm[15] : "Full-Ren",
    comm[16] : "GACH-3",
    comm[17] : "GACH-4",
    comm[18] : "GACH-5",
    comm[19] : "GACH-6"
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
    comm[7]  : "Headshot Page",
    comm[8]  : "Cell-Shaded Halfbodies",
    comm[9]  : "Banner w/ Extra Character",
    comm[10] : "Cell-Shaded Fullbodies",
    comm[11] : "Demonify Me",
    comm[12] : "Rendered Headshots",
    comm[13] : "Sketch Page",
    comm[14] : "Complex Reference Sheet",
    comm[15] : "Full Render w/ Extra Character",
    comm[16] : "Gacha Splash Art 3 Star",
    comm[17] : "Gacha Splash Art 4 Star",
    comm[18] : "Gacha Splash Art 5 Star",
    comm[19] : "Gacha Splash Art 6 Star"
}
