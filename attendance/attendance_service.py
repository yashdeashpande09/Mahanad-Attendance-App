from datetime import datetime

from sheets.sheets_operations import get_attendance_sheet


def attendance_already_marked(username):
    """
    Check if user has already marked attendance today.
    """

    worksheet = get_attendance_sheet()

    records = worksheet.get_all_records()

    today = datetime.now().strftime("%Y-%m-%d")

    for row in records:

        if (
            str(row["Username"]).strip()
            == str(username).strip()
            and str(row["Date"]).strip()
            == today
        ):
            return True

    return False


def save_attendance(
    username,
    name,
    latitude,
    longitude,
    distance,
    status
):
    """
    Save attendance record to Google Sheet.
    """

    worksheet = get_attendance_sheet()

    now = datetime.now()

    worksheet.append_row([
        username,
        name,
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        latitude,
        longitude,
        distance,
        status
    ])

    return True


def get_today_attendance(username):
    """
    Get today's attendance record for a user.
    """

    worksheet = get_attendance_sheet()

    records = worksheet.get_all_records()

    today = datetime.now().strftime("%Y-%m-%d")

    for row in records:

        if (
            str(row["Username"]).strip()
            == str(username).strip()
            and str(row["Date"]).strip()
            == today
        ):
            return row

    return None


def mark_attendance(
    username,
    name,
    latitude,
    longitude,
    distance,
    radius
):
    """
    Complete attendance workflow.

    Returns:
    {
        "success": True/False,
        "message": "...",
        "status": "Present"/"Absent",
        "distance": distance
    }
    """

    if attendance_already_marked(username):

        return {
            "success": False,
            "message": "Attendance already marked today.",
            "status": None,
            "distance": distance
        }

    status = (
        "Present"
        if distance <= radius
        else "Absent"
    )

    save_attendance(
        username=username,
        name=name,
        latitude=latitude,
        longitude=longitude,
        distance=distance,
        status=status
    )

    return {
        "success": True,
        "message": "Attendance marked successfully.",
        "status": status,
        "distance": distance
    }