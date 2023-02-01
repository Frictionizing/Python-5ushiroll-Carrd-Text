import CarrdGenerator as script1
from tkinter import *

#with open(r'C:/Users/Brian/Documents/Python/CarrdTextGenerator/Texts/TextOutput.txt') as f:
with open(script1.findPath("\Scripts","\\Texts\TextOutput.txt")) as f:
    lines = f.readlines()
f.close()

#with open(r'C:/Users/Brian/Documents/Python/CarrdTextGenerator/Texts/SaveFile.txt') as f:
with open(script1.findPath("\Scripts","\\Texts\SaveFile.txt")) as f:
    save = f.readlines()
f.close()

#with open(r'C:/Users/Brian/Documents/Python/CarrdTextGenerator/Texts/SaveColors.txt') as f:
with open(script1.findPath("\Scripts","\\Texts\SaveColors.txt")) as f:
    colorSave = f.readlines()
f.close()

class ButtonMode:
    def __init__(x, i, save, colorsave):
        x.mode = save
        x.placement = i
        x.color = colorsave

    def currentMode(x):
        return x.mode
    def currentPlacement(x):
        return x.placement
    def reset(x):
        x.mode = "BLANK"
    def currentColor(x):
        return x.color
    def changeMode(x):
        change = {
            "BLANK" : "IN PROGRESS",
            "IN PROGRESS" : "COMPLETED",
            "COMPLETED" : "BLANK"
        }
        x.mode = change[x.mode]
    def changeColorOverride(x, i):
        x.color = i
    def changeColor(x):
        change = {
            "BLACK" : "YELLOW",
            "BLUE"  : "YELLOW",
            "YELLOW" : "RED",
            "RED" : "PAYMENT PLAN",
            "PAYMENT PLAN" : "BLACK"
        }
        x.color = change[x.color]

def writeToFile(x, i):
    f = open(script1.findPath("\Scripts","\\Texts\SaveFile.txt"), "w")
    f.write(x)
    f.close()

    f = open(script1.findPath("\Scripts","\\Texts\SaveColors.txt"), "w")
    f.write(i)
    f.close()

def concatenate(x):
    string = ""
    for i in x:
        string += i
    return string

def createButtonObjects():
    buttons = []
    for i in range (0,len(lines)):
        if i == 20:
            break
        buttons.append(ButtonMode(i, save[i][:-1], colorSave[i][:-1]))
    return buttons

def appendProgress(mode):
    inProgress = " [==IN PROGRESS==]{orange}"
    complete   = " [==COMPLETED==]{lime}"
    list = []
    list2= []
    write = ""
    colorWrite = ""

    for i in range(0,len(lines)):
        list.append(lines[i])

        name = script1.Applications[i].getName()

        dic = {
            "BLANK" : "",
            "IN PROGRESS" : inProgress,
            "COMPLETED" : complete,
            "RED" : "[" + name + "]{red}: ",
            "YELLOW" : "[" + name + "]{yellow}: ",
            "BLUE" : "[" + name + "]{cyan}: ",
            "BLACK" : name + ": ",
            "PAYMENT PLAN" : "!" + name + ": "
        }

        list2.append(dic[buttonList[i].currentColor()] + script1.Applications[i].getNewType() + dic[mode[i].currentMode()] + "\n")

        write += mode[i].currentMode() + "\n"
        colorWrite += mode[i].currentColor() + "\n"

    for i in range(len(lines), 20):
        write += "BLANK" + "\n"
        colorWrite += "BLACK" + "\n"

    writeToFile(write, colorWrite)
    return list2

buttonList = createButtonObjects()