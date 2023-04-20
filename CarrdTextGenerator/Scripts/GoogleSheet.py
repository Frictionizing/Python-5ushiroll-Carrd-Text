import MasterClientList as data
import math
import pyperclip

#Price function
def maffs(i):
    ans = i.getPrice()

    if i.getPaymentType() == "SQUARE":
        try:
            ans = math.floor(1.3 * float(ans))
        except:
            print("ERROR EDIT: " + i.getName() + " had price of " + ans + ", resetted to $0")
            return "0.00"
        
    ans += i.getTip()
    
    return str(ans) + ".00"

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
    c = i.getButton().currentColor()
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
    test = data.ClientObj

    for i in test: 
        final += i.getName() + nextCell
        final += i.getShortName() + nextCell
        final += "$" + maffs(i) + nextCell
        final += payment(i) + nextCell
        final += reorder(i) + nextCell
        final += reorder2(i) + newLine
        h += 1

    pyperclip.copy(final)