from modules.misc import loadConfig, getHeader
import requests


def claimPOAP(address: str, qr_hash: str, secret: str):
    r"""Claim a POAP NFT for a specific address.
    :param address: The address to claim the POAP NFT for.
    :param qr_hash: The QR Hash to claim the POAP NFT for.
    :return: Response object if the POAP NFT was claimed successfully, False otherwise.
    :rtype: bool | object

    Reference: https://documentation.poap.tech/reference/postactionsclaim-qr-2
    """

    endpoint = "https://api.poap.tech/actions/claim-qr"

    payload = {
        "address": address,
        "qr_hash": qr_hash,
        "secret": secret,
        "sendEmail": True,
    }

    response = requests.post(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
        return False


def getClaimSecret(qr_hash):
    r"""Get information about a POAP claim hash.
    :param qr_hash: The QR Hash of the POAP claim.
    :return: Information about claim status, secret and more.
    :rtype: object

    Reference: https://documentation.poap.tech/reference/getactionsclaim-qr-2
    """

    endpoint = f"https://api.poap.tech/actions/claim-qr?qr_hash={qr_hash}"

    response = requests.get(endpoint, headers=getHeader())

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
        return False
