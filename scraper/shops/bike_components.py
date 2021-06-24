from scraper.base.base_article import BaseArticle
from scraper.base.base_shop_scraper import BaseShopScraper


class BikeComponents(BaseShopScraper):
    def watch(self, article: BaseArticle):
        print("watching")
