from bs4 import BeautifulSoup

from constants import Shop
from scraper.base.base_shop_scraper import BaseShopScraper


class Bike24(BaseShopScraper):
    SHOP = Shop.BIKE_24

    def scrape_article(self, soup: BeautifulSoup, additional_data=None) -> bool:
        not_in_stock = len(soup.select("[name=notdeliverable]"))
        if not_in_stock:
            return False
        items = soup.select("div.options select option")
        if len(items)>0:
            for item in items:
                in_stock = item["data-deliverable"] == "1"
                if additional_data is not None:
                    variation = item.string.strip()
                    if variation == additional_data:
                        return in_stock
                elif in_stock:
                    return True
        else:
            return True
        return False
