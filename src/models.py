from pydantic import BaseModel, HttpUrl, field_validator
from pydantic.color import Color


class InstantDetail(BaseModel):
    name: str
    slug: str
    sound: HttpUrl
    color: Color
    image: HttpUrl | None = None
    description: str = ""
    tags: list[str] = []

    @field_validator('tags', mode='before')
    @classmethod
    def split_tags(cls, tags: str) -> list[str]:
        if not isinstance(tags, str):
            raise ValueError('"tags" must be a string"')
        return tags.split(' ')


class InstantResult(BaseModel):
    count: int
    next: HttpUrl | None
    previous: HttpUrl | None
    results: list[InstantDetail]
