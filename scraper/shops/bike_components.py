from bs4 import BeautifulSoup

from constants import Shop
from scraper.base.base_shop_scraper import BaseShopScraper


class BikeComponents(BaseShopScraper):
    SHOP = Shop.BIKE_COMPONENTS

    def scrape_article(self, soup: BeautifulSoup, additional_data: str = None) -> bool:
        options = soup.select("div.product-options ul li")
        for option in options:
            item = option.contents[1]
            in_stock = "site-stock-bg-0" in item.contents[1]["class"]
            if additional_data:
                variation = item.contents[2].strip()
                if variation == additional_data:
                    return in_stock
            elif in_stock:
                return True
        return False
