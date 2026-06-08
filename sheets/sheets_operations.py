import streamlit as st

from sheets.sheets_client import get_sheet_client
from config.settings import (
    SHEET_ID,
    USERS_SHEET,
    ATTENDANCE_SHEET,
    CONFIG_SHEET
)

@st.cache_resource
def get_attendance_sheet():

    spreadsheet = get_spreadsheet()

    return spreadsheet.worksheet("Attendance")

def get_config_data():

    spreadsheet = get_spreadsheet()

    worksheet = spreadsheet.worksheet("Config")

    return worksheet.get_all_records()

# -----------------------------
# GET SPREADSHEET CONNECTION
# -----------------------------

@st.cache_resource
def get_spreadsheet():

    client = get_sheet_client()

    spreadsheet = client.open_by_key(SHEET_ID)

    return spreadsheet


# -----------------------------
# USERS
# -----------------------------

@st.cache_data(ttl=300)
def get_users_data():

    spreadsheet = get_spreadsheet()

    worksheet = spreadsheet.worksheet(
        USERS_SHEET
    )

    return worksheet.get_all_records()


# -----------------------------
# CONFIG
# -----------------------------

@st.cache_data(ttl=300)
def get_config_data():

    spreadsheet = get_spreadsheet()

    worksheet = spreadsheet.worksheet(
        CONFIG_SHEET
    )

    return worksheet.get_all_records()


# -----------------------------
# ATTENDANCE WRITE
# -----------------------------

def add_attendance_record(
    username,
    name,
    date,
    time,
    latitude,
    longitude,
    distance,
    status
):

    spreadsheet = get_spreadsheet()

    worksheet = spreadsheet.worksheet(
        ATTENDANCE_SHEET
    )

    worksheet.append_row(
        [
            username,
            name,
            date,
            time,
            latitude,
            longitude,
            distance,
            status
        ]
    )


# -----------------------------
# CHECK IF ALREADY MARKED TODAY
# -----------------------------

def attendance_exists_today(
    username,
    today_date
):

    spreadsheet = get_spreadsheet()

    worksheet = spreadsheet.worksheet(
        ATTENDANCE_SHEET
    )

    records = worksheet.get_all_records()

    for record in records:

        if (
            str(record["Username"]).strip()
            == str(username).strip()
            and
            str(record["Date"]).strip()
            == str(today_date).strip()
        ):
            return True

    return False