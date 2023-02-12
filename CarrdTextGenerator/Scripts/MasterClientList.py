import math
import pyperclip
import pathlib
import CarrdGenerator as main

def readCSV():
    return main.CreateClientObjects()

#Returns a single commission
def readSingle(i):
    return main.CreateClientObjectIndex(i)

#Total amount of commissions
def commLen(x):
    return len(x)

#How many SubscriberStars are there
def subscriberLen(x):
    ct = 0
    for i in x:
        if i.getSub():
            ct += 1
    return ct

test = ""

f = open(script1.findPath("\Scripts","\\Texts\Test.txt"), "w")
f.write(test)
f.close()

test += Client[i].getName() + "\n"
test += str(Client[i].getSub()) + "\n"
test += Client[i].getType() + "\n"
test += str(Client[i].getComplex()) + "\n"
test += str(Client[i].getCharNum()) + "\n"
test += Client[i].getPaymentType() + "\n"

test += Client[i].getShortName() + "\n"
test += mode[i].currentMode() + "\n"
test += mode[i].currentColor() + "\n"
test += "\n"


ClientObj = readCSV()
#ClientObj.append(readSingle(1))