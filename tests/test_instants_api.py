import pytest

from core.exc import InstantNotFoundError, InvalidPageError
from core.instants_api import get_instants, get_instant
from core.models import InstantResult, InstantDetail


def test_get_instants() -> None:
    instants = get_instants(None)
    assert isinstance(instants, InstantResult)
    instants = get_instants(query="foobar")
    assert isinstance(instants, InstantResult)
    instants = get_instants(page=100)
    assert isinstance(instants, InstantResult)
    instants = get_instants(query="a", page=100)
    assert isinstance(instants, InstantResult)


def test_get_instants_invalid_parameters() -> None:
    with pytest.raises(ValueError, match="Query must be a string."):
        get_instants(query=10)
    with pytest.raises(ValueError, match="Page number must be an int greater than 0."):
        get_instants(page=-1)
    with pytest.raises(ValueError, match="Page number must be an int greater than 0."):
        get_instants(page='foo')
    page = 100
    with pytest.raises(InvalidPageError, match=f"Page {page} cannot be reached."):
        get_instants(query="foobar", page=page)


def test_get_instant() -> None:
    name = "errou-faustao"
    instant = get_instant(name)
    assert isinstance(instant, InstantDetail)


def test_get_instant_not_found() -> None:
    name = "instant_impossibile_to_find_i_hope"
    with pytest.raises(InstantNotFoundError, match=f"Instant with name {name!r} not found."):
        get_instant(name)


def test_get_instant_invalid_parameters() -> None:
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        get_instant(name=None)
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        get_instant(name=10)
    with pytest.raises(ValueError, match="Name must be a non-empty string."):
        get_instant(name="")
