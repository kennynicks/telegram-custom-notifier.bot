from bs4 import BeautifulSoup

from constants import Shop
from scraper.base.base_shop_scraper import BaseShopScraper


class BikeComponents(BaseShopScraper):
    SHOP = Shop.BIKE_COMPONENTS

    def scrape_article(self, soup: BeautifulSoup) -> bool:
        return True