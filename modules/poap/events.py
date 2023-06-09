from modules.misc import loadConfig, getHeader
import requests
from classes.Event import Event


def createEvent(event: Event, email, request_codes):
    """Create a new event.
    :param event: The :class:`Event` object to create.
    :return: Event object of the event if created successfully, False otherwise.
    :rtype: bool | object

    Reference: https://documentation.poap.tech/reference/postevents
    """

    endpoint = "https://api.poap.tech/events"

    payload = {
        "name": event.name,
        "description": event.description,
        "country": event.country,
        "city": event.city,
        "start_date": event.start_date,
        "end_date": event.end_date,
        "expiry_date": event.expiry_date,
        "event_url": event.event_url,
        "virtual_event": event.virtual_event,
        "image": event.image,
        "secret_code": loadConfig()["secret_code"],
        "email": email,
        "request_codes": request_codes,
        "event_template_id": event.event_template_id,
        "private_event": event.private_event,
    }

    response = requests.post(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
        return False


def getEvent():
    """Retrieve the event details for a specified event ID.
    :return: :class:`Event` object
    :rtype: Event object

    Reference: https://documentation.poap.tech/reference/geteventsid
    """

    event_id = loadConfig()["event_id"]
    endpoint = f"https://api.poap.tech/events/id/{event_id}"

    response = requests.get(endpoint, headers=getHeader())

    if response.status_code == 200:
        data = response.json()
        return Event(**data)


def editEvent(event: Event):
    """Edit an existing event.
    :param event: The :class:`Event` object to edit.
    :return: Response object if the event was edited successfully, False otherwise.
    :rtype: bool | object

    Reference: https://documentation.poap.tech/reference/putevents
    """

    endpoint = f"https://api.poap.tech/events/{event.fancy_id}"

    payload = {
        "name": event.name,
        "description": event.description,
        "country": event.country,
        "city": event.city,
        "event_url": event.event_url,
        "start_date": event.start_date,
        "end_date": event.end_date,
        "expiry_date": event.expiry_date,
        "event_url": event.event_url,
        "secret_code": loadConfig()["secret_code"],
    }

    response = requests.put(endpoint, headers=getHeader(), json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code, response.text)
        return False
