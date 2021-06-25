from bs4 import BeautifulSoup

from constants import Shop
from scraper.base.base_shop_scraper import BaseShopScraper


class Amazon(BaseShopScraper):
    SHOP = Shop.AMAZON

    def scrape_article(self, soup: BeautifulSoup, additional_data=None) -> bool:
        in_stock = soup.select("#availability span")[0].string.strip() == "Auf Lager."
        return in_stock
