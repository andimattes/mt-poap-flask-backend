from modules.misc import loadConfig, getHeader
import requests


def getEventHashes():
    r"""Retrieve all event hashes for a specific event.
    :return: List of event hashes.
    :rtype: list of dictionaries of type {"qr_hash": number, "secret_code": string}

    Reference: https://documentation.poap.tech/reference/posteventqr-codes
    """

    event_id = loadConfig()["event_id"]
    endpoint = f"https://api.poap.tech/event/{event_id}/qr-codes"

    payload = {"secret_code": loadConfig()["secret_code"]}

    response = requests.post(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
    return False


def requestEventHashes(numberOfHashes=3, rtype="qr_code"):
    r"""Request more codes for one of the following redeem methods: QR Code, Secret Website, or Secret Word.
    :return: The petition ID which is used to track the request's approval status.
    :rtype: string | bool

    Reference: https://documentation.poap.tech/reference/postredeem-requests
    """

    config = loadConfig()
    endpoint = "https://api.poap.tech/redeem-requests"

    payload = {
        "event_id": config["event_id"],
        "requested_codes": numberOfHashes,
        "secret_code": config["secret_code"],
        "redeem_type": rtype,
    }

    response = requests.post(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        if "id" in response.json():
            return response.json()["id"]
    else:
        print(response.status_code, response.text)
    return False


def getActiveRedeemRequests(redeem_type="qr_code"):
    r"""Retrieve all active redeem requests for a specific event.
    :return: List of redeem requests.
    :rtype: list

    Reference: https://documentation.poap.tech/reference/getredeem-requestsactivecount
    """

    event_id = loadConfig()["event_id"]
    endpoint = f"https://api.poap.tech/redeem-requests/active/count?event_id={event_id}&redeem_type={redeem_type}"

    response = requests.get(endpoint, headers=getHeader())

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
    return False


def getUnclaimedHash(hashes=[]):
    for qr_hash in hashes:
        if not qr_hash["claimed"]:
            return qr_hash["qr_hash"]
    return None
