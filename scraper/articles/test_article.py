from constants import Shop
from scraper.base.base_article import BaseArticle


class TestArticle(BaseArticle):
    def __init__(self):
        super().__init__("name", {Shop.BIKE_COMPONENTS: "test"})
