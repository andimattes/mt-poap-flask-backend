import requests
from modules.misc import loadConfig, getHeader, storeConfig
import time


def generateAccessToken():
    """Generate an access token for the POAP API."""

    # Check if the access token is older than 15 minutes (maximum of 4 requests per hour)
    access_token_age = int(time.time()) - int(loadConfig()["auth"]["last_refresh"])
    if access_token_age < 900:
        print("Access token is still valid.")
        return

    # Generate a new access token
    endpoint = "https://poapauth.auth0.com/oauth/token"

    header = getHeader(withBearer=False)
    header["Content-Type"] = "application/x-www-form-urlencoded"

    config = loadConfig()
    payload = {
        "client_id": config["auth"]["client_id"],
        "client_secret": config["auth"]["client_secret"],
        "audience": config["auth"]["audience"],
        "grant_type": config["auth"]["grant_type"],
    }

    response = requests.post(endpoint, data=payload, headers=header)
    access_token = response.json()["access_token"]

    config["auth"]["access_token"] = access_token
    config["auth"]["last_refresh"] = str(int(time.time()))
    print("Got new access token:", access_token)
    storeConfig(config)


def validateAccessToken() -> bool:
    event_id = "124862"
    endpoint = f"https://api.poap.tech/event/{event_id}/qr-codes"

    payload = {"secret_code": loadConfig()["secret_code"]}

    response = requests.post(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        return True
    else:
        print(response.status_code, response.text)
        print("Access token expired...")
        return False


if __name__ == "__main__":
    validateAccessToken()
