from constants import Shop
from scraper.base.base_article import BaseArticle, ArticleEntry


class TestArticle(BaseArticle):
    def __init__(self):
        super().__init__("name", [ArticleEntry("url", Shop.BIKE_COMPONENTS)])
