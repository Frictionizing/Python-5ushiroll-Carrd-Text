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
        "Full Render"                       #15
        ]                      


#Prices of base commission
priceDict = {
    comm[0]  : 85,
    comm[1]  : 0,
    comm[2]  : 85,
    comm[3]  : 95,
    comm[4]  : 135,
    comm[5]  : 110,
    comm[6]  : 125,
    comm[7]  : 150,
    comm[8]  : 175,
    comm[9]  : 160,
    comm[10] : 225,
    comm[11] : 200,
    comm[12] : 230,
    comm[13] : 275,
    comm[14] : 270,
    comm[15] : 400
}

#Complex Background upgrade prices
bgDict = {
    comm[0]  : 0,
    comm[1]  : 0,
    comm[2]  : 30,
    comm[3]  : 0,
    comm[4]  : 0,
    comm[5]  : 0,
    comm[6]  : 30,
    comm[7]  : 0,
    comm[8]  : 40,
    comm[9]  : 30,
    comm[10] : 50,
    comm[11] : 0,
    comm[12] : 30,
    comm[13] : 0,
    comm[14] : 0,
    comm[15] : 0
}

#Extra Character count prices
charDict = {
    comm[0]  : 0,
    comm[1]  : 0,
    comm[2]  : 30,
    comm[3]  : 45,
    comm[4]  : 30,
    comm[5]  : 0,
    comm[6]  : 30,
    comm[7]  : 0,
    comm[8]  : 40,
    comm[9]  : 15,
    comm[10] : 50,
    comm[11] : 0,
    comm[12] : 30,
    comm[13] : 0,
    comm[14] : 0,
    comm[15] : 55
}

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
    comm[15] : "Full-Ren"
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
    comm[15] : "Full Render w/ Extra Character"
}
