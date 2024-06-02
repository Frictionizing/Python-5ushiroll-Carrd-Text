import MasterClientList as data
import CommissionPrices as price
import math
import pyperclip

#Price function
def maffs(i, flag):
    ans = int(i.getPrice())

    if i.getPaymentType() == "SQUARE":
        try:
            ans = int(math.floor(price.cashConvert["SQUARE"] * float(ans)))
        except:
            print("ERROR EDIT: " + i.getName() + " had price of " + ans + ", resetted to $0")
            return "0.00"
        
    if flag:
        ans += int(i.getTip())
    
    return str(ans)

def gst(i):
    e = int(i)

    e *= 100
    e *= 0.05
    e /= 100

    return str(e)


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
        final += "$" + maffs(i, True) + nextCell
        final += "$" + gst(maffs(i, False)) + nextCell
        final += payment(i) + nextCell
        final += reorder(i) + nextCell
        final += reorder2(i) + newLine
        h += 1

    pyperclip.copy(final)