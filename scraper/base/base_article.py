from typing import List

from constants import Shop
from dataclasses import dataclass


@dataclass
class ArticleEntry:
    url: str
    shop: Shop


class BaseArticle:
    def __init__(self, name: str, article_entries: List[ArticleEntry]) -> None:
        self.name = name
        self.article_entries = article_entries
