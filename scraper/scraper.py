from typing import List

from constants import Shop
from scraper.base.article_subscriber import ArticleSubscriber
from scraper.base.base_article import BaseArticle
from scraper.shops.amazon import Amazon
from scraper.shops.bike_24 import Bike24
from scraper.shops.bike_components import BikeComponents
from scraper.shops.bike_discount import BikeDiscount


class Scraper(ArticleSubscriber):
    def __init__(self) -> None:
        self.subscribers: List[ArticleSubscriber] = []

        self.bike_components = BikeComponents()
        self.bike_discount = BikeDiscount()
        self.bike_24 = Bike24()
        self.amazon = Amazon()
        self.bike_components.add_subscriber(self)
        self.bike_discount.add_subscriber(self)
        self.bike_24.add_subscriber(self)
        self.amazon.add_subscriber(self)
        self.articles: List[BaseArticle] = []

    def on_change(self, available: bool, shop: Shop, article: BaseArticle) -> None:
        for subscriber in self.subscribers:
            subscriber.on_change(available, shop, article)

    def watch_article(self, article: BaseArticle):
        self.articles.append(article)
        if Shop.BIKE_COMPONENTS in article.article_entries:
            self.bike_components.watch(article)
        if Shop.BIKE_DISCOUNT in article.article_entries:
            self.bike_discount.watch(article)
        if Shop.BIKE_24 in article.article_entries:
            self.bike_24.watch(article)
        if Shop.AMAZON in article.article_entries:
            self.amazon.watch(article)

    def get_status(self) -> str:
        status_message = ""
        for idx, article in enumerate(self.articles):
            status_message += "{}\.    {}\n".format(idx + 1, article.name)
            amazon_state = self.amazon.get_status(article)
            bike24_state = self.bike_24.get_status(article)
            bikecomponents_state = self.bike_components.get_status(article)
            bikediscount_state = self.bike_discount.get_status(article)
            states = [x for x in [amazon_state, bike24_state, bikecomponents_state, bikediscount_state] if
                      x is not None]
            status_message += "\n".join(states)
            status_message += "\n\n"
        return status_message

    def add_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: ArticleSubscriber):
        self.subscribers.remove(subscriber)
