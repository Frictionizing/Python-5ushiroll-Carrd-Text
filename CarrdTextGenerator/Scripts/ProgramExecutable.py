import MasterClientList as app
import CarrdInProgressCompleted as carrd
import CarrdGenerator as names
import GoogleSheet as goog
import CommissionPrices as price
import webbrowser
from tkinter import *
import os
import pyperclip

maxComm = 20
complete   = " [==COMPLETED==]{lime}"
inProgress = " [==IN PROGRESS==]{orange}"
buttonDict = {}
name_label = {}
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
    yaxis = 150
    xaxis = 0
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

        def convertColor(x=i):
            carrd.buttonList[x].changeColor()
            if carrd.buttonList[x].currentColor() == "BLACK" and app.ClientObj[x].getSub():
                carrd.buttonList[x].changeColorOverride("BLUE")
            colorDict[x].configure(image = progressDict[carrd.buttonList[x].currentColor()])
            app.ClientObj[x].overrideColor(carrd.buttonList[x].currentColor())
            app.writeSave()

        #If more than half commissions, continue on the right side
        if nextRowReady and i >= 10:
            nextRowReady = not nextRowReady
            xaxis = 900
            yaxis = 150

        #List of names
        name_label[i] = Label(window,
                           text = str(i+1) + ". " +  app.ClientObj[i].getName(),
                           font = ("Helvetica", 40),
                           fg = progressDict[app.ClientObj[i].getSub()])
        name_label[i].place(x=xaxis + 10, y=yaxis)

        #List of progress buttons
        buttonDict[i] = Button(window, 
                               command = convertMode,
                               image = progressDict[app.ClientObj[i].getState()])
        buttonDict[i].place(x=680 + xaxis, y=yaxis)

        #Override SubscriberStar color to blue
        if carrd.buttonList[i].currentColor() == "BLACK" and app.ClientObj[i].getSub():
            carrd.buttonList[i].changeColorOverride("BLUE")
        #List of color overlay buttons
        colorDict[i] = Button(window, 
                              command = convertColor,
                              image = progressDict[app.ClientObj[i].getColor()])
        colorDict[i].place(x=605 + xaxis, y=yaxis)
        

        #Move the Y axis every iteration (resets at the halfway point)
        yaxis += 80

#Refreshes the whole page for new CSV information
def refresh():
    for i in range(0, len(name_label)):
        name_label[i].destroy()
        buttonDict[i].destroy()
        colorDict[i].destroy()

    app.appendNewComms()
    carrd.buttonList = carrd.createButtonObjects()
    consolidateObjects(app.ClientObj)
    createButtons()

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
        app.x     = xaxis
        app.y     = yaxis

        app.name.place(x=0 + xaxis, y = yaxis)
        app.name.insert(INSERT, i.getName())

        app.comm.place(x=455 + xaxis, y = yaxis)
        app.comm.insert(INSERT, i.getShortName())

        app.price.place(x=770 + xaxis, y = yaxis)
        app.price.insert(INSERT, i.getPrice())

    def getName(app):
        return app.name.get("1.0", "end-1c")
    def getComm(app):
        return app.comm.get("1.0", "end-1c")
    def getPrice(app):
        return app.price.get("1.0", "end-1c")

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
        return app.base.get("1.0", "end-1c")
    def getChar(app):
        try:
            i = int(app.char.get("1.0", "end-1c"))
        except:
            return str(0)
        return app.char.get("1.0", "end-1c")
    def getBG(app):
        try:
            i = int(app.BG.get("1.0", "end-1c"))
        except:
            return str(0)
        return app.BG.get("1.0", "end-1c")

#Overrides the Script with handmade edits
def edit():
    
    def save():
        for i in range(0,len(app.ClientObj)):
            app.ClientObj[i].OverrideComm(entry_Object[i].getName(),entry_Object[i].getComm(),entry_Object[i].getPrice())
            name_label[i].config(text = str(i+1) + ". " + app.ClientObj[i].getName())
        app.writeSave()
        return

    #Clears edit, goes back to main page
    def destroyEditFrame():
        #Save Changes
        save()
        bg_edit.destroy()
        button_exit.destroy()
        name_tag.destroy()
        comm_tag.destroy()
        price_tag.destroy()
        title.destroy()
        for i in range(0,len(entry_Comm)):
            entry_Name[i].destroy()
            entry_Comm[i].destroy()
            entry_Price[i].destroy()

    #X,Y Axis for editable items
    nextRowReady = True
    count = 0
    yaxis = 150
    xaxis = 10

    entry_Name = []
    entry_Comm = []
    entry_Price = []
    entry_Object = [0] * len(app.ClientObj) 

    bg_edit = Label(window,
                    image = photo_edit)

    title = Label(window, 
                  text = "Edit Comm Information", 
                  font = ("Helvetica", 50))

    name_tag = Label(window, 
                  text = "NAME", 
                  fg = "blue",
                  font = ("Helvetica", 30))
    
    comm_tag = Label(window, 
                  text = "COMM", 
                  fg = "blue",
                  font = ("Helvetica", 30))

    price_tag = Label(window, 
                  text = "USD", 
                  fg = "blue",
                  font = ("Helvetica", 30))

    button_exit =  Button(window, 
                          image = photo_check,
                          height = 130,
                          width = 130,
                          command = destroyEditFrame)
    print(len(app.ClientObj))
    for i in app.ClientObj:
        if nextRowReady and count >= 10:
            nextRowReady = not nextRowReady
            xaxis = 900
            yaxis = 150

        entry_Name.append(Text(window, 
                    width = 15, 
                    height = 1, 
                    font = ("Helvetica", 40),))

        entry_Comm.append(Text(window, 
                    width = 10, 
                    height = 1,
                    font = ("Helvetica", 40),))

        entry_Price.append(Text(window, 
                    width = 3, 
                    height = 1,
                    font = ("Helvetica", 40),))

        entry_Object[count] = (Overwrite([entry_Name[count],entry_Comm[count],entry_Price[count]], i, xaxis, yaxis))

        count += 1
        yaxis += 80

    bg_edit.place(x=0, y=0, relwidth=1, relheight=1)
    title.place(x=0, y=0)
    name_tag.place(x=160, y=90)
    comm_tag.place(x=550, y=90)
    price_tag.place(x=780, y=90)
    button_exit.place(x=900, y=0)
    return

#Updates the Prices
def editPrices():
    #X,Y Axis for editable items
    count = 0
    yaxis = 190
    xaxis = 650

    entry_Name = []
    entry_Base = []
    entry_Char = []
    entry_BG = []
    
    def save():
        return

    #Clears edit, goes back to main page
    def destroyEditFrame():
        #Save Changes
        save()
        bg_edit.destroy()
        button_exit.destroy()
        title.destroy()
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
                
    for i in price.comm:
        """
        if nextRowReady and count >= 10:
            nextRowReady = not nextRowReady
            xaxis = 900
            yaxis = 150
        """
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
    title.place(x=0, y=0)
    button_exit.place(x=900, y=0)
    return

#Sends you to twitter
def link():
    webbrowser.open("https://www.twitter.com/5ushiroll", new=0, autoraise=True)
    return

#Sends you to Rickroll
def link2():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=0, autoraise=True)
    return


#Proportions of window, not allowed to resize
window.geometry("1800x1100")
window.resizable(width=False, height=False)

#Title of program
window.title("SussyExecutable")

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
photo_sheet = photo_sheet.subsample(22,22)
#Image of Carrd
photo_carrd = PhotoImage(file = names.findPath("\Scripts","\\Sprites/CarrdLogo.png"))
photo_carrd = photo_carrd.subsample(10,10)
#Image of Reset
photo_sweep = PhotoImage(file = names.findPath("\Scripts","\\Sprites/sweep.png"))
photo_sweep = photo_sweep.subsample(7,7)
#Image of Power
photo_power = PhotoImage(file = names.findPath("\Scripts","\\Sprites/restart.png"))
photo_power = photo_power.subsample(5,5)
#Image of Pencil
photo_pencil = PhotoImage(file = names.findPath("\Scripts","\\Sprites/pencil.png"))
photo_pencil = photo_pencil.subsample(5,5)
#Image of Green Checkmark
photo_check = PhotoImage(file = names.findPath("\Scripts","\\Sprites/green_check.png"))
photo_check = photo_check.subsample(20,20)
#Image of CSV File
photo_csv = PhotoImage(file = names.findPath("\Scripts","\\Sprites/csv.png"))
photo_csv = photo_csv.subsample(5,5)
#Image of Dollar sign
photo_dollar = PhotoImage(file = names.findPath("\Scripts","\\Sprites/dollar.png"))
photo_dollar = photo_dollar.subsample(15,15)
#Image of Twitter
photo_twitter = PhotoImage(file = names.findPath("\Scripts","\\Sprites/twitter.png"))
photo_twitter = photo_twitter.subsample(12,12)
#Image of Sus
photo_amogus = PhotoImage(file = names.findPath("\Scripts","\\Sprites/amogus.png"))
photo_amogus = photo_amogus.subsample(8,8)

progressDict = { 
        True : "blue",
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
bg_image.place(x=0, y=0, relwidth=1, relheight=1)

#Title
title = Label(window, 
              text = "5ushiroll Text Generator", 
              font = ("Helvetica", 50))
title.place(x=0, y=0)

#Generate the Names, Subscriber, and Progress buttons
createButtons()

#Clipboard Button
button_carrd =    Button(window, 
                       command=click,
                       image = photo_carrd,
                       height = 130,
                       width = 130)

#Sheet Button
button_sheets =   Button(window, 
                       command=click2,
                       image = photo_sheet,
                       height = 130,
                       width = 130)

#Edit Button
button_edit =  Button(window, 
                       image = photo_pencil,
                       height = 76,
                       width = 76,
                       command = edit)

#Refresh Button
button_refresh =  Button(window, 
                       image = photo_csv,
                       height = 120,
                       width = 250,
                       command = refresh)

#Restart Button
button_restart= Button(window, 
                       image = photo_power,
                       height = 76,
                       width = 76,
                       command = restart)

#Clear the board Button
button_sweep =  Button(window, 
                       image = photo_sweep,
                       height = 76,
                       width = 76,
                       command = clear)

#Clear the board Button
button_dollar =  Button(window, 
                       image = photo_dollar,
                       height = 76,
                       width = 76,
                       command = editPrices)

#Twitter
button_twitter =     Button(window, 
                       command=link,
                       image = photo_twitter,
                       height = 130,
                       width = 130)

#Twitter
button_amogus =     Button(window, 
                       command=link2,
                       image = photo_amogus,
                       height = 130,
                       width = 130)


#Top Middle, Sweep, Restart, Edit Names, Edit Prices
button_sweep.place(x=740, y=0)
button_restart.place(x=840, y=0)
button_edit.place(x=940, y=0)
button_dollar.place(x=1040, y=0)

#Top Right, Update CSV
button_refresh.place(x=1506, y=0)

#Bottom Left, Twitter redirect and sus
button_twitter.place(x=150, y=965)
button_amogus.place(x=300, y=965)

#Bottom Right, Google Sheet and Carrd
button_sheets.place(x=1350, y=965)
button_carrd.place(x=1500, y=965)

window.mainloop()