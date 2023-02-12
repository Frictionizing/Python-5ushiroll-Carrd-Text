#This program takes the results from 5ushiroll's response sheet and copies to clipboard the carrd format featured on the carrd website.
# pip install pyperclip
# ^Do that if not done^

#Import pyperclip (Copy to clipboard extension)

import math
import pyperclip
import pathlib
import CommissionPrices as prices

##################CLASSES & VARIABLES##################

#Object of every client application with parsed relevant data
class Client:
    """
    Name:      Username String
    isSub:     SubscriberStar boolean
    Type:      Commission Type String
    isComplex: Complex Background boolean
    numOfChar: # of Characters Featured int
    paymentType: Paypal or Square
    fullType: Detailed Description of Type (ie: Cell Shaded Fullbody -> Cell Shaded Fullbodies w/ Complex BG )
    shortName: Shortened name abbrevation (ie: Cell Shaded Fullbodies w/ Complex BG -> CS-FBs-CB)
    price: Calculated cost in USD
    button: button objects associated with client
    """
    def __init__(app, application):
        app.name        = application[0]
        app.isSub       = application[1]
        app.type        = application[2]
        app.isComplex   = application[3]
        app.numOfChar   = application[4]
        app.paymentType = application[5]
        app.fullType    = textChange(app.type, app.isComplex, app.numOfChar)
        app.shortName   = shortenedComm(app.type, app.numOfChar, app.isComplex)
        app.price       = singlePrice(app.type, app.numOfChar, app.isComplex)

        app.button      = ""
        app.state       = "BLANK"
        app.color       = "BLACK" if not app.isSub else "BLUE"

    #Get Functions
    def getName(app):
        return app.name
    def getSub(app):
        return app.isSub
    def getType(app):
        return app.type
    def getComplex(app):
        return app.isComplex
    def getCharNum(app):
        return app.numOfChar
    def getNewType(app):
        return app.fullType
    def getPaymentType(app):
        return app.paymentType
    def getPrice(app):
        return app.price
    def getShortName(app):
        return app.shortName
    def getButton(app):
        return app.button
    def getFullType(app):
        return app.fullType
    def getState(app):
        return app.state
    def getColor(app):
        return app.color

    #Set Functions
    def assignButton(app, button):
        app.button = button
    def setPrice(app, i):
        app.price = i
    def setShortName(app, i):
        app.shortName = i

    #Override Functions
    def OverrideComm(app, i,j,k):
        app.name = i
        app.shortName = j
        app.price = k

    def overrideComplex(app, i):
        app.isComplex = i
    def overrideType(app, i):
        app.fullType = i
    def overrideShortName(app, i):
        app.shortName = i
    def overridePrice(app, i):
        app.price = i
    def overrideState(app, i):
        app.state = i
    def overrideColor(app, i):
        app.color = i
    
ClientQueue_Error = []

userName = 1; subscriber = 2; commType = 5; complexBG = 6; charNum = 7; payment = 13

##################FUNCTIONS##################

#Find the path to file, x is path to split, y is replacement text
def findPath(x,y):
    p = str(pathlib.Path(__file__))
    return p.split(x)[0] + y

#Reads csv file and returns file
def readFile():

    with open(findPath("\Scripts","\\5ushiroll's Commission Form.csv"), errors = "ignore") as f:
        lines = f.readlines()
    f.close()
    return lines

#Write results to txt file
def writeToFile(x):
    f = open(findPath("\Scripts","\\Texts\TextOutput.txt"), "w")
    f.write(x)
    f.close()

#Find line when data starts in csv file
def iterable(x):
    for i in range(0,len(x)):
        s = x[i]
        #finds first instance of the date "2022"
        if s[0:3] == "\"20":
            return i

def iterablePerComm(x):
    k = 0
    for i in range(0,len(x)):
        s = x[i]
        #finds first instance of the date "2022"
        if s[0:3] == "\"20":
            k += 1
    return k

#Returns capitalized name function
def capital(name):
    return name[0].capitalize() + name[1:]

#Returns removed apostrophies
def apostrophe_removal(x):
    for i in x:
        i.replace('\'','')
    return x

#Turns string "Yes" into boolean
def convertBool(x):
    if x == "Yes":
        return True
    return False

#Converts strings to int
def parseInt(x):
    if x == "Alot" or x == "6+":
        x = 6
    return int(x)

#Adds plural forms for different commission types
#Adds Complex Background description
#x is Type, y is Complex Background, z is # of Characters
def textChange(x,y,z):
    #Temp is the base x commission title

    z = int(z)

    temp = x

    pluralDict = prices.pluralDict
    #Exempt from complex backgrounds
    exemptList = ["Simple Reference Sheet", "Complex Reference Sheet", "YCH", "Demonify Me", "Headshot Page", 
                    "Sketch Page", "Daily Dragon Feature", "Full Render", "Mawshot", "Cell-Shaded Headshot",
                    "Gacha Splash Art 3 Star","Gacha Splash Art 4 Star","Gacha Splash Art 5 Star","Gacha Splash Art 6 Star"]
   
    test = x
    if z >= 2:
        test = pluralDict[x]
    if z >= 3 and " /w Extra Character" in test:
        test += "s"
    if y and temp not in exemptList:
        test += " & Complex BG"
    
    return test

#Concact both strings with subs first and non subs last (in order of submitted application)
def stringConcat(x):
    st = ""
    for i in x:
        st += i.getName() + ": " + textChange(i.getType(), i.getComplex(), i.getCharNum()) + "\n"

    return st[:-1]

#Copy result to clipboard
def copyToClipboard(s):
    pyperclip.copy(s)
    return

def commishType(x,y,z):
    if x == "Daily Dragon Feature (Only available for SubStar Wyvern tier)":
        return "Daily Dragon Feature"

    if (x == "Cell-Shaded" or x == "Reference Sheet") and y == "":
        return "Error: See Remarks"
    if  x == "Cell-Shaded":
        if y == "Simple (ref sheets only)" or y == "Complex (ref sheets only)":
            return "Error: See Remarks"
        else:
            return x + " " + y
    
    if x == "Reference Sheet" and not (y == "Simple (ref sheets only)" or  y == "Complex (ref sheets only)"):
        return "Error: See Remarks"
    if x == "Reference Sheet" and y == "Simple (ref sheets only)":
        return "Simple Reference Sheet"
    if x == "Reference Sheet" and y == "Complex (ref sheets only)":
        return "Complex Reference Sheet"

    if x == "Gacha Splash Art":
        if z == "":
            return "Error: See Remarks"
        s = x + " " + z
        x = s

    return x

def errorText(x,y,z):
    if x == "Gacha Splash Art":
        return z + ': Error - Commissioned "' + x + '" without answering the follow up question.'
    if (x == "Cell-Shaded" or x == "Reference Sheet") and y == "":
        return z + ': Error - Commissioned "' + x + '" without answering the follow up question.'
    return z + ': Error - Commissioned "' + x + '" while answering "' + y + '" in the follow up question.'

#Shortened form with plural cases
def shortenedComm(i,j,k):

    j = int(j)

    exemptList = ["GACH-3","GACH-4","GACH-5","GACH-6", "Full-Ren", "MAW", "DD", "YCH", "SRS", "CRS", "HSP", "DM", "SP", "RH"]
    temp = prices.shortDict[i]
    name = prices.shortDict[i]
    if (name == "BAN" or name == "MAW" or name == "COS") and j >= 2:
        name += "-w/charas"
    elif (name == "CS-H" or name == "CS-HB" or name == "CS-FB" or name == "RH") and j >= 2:
        name += "s"

    if k and temp not in exemptList:
        name += "-CB"

    return name

def shortenPayment(x):
    return "SQUARE" if x == "I can pay with Square" else "PAYPAL"

#Create Client objects and put them in Queue (MAIN FUCNTION)
def CreateClientObjects():
    lines = readFile()

    #ClientList Queue
    ClientQueue = []
    ClientQueue_NoSub = []

    #Find line csv file where data begins and puts data into array; split by the comma and quotes

    for i in range(iterable(lines), len(lines)):

        #Collect all lines of single commission
        preComm = lines[i]
        if preComm[0:3] != "\"20":
            continue

        for y in range(i+1, len(lines)):
            if y >= len(lines) or lines[y][0:3] == "\"20":
                break
            if lines[y] == "\n":
                continue
            preComm += lines[y]

        comm = apostrophe_removal(preComm.split("\",\""))

        #Parsing out Name     
        name = comm[2]

        #Discord Case
        name = name.split("#")[0]

        #Twitter Case
        if len(name.split("@")) == 2:
            name = name.split("@")[1]

        #Space in Name Front
        if name[0] == " ":
            name = name[1:len(name)]

        #Space in Name Back
        if name[len(name)-1] == " ":
            name = name[0:len(name)-1]

        name = capital(name)
        #Simplify array to relevant data
        #Comm[] = Name 2, Sub 3, Comm 4, 6 CellShaded Ref Sheet Q, 7 Gacha Q, 9 Char Num, 10 Background, 14 Payment 
        #0 Name, 1 Subscriber, 2 Comm, 3 Background, 4 #Chars, 5 Payment Type
        simplified_comm = [name,                                                  
                           convertBool(comm[3]), 
                           commishType(comm[4], comm[6], comm[7]), 
                           convertBool(comm[10]), 
                           parseInt(comm[9]), 
                           shortenPayment(comm[14])
                           ]

        if simplified_comm[2] == "Error: See Remarks":
            simplified_comm[2] = errorText(comm[4], comm[6], simplified_comm[0])
            cli = Client(simplified_comm)
            ClientQueue_Error.append(cli)
            continue

        #Turn application into Client object
        cli = Client(simplified_comm)

        #Append to seperate queue depending on SubsriberStar status
        if cli.getSub():
            ClientQueue.append(cli)
        else:
            ClientQueue_NoSub.append(cli)

    for i in ClientQueue_NoSub:
        ClientQueue.append(i)
        
    #Print out suggested prices
    #printPrices(ClientQueue)

    return ClientQueue

def CreateClientObjectIndex(w):
    lines = readFile()
    ClientQueue = []
    ClientQueue_NoSub = []
    #Find line csv file where data begins and puts data into array; split by the comma and quotes

    for i in range(iterable(lines), len(lines)):

        #Collect all lines of single commission
        preComm = lines[i]
        if preComm[0:3] != "\"20":
            continue

        for y in range(i+1, len(lines)):
            if y >= len(lines) or lines[y][0:3] == "\"20":
                break
            if lines[y] == "\n":
                continue
            preComm += lines[y]

        comm = apostrophe_removal(preComm.split("\",\""))

        #Parsing out Name     
        name = comm[2]

        #Discord Case
        name = name.split("#")[0]

        #Twitter Case
        if len(name.split("@")) == 2:
            name = name.split("@")[1]

        #Space in Name Front
        if name[0] == " ":
            name = name[1:len(name)]

        #Space in Name Back
        if name[len(name)-1] == " ":
            name = name[0:len(name)-1]

        name = capital(name)
        #Simplify array to relevant data
        #Comm[] = Name 2, Sub 3, Comm 4, 6 CellShaded Ref Sheet Q, 7 Gacha Q, 9 Char Num, 10 Background, 14 Payment 
        #0 Name, 1 Subscriber, 2 Comm, 3 Background, 4 #Chars, 5 Payment Type
        simplified_comm = [name,                                                  
                           convertBool(comm[3]), 
                           commishType(comm[4], comm[6], comm[7]), 
                           convertBool(comm[10]), 
                           parseInt(comm[9]), 
                           shortenPayment(comm[14])
                           ]

        if simplified_comm[2] == "Error: See Remarks":
            simplified_comm[2] = errorText(comm[4], comm[6], simplified_comm[0])

        cli = Client(simplified_comm)
            #Append to seperate queue depending on SubsriberStar status
        if cli.getSub():
            ClientQueue.append(cli)
        else:
            ClientQueue_NoSub.append(cli)

        for i in ClientQueue_NoSub:
            ClientQueue.append(i)   
        
    return ClientQueue[w]

#Returns Single Price of Client Comm in USD
def singlePrice(i,j,k):
    j = int(j)

    #Current Prices
    priceDict = prices.priceDict

    #Background upgrade prices
    bgDict = prices.bgDict

    #Extra Character count prices
    charDict = prices.charDict

    price = priceDict[i] 
    if k:
        price += bgDict[i]
    if j > 1:
        price += charDict[i]*(j-1)
    return price

#Prints prices to terminal
def printPrices(x):
    totalPrice = 0
    totalPriceCAD = 0

    #Conversion rate to CAD if payment type is Square (set to 1.3)
    cashConvert = prices.cashConvert

    #Money type
    cashConvert2 = prices.cashConvert2

    ##Current Prices
    priceDict = prices.priceDict

    #Background upgrade prices
    bgDict = prices.bgDict

    #Extra Character count prices
    charDict = prices.charDict

    print("TOTAL COMMISSIONS:" + str(len(x)))
    print("ERROR SUBMISSIONS:" + str(len(ClientQueue_Error)) + "\n")

    for i in x:
        if i.getType() == "Error: See Remarks":
            print(i.getName() + ": See Remarks")
            continue

        price = i.getPrice()

        if i.getPaymentType() == "SQUARE":
            price = math.floor(price * cashConvert[i.getPaymentType()])
            totalPriceCAD += price
        else:
            totalPrice += price

        #Complex BG Price
        if bgDict[i.getType()] == 0 or not i.getComplex():
            s = "NO"
        else:
            s = str(math.floor(bgDict[i.getType()]* cashConvert[i.getPaymentType()]))
        
        if i.getCharNum() > 5:
            nameAndPrice = i.getName() + ": $" + str(price) + "+ " + cashConvert2[i.getPaymentType()]
        else:
            nameAndPrice = i.getName() + ": $" + str(price) + " " + cashConvert2[i.getPaymentType()]

        #Pad out the recipt from the total price
        pad = 35 - len(nameAndPrice)
        if pad < 0:
            pad = 0
        pad = " " * pad

        if i.getCharNum() > 5:
            print(nameAndPrice + pad + "(" + i.getType() + ": " + str(math.floor(priceDict[i.getType()]* cashConvert[i.getPaymentType()])) + 
                  ", 5+ Chars: " + str(math.floor(charDict[i.getType()]*(i.getCharNum()-1)* cashConvert[i.getPaymentType()])) + "+, Background: " + s + ")")
        else:
            print(nameAndPrice + pad + "(" + i.getType() + ": " + str(math.floor(priceDict[i.getType()]* cashConvert[i.getPaymentType()])) + ", " + str(i.getCharNum()) + 
                  " Char(s): " + str(math.floor(charDict[i.getType()]*(i.getCharNum()-1)* cashConvert[i.getPaymentType()])) + ", Background: " + s + ")")

    print("\nTOTAL: $" + str(totalPriceCAD) + " CAD + $" + str(totalPrice) + " USD" + " ($" + str(math.floor(totalPrice*1.34)) + "CAD) = $" + str(totalPriceCAD + math.floor(totalPrice*1.34)) + " CAD") 
    #print("Note: Total does not include YCH prices and any extra characters that go beyond 5 per comm")
    print("USD to CAD official conversion rate 2023-1-11: 1.00 USD = 1.34 CAD")
    print("USD to CAD commission conversion rate set to 1.00 USD = " + str(cashConvert["SQUARE"]) + "0 CAD\n")

    print("REMARKS:")

    for i in ClientQueue_Error:
        print(i.getType())

    for i in x:
        if i.getCharNum() > 5:
            print(i.getName() + ": Commissioned more than 5 characters")
        if i.getType() ==  "YCH":
            print(i.getName() + ": Commissioned a YCH (not included in total)")

#Sends final result to file
def Generate(x):
    writeToFile(stringConcat(x))

##################MAIN##################
#Applications = CreateClientObjects()
#Generate(Applications)
#Create Objects and seperate to two seperate queues ClientQueue and ClientQueue_NoSub
