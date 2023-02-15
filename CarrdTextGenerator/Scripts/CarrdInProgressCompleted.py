import CarrdGenerator as script1
import MasterClientList as app
from tkinter import *

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
    def changeModeOverride(x, i):
        x.mode = i
    def changeColor(x):
        change = {
            "BLACK" : "YELLOW",
            "BLUE"  : "YELLOW",
            "YELLOW" : "RED",
            "RED" : "PAYMENT PLAN",
            "PAYMENT PLAN" : "BLACK"
        }
        x.color = change[x.color]

def concatenate(x):
    string = ""
    for i in x:
        string += i
    return string

def createButtonObjects():
    buttons = []
    for i in range (0,app.commLen(app.ClientObj)):
        if i == 20:
            break
        buttons.append(ButtonMode(i, app.ClientObj[i].getState(), app.ClientObj[i].getColor()))
    return buttons

#Returns Carrd Copy Paste Text
def appendProgress(mode):
    Carrd = []

    for i in range(0,app.commLen(app.ClientObj)):

        name = app.ClientObj[i].getName()

        ColorCode = {
            "BLANK"        : "",
            "IN PROGRESS"  : " [==IN PROGRESS==]{orange}",
            "COMPLETED"    : " [==COMPLETED==]{lime}",
            "RED"          : "[" + name + "]{red}: ",
            "YELLOW"       : "[" + name + "]{yellow}: ",
            "BLUE"         : "[" + name + "]{cyan}: ",
            "BLACK"        : name + ": ",
            "PAYMENT PLAN" : "!" + name + ": "
        }

        Carrd.append(ColorCode[app.ClientObj[i].getColor()] + app.ClientObj[i].getNewType() + ColorCode[app.ClientObj[i].getState()] + "\n")

    return Carrd

buttonList = createButtonObjects()