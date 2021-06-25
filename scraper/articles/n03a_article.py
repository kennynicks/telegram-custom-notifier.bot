from constants import Shop
from scraper.base.base_article import BaseArticle


class N03A(BaseArticle):
    def __init__(self):
        super().__init__("Shimano Bremsbeläge N03A", {
            Shop.BIKE_COMPONENTS: "https://www.bike-components.de/de/Shimano/Bremsbelaege-N03A-fuer-XTR-XT-SLX-p68485/"
        })
