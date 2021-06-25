from typing import Dict

from constants import Shop


class BaseArticle:
    def __init__(self, name: str, article_entries: Dict[Shop, str]) -> None:
        self.name = name
        self.article_entries = article_entries
