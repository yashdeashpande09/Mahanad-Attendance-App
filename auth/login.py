from sheets.sheets_operations import get_users_data


def authenticate_user(username, password):

    users = get_users_data()

    for user in users:

        if (
            str(user["Username"]).strip()
            == str(username).strip()
            and str(user["Password"]).strip()
            == str(password).strip()
        ):

            return (
                True,
                user["Username"],
                user["Name"]
            )

    return (
        False,
        None,
        None
    )