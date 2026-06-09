from sheets.sheets_operations import get_users_data


def normalize_value(value, length=8):
    """
    Ensures values like passwords keep leading zeros.
    Example: 9112002 → 09112002
    """
    return str(value).strip().zfill(length)


def authenticate_user(username, password):

    users = get_users_data()

    input_username = str(username).strip()
    input_password = normalize_value(password)

    for user in users:

        sheet_username = str(user["Username"]).strip()
        sheet_password = normalize_value(user["Password"])

        if sheet_username == input_username and sheet_password == input_password:
            return True, user["Username"], user["Name"]

    return False, None, None
