from typing import Dict

from constants import Shop


class BaseArticle:
    def __init__(self, name: str, article_entries: Dict[Shop, str], additional_data=None) -> None:
        self.name = name
        self.article_entries = article_entries
        self.additional_data = additional_data
