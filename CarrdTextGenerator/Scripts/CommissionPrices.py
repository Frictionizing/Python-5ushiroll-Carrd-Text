#Money related Dictionaries
#Prices of base commission
priceDict = {
    "Daily Dragon Feature"    : 85,
    "YCH"                     : 0,
    "Colored Sketch"          : 85,
    "Mawshot"                 : 95,
    "Cell-Shaded Headshot"    : 110,
    "Simple Reference Sheet"  : 110,
    "Flat Colored Fullbody"   : 125,
    "Headshot Page"           : 150,
    "Cell-Shaded Halfbody"    : 155,
    "Banner"                  : 160,
    "Cell-Shaded Fullbody"    : 200,
    "Demonify Me"             : 200,
    "Rendered Headshot"       : 230,
    "Sketch Page"             : 250,
    "Complex Reference Sheet" : 250,
    "Full Render"             : 400
}

#Complex Background upgrade prices
bgDict = {
    "Daily Dragon Feature"    : 0,
    "YCH"                     : 0,
    "Colored Sketch"          : 30,
    "Mawshot"                 : 0,
    "Cell-Shaded Headshot"    : 0,
    "Simple Reference Sheet"  : 0,
    "Flat Colored Fullbody"   : 30,
    "Headshot Page"           : 0,
    "Cell-Shaded Halfbody"    : 40,
    "Banner"                  : 30,
    "Cell-Shaded Fullbody"    : 50,
    "Demonify Me"             : 0,
    "Rendered Headshot"       : 30,
    "Sketch Page"             : 0,
    "Complex Reference Sheet" : 0,
    "Full Render"             : 0
}

#Extra Character count prices
charDict = {
    "Daily Dragon Feature"    : 0,
    "YCH"                     : 0,
    "Colored Sketch"          : 30,
    "Mawshot"                 : 45,
    "Cell-Shaded Headshot"    : 30,
    "Simple Reference Sheet"  : 0,
    "Flat Colored Fullbody"   : 30,
    "Headshot Page"           : 0,
    "Cell-Shaded Halfbody"    : 40,
    "Banner"                  : 15,
    "Cell-Shaded Fullbody"    : 50,
    "Demonify Me"             : 0, 
    "Rendered Headshot"       : 30,
    "Sketch Page"             : 0,
    "Complex Reference Sheet" : 0,
    "Full Render"             : 55
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
    "Daily Dragon Feature"    : "DD",
    "YCH"                     : "YCH",
    "Colored Sketch"          : "COS",
    "Mawshot"                 : "MAW",
    "Cell-Shaded Headshot"    : "CS-H",
    "Simple Reference Sheet"  : "SRS",
    "Flat Colored Fullbody"   : "FC-FB",
    "Headshot Page"           : "HSP",
    "Cell-Shaded Halfbody"    : "CS-HB",
    "Banner"                  : "BAN",
    "Cell-Shaded Fullbody"    : "CS-FB",
    "Demonify Me"             : "DM",
    "Rendered Headshot"       : "RH",
    "Sketch Page"             : "SP",
    "Complex Reference Sheet" : "CRS",
    "Full Render"             : "Full-Ren"
}

#Gramatically correct plural form for commissions with 2 or more characters
pluralDict = {
    "Daily Dragon Feature"    : "Daily Dragon Feature",
    "YCH"                     : "YCH",
    "Colored Sketch"          : "Colored Sketch w/ Extra Character",
    "Mawshot"                 : "Mawshot w/ Extra Character",
    "Cell-Shaded Headshot"    : "Cell-Shaded Headshots",
    "Simple Reference Sheet"  : "Simple Reference Sheet",
    "Flat Colored Fullbody"   : "Flat Colored Fullbodies",
    "Headshot Page"           : "Headshot Page",
    "Cell-Shaded Halfbody"    : "Cell-Shaded Halfbodies",
    "Banner"                  : "Banner w/ Extra Character",
    "Cell-Shaded Fullbody"    : "Cell-Shaded Fullbodies",
    "Demonify Me"             : "Demonify Me",
    "Rendered Headshot"       : "Rendered Headshots",
    "Sketch Page"             : "Sketch Page",
    "Complex Reference Sheet" : "Complex Reference Sheet",
    "Full Render"             : "Full Render w/ Extra Character"
}
