import CarrdGenerator as data
import CommissionPrices as prices
import CarrdInProgressCompleted as buttons
import math
import pyperclip

#Price function
def maffs(i):
    ans = prices.priceDict[i.getType()] + (prices.charDict[i.getType()] * (i.getCharNum()-1))
    if i.getComplex():
        ans += prices.bgDict[i.getType()]

    if i.getPaymentType() == "SQUARE":
        ans = math.floor(1.3 * ans)
    return str(ans) + ".00"

#Shortened form with plural cases
def shortenedComm(i):

    exemptList = ["GACH-3","GACH-4","GACH-5","GACH-6", "Full-Ren"]

    name = prices.shortDict[i.getType()]
    if (name == "BAN" or name == "MAW" or name == "COS") and i.getCharNum() >= 2:
        name += "-w/charas"
    elif (name == "CS-H" or name == "CS-HB" or name == "CS-FB" or name == "RH") and i.getCharNum() >= 2:
        name += "s"

    if i.getComplex() and name not in exemptList:
        name += "-CB"

    return name

def reorder(i):
    if i.getPaymentType() == "SQUARE":
        return "Square"
    elif i.getPaymentType() == "PAYPAL":
        return "PayPal"
    return "error"

def reorder2(i):
    if i.getPaymentType() == "SQUARE":
        return ""
    elif i.getPaymentType() == "PAYPAL":
        return "USD"
    return "error"

#Returns whether commission is paid for or not, or on a payment plan
def payment(i):
    c = buttons.buttonList[i].currentColor()
    if c == "BLACK" or c == "BLUE":
        return "Y"
    elif  c == "YELLOW" or c == "RED":
        return "N"
    elif  c == "PAYMENT PLAN":
        return "PP"
    return "ERROR"

#Copy pasted sheet
def sheet():
    nextCell = "	"
    newLine  = "\n"
    final    = ""

    h = 0
    test = data.Applications

    for i in test: 
        final += i.getName() + nextCell
        final += shortenedComm(i) + nextCell
        final += "$" + maffs(i) + nextCell
        final += payment(h) + nextCell
        final += reorder(i) + nextCell
        final += reorder2(i) + newLine
        h += 1

    pyperclip.copy(final)