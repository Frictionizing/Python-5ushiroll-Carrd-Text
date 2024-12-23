import MasterClientList as app
import CarrdInProgressCompleted as carrd
import CarrdGenerator as names
import GoogleSheet as goog
import GoogleAPI as api
import CommissionPrices as price
import webbrowser
import math
from tkinter import *
import os
import pyperclip

maxComm = 20
complete   = " [==COMPLETED==]{lime}"
inProgress = " [==IN PROGRESS==]{orange}"
buttonDict = {}
name_label = {}
num_label = {}
colorDict = {}
resize = 7

#Combine Application and ButtonList
def consolidateObjects(a):
    x = 0
    for i in a:
        i.assignButton(carrd.buttonList[x])
        x+=1

consolidateObjects(app.ClientObj)

#Concatenate string
def concatenate(x):
    string = ""
    for i in x:
        string += i

    return string + "\n"

#Copy Carrd to clipboard
def click():
    str = concatenate(carrd.appendProgress(carrd.buttonList)).replace(" Star", "★")
    pyperclip.copy(str)

#Copy Google Sheet Info to Clipboard
def click2():
    goog.sheet()

#Generate all the buttons for In Progress and Complete; Handles the changing of modes in the button as well
def createButtons():
    yaxis = 180
    xaxis = 10
    nextRowReady = True

    for i in range(0,(len(carrd.buttonList))):
        #Capped the maximum amount of commissions
        if i > maxComm:
            break

        #Function for changing the mode of each indivudual progress button
        def convertMode(x=i):
            carrd.buttonList[x].changeMode()
            buttonDict[x].configure(image = progressDict[carrd.buttonList[x].currentMode()])
            #Update save file
            app.ClientObj[x].overrideState(carrd.buttonList[x].currentMode())
            app.writeSave()
            api.updateSingle(app.ClientObj[x])

        def convertColor(x=i):
            carrd.buttonList[x].changeColor()
            if carrd.buttonList[x].currentColor() == "BLACK" and app.ClientObj[x].getSub():
                carrd.buttonList[x].changeColorOverride("BLUE")
            colorDict[x].configure(image = progressDict[carrd.buttonList[x].currentColor()])
            app.ClientObj[x].overrideColor(carrd.buttonList[x].currentColor())
            app.writeSave()
            api.updateSingle(app.ClientObj[x])

        #If more than half commissions, continue on the right side
        if nextRowReady and i >= 10:
            nextRowReady = not nextRowReady
            xaxis = 800
            yaxis = 180

        #List of names
        name_label[i] = Label(window,
                           text = app.ClientObj[i].getName(),
                           font = ("Helvetica", 35),
                           width = 16,
                           fg = progressDict[app.ClientObj[i].getSub()])
        name_label[i].place(x=xaxis + 90, y=yaxis)

        num_label[i] = Label(window,
                           text = str(app.ClientObj[i].getCustomer()),
                           font = ("Helvetica", 35),
                           bg = progressDict[app.ClientObj[i].getSub()],
                           width = 3,
                           fg = "white")
        num_label[i].place(x=xaxis + 10, y=yaxis)


        #List of progress buttons
        buttonDict[i] = Button(window, 
                               command = convertMode,
                               width = 170,
                               height = 54,
                               image = progressDict[app.ClientObj[i].getState()])
        buttonDict[i].place(x=600 + xaxis, y=yaxis)

        #Override SubscriberStar color to blue
        if carrd.buttonList[i].currentColor() == "BLACK" and app.ClientObj[i].getSub():
            carrd.buttonList[i].changeColorOverride("BLUE")
        #List of color overlay buttons
        colorDict[i] = Button(window, 
                              command = convertColor,
                              width = 54,
                              height = 54,
                              image = progressDict[app.ClientObj[i].getColor()])
        colorDict[i].place(x=535 + xaxis, y=yaxis)
        

        #Move the Y axis every iteration (resets at the halfway point)
        yaxis += 70

#Refreshes the whole page for new CSV information
def refresh():
    os.system('cls') 
    for i in range(0, len(name_label)):
        num_label[i].destroy()
        name_label[i].destroy()
        buttonDict[i].destroy()
        colorDict[i].destroy()

    carrd.buttonList = carrd.createButtonObjects()
    consolidateObjects(app.ClientObj)
    createButtons()
    names.printPrices(app.ClientObj)

def save():
    api.update(app.ClientObj)
    return

def CSVRefresh():
    save()
    app.resetToOG(1)
    refresh()
    return

#Reset all buttons and modes to BLANK
def clear():
    for i in range(0,len(carrd.buttonList)):
        carrd.buttonList[i].reset()
        buttonDict[i].configure(image = photo_blank)
        if app.ClientObj[i].getSub():
            carrd.buttonList[i].changeColorOverride("BLUE")
        else:
            carrd.buttonList[i].changeColorOverride("BLACK")
        colorDict[i].configure(image = progressDict[carrd.buttonList[i].currentColor()])

    for i in range (0,len(app.ClientObj)):
        app.ClientObj[i].overrideState("BLANK")
        app.ClientObj[i].overrideColor(carrd.buttonList[i].currentColor())

    app.resetToOG()
    refresh()
    app.writeSave()

#Restart Entire program
def restart():
    window.destroy()
    os.startfile(names.findPath("\Scripts","\\Scripts\ProgramExecutable.py"))

#Runs GUI
window = Tk()

#Object holding Overwritten statements
entry_Prices = [0] * len(price.comm) 
class Overwrite:
    def __init__(app, content, i, xaxis, yaxis):
        app.name  = content[0]
        app.comm  = content[1]
        app.price = content[2]

        app.tip   = content[3]

        app.priceCA = content[4]

        app.tipCA   = content[5]

        app.x     = xaxis
        app.y     = yaxis

        app.i = i

        app.name.place(x=0 + xaxis, y = yaxis)
        app.name.insert(INSERT, i.getName())

        app.comm.place(x=360 + xaxis, y = yaxis)
        app.comm.insert(INSERT, i.getShortName())

        app.price.place(x=605 + xaxis, y = yaxis)

        app.tip.place(x=605 + xaxis, y = yaxis+35)

        app.priceCA.place(x=670 + xaxis, y = yaxis)

        app.tipCA.place(x=670 + xaxis, y = yaxis+35)

        conv = price.cashConvert["SQUARE"]

        app.price.insert(INSERT, i.getPrice())
        app.priceCA.insert(INSERT, math.floor(int(float(i.getPrice()) * conv)))


        if i.getPaymentType() == "SQUARE":
            app.tipCA.config(bg = "#63c76e")
            app.priceCA.config(bg = "#63c76e")
            app.tipCA.insert(INSERT, i.getTip())
            app.tip.insert(INSERT, math.floor(int(float(i.getTip()) * 0.73)))

        else:
            app.tip.config(bg = "#63c76e")
            app.price.config(bg = "#63c76e")
            app.tip.insert(INSERT, i.getTip())
            app.tipCA.insert(INSERT, math.floor(int(float(i.getTip()) * conv)))

        app.tip.edit_modified(False) 
        app.tipCA.edit_modified(False) 
        app.priceCA.edit_modified(False) 
        app.price.edit_modified(False) 

    def getName(app):
        return app.name.get("1.0", "end-1c")
    def getComm(app):
        return app.comm.get("1.0", "end-1c")
    def getPrice(app):
        return app.price.get("1.0", "end-1c")
    def getTip(app):
        return app.tip.get("1.0", "end-1c")
    def getPriceCA(app):
        return app.priceCA.get("1.0", "end-1c")
    def getTipCA(app):
        return app.tipCA.get("1.0", "end-1c")

#Object Holding Prices
class OverwritePrices:
    def __init__(app, content, i, xaxis, yaxis):
        app.name  = content[0]
        app.base  = content[1]
        app.char  = content[2]
        app.BG    = content[3]
        app.x     = xaxis
        app.y     = yaxis

        app.name.place(x=0 + xaxis, y = yaxis)

        app.base.place(x=335 + xaxis, y = yaxis)
        app.base.insert(INSERT, price.priceDict[i])

        app.char.place(x=420 + xaxis, y = yaxis)
        app.char.insert(INSERT, price.charDict[i] if price.charDict[i] > 0 else "N/A")

        app.BG.place(x=490 + xaxis, y = yaxis)
        app.BG.insert(INSERT, price.bgDict[i] if price.bgDict[i] > 0 else "N/A")

    def getBase(app):
        try:
            return int(app.base.get("1.0", "end-1c"))
        except:
            return str(0)
    def getChar(app):
        try:
            return int(app.char.get("1.0", "end-1c"))
        except:
            return str(0)
    def getBG(app):
        try:
            return int(app.BG.get("1.0", "end-1c"))
        except:
            return str(0)

#Overrides the Script with handmade edits
def edit():
    def save():
        for i in range(0,len(app.ClientObj)):
            app.ClientObj[i].OverrideComm(entry_Object[i].getName(),entry_Object[i].getComm(),
                                          entry_Object[i].getPrice(),
                                          entry_Object[i].getTipCA() if app.ClientObj[i].getPaymentType() == "SQUARE" 
                                                                        else entry_Object[i].getTip())
            name_label[i].config(text = app.ClientObj[i].getName())
        app.writeSave()

        api.update(app.ClientObj)
        os.system('cls') 
        names.printPrices(app.ClientObj)
        return
    
    def update():
        conv = price.cashConvert["SQUARE"]

        for i in range(0,len(app.ClientObj)):
            if entry_Tip[i].edit_modified():
                entry_TipCA[i].delete(1.0, END)
                entry_TipCA[i].insert(INSERT, math.floor(int(float(entry_Object[i].getTip()) * conv)))
                entry_Tip[i].edit_modified(False)
                entry_TipCA[i].edit_modified(False)

            if entry_TipCA[i].edit_modified():
                entry_Tip[i].delete(1.0, END)
                entry_Tip[i].insert(INSERT, math.floor(int(float(entry_Object[i].getTipCA()) * 0.73)))
                entry_Tip[i].edit_modified(False)
                entry_TipCA[i].edit_modified(False)

            if entry_PriceCA[i].edit_modified():
                entry_Price[i].delete(1.0, END)
                entry_Price[i].insert(INSERT, math.floor(int(float(entry_Object[i].getPriceCA()) * 0.73)))
                entry_Price[i].edit_modified(False)
                entry_PriceCA[i].edit_modified(False)
            
            if entry_Price[i].edit_modified():
                entry_PriceCA[i].delete(1.0, END)
                entry_PriceCA[i].insert(INSERT, math.floor(int(float(entry_Object[i].getPrice()) * conv)))
                entry_PriceCA[i].edit_modified(False)
                entry_Price[i].edit_modified(False)

        return

    #Clears edit, goes back to main page
    def destroyEditFrame():
        #Save Changes
        save()
        bg_edit.destroy()
        button_exit.destroy()
        button_update.destroy()
        name_tag.destroy()
        comm_tag.destroy()
        price_tag.destroy()
        tip_tag.destroy()
        title.destroy()
        us2.destroy()
        cad2.destroy()
        for i in range(0,len(entry_Comm)):
            entry_Name[i].destroy()
            entry_Comm[i].destroy()
            entry_Price[i].destroy()
            entry_Tip[i].destroy()
            entry_Flag[i].destroy()
            entry_FlagTip[i].destroy()
            entry_PriceCA[i].destroy()
            entry_TipCA[i].destroy()

    #X,Y Axis for editable items
    nextRowReady = True
    count = 0
    yaxis = 130
    xaxis = 40

    entry_Name = []
    entry_Comm = []
    entry_Price = []
    entry_Tip = []
    entry_PriceCA = []
    entry_TipCA = []
    entry_Flag = []
    entry_FlagTip = []
    entry_Object = [0] * len(app.ClientObj) 

    bg_edit = Label(window,
                    image = photo_edit)

    title = Label(window, 
                  text = "Edit Comm Information", 
                  font = ("Helvetica", 40))

    name_tag = Label(window, 
                  text = "NAME", 
                  fg = "blue",
                  font = ("Helvetica", 25))
    
    comm_tag = Label(window, 
                  text = "COMM CODE", 
                  fg = "blue",
                  font = ("Helvetica", 25))


    price_tag = Label(window, 
                  text = "TOTAL USD", 
                  fg = "blue",
                  font = ("Helvetica", 15))

    tip_tag = Label(window, 
                  text = "TIP IN USD/CAD", 
                  fg = "blue",
                  font = ("Helvetica", 15))

    button_exit =  Button(window, 
                          image = photo_check,
                          height = 70,
                          width = 70,
                          command = destroyEditFrame)
    
    button_update =  Button(window, 
                            image = photo_saveIcon,
                            height = 70,
                            width = 70,
                            command =update)
    
    us = Label(window, 
           image = photo_USA, 
           width = 52,
           height = 25
          )
    
    cad = Label(window, 
           image = photo_CAD, 
           width = 52,
           height = 25
          )
    
    us2 = Label(window, 
           image = photo_USA, 
           width = 52,
           height = 25
          )
    
    cad2 = Label(window, 
           image = photo_CAD, 
           width = 52,
           height = 25
          )
    
    for i in app.ClientObj:
        if nextRowReady and count >= 10:
            nextRowReady = not nextRowReady
            xaxis = 805
            yaxis = 130

        entry_Name.append(Text(window, 
                    width = 12, 
                    height = 1, 
                    font = ("Helvetica", 40),))

        entry_Comm.append(Text(window, 
                    width = 8, 
                    height = 1,
                    font = ("Helvetica", 40),))

        entry_Price.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 17),))
        
        entry_Tip.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 17),))
        
        entry_PriceCA.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 17),))
        
        entry_TipCA.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 17),))
        
        entry_Flag.append(us)
        
        if i.getPaymentType() == "SQUARE":
            entry_FlagTip.append(cad)
        else:
            entry_FlagTip.append(us)

        entry_Object[count] = (Overwrite([entry_Name[count],entry_Comm[count],entry_Price[count], entry_Tip[count], entry_PriceCA[count], entry_TipCA[count]], i, xaxis, yaxis))

        count += 1
        yaxis += 76

    bg_edit.place(x=0, y=0, relwidth=1, relheight=1)
    title.place(x=0, y=24)
    name_tag.place(x=-170, y=120)
    comm_tag.place(x=-410, y=120)
    price_tag.place(x=-640, y=110)
    tip_tag.place(x=-640, y=140)
    button_exit.place(x=560, y=20)
    button_update.place(x=806, y=20)
    us.place(x=645, y = 90)
    cad.place(x=710, y = 90)
    us2.place(x=1410, y = 90)
    cad2.place(x=1475, y = 90)

    return


#Updates the Prices
def editPrices():
    #X,Y Axis for editable items
    count = 0
    yaxis = 190
    xaxis = 250

    entry_Name = []
    entry_Base = []
    entry_Char = []
    entry_BG = []
    
    def save():
        final = ""
        for k in range(0,3):
            for i in entry_Prices:
                if k == 0:
                    final += str(i.getBase()) + "\n"
                if k == 1:
                    final += str(i.getChar()) + "\n"
                if k == 2:
                    final += str(i.getBG()) + "\n"
            final += "\n"
        
        f = open(price.findPath("\Scripts","\\Texts\MoneySheet.txt"), "w")
        f.write(final)
        f.close()
        price.readSheet()
        os.system('cls')
        names.printPrices(app.ClientObj)
        return

    #Clears edit, goes back to main page
    def destroyEditFrame():
        #Save Changes
        save()
        bg_edit.destroy()
        button_exit.destroy()
        title.destroy()
        comm.destroy()
        base.destroy()
        comm2.destroy()
        base2.destroy()
        for i in range(0,len(entry_Name)):
            entry_Name[i].destroy()
            entry_Base[i].destroy()
            entry_Char[i].destroy()
            entry_BG[i].destroy()

 
    bg_edit = Label(window,
                    image = photo_edit)

    title = Label(window, 
                  text = "Price Sheet", 
                  font = ("Helvetica", 50))

    button_exit =  Button(window, 
                          image = photo_check,
                          height = 130,
                          width = 130,
                          command = destroyEditFrame)

    comm =    (Label(window,
                    text = "Commission", 
                    width = 20, 
                    height = 1,
                    fg = "blue", 
                    bg = "gray",
                    font = ("Helvetica", 20),))

    base =    (Label(window,
                    text = "Base - Char - BG", 
                    width = 14, 
                    height = 1,
                    fg = "blue",
                    bg = "gray",
                    font = ("Helvetica", 20),))
    
    comm2 =    (Label(window,
                    text = "Commission", 
                    width = 20, 
                    height = 1,
                    fg = "blue", 
                    bg = "gray",
                    font = ("Helvetica", 20),))

    base2 =    (Label(window,
                    text = "Base - Char - BG", 
                    width = 14, 
                    height = 1,
                    fg = "blue",
                    bg = "gray",
                    font = ("Helvetica", 20),))

    comm.place(x = 250, y = 144)
    base.place(x = 575, y = 144)

    comm2.place(x = 850, y = 144)
    base2.place(x = 1175, y = 144)

    count = 0
    isNewLine = True

    for i in price.comm:

        if isNewLine and count == 15:
            isNewLine = False
            yaxis = 190
            xaxis = 850

        entry_Name.append(Label(window,
                    text = i, 
                    width = 20, 
                    height = 1,
                    bg = "gray", 
                    font = ("Helvetica", 20),))

        entry_Base.append(Text(window, 
                    width = 5, 
                    height = 1,
                    font = ("Helvetica", 20),))

        entry_Char.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 20),))

        entry_BG.append(Text(window, 
                    width = 4, 
                    height = 1,
                    font = ("Helvetica", 20),))

        entry_Prices[count] = (OverwritePrices([entry_Name[count],entry_Base[count],entry_Char[count],entry_BG[count]], i, xaxis, yaxis))

        count += 1
        yaxis += 45

    bg_edit.place(x=0, y=0, relwidth=1, relheight=1)
    title.place(x=0, y=24)
    button_exit.place(x=400, y=0)
    return

#Sends you to twitter
def link():
    webbrowser.open("https://www.twitter.com/5ushiroll", new=0, autoraise=True)
    return

#Sends you to Rickroll
def link2():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0, autoraise=True)
    return

def editPlace(x):
     api.sheetPlace += x
     if api.sheetPlace < 0:
         api.sheetPlace = 0
     counter.config(text = api.sheetPlace + 1)
     app.resetToUpdate()
     refresh()
     return

#Proportions of window, not allowed to resize
#window.geometry("1800x1100")
window.geometry("1590x900")
window.resizable(width=False, height=False)

#Title of program
window.title("5ushiroll Commission Program June 11 2023 Build")

#Create photos types
#Background images
photo = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Kai_and_Zero.png"))
photo = photo.subsample(2,2)

photo_edit = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Kai_Lightning.png"))
photo_edit = photo_edit.subsample(3,3)
#Blank Button
photo_blank = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Blank.png"))
#In Progress Button
photo_inprogress  = PhotoImage(file = names.findPath("\Scripts","\\Sprites/InProgress.png"))
#Completed button
photo_completed   = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Completed.png"))
#Color Boxes
photo_bluebox     = PhotoImage(file = names.findPath("\Scripts","\\Sprites/BlueBox.png"))
photo_yellowbox   = PhotoImage(file = names.findPath("\Scripts","\\Sprites/YellowBox.png"))
photo_redbox      = PhotoImage(file = names.findPath("\Scripts","\\Sprites/RedBox.png"))
photo_paymentplan = PhotoImage(file = names.findPath("\Scripts","\\Sprites/PaymentPlan.png"))
photo_blackbox    = PhotoImage(file = names.findPath("\Scripts","\\Sprites/BlackBox.png"))
#Image of clipboard
photo_clip  = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Clipboard.png"))
photo_clip  = photo_clip.subsample(resize,resize)
#Image of Sheets
photo_sheet = PhotoImage(file = names.findPath("\Scripts","\\Sprites/GoogleSheets.png"))
photo_sheet = photo_sheet.subsample(21,21)
#Image of Carrd
photo_carrd = PhotoImage(file = names.findPath("\Scripts","\\Sprites/CarrdLogo.png"))
photo_carrd = photo_carrd.subsample(10,10)
#Image of Clear
photo_sweep = PhotoImage(file = names.findPath("\Scripts","\\Sprites/sweep.png"))
photo_sweep = photo_sweep.subsample(7,7)
#Image of Reset
photo_power = PhotoImage(file = names.findPath("\Scripts","\\Sprites/restart.png"))
photo_power = photo_power.subsample(15,15)
#Image of Pencil
photo_pencil = PhotoImage(file = names.findPath("\Scripts","\\Sprites/pencil.png"))
photo_pencil = photo_pencil.subsample(18,18)
#Image of Green Checkmark
photo_check = PhotoImage(file = names.findPath("\Scripts","\\Sprites/green_check.png"))
photo_check = photo_check.subsample(20,20)
#Image of CSV File
photo_csv = PhotoImage(file = names.findPath("\Scripts","\\Sprites/csv.png"))
photo_csv = photo_csv.subsample(5,5)
#Image of Dollar sign
photo_dollar = PhotoImage(file = names.findPath("\Scripts","\\Sprites/dollar.png"))
photo_dollar = photo_dollar.subsample(5,5)
#Image of Twitter
photo_twitter = PhotoImage(file = names.findPath("\Scripts","\\Sprites/twitter.png"))
photo_twitter = photo_twitter.subsample(16,16)
#Image of Sus
photo_amogus = PhotoImage(file = names.findPath("\Scripts","\\Sprites/amogus.png"))
photo_amogus = photo_amogus.subsample(12,12)

#Image of USA
photo_USA = PhotoImage(file = names.findPath("\Scripts","\\Sprites/USFlag.png"))
photo_USA = photo_USA.subsample(8,8)

#Image of CAD
photo_CAD = PhotoImage(file = names.findPath("\Scripts","\\Sprites/CanadaFlag.png"))
photo_CAD = photo_CAD.subsample(8,8)

#Image of LeftArrow
photo_LArrow = PhotoImage(file = names.findPath("\Scripts","\\Sprites/LeftArrow.png"))
photo_LArrow = photo_LArrow.subsample(60,80)

#Image of RightArrowe
photo_RArrow = PhotoImage(file = names.findPath("\Scripts","\\Sprites/RightArrow.png"))
photo_RArrow = photo_RArrow.subsample(60,80)

#Image of FastForward
photo_FFArrow = PhotoImage(file = names.findPath("\Scripts","\\Sprites/FastForward.png"))
photo_FFArrow = photo_FFArrow.subsample(3,3)

#Image of FastRewind
photo_BBArrow = PhotoImage(file = names.findPath("\Scripts","\\Sprites/FastRewind.png"))
photo_BBArrow = photo_BBArrow.subsample(3,3)

#Image of Save
photo_saveIcon = PhotoImage(file = names.findPath("\Scripts","\\Sprites/Save.png"))
photo_saveIcon = photo_saveIcon.subsample(6,6)

progressDict = { 
        True : "#5094d1",
        False : "black",
        "BLANK": photo_blank,
        "IN PROGRESS": photo_inprogress,
        "COMPLETED": photo_completed,
        "BLACK" : photo_blackbox,
        "YELLOW" : photo_yellowbox,
        "RED" : photo_redbox,
        "PAYMENT PLAN" : photo_paymentplan,
        "BLUE" : photo_bluebox
    }

#Background image (Made by 5ushiroll)
bg_image = Label(window,
                 image = photo)

#Title
title = Label(window, 
              text = "Sushi's Commissions", 
              font = ("Helvetica", 48))

#Clipboard Button
button_carrd =    Button(window, 
                       command=click,
                       image = photo_carrd,
                       bg = "#E3BEEA",
                       height = 120,
                       width = 120)

#Sheet Button
button_sheets =   Button(window, 
                       command=click2,
                       image = photo_sheet,
                       bg = "#E3BEEA",
                       height = 120,
                       width = 120)

#Refresh Button
button_refresh =  Button(window, 
                       image = photo_csv,
                       height = 120,
                       width = 250,
                       bg = "#5094d1",
                       command = CSVRefresh)
 
#Clear the board Button
button_sweep =  Button(window, 
                       image = photo_sweep,
                       bg = "#c9d7e9",
                       height = 120,
                       width = 76,
                       command = clear)

#Restart Button
button_restart= Button(window, 
                       image = photo_power,
                       bg = "#c9d7e9",
                       height = 120,
                       width = 76,
                       command = restart)

#Edit Button
button_edit =  Button(window, 
                       image = photo_pencil,
                       bg = "#c9d7e9",
                       height = 120,
                       width = 76,
                       command = edit)

#Clear the board Button
button_dollar =  Button(window, 
                        
                       image = photo_dollar,
                       bg = "#c9d7e9",
                       height = 120,
                       width = 76,
                       command = editPrices,
                       )

#Counter
counter = Label(window, 
              text = api.sheet()+1,
              height = 1,
              width = 4, 
              font = ("Helvetica", 25))

#Left Arrow
button_left =  Button(window, 
                       image = photo_LArrow,
                       bg = "#3187F6",
                       height = 40,
                       width = 40,
                       command = lambda: editPlace(-1),
                       )

#Right Arrow
button_right =  Button(window, 
                       image = photo_RArrow,
                       bg = "#3187F6",
                       height = 40,
                       width = 40,
                       command = lambda: editPlace(1),
                       )

#Fast Forward Arrow
button_ff =  Button(window, 
                       image = photo_FFArrow,
                       bg = "#3187F6",
                       height = 40,
                       width = 40,
                       command = lambda: editPlace(5),
                       )

#Fast Rewind Arrow
button_bb =  Button(window, 
                       image = photo_BBArrow,
                       bg = "#3187F6",
                       height = 40,
                       width = 40,
                       command = lambda: editPlace(-5),
                       )


#Twitter
button_twitter =     Button(window, 
                       command=save,
                       image = photo_saveIcon,
                       bg = "#c9d7e9",
                       height = 120,
                       width = 76)

#Rickroll
button_amogus =     Button(window, 
                       command=link2,
                       image = photo_amogus,
                       height = 76,
                       width = 76)


#Background, BG Image
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

#Top Left, Title
title.place(x=0, y=24)

adjust = 187

#Top Middle, Sweep, Restart, Edit Names, Edit Prices, Twitter
#button_sweep.place(x=740, y=0)
button_restart.place(x=835-adjust, y=0)
button_edit.place(x=930-adjust, y=0)
button_dollar.place(x=1025-adjust, y=0)
button_twitter.place(x=1120-adjust, y=0)

#us.place(x=0,y=0)

#Middle, main
#Generate the Names, Subscriber, and Progress buttons
createButtons()

#Top Middle Large, Google Sheet and Carrd
button_sheets.place(x=1220-adjust, y=0)
button_carrd.place(x=1365-adjust, y=0)

#Top Right, Update CSV
button_refresh.place(x=1506-adjust, y=0)
button_left.place(x=1548-adjust, y=125)
button_bb.place(x=1506-adjust, y=125)
button_right.place(x=1674-adjust, y=125)
button_ff.place(x=1716-adjust, y=125)
counter.place(x=1593-adjust, y=125)

#Bottom Left, sus
button_amogus.place(x=0, y=1020)

window.mainloop()