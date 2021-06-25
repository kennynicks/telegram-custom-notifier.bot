from bs4 import BeautifulSoup

from constants import Shop
from scraper.base.base_shop_scraper import BaseShopScraper


class BikeDiscount(BaseShopScraper):
    SHOP = Shop.BIKE_DISCOUNT

    def scrape_article(self, soup: BeautifulSoup, additional_data=None) -> bool:
        return len(soup.select(".uk-icon-envelope")) == 0
