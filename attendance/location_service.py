from sheets.sheets_operations import get_config_data


def get_ground_location():

    config = get_config_data()[0]

    return {
        "latitude": float(config["Latitude"]),
        "longitude": float(config["Longitude"]),
        "radius": float(config["Radius"])
    }