from constants import Shop
from scraper.base.base_article import BaseArticle


class N03A(BaseArticle):
    def __init__(self):
        super().__init__("Shimano Bremsbeläge N03A", {
            Shop.BIKE_COMPONENTS: "https://www.bike-components.de/de/Shimano/Bremsbelaege-N03A-fuer-XTR-XT-SLX-p68485/",
            Shop.BIKE_DISCOUNT: "https://www.bike-discount.de/de/kaufen/shimano-n03a-resin-disc-belaege-753179",
            Shop.BIKE_24: "https://www.bike24.de/p1296555.html",
            Shop.AMAZON: "https://www.amazon.de/SHIMANO-scheibenbremsbel%C3%A4ge-Xtrn03a-schwarz-St%C3%BCck/dp/B07K5DKL2Y/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=n03a&qid=1624662907&sr=8-1"
        })
