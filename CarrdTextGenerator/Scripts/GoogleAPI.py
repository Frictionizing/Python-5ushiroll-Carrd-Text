import os
import CarrdGenerator as cg

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1V-1TYs_boAOkuJ2pKjk_O11OPlay63NhdBnQds95WzI"

sheetPlace = 50
ClientQueue = []
ClientQueue_NoSub = []

def main():
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
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Form Responses 1").execute()
        values = result.get("values", [])

        result2 = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="APIStuff").execute()
        save_file = result2.get("values", [])

        #test = save_file[52][3].split(",")



        #Counter for the start of commissions
        k = sheetPlace

        #20 counter
        max_of_20 = 0

        for i in values[sheetPlace:]:
            name = cg.shortenName(i[2])
            isSub = cg.convertBool(i[3])
            comm = cg.commishType(i[4],i[6],i[7])
            isBG = cg.convertBool(i[10])
            charNum = cg.parseInt(i[7])
            pay = cg.shortenPayment(i[12])

            pack = [name, isSub, comm, isBG, charNum, pay, k]

            #Turn application into Client object
            cli = cg.Client(pack)

            if save_file[k]:
                cli.overrideName(save_file[k][0])
                info = save_file[k][1].split(",")
                cli.overridePrice(info[1])
                cli.overrideTip(info[2])
                cli.overrideState(info[3])
                cli.overrideColor(info[4])
            else:
                save_file[k].append(name)

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

        for i in entry:
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range = f"APIStuff!A{i.getCustomer()}", valueInputOption="USER_ENTERED", body = {"values":[[i.getName()]]}).execute()
            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range = f"APIStuff!B{i.getCustomer()}", valueInputOption="USER_ENTERED", body = {"values":[[i.getShortName() + "," + i.getPrice() + "," + i.getTip() + "," + i.getState() + "," + i.getColor()]]}).execute()

    except HttpError as error:
        print(error)
        pass


