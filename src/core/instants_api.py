import requests

from core.constants import BASE_URL
from core.exc import InstantNotFoundError, InvalidPageError
from core.models import InstantResult, InstantDetail

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
    :raises ValueError: If page number is less than 1 or is not an int;
    if query, when provided, is not a string
    """
    global INSTANTS_URL
    global FORMAT

    if query and not isinstance(query, str):
        raise ValueError("Query must be a string.")
    if not isinstance(page, int) or page < 1:
        raise ValueError("Page number must be an int greater than 0.")

    params = {
        "name": query,
        "page": page,
        "format": FORMAT,
    }
    response = requests.get(INSTANTS_URL, params)
    json = response.json()
    if response.status_code == 404:
        raise InvalidPageError(page)
    return InstantResult(**json)


def get_instant(name: str) -> InstantDetail:
    """
    Get an instant for a given instant name and return them.

    :param name: The name of the instant to retrieve the details for.
    :return:
    :raises ValueError: If the instant name is not a non-empty string
    :raises InstantNotFoundError: If an instant with the given name is not found.
    """
    global INSTANTS_URL
    global FORMAT

    if not isinstance(name, str) or not name:
        raise ValueError("Name must be a non-empty string.")

    instant_url = f'{INSTANTS_URL}/{name}'
    params = {
        "format": FORMAT,
    }
    response = requests.get(instant_url, params)
    if response.status_code == 404:
        raise InstantNotFoundError(name)
    json = response.json()
    return InstantDetail(**json)
