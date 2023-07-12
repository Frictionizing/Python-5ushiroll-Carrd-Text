import os
import CarrdGenerator as cg

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1V-1TYs_boAOkuJ2pKjk_O11OPlay63NhdBnQds95WzI"

sheetPlace = 0
values = []
save_file = []

#X is flag for whether to use the sheetnumber from Googlesheets or whether to use the local sheetNumber; x is 0 at initialization to grab from GS
def main(x):
    ClientQueue = []
    ClientQueue_NoSub = []
    credentials = None

    if os.path.exists("token.json"):
        try:
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        except:
            print("Expired Token. Requires New Login")
    
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            flow = InstalledAppFlow.from_client_secrets_file(cg.findPath("\Scripts","\\GoogleSheetAPI.json"), SCOPES)
            credentials = flow.run_local_server(port = 0)
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cg.findPath("\Scripts","\\GoogleSheetAPI.json"), SCOPES)
            credentials = flow.run_local_server(port = 0)
        
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        global sheetPlace

        if x == 0:
            sheetPlace = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="APIStuff!F1").execute().get("values")[0][0])

        global values
        global save_file

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Form Responses 1").execute()
        values = result.get("values", [])

        result2 = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="APIStuff").execute()
        save_file = result2.get("values", [])

        for i in range (0,10000):
            save_file.append([])

        #Counter for the start of commissions
        k = sheetPlace

        #20 counter
        max_of_20 = 0

        for i in values[sheetPlace:]:
            i.append("")
            i.append("")
            i.append("")
            i.append("")

            if i == ['','','','']:
                continue
                
            name = cg.shortenName(i[2])
            isSub = cg.convertBool(i[3])
            comm = cg.commishType(i[4],i[6],i[15])
            isBG = cg.convertBool(i[8])
            charNum = cg.parseInt(i[7])
            pay = cg.shortenPayment(i[12])

            pack = [name, isSub, comm, isBG, charNum, pay, k]

            #Turn application into Client object
            cli = cg.Client(pack)

            if save_file[k] != []:
                info = save_file[k][0].split(",")
                cli.overrideName(info[0])
                cli.overridePrice(info[2])
                cli.overrideTip(info[3])
                cli.overrideState(info[4])
                cli.overrideColor(info[5])
            else:
                save_file[k].append(name + "," + cli.getShortName() + "," + str(cli.getPrice()) + "," + str(cli.getTip()) + "," + cli.getState() + "," + cli.getColor())

            k += 1
            max_of_20 += 1

           #Append to seperate queue depending on SubsriberStar status
            if cli.getSub():
               ClientQueue.append(cli)
            else:
               ClientQueue_NoSub.append(cli)

            if max_of_20 == 20:
                break

        for i in ClientQueue_NoSub:
            ClientQueue.append(i)

        return ClientQueue

    except HttpError as error:
        print(error)
        pass


def refreshSheet():
    global sheetPlace
    global values
    global save_file
    ClientQueue = []
    ClientQueue_NoSub = []
    max_of_20 = 0
    k = sheetPlace

    for i in values[sheetPlace:]:
        i.append("")
        i.append("")
        i.append("")
        i.append("")
        name = cg.shortenName(i[2])
        isSub = cg.convertBool(i[3])
        comm = cg.commishType(i[4],i[6],i[15])
        isBG = cg.convertBool(i[8])
        charNum = cg.parseInt(i[7])
        pay = cg.shortenPayment(i[12])

        if comm == "Error: See Remarks":
            continue

        else:
            pack = [name, isSub, comm, isBG, charNum, pay, k]

            #Turn application into Client object
            cli = cg.Client(pack)

            if save_file[k]:
                info = save_file[k][0].split(",")
                cli.overrideName(info[0])
                cli.overridePrice(info[2])
                cli.overrideTip(info[3])
                cli.overrideState(info[4])
                cli.overrideColor(info[5])
            else:
                save_file[k].append(name + "," + cli.getShortName() + "," + str(cli.getPrice()) + "," + str(cli.getTip()) + "," + cli.getState() + "," + cli.getColor())

            #Append to seperate queue depending on SubsriberStar status
            if cli.getSub():
                ClientQueue.append(cli)
            else:
                ClientQueue_NoSub.append(cli)

            if max_of_20 == 19:
                break

            max_of_20 += 1
            k+=1

    for i in ClientQueue_NoSub:
        ClientQueue.append(i)

    return ClientQueue

def update(entry):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cg.findPath("\Scripts","\\GoogleSheetAPI.json"), SCOPES)
            credentials = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range = f"APIStuff!F1", valueInputOption="USER_ENTERED", body = {"values":[[sheetPlace]]}).execute()

        for i in entry:
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range = f"APIStuff!A{i.getCustomer()}", valueInputOption="USER_ENTERED", body = {"values":[[i.getName() + "," + i.getShortName() + "," + str(i.getPrice()) + "," + 
                                                                                                                                                             str(i.getTip()) + "," + i.getState() + "," + i.getColor()]]}).execute()

    except HttpError as error:
        print(error)
        pass

def updateSingle(entry):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cg.findPath("\Scripts","\\GoogleSheetAPI.json"), SCOPES)
            credentials = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        sheets.values().update(spreadsheetId=SPREADSHEET_ID, range = f"APIStuff!A{entry.getCustomer()}", valueInputOption="USER_ENTERED", body = {"values":[[entry.getName() + "," + entry.getShortName() + "," + str(entry.getPrice()) + "," + 
                                                                                                                                                             str(entry.getTip()) + "," + entry.getState() + "," + entry.getColor()]]}).execute()

    except HttpError as error:
        print(error)
        pass

def sheet():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cg.findPath("\Scripts","\\GoogleSheetAPI.json"), SCOPES)
            credentials = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        i = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="APIStuff!F1").execute().get("values")[0][0])
        global sheetPlace
        sheetPlace = i
        return i


    
    except HttpError as error:
        print(error)
        pass
