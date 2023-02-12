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

##Read In Saved File With Edits
def readSave():
    le = 10
    final = []
    every_client = []
    ClientQueue = []
    ClientQueue_NoSub = []

    def dumb(i):
        if i == "True":
            return True
        return False
    
    with open(main.findPath("\Scripts","\\Texts\SaveFile.txt")) as f:
        r = f.readlines()
    f.close()

    for i in range (0,len(r),le+1):
        for j in range(0,le):
            every_client.append(r[i+j][:-1])

        final.append(every_client[:])
        every_client.clear()

    for i in final:
        cli = main.Client([i[0],dumb(i[1]),i[2],dumb(i[3]),int(i[4]),i[5]])
        cli.overrideShortName(i[6])
        cli.overrideState(i[7])
        cli.overrideColor(i[8])
        cli.overridePrice(int(i[9]))
        if cli.getSub():
            ClientQueue.append(cli)
        else:
            ClientQueue_NoSub.append(cli)

    for i in ClientQueue_NoSub:
        ClientQueue.append(i)

    #Print out suggested prices
    main.printPrices(ClientQueue)
    return ClientQueue

def writeSave():
    test = ""
    for i in ClientObj:
        test += i.getName() + "\n"
        test += str(i.getSub()) + "\n"
        test += i.getType() + "\n"
        test += str(i.getComplex()) + "\n"
        test += str(i.getCharNum()) + "\n"
        test += i.getPaymentType() + "\n"
        test += i.getShortName() + "\n"
        test += i.getButton().currentMode() + "\n"
        test += i.getButton().currentColor() + "\n"
        test += str(i.getPrice()) + "\n"
        test += "\n"

    f = open(main.findPath("\Scripts","\\Texts\SaveFile.txt"), "w")
    f.write(test)
    f.close()

ClientObj = readCSV()
ClientObj = readSave()


#ClientObj.append(readSingle(1))