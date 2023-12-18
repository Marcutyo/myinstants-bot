import requests

from constants import BASE_URL
from exc import InstantNotFoundError, InvalidInstantNameError
from models import InstantResult, InstantDetail

API_BASE_URL = f'{BASE_URL}/api/v1'
INSTANTS_URL = f'{API_BASE_URL}/instants'
FORMAT = 'json'


def get_instants(query: str = None, page: int = 1) -> InstantResult:
    """
    Get all instants for a given query and page number and return them.

    If query is provided, only the instants for that query will be returned,
    else all instants.

    Query value will be searched in all the InstantDetail object fields and, if matched,
    will be part of the resulting InstantResult object.

    :param query: The query to get all instants for
    :param page: The page number to retrieve the details
    :return InstantResult: The retrieved instants
    """
    global INSTANTS_URL
    global FORMAT

    params = {
        "name": query,
        "page": page,
        "format": FORMAT,
    }
    response = requests.get(INSTANTS_URL, params)
    json = response.json()
    return InstantResult(**json)


def get_instant(name: str) -> InstantDetail:
    """
    Get an instant for a given instant name and return them.

    :param name: The name of the instant to retrieve the details for.
    :return:
    :raises ValueError: If the instant name is not provided
    :raises InstantNotFoundError: If an instant with the given name is not found.
    """
    global INSTANTS_URL
    global FORMAT

    if not name:
        raise InvalidInstantNameError()

    instant_url = f'{INSTANTS_URL}/{name}'
    params = {
        "format": FORMAT,
    }
    response = requests.get(instant_url, params)
    if response.status_code == 404:
        raise InstantNotFoundError(name)
    json = response.json()
    return InstantDetail(**json)