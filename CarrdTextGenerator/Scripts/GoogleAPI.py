import os
import pathlib
import CarrdGenerator as cg

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1V-1TYs_boAOkuJ2pKjk_O11OPlay63NhdBnQds95WzI"

sheetPlace = 58
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

        for i in values[sheetPlace:]:
            name = cg.shortenName(i[2])
            isSub = cg.convertBool(i[3])
            comm = cg.commishType(i[4],i[6],i[7])
            isBG = cg.convertBool(i[10])
            charNum = cg.parseInt(i[7])
            pay = cg.shortenPayment(i[12])

            pack = [name, isSub, comm, isBG, charNum, pay]

            #Turn application into Client object
            cli = cg.Client(pack)

           #Append to seperate queue depending on SubsriberStar status
            if cli.getSub():
               ClientQueue.append(cli)
            else:
               ClientQueue_NoSub.append(cli)

        for i in ClientQueue_NoSub:
            ClientQueue.append(i)

        return ClientQueue

    except HttpError as error:
        print(error)
        pass

"""
if __name__ == "__main__":
    main()
"""
