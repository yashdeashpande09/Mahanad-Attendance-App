import gspread
from google.oauth2.service_account import Credentials


def get_sheet_client():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "credentials/service_account.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)

    return client