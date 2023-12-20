import pytest
from pydantic import ValidationError

from models import InstantDetail


def test_instant_detail_tags_validator():
    with pytest.raises(ValidationError):
        InstantDetail(
            name='foo',
            slug='bar',
            sound='https://www.myinstants.com/media/sounds/faustao-errou.mp3',
            color='000000',
            image=None,
            description='Foobar.',
            tags=10
        )
