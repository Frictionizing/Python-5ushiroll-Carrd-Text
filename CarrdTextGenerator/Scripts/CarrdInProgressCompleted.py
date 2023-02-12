import CarrdGenerator as script1
import MasterClientList as app
from tkinter import *

Client = app.ClientObj

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

def concatenate(x):
    string = ""
    for i in x:
        string += i
    return string

def createButtonObjects():
    buttons = []
    for i in range (0,app.commLen(Client)):
        if i == 20:
            break
        buttons.append(ButtonMode(i, Client[i].getState(), Client[i].getColor()))
    return buttons

def appendProgress(mode):
    inProgress = " [==IN PROGRESS==]{orange}"
    complete   = " [==COMPLETED==]{lime}"
    list2= []
    write = ""
    colorWrite = ""

    for i in range(0,app.commLen(Client)):

        name = Client[i].getName()

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

        list2.append(dic[buttonList[i].currentColor()] + Client[i].getNewType() + dic[mode[i].currentMode()] + "\n")

        write += mode[i].currentMode() + "\n"
        colorWrite += mode[i].currentColor() + "\n"

    for i in range(app.commLen(Client), 20):
        write += "BLANK" + "\n"
        colorWrite += "BLACK" + "\n"

    return list2

buttonList = createButtonObjects()