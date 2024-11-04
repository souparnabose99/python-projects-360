from dataclasses import dataclass, field
from enum import StrEnum


class Types(StrEnum):
    JOB = 'job'
    STORY = 'story'
    COMMENT = 'comment'


@dataclass
class Item:
    id: int
    type: Types
    deleted: bool = False
    by: str = 'anon'
    time: int = 0
    dead: bool = False
    kids: list[int] = field(default_factory=list)

    def __str__(self):
        return f'{self.id}'


@dataclass
class Story(Item):
    descendants: int = 0
    title: str = ''
    url: str = 'https://news.ycombinator.com/'
    text: str = ''
    score: int = 0
